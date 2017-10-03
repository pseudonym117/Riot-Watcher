
import datetime
import logging
import time

from . import BaseRateLimitHandler

from .._apis import LolStatusApiV3, StaticDataApiV3


class WaitingRateLimitHandler(BaseRateLimitHandler):
    def __init__(self):
        super(WaitingRateLimitHandler, self).__init__()

    def preview_request(self, endpoint_name, method_name, url, query_params):
        super(BaseRateLimitHandler, self).preview_request(endpoint_name, method_name, url, query_params)

        # these APIs do not have rate limits
        if endpoint_name == LolStatusApiV3.__name__ or endpoint_name == StaticDataApiV3.__name__:
            return

        seconds_waited = 0

        last_header = self.last_rate_headers
        if last_header is not None:
            if last_header.retry_after is not None:
                sleep_time = last_header.retry_after - (datetime.datetime.now() - last_header.time).seconds
                if sleep_time > 0:
                    seconds_waited = seconds_waited + sleep_time
                    logging.info('waiting for {} seconds'.format(sleep_time))
                    time.sleep(sleep_time)

            limits_to_check = self._combine_server_headers_with_configured_headers()

            for limit, start_and_count in limits_to_check:
                if seconds_waited > limit.time.seconds:
                    # we already waited longer than this limit is for, just go
                    continue

                start_time = start_and_count[0]
                count = start_and_count[1]

                # check if this call will go over the rate limit
                if limit.calls < count + 1:
                    wait_for = (start_time + limit.time) - datetime.datetime.now()

                    if wait_for.total_seconds() > 0:
                        seconds_waited = seconds_waited + wait_for.total_seconds()
                        logging.info('waiting for {} seconds'.format(wait_for.total_seconds()))
                        time.sleep(wait_for.total_seconds())

    def _combine_server_headers_with_configured_headers(self):
        """
        Combines the last received headers from Riot and the user configured
        rate limits into one list, containing the most recent call count (from Riot)
        and the user configured limits.

        :return list of tuples, [(LimitCount, (datetime, int)), ...] with the datetime
            being the time this limit started and the int being the number of calls.
        """
        if self.app_limits is not None:
            last_header = self.last_rate_headers

            if last_header is not None and last_header.app_rate_limit_count is not None:
                valid_limits = []

                for configured_limit in self.app_limits:
                    matching_limit = next(
                        (
                            riot_limit
                            for riot_limit in last_header.app_rate_limit_count
                            if lambda limit: limit.time == configured_limit.time
                        ),
                        None
                    )

                    if matching_limit is not None:
                        valid_limits.append((configured_limit, (matching_limit.start_time, matching_limit.calls)))

                return valid_limits
        return []

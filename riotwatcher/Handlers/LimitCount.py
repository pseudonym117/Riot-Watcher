
import datetime


class LimitCount(object):
    """
    The LimitCount class contains how many requests have been made in a specified time period,
    as well as how long that time period is.
    It does NOT contain the actual limit for number of requests that can be made in that time period,
    just the number of requests that HAVE been made in that time period
    """

    def __init__(self, str_rep, last_limit=None):
        """
        Creates a new LimitCount object from a string formatted the way Riot's API returns Limit information
        :param str_rep: string in format "<calls>:<time>"
        :param last_limit: previous LimitCount object to use in determining the correct start time
        """
        nums = str_rep.split(':')

        self._calls = int(nums[0])

        seconds = int(nums[1])
        self._time = datetime.timedelta(seconds=seconds)

        if last_limit is not None and self.calls > last_limit.calls:
            self._start_time = last_limit.start_time
        else:
            self._start_time = datetime.datetime.now()

    @property
    def calls(self):
        """the number of calls that have been made in the specified time period"""
        return self._calls

    @property
    def start_time(self):
        """the time that this rate limit starts"""
        return self._start_time

    @property
    def time(self):
        """the time period that this Limit is over. Is a datetime.timedelta object."""
        return self._time

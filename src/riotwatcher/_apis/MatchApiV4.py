from . import NamedEndpoint
from .urls import MatchApiV4Urls


class MatchApiV4(NamedEndpoint):
    """
    This class wraps the Match-v4 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#match-v4 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new MatchApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(MatchApiV4, self).__init__(base_api, self.__class__.__name__)

    def by_id(self, region, match_id):
        """
        Get match by match ID

        :param string region: The region to execute this request on
        :param long match_id: The match ID.

        :returns: MatchDto
        """
        url, query = MatchApiV4Urls.by_id(platform=region, match_id=match_id)
        return self._raw_request(self.by_id.__name__, region, url, query)

    def matchlist_by_account(
        self,
        region,
        encrypted_account_id,
        queue=None,
        begin_time=None,
        end_time=None,
        begin_index=None,
        end_index=None,
        season=None,
        champion=None,
    ):
        """
        Get matchlist for ranked games played on given account ID and platform ID
        and filtered using given filter parameters, if any

        A number of optional parameters are provided for filtering. It is up to the caller to
        ensure that the combination of filter parameters provided is valid for the requested
        account, otherwise, no matches may be returned.

        Note that if either beginIndex or endIndex are specified, then both must be specified and
        endIndex must be greater than beginIndex.

        If endTime is specified, but not beginTime, then beginTime is effectively the start of the
        account's match history.

        If beginTime is specified, but not endTime, then endTime is effectively the current time.

        Note that endTime should be greater than beginTime if both are specified, although there is
        no maximum limit on their range.

        :param string region:               The region to execute this request on
        :param string encrypted_account_id: The account ID.
        :param Set[int] queue:              Set of queue IDs for which to filtering matchlist.
        :param long begin_time:             The begin time to use for filtering matchlist specified
                                            as epoch milliseconds.
        :param long end_time:               The end time to use for filtering matchlist specified
                                            as epoch milliseconds.
        :param int begin_index:             The begin index to use for filtering matchlist.
        :param int end_index:               The end index to use for filtering matchlist.
        :param Set[int] season:             Set of season IDs for which to filtering matchlist.
        :param Set[int] champion:           Set of champion IDs for which to filtering matchlist.

        :returns: MatchlistDto
        """
        url, query = MatchApiV4Urls.matchlist_by_account(
            platform=region,
            encrypted_account_id=encrypted_account_id,
            queue=queue,
            beginTime=begin_time,
            endTime=end_time,
            beginIndex=begin_index,
            endIndex=end_index,
            season=season,
            champion=champion,
        )
        return self._raw_request(self.matchlist_by_account.__name__, region, url, query)

    def timeline_by_match(self, region, match_id):
        """
        Get match timeline by match ID.

        Not all matches have timeline data.

        :param string region: The region to execute this request on
        :param long match_id: The match ID.

        :returns: MatchTimelineDto
        """
        url, query = MatchApiV4Urls.timeline_by_match(
            platform=region, match_id=match_id
        )
        return self._raw_request(self.timeline_by_match.__name__, region, url, query)


from . import NamedEndpoint


class MatchApiV3(NamedEndpoint):
    """
    This class wraps the Match-v3 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#match-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new MatchApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(MatchApiV3, self).__init__(base_api, MatchApiV3.__name__)

    def by_id(self, region, match_id):
        """
        Get match by match ID

        :param string region: The region to execute this request on
        :param long match_id: The match ID.

        :returns: MatchDto
        """
        return self._request(
            self.by_id.__name__,
            region,
            '/lol/match/v3/matches/{matchId}'.format(matchId=match_id)
        )

    def matchlist_by_account(
            self,
            region,
            account_id,
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

        A number of optional parameters are provided for filtering. It is up to the caller to ensure that the
        combination of filter parameters provided is valid for the requested account, otherwise, no matches may
        be returned.
        Note that if either beginIndex or endIndex are specified, then both must be specified and endIndex must be
        greater than beginIndex.
        If endTime is specified, but not beginTime, then beginTime is effectively the start of the account's match
        history.
        If beginTime is specified, but not endTime, then endTime is effectively the current time.
        Note that endTime should be greater than beginTime if both are specified, although there is no maximum
        limit on their range.

        :param string region:       The region to execute this request on
        :param long account_id:     The account ID.
        :param Set[int] queue:      Set of queue IDs for which to filtering matchlist.
        :param long begin_time:     The begin time to use for filtering matchlist specified as epoch milliseconds.
        :param long end_time:       The end time to use for filtering matchlist specified as epoch milliseconds.
        :param int begin_index:     The begin index to use for filtering matchlist.
        :param int end_index:       The end index to use for filtering matchlist.
        :param Set[int] season:      Set of season IDs for which to filtering matchlist.
        :param Set[int] champion:   Set of champion IDs for which to filtering matchlist.

        :returns: MatchlistDto
        """
        return self._request(
            self.matchlist_by_account.__name__,
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}'.format(accountId=account_id),
            queue=queue,
            beginTime=begin_time,
            endTime=end_time,
            beginIndex=begin_index,
            endIndex=end_index,
            season=season,
            champion=champion
        )

    def matchlist_by_account_recent(self, region, account_id):
        """
        Get matchlist for last 20 matches played on given account ID and platform ID

        :param string region:   The region to execute this request on
        :param long account_id: The account ID.

        :returns: MatchlistDto
        """
        return self._request(
            self.matchlist_by_account_recent.__name__,
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}/recent'.format(accountId=account_id)
        )

    def timeline_by_match(self, region, match_id):
        """
        Get match timeline by match ID.

        Not all matches have timeline data.

        :param string region: The region to execute this request on
        :param long match_id: The match ID.

        :returns: MatchTimelineDto
        """
        return self._request(
            self.timeline_by_match.__name__,
            region,
            '/lol/match/v3/timelines/by-match/{matchId}'.format(matchId=match_id)
        )

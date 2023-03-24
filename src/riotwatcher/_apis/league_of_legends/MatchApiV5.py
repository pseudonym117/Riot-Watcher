from .. import BaseApi, NamedEndpoint
from ..helpers import remap_region_to_platform
from .urls import MatchApiV5Urls


class MatchApiV5(NamedEndpoint):
    """
    This class wraps the Match-v5 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#match-v5 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new MatchApiV5 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    @remap_region_to_platform(1)
    def by_id(self, region: str, match_id: str):
        """
        Get match by match ID

        :param string region: The region to execute this request on
        :param string match_id: The match ID.

        :returns: MatchDto
        """
        return self._request_endpoint(
            self.by_id.__name__, region, MatchApiV5Urls.by_id, match_id=match_id
        )

    @remap_region_to_platform(1)
    def matchlist_by_puuid(
        self,
        region: str,
        puuid: str,
        start: int = None,
        count: int = None,
        queue: int = None,
        type: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        """
        Get matchlist for ranked games played on given account ID and platform ID
        and filtered using given filter parameters, if any

        :param string region:   The region to execute this request on
        :param string puuid:    The puuid.
        :param int start:       Defaults to 0. Start index.
        :param int count:       Defaults to 20. Valid values: 0 to 100. Number of
                                match ids to return.
        :param int queue:       Filter the list of match ids by a specific queue id.
                                This filter is mutually inclusive of the type filter
                                meaning any match ids returned must match both the
                                queue and type filters.
        :param string type:     Filter the list of match ids by the type of match.
                                This filter is mutually inclusive of the queue filter
                                meaning any match ids returned must match both the
                                queue and type filters.
        :param long start_time: Epoch timestamp in seconds. The matchlist started
                                storing timestamps on June 16th, 2021. Any matches
                                played before June 16th, 2021 won't be included in the
                                results if the startTime filter is set.
        :param long end_time:   Epoch timestamp in seconds.

        :returns: List[string]
        """
        return self._request_endpoint(
            self.matchlist_by_puuid.__name__,
            region,
            MatchApiV5Urls.matchlist_by_puuid,
            puuid=puuid,
            start=start,
            count=count,
            queue=queue,
            type=type,
            startTime=start_time,
            endTime=end_time,
        )

    @remap_region_to_platform(1)
    def timeline_by_match(self, region: str, match_id: str):
        """
        Get match timeline by match ID.

        Not all matches have timeline data.

        :param string region: The region to execute this request on
        :param string match_id: The match ID.

        :returns: MatchTimelineDto
        """
        return self._request_endpoint(
            self.timeline_by_match.__name__,
            region,
            MatchApiV5Urls.timeline_by_match,
            match_id=match_id,
        )

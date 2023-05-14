from .. import BaseApi, NamedEndpoint
from ..helpers import remap_region_to_platform
from .urls import MatchApiUrls

from typing import Optional


class MatchApi(NamedEndpoint):
    """
    This class wraps the TFT-Match-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-match-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initializes a new MatchApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    @remap_region_to_platform(1)
    def by_puuid(
        self,
        region: str,
        puuid: str,
        count: int = 20,
        start: int = 0,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
    ):
        """
        Get a list of match ids by PUUID.

        :param string region:   The region to execute this request on
        :param string puuid:    The puuid.
        :param int count:       Defaults to 20. Valid values: 0 to 100. Number of
                                match ids to return.
        :param int start:       Defaults to 0. Start index.
        :param int start_time:  Epoch timestamp in seconds.
        :param int end_time:    Epoch timestamp in seconds.

        :returns: List[string]
        """
        args = {
            "count": count,
            "start": start,
        }

        if start_time:
            args["startTime"] = start_time

        if end_time:
            args["endTime"] = end_time

        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            MatchApiUrls.by_puuid,
            puuid=puuid,
            **args,
        )

    @remap_region_to_platform(1)
    def by_id(self, region: str, match_id: str):
        """
        Get a match by match id.

        :param string region:   The region to execute this request on
        :param string match_id: The match ID.

        :returns: MatchDto
        """
        return self._request_endpoint(
            self.by_id.__name__, region, MatchApiUrls.by_id, match_id=match_id
        )

from . import NamedEndpoint


class VersionApi(NamedEndpoint):
    """
    This class wraps the Version endpoint in Data Dragon provided by the Riot API.

    See https://developer.riotgames.com/static-data.html#realms for more detailed
    information
    """

    def __init__(self, base_api):
        """
        Initialize a new VersionApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(VersionApi, self).__init__(base_api, VersionApi.__name__)

    def for_region(self, region):
        return self._base_api.request_version(region)

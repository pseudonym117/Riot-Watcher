
from . import NamedEndpoint


class TournamentApiV3(NamedEndpoint):
	"""
	This class wraps the Tournament-v3 endpoint calls provided by the Riot API.
	See https://developer.riotgames.com/api-methods/#tournament-v3 for more detailed information
	"""
	def __init__(self, base_api):
		"""
		Initialize a new TournamentApiV3 which uses the provided base_api

		:param BaseApi base_api: the root API object to use for making all requests.
		"""
		super(TournamentApiV3, self).__init__(base_api, TournamentApiV3.__name__)
	
	def create_provider(self, region, url):
		"""
		Creates a tournament provider and returns its ID.

		Providers will need to call this endpoint first to register their callback URL and their API key with the tournament system before any other tournament provider endpoints will work.

		:param string region: The region in which the provider will be running tournaments. (Legal values: BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR)
		:parm string url:     The provider's callback URL to which tournament game results in this region should be posted.
							  The URL must be well-formed, use the http or https protocol, and use the default port for the protocol (http URLs must use port 80, https URLs must use port 443).
		
		:returns: int provider id
		"""
		return self._request(
			self.create_provider.__name__,
			'/lol/tournament/v3/providers',
			ProviderRegistrationParameters={'region':region,'url':url})

	def create_tournament(self, provider_id, tournament_name=None):
		"""
		Creates a tournament and returns its ID.

		:param optional string tournament_name: The optional name of the tournament.
		:param int provider_id: The provider ID to specify the regional registered provider data to associate this tournament.

		:returns: int tournament_id
		"""
		return self._request(
			self.create_tournament.__name__,
			'/lol/tournament/v3/tournaments',
			TournamentRegistrationParameters={'name':tournament_name,'providerId':provider_id})

	def codes(self,
			  count,
			  tournament_id,
			  tournament_code_parameters={'spectator_type':'ALL','team_size':5,'pick_type':'TOURNAMENT_DRAFT','map_type':'SUMMONERS_RIFT','allowed_Summoner_ids':None,'metadata':None}
	):
		"""
		Create a tournament code for given tournament.

		:param int count:            The number of codes to create (max 1000)
		:param int tournament_id:    The tournament ID
		:param dict tournament_code_parameters: Contains the following key-value pairs

		:required key-value tournament_code_parameters:
									string spectator_type = The spectator type of the game. (Legal values: NONE, LOBBYONLY, ALL)
									int team_size = The team size of the game. Valid values are 1-5.
									string pick_type = The pick type of the game. (Legal values: BLIND_PICK, DRAFT_MODE, ALL_RANDOM, TOURNAMENT_DRAFT)
									string map_type = The map type of the game. (Legal values: SUMMONERS_RIFT, TWISTED_TREELINE, HOWLING_ABYSS)
		: optional key-value tournament_code_parameters:
									dict allowed_Summoner_ids = Optional list of participants in order to validate the players eligible to join the lobby. {'participants':Set[long]}
									string metadata = Optional string that may contain any data in any format, if specified at all. Used to denote any custom information about the game.
		
		:default key-value tournament_code_parameters if not specified by user: ALL, 5, TOURNAMENT_DRAFT, SUMMONERS_RIFT, None, None

		:returns: List[string] = represents a tournament code
		"""
		return self._request(
			self.codes.__name__,
			'/lol/tournament/v3/codes',
			count=count,
			tournamentId=tournament_id,
			TournamentCodeParameters=tournament_code_parameters
		)

	def update_by_id(self, tournament_code, tournament_parameters={'allowedParticipants':'','mapType':'','pickType':'','spectatorType':''}):
		"""
		Update the pick type, map, spectator type, or allowed summoners for a code.

		:param string tournament_code: The tournament code to update
		:param dict tournament_parameters: 
									string	spectatorType	    The spectator type (Legal values: NONE, LOBBYONLY, ALL)
									string	pickType	        The pick type (Legal values: BLIND_PICK, DRAFT_MODE, ALL_RANDOM, TOURNAMENT_DRAFT)
									string	allowedParticipants	Comma separated list of summoner Ids
									string	mapType	            The map type (Legal values: SUMMONERS_RIFT, TWISTED_TREELINE, HOWLING_ABYSS)

		"""
		return self._request(
			self.update_by_id.__name__,
			'/lol/tournament/v3/codes/{tournamentCode}'.format(tournamentCode=tournament_code),
			TournamentCodeUpdateParameters=tournament_parameters
		)

	def by_id(self, tournament_code):
		"""
		Returns the tournament code DTO associated with a tournament code string.

		:param string tournament_code: The tournament code string.

		:returns: TournamentCodeDTO: tournament details
		"""
		return self._request(
			self.by_id.__name__,
			'/lol/tournament/v3/codes/{tournamentCode}'.format(tournamentCode=tournament_code)
		)
	
	def lobby_events(self, tournament_code):
		"""
		Gets a list of lobby events by tournament code.

		:param string tournament_code: The tournament code string.

		:returns: LobbyEventDTOWrapper: lobby events as a list, each element contains lobby event details
		"""
		return self._request(
			self.lobby_events.__name__,
			'/lol/tournament/v3/lobby-events/by-code/{tournamentCode}'.format(tournamentCode=tournament_code)
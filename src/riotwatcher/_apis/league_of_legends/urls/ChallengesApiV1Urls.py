from .LeagueEndpoint import LeagueEndpoint


class ChallengesApiV1Endpoints(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/challenges/v1{url}"
        super().__init__(nurl, **kwargs)


class ChallengesApiV1Urls:
    config = ChallengesApiV1Endpoints("/challenges/config")
    percentiles = ChallengesApiV1Endpoints("/challenges/percentiles")
    challenge_config = ChallengesApiV1Endpoints("/challenges/{challengeId}/config")
    leaderboards = ChallengesApiV1Endpoints("/challenges/{challengeId}/leaderboards/by-level/{level}")
    percentiles_by_challenge_id = ChallengesApiV1Endpoints("/challenges/{challengeId}/percentiles")
    by_puuid = ChallengesApiV1Endpoints("/player-data/{puuid}")

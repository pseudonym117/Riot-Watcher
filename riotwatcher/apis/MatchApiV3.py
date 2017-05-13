
class MatchApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def __call__(self, match_id, region='na1'):
        return self.by_id(match_id, region=region)

    def by_id(self, match_id, region='na1'):
        return self._base_api.request(region, '/lol/match/v3/matches/{matchId}'.format(matchId=match_id))

    def matchlist_by_account(self, account_id, region='na1'):
        # todo: add query params
        return self._base_api.request(
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}'.format(accountId=account_id)
        )

    def matchlist_by_account_recent(self, account_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}/recent'.format(accountId=account_id)
        )

    def timeline_by_match(self, match_id, region='na1'):
        return self._base_api.request(region, '/lol/match/v3/timelines/by-match/{matchId}'.format(matchId=match_id))

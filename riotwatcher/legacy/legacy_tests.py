# these tests are pretty bad, mostly to make sure no exceptions are thrown

import time
from .riotwatcher import RiotWatcher, NORTH_AMERICA

key = '<your-api-key-here>'
# if summoner doesnt have ranked teams, teams tests will fail
# if summoner doesnt have ranked stats, stats tests will fail
# these are not graceful failures, so try to use a summoner that has them
summoner_name = 'pseudonym117'

w = RiotWatcher(key)


def wait():
    while not w.can_make_request():
        time.sleep(1)


def champion_tests():
    wait()
    temp = w.get_all_champions()
    wait()
    w.get_champion(temp['champions'][0]['id'])


def current_game_tests():
    wait()
    player = w.get_featured_games()['gameList'][0]['participants'][0]['summonerName']
    wait()
    player_id = w.get_summoner(name=player)['id']
    wait()
    w.get_current_game(player_id)


def featured_games_tests():
    wait()
    w.get_featured_games()


def game_tests(summoner):
    wait()
    w.get_recent_games(summoner['id'])


def league_tests(summoner):
    wait()
    w.get_league(summoner_ids=[summoner['id'], ])
    wait()
    w.get_league_entry(summoner_ids=[summoner['id'], ])
    wait()
    w.get_challenger()
    wait()
    w.get_master()


def static_tests():
    temp = w.static_get_champion_list()
    w.static_get_champion(temp['data'][list(temp['data'])[0]]['id'])
    temp = w.static_get_item_list()
    w.static_get_item(temp['data'][list(temp['data'])[0]]['id'])
    temp = w.static_get_mastery_list()
    w.static_get_mastery(temp['data'][list(temp['data'])[0]]['id'])
    w.static_get_realm()
    temp = w.static_get_rune_list()
    w.static_get_rune(temp['data'][list(temp['data'])[0]]['id'])
    temp = w.static_get_summoner_spell_list()
    w.static_get_summoner_spell(temp['data'][list(temp['data'])[0]]['id'])
    w.static_get_versions()


def status_tests():
    w.get_server_status()
    w.get_server_status(region=NORTH_AMERICA)


def match_tests(match):
    wait()
    w.get_match(match['gameId'])


def summoner_tests(summoner_name):
    wait()
    s = w.get_summoner(name=summoner_name)
    wait()
    w.get_summoner(_id=s['id'])
    wait()
    w.get_mastery_pages([s['id'], ])
    wait()
    w.get_rune_pages([s['id'], ])
    wait()
    w.get_summoner_name([s['id'], ])
    return s


def match_list_tests(summoner):
    wait()
    return w.get_match_list(summoner['id'])['matches'][0]


def main():
    static_tests()
    print('static tests passed')
    status_tests()
    print('status tests passed')
    champion_tests()
    print('champion tests passed')
    featured_games_tests()
    print('featured games tests passed')
    current_game_tests()
    print('current games tests passed')
    s = summoner_tests(summoner_name)
    print('summoner tests passed')
    game_tests(s)
    print('game tests passed')
    league_tests(s)
    print('league tests passed')
    m = match_list_tests(s)
    print('match list tests passed')
    match_tests(m)
    print('match passed')
    print('all tests passed, w00t. if only they were better tests...')


if __name__ == '__main__':
    main()

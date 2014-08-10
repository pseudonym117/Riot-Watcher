
# these tests are pretty bad, mostly to make sure no exceptions are thrown

import time
from riotwatcher import RiotWatcher

key = '<ENTER-YOUR-KEY-HERE>'
# if summoner doesnt have ranked teams, teams tests will fail
# if summoner doesnt have ranked stats, stats tests will fail
# these are not graceful failures, so try to use a summoner that has them
summoner_name = 'YOUR NAME HERE'

w = RiotWatcher(key)


def wait():
    while not w.can_make_request():
        time.sleep(1)


def champion_tests():
    wait()
    temp = w.get_all_champions()
    wait()
    w.get_champion(temp['champions'][0]['id'])


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


def stats_tests(summoner):
    wait()
    w.get_stat_summary(summoner['id'])
    wait()
    w.get_ranked_stats(summoner['id'])


def summoner_tests(summoner_name):
    wait()
    s = w.get_summoner(name=summoner_name)
    wait()
    w.get_summoner(id=s['id'])
    wait()
    w.get_mastery_pages([s['id'], ])
    wait()
    w.get_rune_pages([s['id'], ])
    wait()
    w.get_summoner_name([s['id'], ])
    return s


def team_tests(summoner):
    wait()
    t = w.get_teams_for_summoner(summoner['id'])
    wait()
    w.get_team(t[0]['fullId'])


def main():
    static_tests()
    print('static tests passed')
    champion_tests()
    print('champion tests passed')
    s = summoner_tests(summoner_name)
    print('summoner tests passed')
    game_tests(s)
    print('game tests passed')
    league_tests(s)
    print('league tests passed')
    stats_tests(s)
    print('stats tests passed')
    team_tests(s)
    print('team tests passed')
    print('all tests passed, w00t. if only they were better tests...')


if __name__ == '__main__':
    main()

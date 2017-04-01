
if __name__ == '__main__':
    from riotwatcher.main.riotwatcher import RiotWatcher
    from riotwatcher import API_KEY
    from pprint import pprint
    w = RiotWatcher(API_KEY)

    me = w.get_summoner(name='zedt')

    pprint(me)

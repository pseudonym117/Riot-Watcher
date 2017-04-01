
# these tests are pretty bad, mostly to make sure no exceptions are thrown

import unittest
from riotwatcher.main.riotwatcher import RiotWatcher, NORTH_AMERICA, LoLException
from riotwatcher import API_KEY


class TestMain(unittest.TestCase):

    def setUp(self):
        self.__key = API_KEY
        self.__watcher = RiotWatcher(self.__key)

    def test_status_tests(self):
        self.__watcher.get_server_status()
        self.__watcher.get_server_status(region=NORTH_AMERICA)

if __name__ == '__main__':
     unittest.main()
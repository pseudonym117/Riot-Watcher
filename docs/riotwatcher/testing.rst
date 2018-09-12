Testing
=======

There currently are 2 sets of tests. There are basic unit tests for API related
functionality, and there is a full system test, which directly accesses the
API.

Unit tests can be run with the following command from the RiotWatcher folder:

::

    tox

Full access API tests should be run by first creating a file named api_key,
which should contain a valid API key (no newline), to the folder Riot-Watcher.
Then the following command will run the full system test (WARNING: it takes
quite some time to run; definitely hits the dev key rate limit):

::

    python -m unittest discover -p full_test*.py

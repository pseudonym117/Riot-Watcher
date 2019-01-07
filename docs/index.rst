
Welcome to RiotWatcher's documentation!
=======================================

RiotWatcher is a thin wrapper on top of the `Riot Games API for League
of Legends <https://developer.riotgames.com/>`__. All public methods as
of 1/6/2019 are supported in full.

RiotWatcher by default supports a naive rate limiter. This rate limiter will
try to stop you from making too many requests, and in a single threaded test
environment does this rather well. In a multithreaded environment, you may
still get some 429 errors. 429 errors are currently NOT retried for you.

v3 / v4
-------

Until the deprecation date of 1/28/2019, RiotWatcher will default to using API v3 calls.
After the deprecation date, v4 will be the default. 

To enable v4 earlier, the following arguments can be supplied to the RiotWatcher constructor:

====================    =======================================================
Argument                explanation
--------------------    -------------------------------------------------------
v4                      use v4 for all endpoints (overrides all other options)
v4_champion_mastery     use v4 for champion mastery endpoint
v4_league               use v4 for league endpoint
v4_match                use v4 for match endpoint
v4_spectator            use v4 for spectator endpoint
v4_summoner             use v4 for summoner endpoint
v4_third_party_code     use v4 for third party code endpoint
====================    =======================================================

To Start...
-----------

To install RiotWatcher:

::

    pip install riotwatcher

OR:

::

    python setup.py install

You also need to have an API key from Riot. Get that from
`here <https://developer.riotgames.com/>`__.

Using it...
-----------

All methods return dictionaries representing the json objects described
by the official Riot API. Any HTTP errors that are returned by the API are
raised as HTTPError exceptions from the Requests library.

.. code:: python

    from riotwatcher import RiotWatcher

    watcher = RiotWatcher('<your-api-key>', v4=True)

    my_region = 'na1'

    me = watcher.summoner.by_name(my_region, 'pseudonym117')
    print(me)

    # all objects are returned (by default) as a dict
    # lets see if i got diamond yet (i probably didnt)
    my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])
    print(my_ranked_stats)

    # Lets some champions
    static_champ_list = watcher.static_data.champions(my_region)
    print(static_champ_list)

    # Error checking requires importing HTTPError from requests

    from requests import HTTPError

    # For Riot's API, the 404 status code indicates that the requested data wasn't found and
    # should be expected to occur in normal operation, as in the case of a an
    # invalid summoner name, match ID, etc.
    #
    # The 429 status code indicates that the user has sent too many requests
    # in a given amount of time ("rate limiting").

    try:
        response = watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
    except HTTPError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise


Main API and other topics
-------------------------

.. toctree::
   :maxdepth: 1

   riotwatcher/riotwatcher.rst
   riotwatcher/HandlerChains.rst
   riotwatcher/testing.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

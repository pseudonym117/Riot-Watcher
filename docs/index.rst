
Welcome to RiotWatcher's documentation!
=======================================

RiotWatcher is a thin wrapper on top of the `Riot Games API for League
of Legends <https://developer.riotgames.com/>`__. All public methods as
of 6/28/2022 are supported in full.

RiotWatcher by default supports a naive rate limiter. This rate limiter will
try to stop you from making too many requests, and in a single threaded test
environment does this rather well. In a multithreaded environment, you may
still get some 429 errors. 429 errors are currently NOT retried for you.


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

    from riotwatcher import LolWatcher, ApiError

    lol_watcher = LolWatcher('<your-api-key>')

    my_region = 'na1'

    me = lol_watcher.summoner.by_name(my_region, 'pseudonym117')
    print(me)

    # all objects are returned (by default) as a dict
    # lets see if i got diamond yet (i probably didnt)
    my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
    print(my_ranked_stats)

    # First we get the latest version of the game from data dragon
    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']

    # Lets get some champions
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    print(current_champ_list)

    # For Riot's API, the 404 status code indicates that the requested data wasn't found and
    # should be expected to occur in normal operation, as in the case of a an
    # invalid summoner name, match ID, etc.
    #
    # The 429 status code indicates that the user has sent too many requests
    # in a given amount of time ("rate limiting").

    try:
        response = lol_watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise


DataDragon
----------

Keep in mind when using data dragon APIs with LolWatcher that regions are NOT the same as the other API regions.
Specifically, the following regions are renamed (as of writing):

======== ===========
**API**  **ddragon**
-------- -----------
eun1     eune
oc1      oce
======== ===========

Use with kernel
---------------

RiotWatcher can integrate with the API proxy/caching server `kernel <https://github.com/meraki-analytics/kernel/>`__.
This can be done by providing the ``kernel_url`` parameter to the ``LolWatcher`` constructor.

.. code:: python

    from riotwatcher import LolWatcher, ApiError

    lol_watcher = LolWatcher(kernel_url="https://your-kernel-instance") # should not contain trailing slash
    # use watcher as normal


Main API and other topics
-------------------------

.. toctree::
   :maxdepth: 1

   riotwatcher/index.rst
   riotwatcher/Handlers/index.rst
   riotwatcher/testing.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

RiotWatcher
===========

|pypi| |docs| |coverage| |black|

Check for full (read: slightly better) documentation `here <http://riot-watcher.readthedocs.io/en/latest/>`__!

RiotWatcher is a thin wrapper on top of the `Riot Games API for League
of Legends <https://developer.riotgames.com/>`__. All public methods as
of 3/8/2025 are supported in full.

RiotWatcher by default supports a naive rate limiter. This rate limiter will
try to stop you from making too many requests, and in a single threaded test
environment does this rather well. In a multithreaded environment, you may
still get some 429 errors. 429 errors are currently NOT retried for you.


To Start...
-----------

To install RiotWatcher:

::

    pip install riotwatcher

OR for development/testing, clone and run:

::

    pip install -e .[dev]
    pre-commit install

You also need to have an API key from Riot. Get that from
`here <https://developer.riotgames.com/>`__.

Using it...
-----------

All methods return dictionaries representing the json objects described
by the official Riot API. Any HTTP errors that are returned by the API are
raised as HTTPError exceptions from the Requests library.

.. code:: python

    from riotwatcher import LolWatcher, RiotWatcher, ApiError

    lol_watcher = LolWatcher('<your-api-key>')

    riot_watcher = RiotWatcher('<your-api-key>')

    my_region = 'na1'

    my_account = riot_watcher.account.by_riot_id('AMERICAS', 'pseudonym', 'sudo')

    me = lol_watcher.summoner.by_puuid(my_region, my_account['puuid'])
    print(me)

    # all objects are returned (by default) as a dict
    # lets see if i got diamond yet (i probably didnt)
    my_ranked_stats = lol_watcher.league.by_puuid(my_region, me['puuid'])
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
            print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
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


StatusApiV4
-----------

As of 10/14/2021 (and from the looks of it, indefinitely), both v3 and v4 versions of the LolStatus API are supported by Riot.
As such, RiotWatcher provides a method to use both. By default, the v3 API will be used for backwards compatibility.

To use the v4 API by default, use the following to initialize your LolWatcher instance:

.. code:: python

    from riotwatcher import LolWatcher

    lol_watcher = LolWatcher('<your-api-key>', default_status_v4=True)

    # example call
    matchlist = lol_watcher.lol_status.platform_data('na1')

To explicitly use v4 or v5 during the deprecation period, you can use the following properties:


.. code:: python

    from riotwatcher import LolWatcher

    lol_watcher = LolWatcher('<your-api-key>')

    # use v4 explicitly
    matchlist = lol_watcher.lol_status_v4.platform_data('na1')

    # use v3 explicitly
    old_matchlist = lol_watcher.lol_status_v3.shard_data('na1')

Note: this will not be supported after v3 is completely deprecated! Both lol_status_v3 and lol_status_v4 properties will be removed,
and the change will happen with a minor version increase. If you desire seamless backwards compatibility, do not use these
properies.


Use with kernel
---------------

RiotWatcher can integrate with the API proxy/caching server `kernel <https://github.com/meraki-analytics/kernel/>`__.
This can be done by providing the ``kernel_url`` parameter to the ``LolWatcher`` constructor.

.. code:: python

    from riotwatcher import LolWatcher, ApiError

    lol_watcher = LolWatcher(kernel_url="https://your-kernel-instance") # should not contain trailing slash
    # use watcher as normal
    
Testing
-------

Unit tests can be run with the following command from the RiotWatcher folder:

::

    tox

Known Issues
------------

Rate limiter has some race conditions when used concurrently.

Changelog
---------
v3.3.1 - 5/8/2025
~~~~~~~~~~~~~~~~~
Add support for LoL leaguev4/entries/by-puuid endpoint

Add support for TFT DataDragon

Update gh actions to latest versions

Remove deprecated LoLWatcher.summer.by_name endpoint

Drop support for python 3.8; add support for 3.13

v3.3.0 - 4/9/2024
~~~~~~~~~~~~~~~~~
LoL Champion mastery endpoints updated to use puuid

LoL spectator v4 replaced with v5

Remove support for python3.7; add supported for python3.12

v3.2.4 - 10/29/2022
~~~~~~~~~~~~~~~~~~~
Add ``start`` parameter to TFT match API

Correct remapping for SEA region

Add python 3.11 support to CI/CD

v3.2.3 - 6/28/2022
~~~~~~~~~~~~~~~~~~
Added support for LoL Challenges API

v3.2.2 - 4/25/2022
~~~~~~~~~~~~~~~~~~
Added support for remapping 'na1' -> 'americas' for LoL Matchv5 and TFT Match endpoints

Removed LoL 3rd Party Code API, as has been removed by riot

Updated some documentation

v3.2.1 - 4/4/2022
~~~~~~~~~~~~~~~~~
Added ddragon all versions method.

Add support for python 3.10, remove support for python 3.6

v3.2.0 - 10/14/2021
~~~~~~~~~~~~~~~~~~~
Removed match_v4 and match_v5 properties from LolWatcher. Use match property now - will use v5 API.

Use persistent http session to connect to API.

Added startTime and endTime params for match v5 api

Documented ddragon weirdness

Fix potential security issue with some common usage patterns

v3.1.4 - 8/11/2021
~~~~~~~~~~~~~~~~~~
Add LolStatus-V4 API. Didnt realize this existed until now.

v3.1.3 - 8/5/2021
~~~~~~~~~~~~~~~~~
Add query "queue" and "type" params for match v5 api

v3.1.2 - 7/4/2021
~~~~~~~~~~~~~~~~~
Add support for LoL MatchAPI v5

v3.1.1 - 10/4/2020
~~~~~~~~~~~~~~~~~~
Add support for Valorant recent match API.

Add support for LoR MatchAPI.

v3.1.0 - 9/1/2020
~~~~~~~~~~~~~~~~~
Add support for Clash API's

Add support for generic Riot APIs through riotwatcher.RiotWatcher class (note: old deprecated class has been repurposed - you have been warned)

Add support for valorant APIs

Cleaned up documentation. Quite a bit.

v3.0.0 - 3/3/2020
~~~~~~~~~~~~~~~~~

LoR APIs added through riotwatcher.LorWatcher class.

TFT APIs added through riotwatcher.TftWatcher class.

Added support for LoR APIs through riotwatcher.LorWatcher class.

No more python 2 support. Finally. If you need support for python 2, please use v2.7.1.
Also Python 3.5 is no longer supported. Please use 3.6 or newer.

riotwatcher.RiotWatcher class has been deprecated - It has been renamed to LolWatcher.
The riotwatcher.RiotWatcher class has been maintained for backwards compatibility, but
will not exist forever.

custom_handler_chain parameter for LolWatcher (previously RiotWatcher) no longer exists. 
It has been replaced with the parameters rate_limiter, deserializer, and error_handler.
This is part of the goal to decouple riotwatcher's external APIs from requests.

Removed long-deprecated classes.

v2.7.1 - 7/31/2019
~~~~~~~~~~~~~~~~~~

Fixed issue with using kernel on regions other than NA.

v2.7.0 - 7/30/2019
~~~~~~~~~~~~~~~~~~

Add support for connecting to `kernel <https://github.com/meraki-analytics/kernel/>`__.

General cleanup

v2.6.0 - 5/7/2019
~~~~~~~~~~~~~~~~~

Removed deprecated v3 endpoints

Add support for league v4 entry/by-summoner and entry/queue/tier/division endpoints


Added warning log when deprecated endpoint is used

Added support for timeout parameter. Example:

.. code:: python

    from riotwatcher import RiotWatcher, TimeoutError
    
    watcher = RiotWatcher('<your-api-key>', timeout=2.5) # timeout is in seconds
    try:
        watcher.summoner.by_name('na1', 'pseudonym117')
    except TimeoutError:
        print('timed out getting summoner')

v2.5.0 - 1/7/2019
~~~~~~~~~~~~~~~~~

Added v4 API support

Changed exceptions to custom exception (ApiError) from requests exception.
Change is backwards compatible until at least version v2.6. After that,
catching HTTPError will no loger be supported.

BREAKING:

RequestHandler.preview_static_request and RequestHandler.after_static_request no longer recieve
version and locale directly as parameters. Should instead use URL. This API is undocumented,
but technically broken by some ddragon related changes.

Switched tests to use pytest + tox from unittest and remembering to run each
python version supported.

Added coverage measurements when running tests.

Moved source into src folder.

Added integration tests.

Moved URL writing into separate modules.

Removed StaticData API (RIP)

Removed champions.all and champions.by_id (RIP)

v2.4.0 - 8/23/2018
~~~~~~~~~~~~~~~~~~

Added DDragon API support

Added support for champion rotaion API

v2.3.0 - 6/3/2018
~~~~~~~~~~~~~~~~~

Fixed issue #88 (recent matchlist endpoint deprecated)

Removed riotewatcher.legacy namespace and API. Please (finally) update to the
v3 API.

v2.2.2 - 4/2/2018
~~~~~~~~~~~~~~~~~

Fixed issue #84 where old endpoint was in examples

Added league.by_id endpoint

Fixed a few documentation issues


v2.2.1 - 12/28/2017
~~~~~~~~~~~~~~~~~~~

Fixed issue #83 where lower non-1 limits sent by riot would cause an exception
intead of being handled correctly.

Also added unit tests to Limit class. Because tests are good.

v2.2.0 - 12/1/2017
~~~~~~~~~~~~~~~~~~

Completely removed masteries and runes APIs

Added ThirdPartyCode API

Fixed some documentation typos

Learned what PyLint is and used it.

Legacy interface is to be removed with next non-bugfix version.
Time to adapt to proper usage of v3 interfaces!

v2.1.0 - 10/9/2017
~~~~~~~~~~~~~~~~~~

Service Rate limits now actually respected!

A bunch of random doc fixes... other non-insteresting stuff. etc.

v2.0.3 - 10/3/2017
~~~~~~~~~~~~~~~~~~

Many fixes to documentation and automatic test runners (no pypi version)

Fixed defect #80 (booleans not converted to lower case in requests)

v2.0.2 - 7/25/2017
~~~~~~~~~~~~~~~~~~

Python 2 Support

Fixed a bunch of PEP violations and fixed comments format.

v2.0.1 - 7/18/2017
~~~~~~~~~~~~~~~~~~

fixed nasty packaging bug rendering everything unusable. Oops.

v2.0.0 - 7/18/2017
~~~~~~~~~~~~~~~~~~

v3 API support.

Huge refactor of code, many old calls broken.

Rate limiting added by default, can be removed/replaced.

v1.3.2 - 11/16/2015
~~~~~~~~~~~~~~~~~~~

fixed issue with special characters in names in get_summoners method
(issue #28)

fixed bug in matchlist API causing requests for past seasons to fail,
added constants for each possible season. (issue #44)

fixed bug introduced in pull request #35
(method of checked for what exception is thrown changed from what was
documented) - old method should work now. (issue #43)

v1.3.1 - 10/24/2015
~~~~~~~~~~~~~~~~~~~

removed match history functions, as these were deprecated.

v1.3 - 7/29/2015
~~~~~~~~~~~~~~~~

merged pull requests to (done at previous date, changelog not updated):
 - use matchlist endpoint
 - use nemesis draft
 - use riot attribution
 - get master tier

fixed issue with merged matchlist endpoint tests
fixed issue #24 in readme
added black market brawlers constants

v1.2.5 - 3/8/2015
~~~~~~~~~~~~~~~~~

fixed issue with __init__.py not importing the correct packages

v1.2.4 - 2/13/2015
~~~~~~~~~~~~~~~~~~

Added current-game-v1.0 and featured-games-v1.0 api's

v1.2.3 - 12/31/2014
~~~~~~~~~~~~~~~~~~~

Fixed bug/undocumented feature when getting a single summoner with space
in the name. Also added static method
``RiotWatcher.sanitize_name(name)`` for stripping special characters
from summoner names.

v1.2.2 - 12/22/2014
~~~~~~~~~~~~~~~~~~~

Tiny changes, function signature of get\_summoner changed, to get by ID
the keyword is now ``_id``, not ``id``, tests updated to reflect this

Some game constants updated, if anyone has actually been using them.

v1.2.1 - 10/14/2014
~~~~~~~~~~~~~~~~~~~

Add lol-status API. not a huge thing but i had time to do it.

v1.2 - 9/4/2014
~~~~~~~~~~~~~~~

Added Match and MatchHistory APIs! Also are somewhat tested, but query
parameters are not tested.

Added some new constants. Probably not useful, but who knows. Maybe
someone will want them.

Some code changed to look slightly nicer too.

v1.1.8 - 9/4/2014
~~~~~~~~~~~~~~~~~

Updated APIs supported. Updated APIs:

-  league-v2.5
-  team-v2.4

Don't worry, support for match data is coming. I just wanted to commit
these changes first, since they already had tests.

v1.1.7 - 8/10/2014
~~~~~~~~~~~~~~~~~~

Fixed issue #4 (forgot to change a number, oops) and made it much much
less likely for me to do it again (moved api version part of url into a
different method just to be sure I don't mess it up).

Also there are now TESTS!! WOO! Everyone rejoice. They aren't very good
tests though, so don't be too excited. BUT if they should detect if
there's a clear issue in the API wrapper.

Oh and some better formatting done (spaces not tabs, more consistent
indentation, etc.). Should be no functional difference at all.

v1.1.6 - 6/19/2014
~~~~~~~~~~~~~~~~~~

Added support for regional proxies, because EUW broke without it

v1.1.5 - 5/9/2014
~~~~~~~~~~~~~~~~~

Cause what do version numbers really mean anyways?

Actually add endpoints to league API that I just forgot to add. Change
is NOT backwards compatible, any use of the old league api calls will
need to be changed, in addition to the riot changes.

Newly supported API's: - league-v2.4 - team-v2.3

v1.1.1 - 5/3/2014
~~~~~~~~~~~~~~~~~

Fix issue with static calls, namely that they didn't do anything right
before. Now they work.

v1.1 - 4/29/2014
~~~~~~~~~~~~~~~~

Updated to latest API versions, now supported API's are:

-  champion-v1.2
-  game-v1.3
-  league-v2.3
-  lol-static-data-v1.2
-  stats-v1.3
-  summoner-v1.4
-  team-v2.2

Changes are NOT backwards compatible, you will need to update any code
that used an old API version. Check `Riots
documentation <https://developer.riotgames.com/change-history>`__ for
more information on what changes were made

v1.0.2 - 2/25/2014
~~~~~~~~~~~~~~~~~~

Added Riots new methods to get teams by id. In methods
'get\_teams(team\_ids, region)' and 'get\_team(team\_id, region)'.

v1.0.1a
~~~~~~~

Alpha only, experimental rate limiting added

v1.0
~~~~

Initial release

Attribution
~~~~~~~~~~~

RiotWatcher isn't endorsed by Riot Games and doesn't reflect the views or
opinions of Riot Games or anyone officially involved in producing or managing
*League of Legends*. *League of Legends* and Riot Games are trademarks or
registered trademarks ofRiot Games, Inc.
*League of Legends* (c) Riot Games, Inc.


.. |pypi| image:: https://img.shields.io/pypi/v/riotwatcher.svg
  :target: https://pypi.python.org/pypi/riotwatcher
  :alt: Latest version released on PyPi

.. |docs| image:: https://readthedocs.org/projects/riot-watcher/badge/?version=latest
  :target: http://riot-watcher.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. |coverage| image:: https://img.shields.io/codecov/c/gh/pseudonym117/Riot-Watcher.svg
  :target: https://codecov.io/gh/pseudonym117/Riot-Watcher
  :alt: Test coverage

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/ambv/black
  :alt: Code style

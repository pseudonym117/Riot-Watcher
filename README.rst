RiotWatcher v2.2.2
==================

|pypi| |docs| |build| |coverage|

Check for full (read: slightly better) documentation `here <http://riot-watcher.readthedocs.io/en/latest/>`__!

RiotWatcher is a thin wrapper on top of the `Riot Games API for League
of Legends <https://developer.riotgames.com/>`__. All public methods as
of 4/2/2018 are supported in full.

RiotWatcher by default supports a naive rate limiter. This rate limiter will
try to stop you from making too many requests, and in a single threaded test environment
does this rather well. In a multithreaded environment, you may still get some
429 errors. 429 errors are currently NOT retried for you.

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

    watcher = RiotWatcher('<your-api-key>')

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

Advanced
--------

All rate limiting, caching, and data transformation is handled by objects extending
the Handlers.RequestHandler class. These are completely user configurable.

TODO: add more info about this

Backwards Compatibility
-----------------------

A wrapper has been made to make the API somewhat backwards compatible. If you
REALLY dont want to change much of your code, you can use the following
package to keep all the same method signatures (note that the schema of the data
you receive may be completely different):

::

    from riotwatcher.legacy import RiotWatcher

This legacy wrapper SEEMS to work ok, but I would HIGHLY encourage everyone
to switch to the new API in the standard riotwatcher package.

This wrapper is going to be removed from the library with the next version of
Riot-Watcher. Please discontinue use, or freeze your version of Riot-Watcher.

Testing
-------

There currently are 2 sets of tests. There are basic unit tests for API related
functionality, and there is a full system test, which directly accesses the API.

Unit tests can be run with the following command from the RiotWatcher folder:

::

    python -m unittest

Full access API tests should be run by first creating a file named api_key,
which should contain a valid API key (no newline), to the folder Riot-Watcher.
Then the following command will run the full system test (WARNING: it takes
quite some time to run; definitely hits the dev key rate limit):

::

    python -m unittest discover -p full_test*.py

Known Issues
------------

Rate limiter has some race conditions when used concurrently.

Changelog
---------
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

fixed issue with special characters in names in get_summoners method (issue #28)

fixed bug in matchlist API causing requests for past seasons to fail,
added constants for each possible season. (issue #44)

fixed bug introduced in pull request #35
(method of checked for what exception is thrown changed from what was documented) - old method should work now. (issue #43)

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

RiotWatcher isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially
involved in producing or managing *League of Legends*. *League of Legends* and Riot Games are trademarks or registered
trademarks of Riot Games, Inc. *League of Legends* (c) Riot Games, Inc.


.. |pypi| image:: https://img.shields.io/pypi/v/riotwatcher.svg
  :target: https://pypi.python.org/pypi/riotwatcher
  :alt: Latest version released on PyPi

.. |docs| image:: https://readthedocs.org/projects/riot-watcher/badge/?version=latest
  :target: http://riot-watcher.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. |build| image:: https://travis-ci.org/pseudonym117/Riot-Watcher.svg?branch=master
  :target: https://travis-ci.org/pseudonym117/Riot-Watcher
  :alt: Build status

.. |coverage| image:: https://img.shields.io/codecov/c/gh/pseudonym117/Riot-Watcher.svg
  :target: https://codecov.io/gh/pseudonym117/Riot-Watcher
  :alt: Test coverage

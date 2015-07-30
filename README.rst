RiotWatcher v1.3
==================

RiotWatcher is a thin wrapper on top of the `Riot Games API for League
of Legends <https://developer.riotgames.com/>`__. All public methods as
of 7/29/2015 are supported in full. All game constants are also included
in variable declarations. Requests are kept track of so that you can
stay below your rate limit. The default rate limits are set to 10
requests every 10 seconds and 500 requests every 10 minutes (the limit
for development keys). The rate limiter does not prevent you from making
requests that will be blocked and cause an exception, it simply allows
you to check if you request will go through.

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
by the official Riot API. Any error (e.g. 404) that are known to the
service are returned as custom objects (error\_404, error\_500, ...),
for you to deal with however you like. Any other HTTP errors that are
not known returns of the API are raised as exceptions as in the Requests
API.

Default region of this application is NA, but that can be changed during
initialization.

.. code:: python

    from riotwatcher import RiotWatcher

    w = RiotWatcher('<your-api-key>')

    # check if we have API calls remaining
    print(w.can_make_request())

    me = w.get_summoner(name='pseudonym117')
    print(me)

    # takes list of summoner ids as argument, supports up to 40 at a time
    # (limit enforced on riot's side, no warning from code)
    my_mastery_pages = w.get_mastery_pages([me['id', ])[str(me['id'])]
    # returns a dictionary, mapping from summoner_id to mastery pages
    # unfortunately, this dictionary can only have strings as keys,
    # so must convert id from a long to a string
    print(my_mastery_pages)

    my_ranked_stats = w.get_ranked_stats(me['id'])
    print(my_ranked_stats)

    my_ranked_stats_last_season = w.get_ranked_stats(me['id'], season=3)
    print(my_ranked_stats_last_season)

    # all static methods are prefaced with 'static'
    # static requests do not count against your request limit
    # but at the same time, they don't change often....
    static_champ_list = w.static_get_champion_list()
    print(static_champ_list)

    # import new region code
    from riotwatcher import EUROPE_WEST

    # request data from EUW
    froggen = w.get_summoner(name='froggen', region=EUROPE_WEST)
    print(froggen)

    # create watcher with EUW as its default region
    euw = RiotWatcher('<your-api-key>', default_region=EUROPE_WEST)

    # proper way to send names with spaces is to remove them, still works with spaces though
    xpeke = w.get_summoner(name='fnaticxmid')
    print(xpeke)

I might get around to fully documenting this at some point, but I am
working on using it right now for other things, not documenting it.

Testing
-------

After a couple bugs that were due to me forgetting to change one
character and not testing the change, I decided to finally make a few
tests. The tests included are not perfect, and don't have full code
coverage, but they should detect most issues. To run these tests (to
make sure its the API f-ing up not your code):

-  change key in tests.py to your API key
-  change summoner\_name in tests.py to your summoner name (provided you
   have at least one ranked team and have ranked stats). Or just enter a
   name that does have those.
-  run python tests.py (I only tested these tests with python3, but I
   really doubt they are incompatible with python2 - if I'm wrong
   someone open an issue)

Changelog
---------

v1.3 - 7/29/2015
~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~

RiotWatcher isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially
involved in producing or managing *League of Legends*. *League of Legends* and Riot Games are trademarks or registered
trademarks of Riot Games, Inc. *League of Legends* © Riot Games, Inc.

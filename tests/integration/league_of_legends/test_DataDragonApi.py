import re

import pytest


@pytest.mark.lol
@pytest.mark.integration
@pytest.mark.parametrize("version", ("6.24.1", "8.24.1"))
@pytest.mark.parametrize("locale", (None, "en_US", "zh_CN"))
class TestDataDragonApi:
    def test_champion(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.champions(
            version, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/champion.json",
            params={},
        )

    def test_champion_full(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.champions(
            version, full=True, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/championFull.json",
            params={},
        )

    def test_items(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.items(version, locale=locale)

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/item.json",
            params={},
        )

    def test_languages(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.languages(
            version, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/language.json",
            params={},
        )

    def test_maps(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.maps(version, locale=locale)

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/map.json",
            params={},
        )

    def test_masteries(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.masteries(
            version, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/mastery.json",
            params={},
        )

    def test_profile_icons(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.profile_icons(
            version, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/profileicon.json",
            params={},
        )

    def test_runes(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.runes(version, locale=locale)

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/rune.json",
            params={},
        )

    def test_runes_reforged(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.runes_reforged(
            version, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/runesReforged.json",
            params={},
        )

    def test_summoner_spells(self, lol_context, version, locale):
        actual_response = lol_context.watcher.data_dragon.summoner_spells(
            version, locale=locale
        )

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/summoner.json",
            params={},
        )


@pytest.mark.integration
class TestDataDragonVersionsApi(object):
    @pytest.mark.parametrize(
        "region",
        [
            "br1",
            "eun1",
            "euw1",
            "jp1",
            "kr",
            "la1",
            "la2",
            "na",
            "na1",
            "oc1",
            "tr1",
            "ru",
            "pbe1",
        ],
    )
    def test_versions_for_region(self, lol_context, region):
        actual_response = lol_context.watcher.data_dragon.versions_for_region(region)

        assert lol_context.expected_response == actual_response
        lol_context.get.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/realms/{region}.json".format(
                region=re.sub(r"\d", "", region)
            ),
            params={},
        )

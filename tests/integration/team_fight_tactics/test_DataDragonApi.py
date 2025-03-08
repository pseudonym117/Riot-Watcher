import re

import pytest


@pytest.mark.tft
@pytest.mark.integration
@pytest.mark.parametrize("version", ("6.24.1", "15.5.1"))
@pytest.mark.parametrize("locale", (None, "en_US", "zh_CN"))
class TestDataDragonApi:
    def test_arenas(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.arenas(version, locale=locale)

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-arena.json",
            params={},
        )

    def test_augments(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.augments(
            version, locale=locale
        )

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-augments.json",
            params={},
        )

    def test_champions(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.champions(
            version, locale=locale
        )

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-champion.json",
            params={},
        )

    def test_items(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.items(version, locale=locale)

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-item.json",
            params={},
        )

    def test_queues(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.queues(version, locale=locale)

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-queues.json",
            params={},
        )

    def test_regalia(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.regalia(
            version, locale=locale
        )

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-regalia.json",
            params={},
        )

    def test_tacticians(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.tacticians(
            version, locale=locale
        )

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-tactician.json",
            params={},
        )

    def test_traits(self, tft_context, version, locale):
        actual_response = tft_context.watcher.data_dragon.traits(version, locale=locale)

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale if locale else 'en_US'}/tft-trait.json",
            params={},
        )


@pytest.mark.tft
@pytest.mark.integration
class TestDataDragonVersionsApi:
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
    def test_versions(self, tft_context, region):
        actual_response = tft_context.watcher.data_dragon.versions_for_region(region)

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/realms/{region}.json".format(
                region=re.sub(r"\d", "", region)
            ),
            params={},
        )

    def test_versions_all(self, tft_context):
        actual_response = tft_context.watcher.data_dragon.versions_all()

        assert tft_context.expected_response == actual_response
        tft_context.get.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/api/versions.json",
            params={},
        )

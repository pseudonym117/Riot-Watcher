from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.team_fight_tactics import DataDragonApi


@pytest.mark.tft
@pytest.mark.unit
class TestDataDragonApi:
    def test_arenas(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.arenas(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-arena.json",
            {},
        )

        assert ret is expected_return

    def test_augments(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.augments(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-augments.json",
            {},
        )

        assert ret is expected_return

    def test_champions(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.champions(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-champion.json",
            {},
        )

        assert ret is expected_return

    def test_items(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.items(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-item.json",
            {},
        )

        assert ret is expected_return

    def test_queues(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.queues(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-queues.json",
            {},
        )

        assert ret is expected_return

    def test_regalia(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.regalia(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-regalia.json",
            {},
        )

        assert ret is expected_return

    def test_tacticians(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.tacticians(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-tactician.json",
            {},
        )

        assert ret is expected_return

    def test_traits(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.traits(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/tft-trait.json",
            {},
        )

        assert ret is expected_return

    def test_version(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        region = "euw1"

        ret = static_data.versions_for_region(region)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/realms/{region}.json".format(
                region="euw"
            ),
            {},
        )

        assert ret is expected_return

    def test_version_all(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        ret = static_data.versions_all()

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/api/versions.json",
            {},
        )

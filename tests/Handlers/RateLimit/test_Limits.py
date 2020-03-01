import datetime
import sys

import pytest

from riotwatcher.Handlers.RateLimit import Limit, RawLimit


@pytest.mark.common
@pytest.mark.unit
class TestLimit:
    def test_initial_start_time_correct(self):
        lim = Limit()
        assert lim.start_time is None

    def test_initial_duration_correct(self):
        lim = Limit()
        assert 0 == lim.duration

    def test_initial_count_correct(self):
        lim = Limit()
        assert 0 == lim.count

    def test_initial_limit_correct(self):
        lim = Limit()
        assert 0 == lim.limit

    @pytest.mark.usefixtures("mock_datetime")
    def test_set_raw_limit_first_set(self):
        initial_date = datetime.datetime(2013, 4, 30, 1, 1, 1)

        datetime.datetime.set_now(initial_date)

        lim = Limit()

        raw = RawLimit(50, 100, 10)

        lim.set_raw_limit(raw)

        assert initial_date == lim.start_time

        assert 50 == lim.count
        assert 100 == lim.limit
        assert 10 == lim.duration

    @pytest.mark.usefixtures("mock_datetime")
    def test_limit_duration_changed(self):
        initial_date = datetime.datetime(2013, 4, 30, 1, 1, 1)
        changed_date = datetime.datetime(2013, 6, 13, 1, 1, 1)

        datetime.datetime.set_now(initial_date)

        lim = Limit()

        initial = RawLimit(50, 100, 10)
        changed = RawLimit(50, 100, 20)

        lim.set_raw_limit(initial)

        initial_start_time = lim.start_time

        datetime.datetime.set_now(changed_date)

        lim.set_raw_limit(changed)

        assert initial_start_time != lim.start_time

        assert 20 == lim.duration

    @pytest.mark.usefixtures("mock_datetime")
    def test_resets_when_count_is_1(self):
        initial_date = datetime.datetime(2013, 4, 30, 1, 1, 1)
        changed_date = datetime.datetime(2013, 6, 13, 1, 1, 1)

        datetime.datetime.set_now(initial_date)

        lim = Limit()

        initial = RawLimit(50, 100, 10)
        changed = RawLimit(1, 100, 10)

        lim.set_raw_limit(initial)

        initial_start_time = lim.start_time

        datetime.datetime.set_now(changed_date)

        lim.set_raw_limit(changed)

        assert initial_start_time != lim.start_time

        assert 1 == lim.count

    @pytest.mark.usefixtures("mock_datetime")
    def test_start_time_stays_constant(self):
        initial_date = datetime.datetime(2013, 4, 30, 1, 1, 1)
        changed_date = datetime.datetime(2013, 6, 13, 1, 1, 1)

        datetime.datetime.set_now(initial_date)

        lim = Limit()

        initial = RawLimit(1, 100, 10)

        lim.set_raw_limit(initial)

        datetime.datetime.set_now(changed_date)

        for count in range(2, 200):
            changed = RawLimit(count, 100, 10)

            lim.set_raw_limit(changed)

            assert initial_date == lim.start_time

            assert count == lim.count
            assert 100 == lim.limit
            assert 10 == lim.duration

    def test_setting_lower_count(self):
        lim = Limit()

        initial = RawLimit(50, 100, 10)
        changed = RawLimit(10, 100, 10)

        lim.set_raw_limit(initial)
        lim.set_raw_limit(changed)

        assert 50 == lim.count

    def test_wait_time_under_limit(self):
        lim = Limit()

        lim.set_raw_limit(RawLimit(50, 100, 10))

        until = lim.wait_until()

        assert datetime.datetime(datetime.MINYEAR, 1, 1) == until

    @pytest.mark.usefixtures("mock_datetime")
    def test_wait_time_over_limit(self):
        initial_date = datetime.datetime(2013, 4, 30, 1, 1, 1)

        limit_duration = 200

        datetime.datetime.set_now(initial_date)

        lim = Limit()

        lim.set_raw_limit(RawLimit(10, 10, limit_duration))

        expected_time = initial_date + datetime.timedelta(seconds=limit_duration)
        actual_time = lim.wait_until()

        assert expected_time == actual_time

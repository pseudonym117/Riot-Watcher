
import datetime
import sys
import unittest

from .. import Limit, RawLimit

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class LimitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._initial_date = datetime.datetime(2013, 4, 30, 1, 1, 1)
        cls._changed_date = datetime.datetime(2013, 6, 13, 1, 1, 1)

    def test_initial_start_time_correct(self):
        lim = Limit()
        self.assertIsNone(lim.start_time)

    def test_initial_duration_correct(self):
        lim = Limit()
        self.assertEqual(0, lim.duration)

    def test_initial_count_correct(self):
        lim = Limit()
        self.assertEqual(0, lim.count)

    def test_initial_limit_correct(self):
        lim = Limit()
        self.assertEqual(0, lim.limit)

    @mock.patch(Limit.__module__ + '.datetime.datetime')
    def test_set_raw_limit_first_set(self, mock_datetime):
        mock_datetime.now.return_value = LimitTestCase._initial_date

        lim = Limit()

        raw = RawLimit(50, 100, 10)

        lim.set_raw_limit(raw)

        self.assertEqual(LimitTestCase._initial_date, lim.start_time)

        self.assertEqual(50, lim.count)
        self.assertEqual(100, lim.limit)
        self.assertEqual(10, lim.duration)

    @mock.patch(Limit.__module__ + '.datetime.datetime')
    def test_limit_duration_changed(self, mock_datetime):
        mock_datetime.now.return_value = LimitTestCase._initial_date

        lim = Limit()

        initial = RawLimit(50, 100, 10)
        changed = RawLimit(50, 100, 20)

        lim.set_raw_limit(initial)

        initial_start_time = lim.start_time
        mock_datetime.now.return_value = LimitTestCase._changed_date

        lim.set_raw_limit(changed)

        self.assertNotEqual(initial_start_time, lim.start_time)

        self.assertEqual(20, lim.duration)

    @mock.patch(Limit.__module__ + '.datetime.datetime')
    def test_resets_when_count_is_1(self, mock_datetime):
        mock_datetime.now.return_value = LimitTestCase._initial_date

        lim = Limit()

        initial = RawLimit(50, 100, 10)
        changed = RawLimit(1, 100, 10)

        lim.set_raw_limit(initial)

        initial_start_time = lim.start_time
        mock_datetime.now.return_value = LimitTestCase._changed_date

        lim.set_raw_limit(changed)

        self.assertNotEqual(initial_start_time, lim.start_time)

        self.assertEqual(1, lim.count)

    @mock.patch(Limit.__module__ + '.datetime.datetime')
    def test_start_time_stays_constant(self, mock_datetime):
        mock_datetime.now.return_value = LimitTestCase._initial_date

        lim = Limit()

        initial = RawLimit(1, 100, 10)

        lim.set_raw_limit(initial)

        mock_datetime.now.return_value = LimitTestCase._changed_date

        for count in range(2, 200):
            changed = RawLimit(count, 100, 10)

            lim.set_raw_limit(changed)

            self.assertEqual(LimitTestCase._initial_date, lim.start_time)

            self.assertEqual(count, lim.count)
            self.assertEqual(100, lim.limit)
            self.assertEqual(10, lim.duration)

    def test_setting_lower_count(self):
        lim = Limit()

        initial = RawLimit(50, 100, 10)
        changed = RawLimit(10, 100, 10)

        lim.set_raw_limit(initial)
        lim.set_raw_limit(changed)

        self.assertEqual(50, lim.count)

    def test_wait_time_under_limit(self):
        lim = Limit()

        lim.set_raw_limit(RawLimit(50, 100, 10))

        until = lim.wait_until()

        self.assertEqual(datetime.datetime(datetime.MINYEAR, 1, 1), until)

    @mock.patch(Limit.__module__ + '.datetime.datetime')
    def test_wait_time_over_limit(self, mock_datetime):
        initial_date = LimitTestCase._initial_date
        limit_duration = 200

        mock_datetime.now.return_value = initial_date

        lim = Limit()

        lim.set_raw_limit(RawLimit(10, 10, limit_duration))

        expected_time = initial_date + datetime.timedelta(seconds=limit_duration)
        actual_time = lim.wait_until()

        self.assertEqual(expected_time, actual_time)

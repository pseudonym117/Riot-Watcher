import datetime

import pytest


real_datetime_class = datetime.datetime


class DatetimeSubclassMeta(type):
    @classmethod
    def __instancecheck__(mcs, obj):
        return isinstance(obj, real_datetime_class)


class BaseMockDatetime(real_datetime_class):
    @classmethod
    def now(cls):
        if hasattr(cls, "_now") and cls._now is not None:
            return cls._now
        else:
            return real_datetime_class.now()

    @classmethod
    def set_now(cls, datetime_value):
        cls._now = datetime_value


MockedDatetime = DatetimeSubclassMeta("datetime", (BaseMockDatetime,), {})


@pytest.fixture
def mock_datetime(monkeypatch):
    with monkeypatch.context() as ctx:
        ctx.setattr(datetime, "datetime", MockedDatetime)
        yield

        del MockedDatetime._now

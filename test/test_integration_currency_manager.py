import pytest

from api.currency_management import *
from urllib.error import HTTPError

cm = CurrencyManager()


def test_passes():
    assert 1 == 1


def test_get_available_currencies():
    currencies = cm.get_available_currencies()
    assert any(currencies)


def test_get_array_from_period_correct_1():
    data = cm.get_array_from_period("usd", Period.ONE_WEEK)
    assert any(data)


def test_get_array_from_period_incorrect():
    with pytest.raises(HTTPError):
        cm.get_array_from_period("xxx", Period.ONE_WEEK)

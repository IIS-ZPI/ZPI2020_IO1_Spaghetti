from api.currency_management import *

cm = CurrencyManager()


def test_passes():
    assert 1 == 1


def test_count_drops():
    drops = cm.count_drops([12, 14, 13, 11, 12, 11])
    assert 2 == drops


def test_count_raises():
    raises = cm.count_rises([12, 14, 13, 11, 12, 11, 11, 12, 10])
    assert 3 == raises


def test_count_no_change():
    no_change = cm.count_no_change([12, 14, 13, 11, 12, 11, 11, 12, 10])
    assert 1 == no_change


def test_find_dates():
    dates = cm.find_dates(Period.ONE_WEEK)
    first_day = date.today().strftime('%Y-%m-%d')
    last_day = (date.today() - timedelta(7)).strftime('%Y-%m-%d')
    assert dates[0] == first_day
    assert dates[1] == last_day

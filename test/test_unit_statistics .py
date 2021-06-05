from api.currency_management import *


def test_passes():
    assert 1 == 1


def test_count_median():
    median = count_median([16, 14, 12])
    assert 14 == median


def test_round_two_decimal():
    rounded = round_2_two_decimals([12.3432])
    assert [12.34] == rounded


def test_average():
    average = count_average([12.5, 13.42, 19.32])
    assert 15.08 == average


def test_mode():
    mode = count_mode([1, 3, 3, 3, 5, 7, 7, 9])
    assert 3 == mode


def test_standard_deviation():
    standard_deviation = count_standard_deviation([1, 3, 5, 7, 9, 11])
    assert [3.42] == round_2_two_decimals([standard_deviation])


def test_coefficient_of_variation():
    result = coefficient_of_variation([12, 3, 56, 34, 12, 3, 7, 8])
    assert [1.03] == round_2_two_decimals([result])
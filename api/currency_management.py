from api.json_management import *
from datetime import date, timedelta
from enum import IntEnum
from statistics import mode
import numpy as np


class Period(IntEnum):
    ONE_WEEK = 7
    TWO_WEEKS = 14
    ONE_MONTH = 30
    QUARTER = 91
    HALF_YEAR = 182
    ONE_YEAR = 365


class Currency:
    def __init__(self, name, code, table):
        self.name = name
        self.code = code
        self.table = table


class CurrencyManager:
    def __init__(self):
        self.dict = None
        self.available_currencies = self.get_available_currencies()

    def find_dates(self, period):
        now = date.today()
        before = now
        before -= timedelta(days=period)

        return now.strftime('%Y-%m-%d'), before.strftime('%Y-%m-%d')

    def get_available_currencies(self):
        currencies = []

        for letter in ['a', 'b']:
            txt = f'http://api.nbp.pl/api/exchangerates/tables/{letter}/?format=json'
            temp = get_dictionary_from_json(txt)[0]
            for v in temp['rates']:
                name = v['currency']
                code = v['code']
                table = 'a'
                currencies.append(Currency(name, code, table))

        return currencies

    def get_array_from_period(self, name, period):
        end, start = self.find_dates(period)
        url = "http://api.nbp.pl/api/exchangerates/rates/a/" + name + "/" + start + "/" + end + "/?format=json"
        dict = get_dictionary_from_json(url)
        print(dict)
        self.dict = dict
        values = []
        for v in dict['rates']:
            values.append(v['mid'])

        return values

    def count_changes_percentage(self, name1, name2, period):
        value1 = self.get_array_from_period(name1, period)
        value2 = self.get_array_from_period(name2, period)
        values = np.divide(value1, value2)

        changes_array = []
        x = range(1, len(values))
        for i in x:
            changes_array.append(((values[i] - values[i - 1]) / values[i - 1]) * 100)

        return changes_array

    def count_rises(self, values):
        in_rise = False
        rises = 0
        prev = None
        for value in values:
            if prev is not None:
                if value > prev and not in_rise:
                    rises += 1
                    in_rise = True
                elif value <= prev:
                    in_rise = False

            prev = value

        return rises

    def count_drops(self, values):
        in_drop = False
        drops = 0
        prev = None
        for value in values:
            if prev is not None:
                if value < prev and not in_drop:
                    drops += 1
                    in_drop = True
                elif value >= prev:
                    in_drop = False

            prev = value

        return drops

    def count_no_change(self, values):
        in_no_change = False
        no_changes = 0
        prev = None
        val = round_2_two_decimals(values)
        for value in val:
            if prev is not None:
                if value == prev and not in_no_change:
                    no_changes += 1
                    in_no_change = True
                elif value < prev or value > prev:
                    in_no_change = False

            prev = value

        return no_changes


def count_median(values):
    n = len(values)
    if n % 2 == 0:
        m1 = values[n // 2]
        m2 = values[n // 2 + 1]
        median = (m1 + m2) / 2
    else:
        median = values[n // 2]

    return median


def count_average(values):
    n = len(values)
    return sum(values) / n


def count_standard_deviation(values):
    avg = count_average(values)
    n = len(values)
    variance = 0
    for v in values:
        variance += (v - avg) ** 2

    variance /= n
    return variance ** (1 / 2)


def count_mode(values):
    val = round_2_two_decimals(values)
    return mode(val)


def coefficient_of_variation(values):
    return count_standard_deviation(values) / count_average(values)


def round_2_two_decimals(values):
    val = []
    for v in values:
        val.append(round(v, 2))

    return val

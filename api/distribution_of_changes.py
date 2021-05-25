from json_management import *
from datetime import date, timedelta
from enum import IntEnum
import numpy
from statistics import mode

class Period(IntEnum):
    ONE_MONTH = 30
    QUARTER = 91


class DistributionChanges:
    def __init__(self, currency_name_1, currency_name_2, period):
        self.name1 = currency_name_1
        self.name2 = currency_name_2
        self.period = period
        self.end, self.start = self.find_dates()
        self.dict1 = None
        self.dict2 = None

    def find_dates(self):
        now = date.today()
        before = now
        before -= timedelta(days=self.period)

        return now.strftime('%Y-%m-%d'), before.strftime('%Y-%m-%d')

    def get_array_from_period(self):
        url = "http://api.nbp.pl/api/exchangerates/rates/a/" + self.name1 + "/" + self.start + "/" + self.end + "/?format=json"
        dict1 = get_dictionary_from_json(url)
        self.dict1 = dict1
        values1 = []
        for v in dict1['rates']:
            values1.append(v['mid'])

        url = "http://api.nbp.pl/api/exchangerates/rates/a/" + self.name2 + "/" + self.start + "/" + self.end + "/?format=json"
        dict2 = get_dictionary_from_json(url)
        self.dict2 = dict2
        values2 = []
        for v in dict2['rates']:
            values2.append(v['mid'])

        values = numpy.divide(values1,values2)

        return values

    def count_changes_percentage(self, values):
        changes_array=[]
        x = range(1, len(values))
        for i in x:
            changes_array.append(((values[i]-values[i-1])/values[i-1])*100)

        return changes_array
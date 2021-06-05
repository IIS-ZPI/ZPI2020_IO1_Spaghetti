import json
from urllib.request import urlopen
from json_management import JsonManager, read_from_url
from currency_management import *
from Window import *

if __name__ == '__main__':

    cm = CurrencyManager()

    tab = cm.get_array_from_period('gbp', Period.ONE_MONTH)

    print(tab)
    print(coefficient_of_variation(tab))

    tab2 = cm.count_changes_percentage('usd', 'eur', Period.ONE_MONTH)
    print(tab2)

    for currency in cm.available_currencies:
        print(currency.name)

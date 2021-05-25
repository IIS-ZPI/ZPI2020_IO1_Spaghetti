import json
from urllib.request import urlopen
from json_management import JsonManager, read_from_url
from currency_management import *
from distribution_of_changes import *



if __name__ == '__main__':
    cm = CurrencyManager('gbp', Period.ONE_MONTH)
    tab = cm.get_array_from_period()
    print(tab)
    print(coefficient_of_variation(tab))

    dc = DistributionChanges('usd', 'eur', Period.ONE_MONTH)
    tab = dc.get_array_from_period()
    tab2 = dc.count_changes_percentage(tab)
    print(tab2)
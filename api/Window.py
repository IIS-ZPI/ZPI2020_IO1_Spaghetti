from matplotlib import pyplot as plt
import tkinter
from tkinter import ttk
from currency_management import *

root = tkinter.Tk()
root.title('NPB')
root.geometry('500x500')


def plot_statistical_analysis(currencyCode, period):
    cm = CurrencyManager()
    tab = cm.get_array_from_period(currencyCode, period)
    plt.plot(tab)
    plt.show()


def plot_statistical_measurements():
    print('plot_statistical_measurements')


def plot_distribution_of_changes():
    print('plot_distribution_of_changes')


def currency_changed(event):
    global currencyCode
    currencyCode = event.widget.get()


def create_currencies_combobox():
    cm = CurrencyManager()
    label = tkinter.Label(text="Please select a currency:")
    label.pack(fill='x', padx=5, pady=5)
    selected_currency = tkinter.StringVar()
    currency_cb = ttk.Combobox(root, textvariable=selected_currency)
    currencies = []
    for c in cm.available_currencies:
        currencies.append(c.code)
    currencies_names = currencies
    currency_cb['values'] = sorted(currencies_names)
    currency_cb['state'] = 'readonly'
    currency_cb.pack(fill='x', padx=5, pady=5)
    currency_cb.bind('<<ComboboxSelected>>', currency_changed)
    return currency_cb


currencyCode = ''
period = ''

mainMenu = tkinter.Menu()
root.config(menu=mainMenu)
currencyMenu = tkinter.Menu(mainMenu)
currencyCombobox = create_currencies_combobox()

buttonPeriodWeek = tkinter.Button(root, text="One Week", command=lambda: plot_statistical_analysis(currencyCode,
                                                                                                   Period.ONE_WEEK))
buttonPeriodWeek.pack()

buttonPeriod2Weeks = tkinter.Button(root, text="Two Weeks", command=lambda: plot_statistical_analysis(currencyCode,
                                                                                                      Period.TWO_WEEKS))
buttonPeriod2Weeks.pack()

buttonPeriodMonth = tkinter.Button(root, text="One Month", command=lambda: plot_statistical_analysis(currencyCode,
                                                                                                     Period.ONE_MONTH))
buttonPeriodMonth.pack()

buttonPeriodQuarter = tkinter.Button(root, text="One Quarter", command=lambda: plot_statistical_analysis(currencyCode,
                                                                                                         Period.QUARTER))
buttonPeriodQuarter.pack()

buttonPeriodHalfYear = tkinter.Button(root, text="Half a Year", command=lambda: plot_statistical_analysis(currencyCode,
                                                                                                          Period.HALF_YEAR))
buttonPeriodHalfYear.pack()

buttonPeriodYear = tkinter.Button(root, text="Year", command=lambda: plot_statistical_analysis(currencyCode,
                                                                                               Period.ONE_YEAR))
buttonPeriodYear.pack()

root.mainloop()
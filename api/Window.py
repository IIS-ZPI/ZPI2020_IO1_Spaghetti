from matplotlib import pyplot as plt
import tkinter
from tkinter import ttk
from currency_management import *

root = tkinter.Tk()
root.title('NPB')
root.geometry('500x500')


def plot_statistical_analysis():
    global currencyCode
    cm = CurrencyManager()
    tab = cm.get_array_from_period(currencyCode, Period.ONE_WEEK)
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

mainMenu = tkinter.Menu()
root.config(menu=mainMenu)
currencyMenu = tkinter.Menu(mainMenu)
currencyCombobox = create_currencies_combobox()

buttonPeriodWeek = tkinter.Button(root, text="One Week", command=plot_statistical_analysis)
buttonPeriodWeek.pack()

buttonPeriod2Weeks = tkinter.Button(root, text="Two Weeks", command=plot_statistical_analysis)
buttonPeriod2Weeks.pack()

buttonPeriodMonth = tkinter.Button(root, text="One Month", command=plot_statistical_analysis)
buttonPeriodMonth.pack()

buttonPeriodQuarter = tkinter.Button(root, text="One Quarter", command=plot_statistical_analysis)
buttonPeriodQuarter.pack()

buttonPeriodHalfYear = tkinter.Button(root, text="Half a Year", command=plot_statistical_analysis)
buttonPeriodHalfYear.pack()

buttonPeriodYear = tkinter.Button(root, text="Year", command=plot_statistical_analysis)
buttonPeriodYear.pack()

root.mainloop()
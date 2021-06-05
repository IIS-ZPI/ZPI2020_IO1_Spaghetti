from matplotlib import pyplot as plt
import tkinter
from tkinter import ttk
from currency_management import *

root = tkinter.Tk()
root.title('NPB')
root.geometry('500x500')


def display_analysis(currencyCode, period):
    global analysis_window
    if analysis_window is None:
        analysis_window = create_analysis_window()
    else:
        analysis_window.quit()

    display_changes(analysis_window, currencyCode, period)
    plot_statistical_measurements(analysis_window, currencyCode, period)
    plot_statistical_analysis(currencyCode, period)


def plot_statistical_analysis(currencyCode, period):
    cm = CurrencyManager()
    tab = cm.get_array_from_period(currencyCode, period)
    plt.cla()
    plt.plot(tab)
    plt.show()


def create_analysis_window():
    window = tkinter.Toplevel(root)
    window.geometry('300x300')
    return window


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def display_changes(window, currencyCode, period):
    clear_window(window)
    cm = CurrencyManager()
    currency_values = cm.get_array_from_period(currencyCode, period)
    rises = cm.count_rises(currency_values)
    drops = cm.count_drops(currency_values)
    no_change = cm.count_no_change(currency_values)
    rises_label = tkinter.Label(window, text="Rises: " + str(rises))
    drops_label = tkinter.Label(window, text="Drops: " + str(drops))
    no_change_label = tkinter.Label(window, text="No change: " + str(no_change))
    rises_label.pack()
    drops_label.pack()
    no_change_label.pack()


def plot_statistical_measurements(window, currencyCode, period):
    cm = CurrencyManager()
    currency_values = cm.get_array_from_period(currencyCode, period)
    median = count_median(currency_values)
    median_label = tkinter.Label(window, text="Median: " + str(median))
    median_label.pack()

    mode = count_mode(currency_values)
    mode_label = tkinter.Label(window, text="Mode: " + str(mode))
    mode_label.pack()

    standard_deviation = count_standard_deviation(currency_values)
    standard_deviation_label = tkinter.Label(window, text="Standard Deviation: " + str(standard_deviation))
    standard_deviation_label.pack()

    variation = coefficient_of_variation(currency_values)
    variation_label = tkinter.Label(window, text="Coefficient of variation " + str(variation))
    variation_label.pack()


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
analysis_window = None

buttonPeriodWeek = tkinter.Button(root, text="One Week",
                                  command=lambda: display_analysis(currencyCode, Period.ONE_WEEK))
buttonPeriodWeek.pack()

buttonPeriod2Weeks = tkinter.Button(root, text="Two Weeks",
                                    command=lambda: display_analysis(currencyCode, Period.TWO_WEEKS))
buttonPeriod2Weeks.pack()

buttonPeriodMonth = tkinter.Button(root, text="One Month",
                                   command=lambda: display_analysis(currencyCode, Period.ONE_MONTH))
buttonPeriodMonth.pack()

buttonPeriodQuarter = tkinter.Button(root, text="One Quarter",
                                     command=lambda: display_analysis(currencyCode, Period.QUARTER))
buttonPeriodQuarter.pack()

buttonPeriodHalfYear = tkinter.Button(root, text="Half a Year",
                                      command=lambda: display_analysis(currencyCode, Period.HALF_YEAR))
buttonPeriodHalfYear.pack()

buttonPeriodYear = tkinter.Button(root, text="Year",
                                  command=lambda: display_analysis(currencyCode, Period.ONE_YEAR))
buttonPeriodYear.pack()

root.mainloop()
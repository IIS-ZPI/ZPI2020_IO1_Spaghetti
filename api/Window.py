from matplotlib import pyplot as plt
import tkinter
from tkinter import ttk
from tkinter import *
from currency_management import *
from numpy import *

root = tkinter.Tk()
root.title('NPB')
root.geometry('500x500')


def display_analysis(currencyCode, period):
    analysis_window = create_analysis_window()
    display_changes(analysis_window, currencyCode, period)
    plot_statistical_measurements(analysis_window, currencyCode, period)
    plot_statistical_analysis(currencyCode, period)


def plot_statistical_analysis(currencyCode, period):
    cm = CurrencyManager()
    tab = cm.get_array_from_period(currencyCode, period)
    plt.cla()
    plt.plot(tab)
    plt.title("Plot for " + currencyCode)
    plt.xlabel("Records")
    plt.ylabel("PLN value")
    plt.xticks(np.linspace(1, period, num=7, dtype=int, endpoint=True))
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


def plot_distribution_of_changes(currencyCode1, currencyCode2, period):
    cm = CurrencyManager()
    compartments, values = cm.count_changes_percentage(currencyCode1, currencyCode2, period)
    plt.cla()
    plt.title("Distribution of changes for " + currencyCode1 + " and " + currencyCode2)
    plt.ylabel("Daily change")
    plt.xlabel("Range")
    labels_plot = np.array(compartments)
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.xticks(x, labels_plot, rotation=85, fontsize=6)
    plt.stairs(values, fill=True)
    plt.show()


def distribution_btn_onclick(currencies, period):
    global error_message
    error_message.config(text="")
    if len(currencies) == 2:
        plot_distribution_of_changes(currencies[0], currencies[1], period)
    else:
        error_message.config(text="Please select 2 currencies !")


def currency_changed(event):
    global currencyCode
    currencyCode = event.widget.get()


def currencies_selected(event):
    global selected_currencies
    widget = event.widget
    selected_currencies = []
    for index in widget.curselection():
        selected_currencies.append(widget.get(index))
    print(selected_currencies)


def create_currencies_combobox():
    cm = CurrencyManager()
    label = tkinter.Label(text="Please select a currency:", font=("Times New Roman", 11))
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


def create_currencies_double_choice():
    cm = CurrencyManager()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    label = Label(root,
                  text="Please select two currencies:  ",
                  font=("Times New Roman", 11),
                  padx=10, pady=10)
    label.pack()
    list = Listbox(root, selectmode="multiple")
    list.pack(expand=YES, fill="both")
    currencies = []
    for c in cm.available_currencies:
        currencies.append(c.code)
    for each_item in range(len(currencies)):
        currencies = sorted(currencies)
        list.insert(END, currencies[each_item])
    scrollbar.config(command=list.yview)
    list.bind("<<ListboxSelect>>", currencies_selected)


selected_currencies = []
currencyCode = ''

period = ''

mainMenu = tkinter.Menu()
root.config(menu=mainMenu)
currencyMenu = tkinter.Menu(mainMenu)
currencyCombobox = create_currencies_combobox()
currencyCombobox.current(0)
currencyCode = currencyCombobox.get()
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

create_currencies_double_choice()

buttonMonth = tkinter.Button(root, text="Month",
                             command=lambda: distribution_btn_onclick(selected_currencies, Period.ONE_MONTH))
buttonMonth.pack()

buttonQuat = tkinter.Button(root, text="One Quarter",
                            command=lambda: distribution_btn_onclick(selected_currencies, Period.QUARTER))
buttonQuat.pack()

error_message = tkinter.Label(root, text="")
error_message.pack()

root.mainloop()

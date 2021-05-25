from matplotlib import pyplot as plt
import tkinter
from currency_management import *

root = tkinter.Tk()
root.title('NPB')
root.geometry('500x500')

cm = CurrencyManager()

def plot_statistical_analysis():
    tab = cm.get_array_from_period('gbp', Period.ONE_MONTH)
    plt.plot(tab)
    plt.show()

def plot_statistical_measurements():
    print('plot_statistical_measurements')

def plot_distribution_of_changes():
    print('plot_distribution_of_changes')

mainMenu = tkinter.Menu()
root.config(menu=mainMenu)
currencyMenu = tkinter.Menu(mainMenu)
mainMenu.add_cascade(label='Select currency', menu=currencyMenu)

for currency in cm.available_currencies:
    currencyMenu.add_command(label=currency.name)


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
import json
from urllib.request import urlopen
from json_management import JsonManager, read_from_url
from currency_management import *
from matplotlib import pyplot as plt
import tkinter

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('NPB')
    root.geometry('500x500')

    def plot_statistical_analysis():
        cm = CurrencyManager('gbp', Period.ONE_MONTH)
        tab = cm.get_array_from_period()
        plt.plot(tab)
        plt.show()
        print('test')

    mainMenu = tkinter.Menu()
    root.config(menu=mainMenu)
    currencyMenu = tkinter.Menu(mainMenu)
    mainMenu.add_cascade(label='Select currency', menu=currencyMenu)
    currencyMenu.add_command(label='GBP')
    buttonPeriodMonth = tkinter.Button(root, text="One Month", command=plot_statistical_analysis)
    buttonPeriodMonth.pack()
    root.mainloop()

    cm = CurrencyManager('gbp', Period.ONE_MONTH)
    tab = cm.get_array_from_period()
    print(tab)
    print(coefficient_of_variation(tab))

from tkinter import *
import CurrencyModule
import tkinter.messagebox


def exchange():
    amount = plnEnter.get()
    try:
        amount = float(amount)
    except:
        tkinter.messagebox.showerror("Błąd", "Nie wprowadziłeś prawidłowej liczby")
    else:
        if (amount <= 0):
            tkinter.messagebox.showerror("Błąd", "Wprowadź dodatnią liczbę")
        else:
            exchangedMoney = CurrencyModule.getListOfExchangedCurrencies(amount, currencies)
            i = 0
            for x in enters:
                x.config(state='normal')
                x.delete(0, END)
                x.insert(0, exchangedMoney[i]['exchanged'])
                x.config(state='disabled')
                i += 1


currencies = ['usd', 'eur', 'gbp', 'cad', 'czk', 'jpy', 'nok', 'ils']

window = Tk()
window.title("Konwerter walut")
window.geometry("300x300")

openingLabel = Label(window, text="Wprowadź wartość")
openingLabel.grid(row=0, column=0, sticky='w')

plnLabel = Label(window, text="PLN: ")
plnLabel.grid(row=2, column=0, sticky="w")

plnEnter = Entry()
plnEnter.grid(row=2, column=1, sticky="w")

labels = list()
enters = list()
i = 0
for curr in currencies:
    labels.append(Label(window, text=curr.upper()))
    enters.append(Entry(window, state=DISABLED))
    labels[i].grid(row=i + 3, column=0, sticky='w')
    enters[i].grid(row=i + 3, column=1, sticky='w')
    i += 1

button = Button(window, text="Przelicz waluty", command=exchange)
button.grid(row=11, column=0, sticky='w')

mainloop()

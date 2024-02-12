from tkinter import *
from time import *

def update():
    # pomoću direktiva prikazujemo vrijeme unutar naše funkcije
    vrijeme_string = strftime("%H:%M:%S")
    vrijeme.config(text=vrijeme_string)

    dan_string = strftime("%A")
    dan.config(text=dan_string)

    datum_string = strftime("%d. %B %Y.")
    datum.config(text=datum_string)
    # rekurzivna funkcija, pozivamo se na nju iznutra
    prozor.after(1000, update)

prozor = Tk()

vrijeme = Label(prozor, font=("Ubuntu Mono", 50), fg="#00FF00", bg="black")
vrijeme.pack()

dan = Label(prozor, font=("Ubuntu Mono", 25), fg="red")
dan.pack()

datum = Label(prozor, font=("Ubuntu Mono", 30), fg="black")
datum.pack()

update()

prozor.mainloop()

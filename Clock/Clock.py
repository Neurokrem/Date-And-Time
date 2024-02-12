from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S")
    time.config(text=time_string)

    day_string = strftime("%A")
    day.config(text=day_string)

    datum_string = strftime("%d. %B %Y.")
    date.config(text=datum_string)
    # rekurzivna funkcija, pozivamo se na nju iznutra
    window.after(1000, update)

window = Tk()

time = Label(window, font=("Ubuntu Mono", 50), fg="#00FF00", bg="black")
time.pack()

day = Label(window, font=("Ubuntu Mono", 25), fg="red")
day.pack()

date = Label(window, font=("Ubuntu Mono", 30), fg="black")
date.pack()

update()

window.mainloop()

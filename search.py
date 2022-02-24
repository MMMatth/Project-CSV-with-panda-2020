import pandas as pd
from tkinter import *
from tkinter import ttk
import os


def quit_():
    """function allowing to exit the window by resetting the menu"""
    fen.destroy()
    cmd = "menu.py"  # Open "Menu.py"
    os.system(cmd)


def add_(title):
    """
    @type title: object

    """
    global text_, val_nam, val_years, val_type, val_age
    items = exel.loc[exel["nom"] == title, :]

    for val_nam in items["nom"]:
        pass
    for val_years in items["anne"]:
        pass
    for val_type in items["type"]:
        pass
    for val_age in items["age"]:
        pass

    text = "Name : " + val_nam + "\n" + "Years : " + str(
        val_years) + "\n" + "Type : " + val_type + "\n" + "Age required  : " + str(val_age) + " years"
    text_.set(text)


## Tk ##
fen = Tk()
fen.geometry("1200x700")
fen.title("Info game")
fen.resizable(width=False, height=False)
back = PhotoImage(file="IMG/back1.png")
back_tk = Label(fen, image=back)
back_tk.pack()

## -- Unwind -- ##
exel = pd.read_csv("exel.csv", sep=",")
info_game = exel.loc[:, "nom"]
list_ = []
for val in info_game:
    list_.append(val)
combo = ttk.Combobox(fen, width=40, state="readonly", values=list_, font=("Courier", 18))
combo.current(0)
combo.place(x=110, y=200)
text_ = StringVar()
text_.set("")

## -- Display area -- ##
frame = Frame(fen, bg="#cacaca", width=300, height=100, bd=3)
frame.place(x=110, y=280)

Element = Label(frame, textvariable=text_, font=("Courier", 18), fg='black', justify="left")
Element.pack()

## -- Button -- ##
save = Button(fen, text="Save", width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
              command=lambda: add_(combo.get()))
save.place(x=110, y=480)

quit = Button(fen, text='Quit', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
              command=quit_)
quit.place(x=110, y=550)

fen.mainloop()

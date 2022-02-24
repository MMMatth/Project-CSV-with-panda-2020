import pandas as pd
from tkinter import *
import os


def _quit():
    cmd = "menu.py"  # Open "Menu.py"
    fen.destroy()
    os.system(cmd)


def add():
    nom = Name.get()  # we look for the name type
    anne = Year.get()
    genre = Type.get()
    age = Age.get()
    Exel = pd.read_csv("exel.csv", sep=',')  # We open our file with panda
    liste_ = Exel.loc[:, "nbr"]  # we create a list with the numbers
    n = int(liste_[len(liste_) - 1])  # we look on our list the last numbers
    Exel.loc[n] = [n + 1, nom, anne, genre, age]
    Exel.to_csv("exel.csv", index=False)  # we save the news data
    Year.delete(0, END)
    Type.delete(0, END)
    Name.delete(0, END)



## -- Tk -- ##
fen = Tk()  # Create the fen
fen.title("Add a video game")  # The Title is " Add a video game "
fen.geometry("1200x700")
fen.resizable(width=False, height=False)

## -- Back -- ##
back = PhotoImage(file="IMG/back2.png")
backtk = Label(fen, image=back)
backtk.pack()

## -- Entry field -- ##

name_ = Label(fen, text="Name of video game:", font="Courier")
name_.place(x=110, y=200)
Name = Entry(fen, width=50, font="Courier")
Name.place(x=110, y=225)

year_ = Label(fen, text="Release year :", font="Courier")
year_.place(x=110, y=260)
Year = Entry(fen, width=50, font="Courier")
Year.place(x=110, y=285)

type_ = Label(fen, text="Type :", font="Courier")
type_.place(x=110, y=320)
Type = Entry(fen, width=50,font="Courier")
Type.place(x=110, y=345)

age_ = Label(fen, text="Age required  :",  font="Courier")
age_.place(x=110, y=380)
Age = Scale(fen,orient="horizontal",from_=3, to=18, length = 260)
Age.place(x=110, y=405)

# -- Button -- #
save = Button(fen, text="Save", width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
             command=add)
save.place(x=110, y=460)

Quit = Button(fen, text='Quit', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
              command=_quit)
Quit.place(x=110, y=520)

fen.mainloop()

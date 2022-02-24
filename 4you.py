import pandas as pd
from tkinter import *
from tkinter import ttk
import os



def quit_():
    """function allowing to exit the window by resetting the menu"""
    fen.destroy()
    cmd = "menu.py"  # Open "Menu.py"
    os.system(cmd)


def save():
    global Age, exel,  Name, Surname
    my_file = "Results.txt"
    files = open(my_file, "w")
    name_get = Name.get()
    surname_get = Surname.get()
    age_get = int(Age.get())
    info = exel.loc[exel["age"] <= age_get, ["nom"]]
    info = str(info)
    files.write("\n"+"Hello " + name_get +" "+ surname_get + " you can play at:" + info+ "\n")
    files.close()
    cmd = "results.txt"
    os.system(cmd)





## Tk ##
fen = Tk()
fen.geometry("1200x700")
fen.title("Game for you")
fen.resizable(width=False, height=False)
back = PhotoImage(file="IMG/back3.png")
back_tk = Label(fen, image=back)
back_tk.pack()

##-- var -- #


## -- Unwind -- ##
exel = pd.read_csv("exel.csv", sep=",")
info_game = exel.loc[:, "nom"]


name_ = Label(fen, text="Your name:", font="Courier")
name_.place(x=110, y=200)
Name = Entry(fen, width=50, font="Courier")
Name.place(x=110, y=225)

surname_ = Label(fen, text="Your surname:", font="Courier")
surname_.place(x=110, y=250)
Surname = Entry(fen, width=50, font="Courier")
Surname.place(x=110, y=275)

age_ = Label(fen, text="Your age:", font="Courier")
age_.place(x=110, y=300)
Age = Scale(fen,orient="horizontal",from_=3, to=18, length = 260)
Age.place(x=110, y=325)





text_ = StringVar()
text_.set("")


## -- Button -- ##
save = Button(fen, text="Results 🎮", width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
              command=save)
save.place(x=110, y=480)

quit = Button(fen, text='Quit', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
              command=quit_)
quit.place(x=110, y=550)



fen.mainloop()

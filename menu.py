from tkinter import *
import os


def main_():
    """function which allows to change window by opening "search.py" and then closing the window"""
    cmd = "search.py"
    fen.destroy()
    os.system(cmd)


def add_games():
    """function which allows to change window by opening "add.py" and then closing the window"""
    cmd = "add.py"
    fen.destroy()
    os.system(cmd)



def game4you():
    """function which allows to change window by opening "add.py" and then closing the window"""
    cmd = "4you.py"
    fen.destroy()
    os.system(cmd)



fen = Tk()
fen.geometry("1200x700")
fen.title("Biblio Video Games")
fen.resizable(width=False, height=False)

## -- Back -- ##
back = PhotoImage(file="IMG/back0.png")
back_tk = Label(fen, image=back)
back_tk.pack()

b1 = Button(fen, text='Info on Games', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
            command=main_)
b1.place(x=110, y=300)

b2 = Button(fen, text='Add Games', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
            command=add_games)
b2.place(x=110, y=380)

b3 = Button(fen, text='Find a game for you', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
            command=game4you)
b3.place(x=110, y=460)

quit_ = Button(fen, text='Quit', width=20, height=2, font="Courier", fg="black", bg="#cacaca", cursor="hand2",
               command=fen.destroy)
quit_.place(x=110, y=540)

fen.mainloop()

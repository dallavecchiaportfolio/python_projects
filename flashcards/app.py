from tkinter import Frame, Tk, Menu
from PIL import ImageTk, Image


def flask():
    flaskFrame.pack(fill="both", expand=1)


def git():
    gitFrame.pack(fill="both", expand=1)


def linux():
    linuxFrame.pack(fill="both", expand=1)


def python():
    pythonFrame.pack(fill="both", expand=1)


def animals():
    animalsFrame.pack(fill="both", expand=1)


def colors():
    colorsFrame.pack(fill="both", expand=1)


def letters():
    lettersFrame.pack(fill="both", expand=1)


def numbers():
    numbersFrame.pack(fill="both", expand=1)


def framesOff():
    flaskFrame.pack_forget()
    gitFrame.pack_forget()
    linuxFrame.pack_forget()
    pythonFrame.pack_forget()
    animalsFrame.pack_forget()
    colorsFrame.pack_forget()
    lettersFrame.pack_forget()
    numbersFrame.pack_forget()


mainWindows = Tk()
mainWindows.title("FlashCards")
mainWindows.iconbitmap("images/Gakuseisean-Aire-Images.ico")
mainWindows.geometry("500x500")

mainMenu = Menu(mainWindows)
mainWindows.config(menu=mainMenu)

playMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Play", menu=playMenu)
playMenu.add_command(label="Exit", command=mainMenu.quit)

categoryMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Create", menu=categoryMenu)
categoryMenu.add_command(label="Flask", command=flask)
categoryMenu.add_command(label="GIT", command=git)
categoryMenu.add_command(label="Linux", command=linux)
categoryMenu.add_command(label="Python", command=python)
categoryMenu.add_separator()
categoryMenu.add_command(label="Animals", command=animals)
categoryMenu.add_command(label="Colors", command=colors)
categoryMenu.add_command(label="Letters", command=letters)
categoryMenu.add_command(label="Numbers", command=numbers)

flaskFrame = Frame(mainWindows, width=500, height=500)
gitFrame = Frame(mainWindows, width=500, height=500)
linuxFrame = Frame(mainWindows, width=500, height=500)
pythonFrame = Frame(mainWindows, width=500, height=500)
animalsFrame = Frame(mainWindows, width=500, height=500)
colorsFrame = Frame(mainWindows, width=500, height=500)
lettersFrame = Frame(mainWindows, width=500, height=500)
numbersFrame = Frame(mainWindows, width=500, height=500)

mainWindows.mainloop()

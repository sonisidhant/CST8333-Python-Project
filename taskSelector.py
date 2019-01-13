######################
# taskSelector.py
# By Sidhant Soni
# October 11, 2018
######################

"""import statements"""
import threading
from tkinter import *
import tkinter.messagebox
import os

root = Tk()


def insert():
    threading.Thread(target=os.system('openFile.py')).start()


def read():
    os.system('read.py')


def quit():
    sys.exit(0)


def about():
    tkinter.messagebox.showinfo('Window Title', 'Program by Sidhant Soni')


def ExitApplication():
    MsgBox = tkinter.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                            icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tkinter.messagebox.showinfo('Return', 'You will now return to the application screen')


root.geometry('{}x{}'.format(800, 600))
root.title("Sidhant_Soni_TaskSelector")

menu = Menu(root)

root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Insert Data", command=insert)
submenu.add_command(label="Read File", command=read)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)
helpMenu.add_separator()
helpMenu.add_command(label="Quit", command=ExitApplication)

frame = Frame(root)
label = Label(frame, text="Select task from menu bar to perform", font=(None, 30), bg="black", fg="red", height=30,
              width=124)
label.pack()
frame.pack(fill=BOTH)

root.mainloop()

# import the time module
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import os
from PIL import Image, ImageTk
import sqlite3

# Start Tkinter
root = Tk()
bg_color = "#0066FF"
# what starts the program+the title

root.title("Timer")
root.eval("tk::PlaceWindow . center")

# Geometry
root.geometry('300x300')

# creating the icon
photo = PhotoImage(file="download.png")
root.iconphoto(False, photo)

# Take the first input
e = Entry(root)

e.focus_set()

def count():
    num = 10
    while num:
        minutes, secs = divmod(num, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        num -= 1

    print('Times up!!')
def print_text():
    string = e.get()
    input_choices()
    print(string)


b = Button(root, text='okay', command=count)
b.pack()

# define the countdown func.
def count():
    num = 10
    while num:
        minutes, secs = divmod(num, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        num -= 1

    print('Times up!!')


# input time in seconds
#def input_choices():
    #numA = 0
    #t = input("'s' for seconds, 'm' for minutes, 'h' for hours\n Enter your choice of input: ")
    #if t == "s":
        #numA = input("Enter the number of seconds ")
        #numA = int(numA)

    ##elif t == "m":
        #numA = input("Enter the number of seconds ")
        #numA = int(numA)
        #numA = numA * 60

    #elif t == "h":
        #numA = input("Enter the number of seconds ")
        #numA = int(numA)
        #numA = numA * 60 * 60

    #return numA


# function call
# countdown(input_choices())

# Execution of the window.
root.mainloop()

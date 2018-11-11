import os
import sys
from Tkinter import *
import tkMessageBox
import Tkinter
root = Tkinter.Tk()
def callf(string):
    print string
    os.system('./script.sh '+string)

def printtext():
    global e
    string = e.get()
    callf(string)

root.title('Name')
e=Entry(root)
e.pack()
b = Tkinter.Button(root,text='okay',command=printtext)
b.pack()
b.place(bordermode=OUTSIDE, height=100, width=100)
root.mainloop()

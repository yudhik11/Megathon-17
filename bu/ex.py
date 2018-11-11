import os
import sys
from Tkinter import *
import tkMessageBox
root = Tk()
def callf(string):
    print string
    os.system('./run.sh '+string)

def printtext():
    global e
    string = e.get()
    callf(string)

root.title('Enter Country Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')
root.mainloop()

import os
import sys
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
       os.system('python a.py')

B = Tkinter.Button(top, text ="Hello", command =helloCallBack)

B.pack()
top.mainloop()

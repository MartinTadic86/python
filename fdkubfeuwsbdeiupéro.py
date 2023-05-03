import tkinter as tk
from tkinter import messagebox

from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
def testfunction():
    showinfo(
        message='Hallo dis is Jamal from mikrosoft" " hau ar jú'    
    )
root = Tk()
root.geometry("250x250")
frm = ttk.Frame(root, padding=60)
frm.grid()
ttk.Label(frm, text="secret hacker stuff").grid(column=0, row=1)
ttk.Button(frm, text="secret hacker stuff.péro", command=testfunction).grid(column=0, row=2)
root.mainloop()
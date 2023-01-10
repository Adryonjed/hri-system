from imaplib import Commands
from turtle import onclick, position
from matplotlib import image, style
from matplotlib.pyplot import show
from tkinter import *
from db import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from tkinter.ttk import Progressbar
import tkinter as tk
import customtkinter
import time

def performance():
    f3 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8ad4c9")
    f3.place(x=380, y=200)

    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', font=('Arial', 12))

    sty = ttk.Style()
    sty.theme_use("default")
    sty.configure("Treeview", rowheight="50",fieldbackground = '#c9c9c7',background = '#c9c9c7')
    sty.configure("Treeview.Heading", font=(None, 15))
    sty.map('Treeview', background=[('selected', 'green')])

    fi = tk.StringVar()

    def ms(word,num):
        if num == 1:
            fi.set(word)

    def mouse_select():
        try:
            selected_item = my_tree.selection()[0]
            name = str(my_tree.item(selected_item)['values'][1])
    
            ms(name,1)
        except:
            messagebox.showinfo("Error", "Please select a data row")

    def dclick(e):
        mouse_select()


    my_tree =ttk.Treeview(f3, show="headings", height=12)
    my_tree['columns'] = ("id","name","sur","pos","dept")


    my_tree.column("id", anchor=CENTER, width=287)
    my_tree.column("name", anchor=W, width=287)
    my_tree.column("sur", anchor=W, width=287)
    my_tree.column("pos", anchor=W, width=287)
    my_tree.column("dept", anchor=W, width=287)


    my_tree.heading("id", text="ID", anchor=CENTER)
    my_tree.heading("name", text="NAME", anchor=CENTER)
    my_tree.heading("sur", text="SURNAME", anchor=CENTER)
    my_tree.heading("pos", text="POSITION", anchor=CENTER)
    my_tree.heading("dept", text="DEPARTMENT", anchor=CENTER)

    my_tree.place(x=27, y=27)
    my_tree.bind("<Double-1>", dclick)
    populate()
    refreshTable()  

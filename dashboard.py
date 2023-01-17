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


def dash():
    f1 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#d4b88a", corner_radius=50)
    f1.place(x=380, y=200)

    f1_1 = customtkinter.CTkFrame(f1, width=350, height=300, fg_color="#86babd",)
    f1_1.place(x=30, y=30)
    ln = Label(f1_1, text="Total Employees", font=('Arial', 20), background="#86babd")
    ln.place(x=10, y=10)

    f1_2 = customtkinter.CTkFrame(f1, width=350, height=300, fg_color="#95c791")
    f1_2.place(x=1100, y=30)
    ln2= Label(f1_2, text="department", font=('Arial', 20), background="#95c791")
    ln2.place(x=10, y=10)
    count2= Label(f1_2, text="9", font=('Arial', 70), background="#95c791", justify= CENTER)
    count2.place(relx=0.5, rely=0.5, anchor= CENTER)

    my_tree =ttk.Treeview()


    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', font=('Arial', 12))
        
        conn = connection()
        cursor = conn.cursor()
        em_number = cursor.execute("SELECT * FROM person")
        Label(f1_1, text=(em_number), font=('Arial', 70), background="#86babd").place(relx=0.5,rely=0.5, anchor=CENTER)


    


    def my_time():
        time_string = strftime('%I:%M:%S %p \n %A \n %x') # time format 
        l1.config(text=time_string)
        l1.after(1000,my_time) # time delay of 1000 milliseconds 

    my_font=('times',45,'bold') # display size and style
    l1=tk.Label(f1,font=my_font,bg="#d4b88a")
    l1.place(x=550, y=300)

    my_time()
    refreshTable()
from cProfile import label
from imaplib import Commands
from turtle import onclick, position
from matplotlib import image, style
from matplotlib.pyplot import show
from numpy import place
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from time import strftime
from tkcalendar import DateEntry
from datetime import date


def la_es (parent):
    
    pilabel = Label(parent, text="PERSONAL INFORMATION ", font=('Arial', 17),bg="#8ed1ba")
    pilabel.place(x=30, y=25)

    snlabel = Label(parent, text="SURNAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=85)
    snEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0, placeholder_text = "Name extension (Jr.,Sr.)",text_font=('Arial', 16,),placeholder_text_color= "gray",text_color='black').place(x=160, y=83)

    fnlabel = Label(parent, text="FIRSTNAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=135)
    fnEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0 ,text_font=('Arial', 16,),text_color='black').place(x=160, y=133)

    mnlabel = Label(parent, text="MIDDLENAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=185)
    mnEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0 ,text_font=('Arial', 16,),text_color='black').place(x=160, y=183)

    ctlabel = Label(parent, text="CITIZENSHIP : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=235)
    ctEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0 ,text_font=('Arial', 16,),text_color='black').place(x=160, y=233)


    btlabel = Label(parent, text="BLOOD TYPE : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=385)
    btt = tk.StringVar()
    bt = customtkinter.CTkOptionMenu(parent,width = 300,fg_color='white',text_font=('arial', 14),dropdown_text_font = ('arial', 14),dropdown_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = 'white',button_hover_color = 'gray',text_color = "black",variable = btt, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    bt.place(x=160, y= 383)
    bt.set("")

    tlabel = Label(parent, text="TEL NO. : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=435)
    tEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0 ,text_font=('Arial', 16),text_color='black').place(x=160, y=433)

    clabel = Label(parent, text="CEL NO. : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=485)
    cEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0 ,text_font=('Arial', 16),text_color='black').place(x=160, y=483)

    elabel = Label(parent, text="EMAIL : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=535)
    eEntry = customtkinter.CTkEntry(parent, width=500, fg_color='white',border_width = 0 ,text_font=('Arial', 16),text_color='black').place(x=160, y=533)

    eblabel = Label(parent, text="EDUCATIONAL BACKGROUND ", font=('Arial', 17),bg="#8ed1ba")
    eblabel.place(x=30, y=600)

    doblabel = Label(parent, text="DATE OF BIRTH : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=800, y=85)
    doblabel = DateEntry(parent, width=23, font = ('arial', 16), year=2019, month=6, day=22,background='gray', foreground='white', borderwidth=0, weekendbackground ="red",bd = 0)
    dt = date(2022,1,1)
    doblabel.set_date(dt)
    doblabel.place(x=950, y= 83)

    sexlabel = Label(parent, text="SEX : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=800, y=135)
    rb = tk.StringVar()
    r1 = customtkinter.CTkRadioButton(parent, text="Male", bd= 0, value='male',bg="#8ed1ba",variable=rb,cursor='hand2', text_font=('arial', 14),text_color='black').place(x=950,y= 135)
    r2 = customtkinter.CTkRadioButton(parent, text="Female",bd = 0, value='female',bg="#8ed1ba",variable=rb,cursor='hand2',text_font=('arial', 14),text_color='black').place(x=1050,y= 135)
    rb.set(None)

    statuslabel = Label(parent, text="CIVIL STATUS : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=800, y=185)
    cb = tk.StringVar()
    st = customtkinter.CTkOptionMenu(parent,width = 300,fg_color='white',text_font=('arial', 14),dropdown_text_font = ('arial', 14),dropdown_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = 'white',button_hover_color = 'gray',text_color = "black",variable = cb, values=["NARS", "DOKS", "HATDOG"])
    st.place(x=950, y= 183)
    st.set("")


    
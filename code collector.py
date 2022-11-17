from cProfile import label
from imaplib import Commands
from turtle import onclick, position
from matplotlib import image, style
from matplotlib.pyplot import show
from numpy import place
import numpy as np
from tkinter import *
from db import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from tkinter.ttk import Progressbar




def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='ewe',
    )
    return conn
pg = StringVar()
def show():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bayhon WHERE name=%s",(li.get(),))
    result = cursor.fetchone()
    drow = result
    if result:
        pg.set(drow)
    else:
        print('we')

addBtn = Button(
    window, text="Add", padx=5, pady=5, width=10,
    bd=5, font=('Arial', 15), bg="#f08080", command=show)

addBtn.place(x=720, y=350)

tasd = Label(window, text="", font=('Arial', 15),bg="#a3b18a",textvariable=pg)
tasd.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
li = Entry(window, width=20, bd=5, font=('Arial', 15))
li.grid(row=5, column=1, columnspan=4, padx=5, pady=0)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def validate(u_input): # callback function
    return u_input.isdigit()
my_valid = my_w.register(validate) # register 
l1=tk.Label(my_w,text='Enter Number only')
l1.grid(row=1,column=1,padx=20,pady=20)
e1 = Entry(my_w,validate='key',validatecommand=(my_valid,'%S'))
e1.grid(row=1,column=2,padx=20)

my_w.mainloop()

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(master=window,
                                 text="CTkButton",
                                 command=button_event,
                                 fg_color=("black",),
                                 bg_color= 'white',
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()



customtkinter.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("CustomTkinter simple_example.py")


def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)
    entry_1.get()


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=12, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=12, padx=10)
slider_1.set(0.5)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Name extension (Jr.,Sr.)",)
entry_1.pack(pady=12, padx=10)
en

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=12, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=12, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=12, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1)
switch_1.pack(pady=12, padx=10)


def dclick(e):
    select()

my_tree.bind("<Double-1>", dclick)

def entered(event):
    bttn.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1, width=42
    )
    
def left(event):
    bttn.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
       height=2, width=51
    ) 

bttn = Button(mbar, text='Dashboard',height=2, width=51, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f1))
bttn.place(x=-344, y=420)


bttn.config(activebackground="#476496")
bttn.config(activeforeground="#000000")

bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)


def entered2(event):
    bttn2.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
         height=1, width=43  
    )
    
def left2(event):
    bttn2.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
       height=2, width=51
    ) 

bttn2 = Button(mbar, text='Records',height=2, width=51, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f2))
bttn2.place(x=-360, y=500)

bttn2.config(activebackground="#476496")
bttn2.config(activeforeground="#000000")


bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

def entered3(event):
    bttn3.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
         height=1, width=41
    )
    
def left3(event):
    bttn3.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2, width=51
    ) 

bttn3 = Button(mbar, text='Performance',height=2, width=51, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f3))
bttn3.place(x=-330, y=590)

bttn3.config(activebackground="#476496")
bttn3.config(activeforeground="#000000")


bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)



def entered4(event):
    bttn4.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
         height=1, width=45
    )
    
def left4(event):
    bttn4.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
       height=2, width=51
    ) 

bttn4 = Button(mbar, text='Leave',height=2, width=51, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f4))
bttn4.place(x=-375, y=680)

bttn4.config(activebackground="#476496")
bttn4.config(activeforeground="#000000")


bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)



def entered5(event):
    bttn5.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1, width=44
    )
    
def left5(event):
    bttn5.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2, width=51
    )


bttn5 = Button(mbar, text='Report',height=2, width=51, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f5))
bttn5.place(x=-370, y=770)

bttn5.config(activebackground="#476496")
bttn5.config(activeforeground="#000000")

bttn5.bind("<Enter>", entered5)
bttn5.bind("<Leave>", left5)
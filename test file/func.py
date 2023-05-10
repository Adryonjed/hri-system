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


mainframe = tk.Frame(app, bg='#aee0e8')
mainframe.pack(side=tk.BOTTOM)
mainframe.pack_propagate(False)
mainframe.configure (width=1570, height=900)
mainframe.place(x=350,y=150)



def deletef():
    for frame in mainframe.winfo_children():
        frame.destroy()

def hide_indi():
    bttn.configure(fg_color="transparent")
    bttn2.configure(fg_color="transparent")
    bttn3.configure(fg_color="transparent")
    bttn4.configure(fg_color="transparent")
    bttn5.configure(fg_color="transparent")

def indicate (lb,page):
    hide_indi()
    lb.configure(fg_color = "red")
    deletef()
    page()

def entered(event):
    bttn.configure(text_color = '#d6af74')
    bttn.place_configure(x=-145,y=420)
    
def left(event):
    bttn.configure(text_color = 'white')
    bttn.place_configure(x=-170,y=420)
    


bttn = customtkinter.CTkButton(mbar, text='Dashboard',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= 'red',
cursor='hand2',command=lambda: indicate(bttn, dash))
bttn.place(x=-170, y=420)

bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)


def entered2(event):
    bttn2.configure(text_color = '#d6af74')
    bttn2.place_configure(x=-145,y=500)
    
def left2(event):
    bttn2.configure(text_color = 'white')
    bttn2.place_configure(x=-190,y=500)
    

bttn2 = customtkinter.CTkButton(mbar, text='Records',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn2, record))
bttn2.place(x=-190, y=500)
bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)



def entered3(event):
    bttn3.configure(text_color = '#d6af74')
    bttn3.place_configure(x=-145,y=580)
    
def left3(event):
    bttn3.configure(text_color = 'white')
    bttn3.place_configure(x=-160,y=580)

bttn3 =customtkinter.CTkButton(mbar, text='Performance',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn3,performance))
bttn3.place(x=-160, y=580)
bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)


def entered4(event):
    bttn4.configure(text_color = '#d6af74')
    bttn4.place_configure(x=-145,y=660)
    
def left4(event):
    bttn4.configure(text_color = 'white')
    bttn4.place_configure(x=-210,y=660)

bttn4 = customtkinter.CTkButton(mbar, text='Leave',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn4,leave))
bttn4.place(x=-210, y=660)
bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)



def entered5(event):
    bttn5.configure(text_color = '#d6af74')
    bttn5.place_configure(x=-145,y=740)
    
def left5(event):
    bttn5.configure(text_color = 'white')
    bttn5.place_configure(x=-198,y=740)

bttn5 = customtkinter.CTkButton(mbar, text='Reports',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn5,report))
bttn5.place(x=-198, y=740)
bttn5.bind("<Enter>", entered5)
bttn5.bind("<Leave>", left5)



#=========================================================================================frames=====================================================================================#

dash()

#=========================================================================================frames=====================================================================================#


photo = PIL.Image.open("Assets\\logo.png")
resized = photo.resize((200,200))
nphoto = ImageTk.PhotoImage(resized)

j = Label(app, image= nphoto, bg="#335791")
j.place(x=50, y=40)



app.state('zoomed')
app.mainloop()

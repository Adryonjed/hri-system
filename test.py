from cProfile import label
from imaplib import Commands
from turtle import onclick, position
from matplotlib import image, style
from matplotlib.pyplot import show
from numpy import place
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from setuptools import Command

app = Tk()
app.title("Human Resource Management System")
app.geometry("1920x1080")
app.resizable()
app.state('zoomed')
app.configure(bg='#c5c6c9')
app.iconbitmap("logo1.ico")
my_tree = ttk.Treeview(app)
my_tree2 = ttk.Treeview(app)

mbar = Frame(app, height=1060, width=350, bg="#5f8ad9", bd=1, relief=FLAT)



#dashboard#
f1 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#d4b88a")
#records#
f2 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8aafd4")
#Performance#
f3 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8ad4c9")
#Leave#
f4 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8a9dd4")
#Reports#
f5 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8ad494")

for frame in (f1,f2,f3,f4,f5):
    f1.place(x=380, y=200)


def show_frame(frame):
        frame.tkraise()
        
show_frame(f1)

def entered(event):
    bttn.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1,
        width=15,   
    )
    
def left(event):
    bttn.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2,
        width=21 
    ) 

bttn = Button(mbar, text='Dashboard',height=2, width=21, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f1))
bttn.place(x=-10, y=420)


bttn.config(activebackground="#476496")
bttn.config(activeforeground="#000000")

bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)


def entered2(event):
    bttn2.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1,
        width=15,   
    )
    
def left2(event):
    bttn2.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2,
        width=21 
    ) 

bttn2 = Button(mbar, text='Records',height=2, width=21, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f2))
bttn2.place(x=-10, y=500)

bttn2.config(activebackground="#476496")
bttn2.config(activeforeground="#000000")


bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

def entered3(event):
    bttn3.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1,
        width=15,   
    )
    
def left3(event):
    bttn3.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2,
        width=21 
    ) 

bttn3 = Button(mbar, text='Performance',height=2, width=21, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f3))
bttn3.place(x=-10, y=590)

bttn3.config(activebackground="#476496")
bttn3.config(activeforeground="#000000")


bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)



def entered4(event):
    bttn4.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1,
        width=15,   
    )
    
def left4(event):
    bttn4.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2,
        width=21 
    ) 

bttn4 = Button(mbar, text='Leave',height=2, width=21, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f4))
bttn4.place(x=-10, y=680)

bttn4.config(activebackground="#476496")
bttn4.config(activeforeground="#000000")


bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)



def entered5(event):
    bttn5.config(
        bg = "#5f8ad9",
        fg = "#000000",
        font = ("",30,"bold"),
        height=1,
        width=15,   
    )
    
def left5(event):
    bttn5.config(
        bg = "#5f8ad9",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2,
        width=21 
    ) 

bttn5 = Button(mbar, text='Report',height=2, width=21, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame(f5))
bttn5.place(x=-10, y=770)

bttn5.config(activebackground="#476496")
bttn5.config(activeforeground="#000000")

bttn5.bind("<Enter>", entered5)
bttn5.bind("<Leave>", left5)




#-------------------------------------------photo----------------------------------------------------#

photo = Image.open("logo.png")
resized = photo.resize((250,250), Image.ANTIALIAS)
nphoto = ImageTk.PhotoImage(resized)

j = Label(app, image= nphoto, bg="#5f8ad9")
j.place(x=40, y=10)


app.mainloop()

if onclick:
            lnEntry.delete(0,'end')
        return
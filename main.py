from tkinter import *
from db import *
from PIL import ImageTk
from time import strftime
import tkinter as tk
from tkinter import ttk
import customtkinter
import PIL.Image
from dashboard import *
from records import *
from perform import * 
from report import *
from leaves import *


app = tk.Tk()
app.title("Human Resource Management System")
app.geometry("1920x1080")

app.resizable(True,True)
app.configure(bg ='#aee0e8')
app.iconbitmap("Assets\\logo1.ico")


customtkinter.set_appearance_mode("System")

wel = Label(app, text="ROXAS MEMORIAL PROVINCIAL HOSPITAL", font=('Arial', 40, 'bold'),bg="#aee0e8")
wel.place(x=580,y=50)


mbar = customtkinter.CTkFrame(app, bg_color="transparent", fg_color="#335791",corner_radius=40)
mbar.pack(side=tk.LEFT)
mbar.pack_propagate (False)
mbar.configure (width=380, height=1060)
mbar.place(x=-35,y=0)

   
mainframe = tk.Frame(app, bg='#aee0e8')
mainframe.pack(side=tk.BOTTOM)
mainframe.pack_propagate(False)
mainframe.configure (width=1570, height=900)
mainframe.place(x=350,y=150)



def deletef():
    for frame in mainframe.winfo_children():
        frame.destroy()

def hide_indi():
    indicate1.config(bg="#335791")
    indicate2.config(bg="#335791")
    indicate3.config(bg="#335791")
    indicate4.config(bg="#335791")
    indicate5.config(bg="#335791")

def indicate (lb,page):
    hide_indi()
    lb.config(bg="#8abdb2")
    deletef()
    page()

def entered(event):
    bttn.configure(text_color = '#d6af74')
    bttn.place_configure(x=-145,y=420)
    
def left(event):
    bttn.configure(text_color = 'white')
    bttn.place_configure(x=-170,y=420)
    


bttn = customtkinter.CTkButton(mbar, text='Dashboard',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate1, dash))
bttn.place(x=-170, y=420)

bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)

indicate1 = tk.Label (mbar, text='', bg='#335791')
indicate1.place(x=-3, y= 420, width=13, height=80)

def entered2(event):
    bttn2.configure(text_color = '#d6af74')
    bttn2.place_configure(x=-145,y=500)
    
def left2(event):
    bttn2.configure(text_color = 'white')
    bttn2.place_configure(x=-190,y=500)
    

bttn2 = customtkinter.CTkButton(mbar, text='Records',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate2, record))
bttn2.place(x=-190, y=500)
bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

indicate2 = tk.Label (mbar, text='', bg='#335791')
indicate2.place(x=-3, y= 502,width=13, height=80)


def entered3(event):
    bttn3.configure(text_color = '#d6af74')
    bttn3.place_configure(x=-145,y=580)
    
def left3(event):
    bttn3.configure(text_color = 'white')
    bttn3.place_configure(x=-160,y=580)

bttn3 =customtkinter.CTkButton(mbar, text='Performance',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate3,performance))
bttn3.place(x=-160, y=580)
bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)

indicate3 = tk.Label (mbar, text='', bg='#335791')
indicate3.place(x=-3, y= 582, width=13, height=80)



def entered4(event):
    bttn4.configure(text_color = '#d6af74')
    bttn4.place_configure(x=-145,y=660)
    
def left4(event):
    bttn4.configure(text_color = 'white')
    bttn4.place_configure(x=-210,y=660)

bttn4 = customtkinter.CTkButton(mbar, text='Leave',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate4,leave))
bttn4.place(x=-210, y=660)
bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)

indicate4 = tk.Label (mbar, text='', bg='#335791')
indicate4.place(x=-3, y= 662, width=13, height=80)



def entered5(event):
    bttn5.configure(text_color = '#d6af74')
    bttn5.place_configure(x=-145,y=740)
    
def left5(event):
    bttn5.configure(text_color = 'white')
    bttn5.place_configure(x=-198,y=740)

bttn5 = customtkinter.CTkButton(mbar, text='Reports',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate5,report))
bttn5.place(x=-198, y=740)
bttn5.bind("<Enter>", entered5)
bttn5.bind("<Leave>", left5)

indicate5 = tk.Label (mbar, text='', bg='#335791')
indicate5.place(x=-3, y= 742, width=13, height=80)



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

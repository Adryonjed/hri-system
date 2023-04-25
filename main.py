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
from Perma import *


app = tk.Tk()
app.title("Human Resource Management System")
app.geometry("1920x1080")

app.resizable(True,True)
app.configure(bg ='#aee0e8')
app.iconbitmap("Assets\\logo1.ico")


customtkinter.set_appearance_mode("System")

wel = Label(app, text="ROXAS MEMORIAL PROVINCIAL HOSPITAL", font=('Arial', 40, 'bold'),bg="#aee0e8")
wel.place(x=580,y=50)


mbar = customtkinter.CTkFrame(app, bg_color="transparent", fg_color="#335791",corner_radius=40,width=380, height=1060)
mbar.pack(side=tk.LEFT)
mbar.pack_propagate (False)
mbar.place(x=-35,y=0)

mbarframe = customtkinter.CTkFrame(app, bg_color="transparent", fg_color="#335791",corner_radius=40, width=380, height=1060)
   
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
    bttn2.place_configure(x=-170,y=500)
    
def toggle_switch():
    global is_on
    is_on = not is_on
    update_switch()

def update_switch():
    if is_on:
        mbarframe.place(x=30,y=520)
        bttn5.place(x=-198, y=840)
        bttn4.place(x=-210, y=760)
        bttn3.place(x=-160, y=680)
        
    else:
        mbarframe.place_forget()
        bttn5.place(x=-198, y=740)
        bttn4.place(x=-210, y=660)
        bttn3.place(x=-160, y=580)
        

is_on = False

mbarframe = customtkinter.CTkFrame(mbar, bg_color="transparent", fg_color="red", width=350, height=150)


bttn2 = customtkinter.CTkButton(mbar, text='Employees',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn2, toggle_switch))
bttn2.place(x=-170, y=500)
bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

bttn2_1 = customtkinter.CTkButton(mbarframe, text='Records',height=50, width=300, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn2_1, permas))
bttn2_1.place(x=70, y=80)

bttn2_2 = customtkinter.CTkButton(mbarframe, text='Records',height=50, width=300, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn2_2, record))
bttn2_2.place(x=70, y=120)



def entered3(event):
    bttn3.configure(text_color = '#d6af74')
    wid = bttn3.winfo_y()
    bttn3.place_configure(x=-145,y=wid)
    
def left3(event):
    wid = bttn3.winfo_y()
    bttn3.configure(text_color = 'white')
    bttn3.place_configure(x=-160,y=wid)

bttn3 =customtkinter.CTkButton(mbar, text='Performance',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn3,performance))
bttn3.place(x=-160, y=580)
bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)


def entered4(event):
    wid = bttn4.winfo_y()
    bttn4.configure(text_color = '#d6af74')
    bttn4.place_configure(x=-145,y=wid)
    
def left4(event):
    wid = bttn4.winfo_y()
    bttn4.configure(text_color = 'white')
    bttn4.place_configure(x=-210,y=wid)

bttn4 = customtkinter.CTkButton(mbar, text='Leave',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn4,leave))
bttn4.place(x=-210, y=660)
bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)



def entered5(event):
    bttn5.configure(text_color = '#d6af74')

    wid = bttn5.winfo_y()
    bttn5.place_configure(x=-145,y=wid)
    
def left5(event):
    bttn5.configure(text_color = 'white')
   
    wid = bttn5.winfo_y()
    bttn5.place_configure(x=-198,y=wid)

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

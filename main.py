from tkinter import *
from database.db import *
from PIL import ImageTk
from time import strftime
import tkinter as tk
import customtkinter
import PIL.Image
from dashboard import *
from submenu.Ancillary import *
from report_submenu.report import *
from submenu.Nursing import *
from submenu.Admin import *
from submenu.Medical import *
from submenu.addEmployee import *
from leaveData import *
from ratingData import *
from report_submenu.highranking import *



app = tk.Tk()
app.title("Human Resource Management System")
app.geometry("1920x1080")

app.resizable(True,True)
app.configure(bg ='#aee0e8')
app.iconbitmap("Assets\\logo1.ico")

f2title = customtkinter.CTkFrame(app, width=1500, height=130, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
f2title.place(x=380, y=20)

mem= PIL.Image.open("Assets\\logo.png")
cap= PIL.Image.open("Assets\\capizlogo.png")
memor = customtkinter.CTkImage(mem,size=(100,100))
capiz = customtkinter.CTkImage(cap,size=(110,110))

logo1 = customtkinter.CTkLabel(f2title, text="",image=memor).place(x=220,y=15)
logo2 = customtkinter.CTkLabel(f2title, text="",image=capiz).place(x=1180,y=11)

tit = customtkinter.CTkLabel(f2title, text="Human Resource Information Management", font=("Arial", 40, 'bold'))
tit.place(x=350,y=20)
subtit = customtkinter.CTkLabel(f2title, text="Roxas Memorial Provincial Hospital", font=("Arial", 30))
subtit.place(x=490,y=80)



mbar = customtkinter.CTkFrame(app, bg_color="transparent", fg_color="#335791",corner_radius=40,width=380, height=1060)
mbar.pack(side=tk.LEFT)
mbar.pack_propagate (False)
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
    bttn.configure(fg_color="transparent")
    bttn2.configure(fg_color="transparent")
    bttn2_1.configure(fg_color="transparent",text_color ="white")
    bttn2_2.configure(fg_color="transparent",text_color ="white")
    bttn2_3.configure(fg_color="transparent",text_color ="white")
    bttn2_4.configure(fg_color="transparent",text_color ="white")
    bttn2_5.configure(fg_color="transparent",text_color ="white")
    bttn3.configure(fg_color="transparent")
    bttn4.configure(fg_color="transparent")
    bttn5.configure(fg_color="transparent")
    bttn5_1.configure(fg_color="transparent",text_color ="white")
    bttn5_5.configure(fg_color="transparent",text_color ="white")
    
def indicate (lb,page):
    hide_indi()
    lb.configure(fg_color = "#6e9fb8",text_color ="black")
    deletef()
    page()

def entered(event):
    bttn.configure(text_color = '#d6af74')
    bttn.place_configure(x=-115,y=320)
    
def left(event):
    bttn.configure(text_color = 'white')
    bttn.place_configure(x=-170,y=320)
    


bttn = customtkinter.CTkButton(mbar, text='Dashboard',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White',hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn, dash))
bttn.place(x=-170, y=320)

bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)


def entered2(event):
    bttn2.configure(text_color = '#d6af74')
    bttn2.place_configure(x=-115,y=400)
    
def left2(event):
    bttn2.configure(text_color = 'white')
    bttn2.place_configure(x=-170,y=400)
    
def toggle_switch():
    global is_on
    is_on = not is_on
    update_switch()

def update_switch():
    if is_on:
        mbarframe2.place_forget()
        mbarframe.place(x=30,y=420)
        bttn5.place(x=-198, y=880)
        bttn4.place(x=-210, y=800)
        bttn3.place(x=-160, y=720)
    else:
        mbarframe.place_forget()
        bttn5.place(x=-198, y=640)
        bttn4.place(x=-210, y=560)
        bttn3.place(x=-160, y=480)

global is_on
is_on = False   

mbarframe = customtkinter.CTkFrame(mbar, bg_color="transparent", fg_color="transparent", width=350, height=300)


bttn2 = customtkinter.CTkButton(mbar, text='Employees',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn2, toggle_switch))
bttn2.place(x=-170, y=400)
bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

bttn2_5 = customtkinter.CTkButton(mbarframe, text='ADD EMPLOYEE',height=50, width=700, fg_color="transparent", font=("", 20, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn2_5, add_e))
bttn2_5.place(x=-130, y=60)

bttn2_1 = customtkinter.CTkButton(mbarframe, text='ADMIN',height=50, width=700, fg_color="transparent", font=("", 20, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn2_1, adm))
bttn2_1.place(x=-175, y=110)


bttn2_2 = customtkinter.CTkButton(mbarframe, text='ANCILLARY',height=50, width=700, fg_color="transparent", font=("", 20, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn2_2, anci))
bttn2_2.place(x=-153, y=160)

bttn2_3 = customtkinter.CTkButton(mbarframe, text='MEDICAL',height=50, width=700, fg_color="transparent", font=("", 20, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn2_3, medic))
bttn2_3.place(x=-165, y=210)

bttn2_4 = customtkinter.CTkButton(mbarframe, text='NURSING',height=50, width=700, fg_color="transparent", font=("", 20, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn2_4, nurse))
bttn2_4.place(x=-165, y=260)



def entered3(event):
    bttn3.configure(text_color = '#d6af74')
    wid = bttn3.winfo_y()
    bttn3.place_configure(x=-118,y=wid)
    
def left3(event):
    wid = bttn3.winfo_y()
    bttn3.configure(text_color = 'white')
    bttn3.place_configure(x=-160,y=wid)

bttn3 =customtkinter.CTkButton(mbar, text='Performance',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn3,perform))
bttn3.place(x=-160, y=480)
bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)


def entered4(event):
    wid = bttn4.winfo_y()
    bttn4.configure(text_color = '#d6af74')
    bttn4.place_configure(x=-120,y=wid)
    
def left4(event):
    wid = bttn4.winfo_y()
    bttn4.configure(text_color = 'white')
    bttn4.place_configure(x=-210,y=wid)



bttn4 = customtkinter.CTkButton(mbar, text='Leave',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn4,leaves))
bttn4.place(x=-210, y=560)
bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)


def entered5(event):
    bttn5.configure(text_color = '#d6af74')
    wid = bttn5.winfo_y()
    bttn5.place_configure(x=-120,y=wid)
    
def left5(event):
    bttn5.configure(text_color = 'white')
    wid = bttn5.winfo_y()
    bttn5.place_configure(x=-198,y=wid)

def toggle_switch2():
    global is_onr
    is_onr = not is_onr
    update_switch2()

def update_switch2():
    if is_onr:
        mbarframe.place_forget()
        mbarframe2.place(x=30,y=660)
        bttn5.place(x=-198, y=640)
        bttn4.place(x=-210, y=560)
        bttn3.place(x=-160, y=480)
    else:
        mbarframe2.place_forget()
        
global is_onr
is_onr = False

mbarframe2 = customtkinter.CTkFrame(mbar, bg_color="transparent", fg_color="transparent", width=350, height=160)

bttn5 = customtkinter.CTkButton(mbar, text='Records',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(bttn5,toggle_switch2))
bttn5.place(x=-198, y=640)
bttn5.bind("<Enter>", entered5)
bttn5.bind("<Leave>", left5)

bttn5_1 = customtkinter.CTkButton(mbarframe2, text='HIGH RANKING OFFICALS',height=50, width=700, fg_color="transparent", font=("", 18, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn5_1, Highr))
bttn5_1.place(x=-130, y=60)

bttn5_5 = customtkinter.CTkButton(mbarframe2, text='DATA SHEET RECORDS',height=50, width=700, fg_color="transparent", font=("", 18, "bold"),text_color= 'White', hover_color= '#6fabc9',
cursor='hand2',command=lambda: indicate(bttn5_5, rept))
bttn5_5.place(x=-140, y=110)



#=========================================================================================frames=====================================================================================#

dash()

#=========================================================================================frames=====================================================================================#


photo = PIL.Image.open("Assets\\logo.png")
imgs = customtkinter.CTkImage(photo,size=(200,200))

j = customtkinter.CTkLabel(mbar, image=imgs, bg_color="#335791").place(x=90, y=40)

"""def my_time():
    time_string = strftime('%b %d, %Y \n %A') 
    l1.configure(text=time_string)
    l1.after(1000,my_time) 

my_font=('times',25,'bold')
l1=customtkinter.CTkLabel(f2title,font=my_font,bg_color="transparent")
l1.place(x=1330, y=35)

my_time()"""
app.state('zoomed')
app.mainloop()

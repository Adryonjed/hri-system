from tkinter import *
from db import *
from PIL import ImageTk, Image
from time import strftime
import tkinter as tk
from tkinter import ttk
import customtkinter
import PIL.Image
from dashboard import *
from records import *
from perform import *


app = tk.Tk()
app.title("Human Resource Management System")
app.geometry("1920x1080")

app.resizable(True,True)
app.state('zoomed')
app.configure(bg='#aee0e8')
app.iconbitmap("Assets\\logo1.ico")

wel = Label(app, text="ROXAS MEMORIAL PROVINCIAL HOSPITAL", font=('Arial', 40, 'bold'),bg="#aee0e8")
wel.place(x=580,y=50)


mbar = tk.Frame(app, background="#335791")
mbar.pack(side=tk.LEFT)
mbar.pack_propagate (False)
mbar.configure (width=330, height=1080)

mainframe = tk.Frame(app, bg='#aee0e8')
mainframe.pack(side=tk.BOTTOM)
mainframe.pack_propagate(False)
mainframe.configure (width=1570, height=900)


def deletef():
    for frame in mainframe.winfo_children():
        frame.destroy()

def hide_indi():
    indicate1.config(bg="#335791")
    indicate2.config(bg="#335791")
    indicate3.config(bg="#335791")
    indicate4.config(bg="#335791")

def indicate (lb,page):
    hide_indi()
    lb.config(bg="#b1c2de")
    deletef()
    page()

def entered(event):
    bttn.config(
        bg = "#335791",
        fg = "#7ddae8",
        font = ("",30,"bold"),
        height=1, width=42
    )
    
def left(event):
    bttn.config(
        bg = "#335791",
        fg = "#ffffff",
        font = ("",20,"bold"),
    height=2, width=51
    ) 


bttn = Button(mbar, text='Dashboard',height=2, width=51, bg="#335791", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: indicate(indicate1, dash))
bttn.place(x=-344, y=420)
bttn.config(activebackground="#476496")
bttn.config(activeforeground="#7ddae8")
bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)

indicate1 = tk.Label (mbar, text='', bg='#335791')
indicate1.place(x=3, y= 438, width=5, height=40)

def entered2(event):
    bttn2.config(
        bg = "#335791",
        fg = "#7ddae8",
        font = ("",30,"bold"),
        height=1, width=43  
    )
    
def left2(event):
    bttn2.config(
        bg = "#335791",
        fg = "#ffffff",
        font = ("",20,"bold"),
    height=2, width=51
    ) 

bttn2 = Button(mbar, text='Records',height=2, width=51, bg="#335791", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: indicate(indicate2, record))
bttn2.place(x=-360, y=500)
bttn2.config(activebackground="#476496")
bttn2.config(activeforeground="#7ddae8")
bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

indicate2 = tk.Label (mbar, text='', bg='#335791')
indicate2.place(x=3, y= 520, width=5, height=40)


def entered3(event):
    bttn3.config(
        bg = "#335791",
        fg = "#7ddae8",
        font = ("",30,"bold"),
        height=1, width=41
    )
    
def left3(event):
    bttn3.config(
        bg = "#335791",
        fg = "#ffffff",
        font = ("",20,"bold"),
        height=2, width=51
    ) 

bttn3 = Button(mbar, text='Performance',height=2, width=51, bg="#335791", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: indicate(indicate3,performance))
bttn3.place(x=-330, y=580)
bttn3.config(activebackground="#476496")
bttn3.config(activeforeground="#7ddae8")
bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)

indicate3 = tk.Label (mbar, text='', bg='#335791')
indicate3.place(x=3, y= 600, width=5, height=40)



def entered4(event):
    bttn4.config(
        bg = "#335791",
        fg = "#7ddae8",
        font = ("",30,"bold"),
        height=1, width=45
    )
    
def left4(event):
    bttn4.config(
        bg = "#335791",
        fg = "#ffffff",
        font = ("",20,"bold"),
    height=2, width=51
    ) 

bttn4 = Button(mbar, text='Leave',height=2, width=51, bg="#335791", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: indicate(indicate4,leave))
bttn4.place(x=-375, y=660)
bttn4.config(activebackground="#476496")
bttn4.config(activeforeground="#7ddae8")
bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)

indicate4 = tk.Label (mbar, text='', bg='#335791')
indicate4.place(x=3, y= 680, width=5, height=40)



#=========================================================================================frames=====================================================================================#

f1 = customtkinter.CTkFrame(mainframe, width=1500, height=820, fg_color ="#d4b88a", corner_radius=50)
f1.place(x=40, y=43)

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
    Label(f1_1, text=(em_number), font=('Arial', 70), background="#86babd").place(relx=0.5,rely=0.5, anchor="center")

def my_time():
    time_string = strftime('%I:%M:%S %p \n %A \n %x') # time format B
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
        
my_font=('times',45,'bold') # display size and style
l1=tk.Label(f1,font=my_font,bg="#d4b88a")
l1.place(x=550, y=300)

my_time()
refreshTable()





#=========================================================================================frames=====================================================================================#







photo = PIL.Image.open("Assets\\logo.png")
resized = photo.resize((200,200), PIL.Image.ANTIALIAS)
nphoto = ImageTk.PhotoImage(resized)

j = Label(app, image= nphoto, bg="#335791")
j.place(x=50, y=40)



app.state('zoomed')
app.mainloop()

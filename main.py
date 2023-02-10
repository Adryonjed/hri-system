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

customtkinter.set_appearance_mode("dark")

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
    lb.config(bg="#8abdb2")
    deletef()
    page()

def entered(event):
    bttn.configure(text_color = '#d6af74')
    bttn.place_configure(x=-145,y=420)
    
def left(event):
    bttn.configure(text_color = 'white')
    bttn.place_configure(x=-200,y=420)
    


bttn = customtkinter.CTkButton(mbar, text='Dashboard',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate1, dash))
bttn.place(x=-200, y=420)

bttn.bind("<Enter>", entered)
bttn.bind("<Leave>", left)

indicate1 = tk.Label (mbar, text='', bg='#335791')
indicate1.place(x=-3, y= 420, width=13, height=80)

def entered2(event):
    bttn2.configure(text_color = '#d6af74')
    bttn2.place_configure(x=-145,y=500)
    
def left2(event):
    bttn2.configure(text_color = 'white')
    bttn2.place_configure(x=-220,y=500)
    

bttn2 = customtkinter.CTkButton(mbar, text='Records',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate2, record))
bttn2.place(x=-220, y=500)
bttn2.bind("<Enter>", entered2)
bttn2.bind("<Leave>", left2)

indicate2 = tk.Label (mbar, text='', bg='#335791')
indicate2.place(x=-3, y= 502,width=13, height=80)


def entered3(event):
    bttn3.configure(text_color = '#d6af74')
    bttn3.place_configure(x=-145,y=580)
    
def left3(event):
    bttn3.configure(text_color = 'white')
    bttn3.place_configure(x=-190,y=580)

bttn3 =customtkinter.CTkButton(mbar, text='Performance',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate3,performance))
bttn3.place(x=-190, y=580)
bttn3.bind("<Enter>", entered3)
bttn3.bind("<Leave>", left3)

indicate3 = tk.Label (mbar, text='', bg='#335791')
indicate3.place(x=-3, y= 582, width=13, height=80)



def entered4(event):
    bttn4.configure(text_color = '#d6af74')
    bttn4.place_configure(x=-145,y=660)
    
def left4(event):
    bttn4.configure(text_color = 'white')
    bttn4.place_configure(x=-240,y=660)

bttn4 = customtkinter.CTkButton(mbar, text='Leave',height=80, width=600, fg_color="transparent", font=("", 30, "bold"),text_color= 'White', hover_color= '#335791',
cursor='hand2',command=lambda: indicate(indicate4,leave))
bttn4.place(x=-240, y=660)
bttn4.bind("<Enter>", entered4)
bttn4.bind("<Leave>", left4)

indicate4 = tk.Label (mbar, text='', bg='#335791')
indicate4.place(x=-3, y= 662, width=13, height=80)



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
    em_number = cursor.execute("SELECT * FROM personal")
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
resized = photo.resize((200,200))
nphoto = ImageTk.PhotoImage(resized)

j = Label(app, image= nphoto, bg="#335791")
j.place(x=50, y=40)



app.state('zoomed')
app.mainloop()

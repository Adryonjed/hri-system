from cProfile import label
from imaplib import Commands
from turtle import onclick, position
from matplotlib import image, style
from matplotlib.pyplot import show
from numpy import place
from tkinter import *
from db import populate
from db import read
from db import connection
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from time import strftime


app = Tk()
app.title("Human Resource Management System")
app.geometry("1920x1080")
app.resizable()
app.state('zoomed')
app.configure(bg='#c5c6c9')
app.iconbitmap("logo1.ico")



#-------------side manu functions-------------#
mbar = Frame (app, height=1060, width=350, bg="#5f8ad9", bd=1, relief=FLAT)
mbar.place(x=0, y=0)

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

#----------frame functions------------#

#dashboard#
f1 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#d4b88a")
f1_1 = customtkinter.CTkFrame(f1, width=350, height=300, fg_color="#86babd")
f1_1.place(x=30, y=30)
ln = Label(f1_1, text="persons", font=('Arial', 15), background="#86babd")
ln.place(x=10, y=10)
count= Label(f1_1, text="56", font=('Arial', 70), background="#86babd")
count.place(x=120, y=100)
f1_2 = customtkinter.CTkFrame(f1, width=350, height=300, fg_color="#86babd")
f1_2.place(x=400, y=30)
ln2= Label(f1_2, text="department", font=('Arial', 15), background="#86babd")
ln2.place(x=10, y=10)
count2= Label(f1_2, text="9", font=('Arial', 70), background="#86babd")
count2.place(x=140, y=100)


#records#


f2 = customtkinter.CTkFrame(app, width=1500, height=820, fg_color ="#8aafd4")
f2_1 = customtkinter.CTkFrame(app, width=1500, height=820, fg_color ="#8ed1ba")

s = ttk.Style()
s.configure("Treeview", rowheight="50")
s.map('Treeview', background=[('selected', 'green')])

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))


ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()

def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)


def add():
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    position = str(posEntry.get())
    department = str(depEntry.get())


    if (name == "" or name == " ") or (email == "" or email == " ") or (position == "" or position == " ") or (department == "" or department == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO firstt VALUES ('"+name+"','"+email+"','"+position+"','"+department+"')")
            conn.commit()
            conn.close()
            msg = messagebox.askquestion('',"Do you want to add this person?")
            if msg == 'yes':
                nameEntry.delete(0,'end')
                emailEntry.delete(0,'end')
                posEntry.delete(0,'end')
                depEntry.delete(0,'end')
            else:
                messagebox.showinfo('Return', 'You will now return to the application screen')
        except:
            messagebox.showinfo("Error", "Inventory already exist")
            return
        refreshTable()

for frame2 in (f2, f2_1):
    frame2.place(x=380, y=200)

def show_frame2(frame):
        frame.tkraise()
        
show_frame2(f2)
    

pho = Image.open("cbttn.png")
resized = pho.resize((120,70), Image.ANTIALIAS)
c_bbtn = ImageTk.PhotoImage(resized)

cbttn = Button(f2, image = c_bbtn ,bg="#8aafd4", borderwidth=0,
cursor='hand2',command=lambda: show_frame2(f2_1))
cbttn.place(x=1200, y=690)
cbttn.config(activebackground="#8aafd4")

bbttn = Button(f2_1, text='Back',height=2, width=11, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=lambda: show_frame2(f2))
bbttn.place(x=1000, y=700)

bbttn = Button(f2_1, text='add',height=2, width=11, bg="#5f8ad9", font=("", 20, "bold"), fg="white", bd=0,
cursor='hand2',command=add)
bbttn.place(x=1200, y=700)

namelabel = Label(f2_1, text="Name: ", font=('Arial', 15),bg="#8ed1ba")
namelabel.place(x=30, y=25)
nameEntry = Entry(f2_1, width=20, bd=0, font=('Arial', 15),textvariable = ph1)
nameEntry.place(x=100, y=27)

emaillabel = Label(f2_1, text="Email: ", font=('Arial', 15),bg="#8ed1ba")
emaillabel.place(x=330, y=25)
emailEntry = Entry(f2_1, width=20, bd=0, font=('Arial', 15),textvariable = ph2)
emailEntry.place(x=400, y=27)

poslabel = Label(f2_1, text="Position: ", font=('Arial', 15),bg="#8ed1ba")
poslabel.place(x=630, y=25)
posEntry = Entry(f2_1, width=20, bd=0, font=('Arial', 15),textvariable = ph3)
posEntry.place(x=720, y=27)

deplabel = Label(f2_1, text="Department: ", font=('Arial', 15),bg="#8ed1ba")
deplabel.place(x=950, y=25)
depEntry = Entry(f2_1, width=20, bd=0, font=('Arial', 15),textvariable = ph4)
depEntry.place(x=1070, y=27)







my_tree =ttk.Treeview(f2, show="headings", height=12)
my_tree['columns'] = ("name","email","position","department")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("name", anchor=W, width=360)
my_tree.column("email", anchor=W, width=360)
my_tree.column("position", anchor=W, width=360)
my_tree.column("department", anchor=W, width=360)


my_tree.heading("name", text="NAME", anchor=CENTER)
my_tree.heading("email", text="EMAIL", anchor=CENTER)
my_tree.heading("position", text="POSITION", anchor=CENTER)
my_tree.heading("department", text="DEPARTMENT", anchor=CENTER)


my_tree.place(x=27, y=27)

populate()
refreshTable()

#Performance#
f3 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8ad4c9")
#Leave#
f4 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8a9dd4")
#Reports#
f5 = customtkinter.CTkFrame(width=1500, height=820, fg_color ="#8ad494")


for frame in (f1,f2,f3,f4,f5):
    frame.place(x=380, y=200)

def show_frame(frame):
        frame.tkraise()
        
show_frame(f1)

#conn = connection()ewew
#cursor = conn.cursor()
#number_of_rows = cursor.execute("SELECT * FROM bayhon")
#Label(ff1, text=f"Total: {number_of_rows}", font=("Arial", 15),bg='#fbc4ab').place(x=850, y=450)

#------------------time function-------------------#
def my_time():
    time_string = strftime('%I:%M:%S %p \n %A \n %x') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',45,'bold') # display size and style

l1=tk.Label(f1,font=my_font,bg="#d4b88a")
l1.place(x=550, y=350)

my_time()

#-------------------------------------------photo----------------------------------------------------#

photo = Image.open("logo.png")
resized = photo.resize((250,250), Image.ANTIALIAS)
nphoto = ImageTk.PhotoImage(resized)

j = Label(app, image= nphoto, bg="#5f8ad9")
j.place(x=40, y=10)


app.mainloop()
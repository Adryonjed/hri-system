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


def change_appearance_mode_event(app, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)



def leave_his():
         conn = connection()
         cursor = conn.cursor()
         cursor.execute("SELECT datefile, fromdate, todate, days FROM leave WHERE ids=%s ORDER BY datefile DESC",(name))
         result = cursor.fetchall()

         i = 1
   
         for g in result:

               jo = Label(f3_2, text=g[1],font=('Arial', 14),background="#8ad4c9")
               jo.grid(row=i, column=1,padx=30,pady=10)
               jo2= Label(f3_2, text="Passed A Document",font=('Arial', 14),background="#8ad4c9",textvariable=g[0])
               jo2.grid(row=i, column=2,padx=30,pady=10)

               delp = customtkinter.CTkButton(f3_2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
               cursor='hand2')
               delp.grid(row= i, column = 3,pady=10,padx = 30)

               delp = customtkinter.CTkButton(f3_2,text="view",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
               cursor='hand2')
               delp.grid(row= i, column = 4,pady=10,padx = 30)

               delp = customtkinter.CTkButton(f3_2,text="save",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
               cursor='hand2')
               delp.grid(row= i, column = 5,pady=10,padx = 30)

               i = i+1

               if i == 4:
                  break
               

         conn.commit()
         conn.close()
      leave_his()

pdf.drawString(50,525,f'            CURRENT BALANCE :  Rs. {cashData[2]}')

"SELECT id FROM rating GROUP BY id"

my_path = "C:\\Users\\ferna\\Downloads\\jed.pdf"

c = canvas.Canvas(my_path,pagesize=GOV_LEGAL)
c.setFillColorRGB(0,0,1)
c.drawString(20, 10, 'Hello world')
c.showPage()
c.save()

my_w = tk.Tk()
my_w.geometry("380x200")  
sel=tk.StringVar() # declaring string variable 

cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.grid(row=1,column=1,padx=20)

def my_upd(*args): # triggered when value of string varaible changes
    if(len(sel.get())>4):
        l1.config(text=sel.get()) # read and display date
        dob = datetime.strptime(sel.get(),'%m/%d/%y')
        dt=date.today()
        dt3=relativedelta(dt,dob)
        l2.config(text="Years:"+ str(dt3.years) )
l1=tk.Label(my_w,bg='yellow')  # Label to display date 
l1.grid(row=1,column=2)

l2=tk.Label(my_w)  # Label to display date 
l2.grid(row=1,column=3,padx=10)

sel.trace('w',my_upd) # on change of string variable 
my_w.mainloop()



conn = connection()
                cursor = conn.cursor()
                cursor.execute("INSERT * FROM personal WHERE id=%s",(find2Entry.get()))
                
                
                i = 1
                
                for g in cursor:

                    jo = Label(f3_2, text=g[5],font=('Arial', 50))
                    jo.grid(row=i, column=1, ipadx= 10,padx=20)
                    
                    jo2 = Label(f3_2,  text='', font=('Arial', 50))
                    jo2.grid(row=i, column=2, ipadx= 10,padx=20)

                    delp = customtkinter.CTkButton(f3_2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,hover_color = '#2a4859',cursor='hand2')
                    delp.grid(row= i, column = 3)

                    if i == 4:
                        break
                    i = i+1
                

                conn.commit()
                conn.close()


         def upload():

            global file
            f_types = [('All Files', '*.*'), 
                    ('JPG', '*.jpg'),
                    ('PNG', '*.png'),('DOCX','*.docx')]
            file = filedialog.askopenfilename(filetypes=f_types)
            fob = open(file, 'rb').read()
            conn = connection()
            cursor = conn.cursor()
            args = (res.cget("text"),dobbs.get_date(),fob)

            
            query = 'INSERT * INTO image (id,date,img) VALUES (%s,%s,%s)'
            cursor.execute(query, args)
            conn.commit()


cursor.execute("UPDATE residential SET houseblock = '"+res1+"', street = '"+res2+"', subd  = '"+res3+"', brgy = '"+res4+"', city = '"+res5+"', province = '"+res6+"', zip = '"+res7+"'  ")
cursor.execute("UPDATE permanent SET houseblock = '"+per1+"', street = '"+per2+"', subd  = '"+per3+"', brgy = '"+per4+"', city = '"+per5+"', province = '"+per6+"', zip = '"+per7+"'  ")
cursor.execute("UPDATE spouse SET surname = '"+sposn+"', firstname = '"+spofn+"', middlename  = '"+spomn+"', occupation = '"+spooc+"', businessname = '"+spoebn+"', businessadd = '"+spoba+"', telephone = '"+spotel+"'  ")
cursor.execute("UPDATE family SET fathersn = '"+fsn+"', fatherfn = '"+ffn+"', fathermn  = '"+fmn+"', mothermn = '"+mmn+"', mothersn = '"+msn+"', motherfn = '"+mfn+"', mothermmn = '"+mmd+"'  ")
cursor.execute("UPDATE elementary SET school = '"+ens+"', degree = '"+ebdc+"', froms  = '"+efrom+"', tos = '"+eto+"', units = '"+ehigh+"', graduated = '"+eyg+"', acads = '"+esa+"' ")
cursor.execute("UPDATE highschool SET school = '"+hsns+"', degree = '"+hsbdc+"', froms  = '"+hsfrom+"', tos = '"+hsto+"', units = '"+hshigh+"', graduated = '"+hsyg+"', acads = '"+hssa+"'  ")
cursor.execute("UPDATE vocational SET school = '"+vtns+"', degree = '"+vtbdc+"', froms  = '"+vtfrom+"', tos = '"+vtto+"', units = '"+vthigh+"', graduated = '"+vtyg+"', acads = '"+vtsa+"'  ")
cursor.execute("UPDATE college SET school = '"+cns+"', degree = '"+cbdc+"', froms  = '"+cfrom+"', tos = '"+cto+"', units = '"+chigh+"', graduated = '"+cyg+"', acads = '"+csa+"'  ")
cursor.execute("UPDATE graduate SET school = '"+gns+"', degree = '"+gbdc+"', froms  = '"+gfrom+"', tos = '"+gto+"', units = '"+ghigh+"', graduated = '"+gyg+"', acads = '"+gsa+"'  ")

  
if mnshow.cget("text") == "male":
         mnshow.place(x=300,y=400)
      else:
         mnshow.place(x=300,y=300)

   def imported():
            f3_2 = customtkinter.CTkFrame(None, fg_color ="#8ad4c9")
            f3_2.place(x=1000, y=400)
            
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM image WHERE id=%s ORDER BY date DESC",(find2Entry.get()))  
            i = 1
            
            for g in cursor:

                jo = Label(f3_2, text=g[2],font=('Arial', 50))
                jo.grid(row=i, column=1, ipadx= 10,padx=20)
                
                jo2 = Label(f3_2,  text='imported', font=('Arial', 50),textvariable=g[1])
                jo2.grid(row=i, column=2, ipadx= 10,padx=20)

                delp = customtkinter.CTkButton(f3_2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
                hover_color = '#2a4859',cursor='hand2')
                delp.grid(row= i, column = 3)

                if i == 4:
                    break
                i = i+1

            conn.commit()
            conn.close()
       
def my_upd(value):
    my_str=t1.get('1.0','end-1c') #The input string except the last line break
    breaks=my_str.count('\n') # Number of line breaks ( except the last one )
    char_numbers=len(my_str)-breaks # Number of chars user has entered 
    l2.config(text=str(char_numbers)) # display number of chars 
    if(char_numbers > 20):
        t1.delete('end-2c') # remove last char of text widget
t1.bind('<KeyRelease>',my_upd) # Key release event to call function.  
        



def my_upd(value):
            my_str=htEntry.get()
            char_numbers=len(my_str)
            if(char_numbers > 10):
               htEntry.delete(10,END)

        htEntry.bind('<KeyRelease>',my_upd)


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
from tkinter import *
from database.db import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from tkinter import filedialog
from PIL import Image, ImageTk
import PIL.Image
import math
import base64
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime




def show_edit(s_ids):

    root = customtkinter.CTkToplevel()
    root.geometry('800x900')
    root.overrideredirect(True)
    root.title("Rating Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()

    p_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=800,height=900,corner_radius=30)
    p_frame.pack()

    f2title = customtkinter.CTkFrame(p_frame, width=770, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=20, y=60)

    tit = customtkinter.CTkLabel(f2title, text="PERFORMANCE EVALUATION RATING", font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text="Rate based on your performance", font=("Arial", 20))
    subtit.place(x=20,y=60)

    def start_drag(e):
        e.widget.offset = (e.x, e.y)

    def move_app(e):
        root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')


    ide = tk.StringVar()
    crii1 = tk.StringVar()
    crii2 = tk.StringVar()
    crii3 = tk.StringVar()
    crii4 = tk.StringVar()
    crii5 = tk.StringVar()
    crii6 = tk.StringVar()


    def store(word,num):
        if num == 1:
            ide.set(word)
        if num == 2:
            crii1.set(word)
        if num == 3:
            crii2.set(word)
        if num == 4:
            crii3.set(word)
        if num == 5:
            crii4.set(word)
        if num == 6:
            crii5.set(word)
        if num == 7:
            crii6.set(word)

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM perform WHERE ide = %s",(s_ids))
    results = cursor.fetchone()
    store(results[0],1)
    fname = results[3]
    sname = results[4]
    store(results[5],2)
    store(results[6],3)
    store(results[7],4)
    store(results[8],5)
    store(results[9],6)
    store(results[10],7)
    conn.commit()
    conn.close()
    
    
    

    nat = datetime.now() 
    now = nat.strftime("%b %d, %Y")
    doblabel = Label(text=now)
  
    def start_drag(e):
            e.widget.offset = (e.x, e.y)

    def move_app(e):
        root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')



    def cancels():
        root.destroy()

    def solve(): 
        global ttl, average

        c1 = int(cr1.get())
        c2 = int(cr2.get())
        c3 = int(cr3.get())
        c4 = int(cr4.get())
        c5 = int(cr5.get())
        c6 = int(cr6.get())

        ttal = c1 + c2 + c3 + c4 + c5 + c6
        tots.configure(text=str(ttal))
        ttl = str(ttal)

        aver = ttal / 6
        avera.configure(text='{:.2f}'.format(aver))
        average = str(aver)


    def validate(u_input): 
            return u_input.isdigit()
    
    my_valid = p_frame.register(validate)

    idd = Label(textvariable=ide)

    def proceed():

        idss = str(idd.cget("text"))
        ffname = str(fname)
        ssname = str(sname)
        dfile = str(doblabel.cget("text"))
        cri1 = str(cr1.get())
        cri2 = str(cr2.get())
        cri3 =  str(cr3.get())
        cri4 =  str(cr4.get())
        cri5 = str(cr5.get())
        cri6 = str(cr6.get())

    
        if (cri1 == "" or cri1 == " ") or (cri2 == "" or cri2 == " ") or (cri3 == "" or cri3 == " ") or (cri4 == "" or cri4 == " ") or (cri5 == "" or cri5 == " ") or (cri6 == "" or cri6 == " "):
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
        else:
                try:
                    msg = messagebox.askquestion('',"Do you want to Update this data?")
                    if msg == 'yes':
                        conn = connection()
                        cursor = conn.cursor()
                        cursor.execute("UPDATE perform SET datefile = '"+dfile+"', fname = '"+ffname+"', sname = '"+ssname+"', cr1 = '"+cri1+"', cr2 = '"+cri2+"', cr3 = '"+cri3+"', cr4 = '"+cri4+"', cr5 = '"+cri5+"', cr6 = '"+cri6+"', totals = '"+ttl+"', averages = '"+average+"' WHERE ide = '"+idss+"' ")
                        conn.commit()
                        conn.close()
                        root.destroy()
                    elif msg == 'no':
                        pass
                    else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                        root.destroy()
                       
                except:
                    messagebox.showinfo("Error", "Data already exist")
                    return
        

    def allsave():
        proceed()


    criteria = customtkinter.CTkLabel(p_frame, text="Criteria", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=270, y=200)

    rating = customtkinter.CTkLabel(p_frame, text="Rate", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=655, y=200)


    cr1label = customtkinter.CTkLabel(p_frame, text="Appearance / wears prescribed uniform with ID ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=250)
    cr1 = customtkinter.CTkEntry(p_frame, textvariable= crii1,height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr1.place(x=650, y=250)

    cr2label = customtkinter.CTkLabel(p_frame, text="Respectful, courteous and considerate", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=300)
    cr2 = customtkinter.CTkEntry(p_frame, textvariable= crii2, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr2.place(x=650, y=300)

    cr3label = customtkinter.CTkLabel(p_frame, text="Performs Porter function with regards \n to transfer of patients", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=350)
    cr3 = customtkinter.CTkEntry(p_frame,textvariable= crii3, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr3.place(x=650, y=350)

    cr4label = customtkinter.CTkLabel(p_frame, text="Performance of job delegated by Nurse Supervisor", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=400)
    cr4 = customtkinter.CTkEntry(p_frame,textvariable= crii4, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr4.place(x=650, y=400)

    cr5label = customtkinter.CTkLabel(p_frame, width = 2, text="Compliance with the existing terms and conditions \nas stated in the Memorandum of Agreement (MOA) \nwith documents required for submission", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=450)
    cr5 = customtkinter.CTkEntry(p_frame,textvariable= crii5, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr5.place(x=650, y=460)

    cr6label = customtkinter.CTkLabel(p_frame, text="Follows the infection control procedures ensures \nthat Universal Precaution protocols are followed", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=520)
    cr6 = customtkinter.CTkEntry(p_frame,textvariable= crii6, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr6.place(x=650, y=520)

    crilabel = customtkinter.CTkLabel(p_frame, text="(On a scale of 1 - 5, 1 being the lowest and 5 the highest rating)", font=('Courier', 18, "bold"),bg_color="transparent", text_color="black").place(x=30, y=590)

    totl = customtkinter.CTkLabel(p_frame, text="Total", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=660)
    tots = customtkinter.CTkLabel(p_frame, text=results[11],font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
    tots.place(x=650, y=660)

    aver = customtkinter.CTkLabel(p_frame, text="Average", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=700)
    avera = customtkinter.CTkLabel(p_frame, text=results[12], font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
    avera.place(x=650, y=700)


    sol = customtkinter.CTkButton(p_frame,text="count",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= solve)
    sol.place(x=70, y=750)

            
    proc = customtkinter.CTkButton(p_frame,text="Proceed",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=120, height=55, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2', command= allsave)
    proc.place(x=630, y=810)

    can = PIL.Image.open("Assets\\cancel.png")
    checked2 = customtkinter.CTkImage(can,size=(30,30))
    cancel = customtkinter.CTkButton(p_frame, text="", image=checked2, bg_color= 'white',fg_color="white",hover_color= "#8a8987", width= 20,cursor='hand2',command=cancels)
    cancel.place(x=740,y=10)


    
    root.bind("<Button-1>", start_drag)
    root.bind("<B1-Motion>", move_app)

    root.mainloop()


    


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
import io
from PIL import ImageGrab
from ratingForm.EditRating import *


def show_perform(s_id):
      
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal WHERE id=%s",(s_id))
    result = cursor.fetchone()
    ide = result[0]
    fname = result[2]
    sname = result[1]
    conn.commit()
    conn.close()
    

    f4_1 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#d4d4d4",bg_color="transparent",corner_radius=50)
    f4_1.place(x=380, y=200)

    nat = datetime.now() 
    now = nat.strftime("%b %d, %Y")

    f2title = customtkinter.CTkFrame(f4_1, width=1450, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=20, y=20)

    tit = customtkinter.CTkLabel(f2title, text=result[2], font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text=result[1] + " - " + result[17], font=("Arial", 20))
    subtit.place(x=20,y=60)
    doblabel = customtkinter.CTkLabel(f2title,text=now, font=('Arial', 16, 'bold'))
    doblabel.place(x=1330, y=20)

    
    f5_2 = customtkinter.CTkScrollableFrame(f4_1, fg_color ="transparent",bg_color ="transparent", width= 1380,height= 500)
    f5_2.place(x=50, y=150)


    ed = PIL.Image.open("Assets\\edit.png")
    edt = customtkinter.CTkImage(ed,size=(25,25))

    def show_data():
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM perform WHERE ids = %s",(s_id))
        result = cursor.fetchall()
        conn.commit()
        conn.close()
    

        i = 1

        tableframe = customtkinter.CTkFrame(f4_1,fg_color ="transparent",bg_color ="transparent",width=1200,height=50)
        tableframe.place(x=55,y=150)

        dfile = customtkinter.CTkLabel(tableframe, text="Date Filed                                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dfile.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

        tol = customtkinter.CTkLabel(tableframe, text="Total                                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        tol.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

        dayss = customtkinter.CTkLabel(tableframe, text="Average                                             ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dayss.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

        aps = customtkinter.CTkLabel(tableframe, text="Action     ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        aps.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)


        for g2 in result:
            

            dfile2 = customtkinter.CTkLabel(f5_2, text="                                                       ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=0,padx=35,pady=10,sticky = NSEW)

            tol2 = customtkinter.CTkLabel(f5_2, text="                                              ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol2.grid(row=0, column=1,padx=35,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f5_2, text="                                ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=2,padx=35,pady=10,sticky = NSEW)

            ap2 = customtkinter.CTkLabel(f5_2, text="      ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ap2.grid(row=0, column=3,padx=35,pady=10,sticky = NSEW)

            
            jo = customtkinter.CTkLabel(f5_2, text=g2[2],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo.grid(row=i, column=0,padx=5,pady=10,sticky = NSEW)
            jo2= customtkinter.CTkLabel(f5_2, text=g2[11],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
            jo3= customtkinter.CTkLabel(f5_2, text=g2[12],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo3.grid(row=i, column=2,padx=5,pady=10,sticky = NSEW)
           
            shoow = customtkinter.CTkButton(f5_2,text="",image= edt, fg_color='#46729c',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=g2[0]:showit(k))
            shoow.grid(row= i, column = 4,pady=5,padx = 3)

            i = i+1
    
    show_data()

    def showit(s_ide):
        show_edit(s_ide)


    def apply():
        root = customtkinter.CTkToplevel()
        root.geometry('800x900')
        root.overrideredirect(True)
        root.title("Rating Form")
        root.wm_attributes("-transparentcolor",'#333333')
        root.wait_visibility()
        root.grab_set()

        

        def start_drag(e):
            e.widget.offset = (e.x, e.y)

        def move_app(e):
            root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')


        l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=800,height=900,corner_radius=30)
        l_frame.pack()

        f2title = customtkinter.CTkFrame(l_frame, width=770, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
        f2title.place(x=20, y=60)

        tit = customtkinter.CTkLabel(f2title, text="PERFORMANCE EVALUATION RATING", font=("Arial", 30, 'bold'))
        tit.place(x=20,y=20)
        subtit = customtkinter.CTkLabel(f2title, text="Rate based on your performance", font=("Arial", 20))
        subtit.place(x=20,y=60)


        def cancels():
            root.destroy()
            aply.configure(state = NORMAL)

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
        my_valid = l_frame.register(validate)


        def proceed():

            idss = str(ide)
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
                        msg = messagebox.askquestion('',"Do you want to add this person?")
                        if msg == 'yes':
                            conn = connection()
                            cursor = conn.cursor()
                            cursor.execute(
                                "INSERT INTO perform VALUES ('""','"+idss+"','"+dfile+"','"+ffname+"','"+ssname+"','"+cri1+"','"+cri2+"','"+cri3+"','"+cri4+"','"+cri5+"','"+cri6+"','"+ttl+"','"+average+"') ")
                            conn.commit()
                            conn.close()
                            root.destroy()
                            aply.configure(state = NORMAL)
                        elif msg == 'no':
                            pass
                        else:
                            messagebox.showinfo('Return', 'You will now return to the application screen')
                            root.destroy()
                            aply.configure(state = NORMAL)
                    except:
                        messagebox.showinfo("Error", "Data already exist")
                        return
            show_data()

        def allsave():
            proceed()


        criteria = customtkinter.CTkLabel(l_frame, text="Criteria", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=270, y=200)

        rating = customtkinter.CTkLabel(l_frame, text="Rate", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=655, y=200)

        cr1label = customtkinter.CTkLabel(l_frame, text="Appearance / wears prescribed uniform with ID ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=250)
        cr1 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr1.place(x=650, y=250)

        cr2label = customtkinter.CTkLabel(l_frame, text="Respectful, courteous and considerate", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=300)
        cr2 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr2.place(x=650, y=300)

        cr3label = customtkinter.CTkLabel(l_frame, text="Performs Porter function with regards \n to transfer of patients", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=350)
        cr3 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr3.place(x=650, y=350)

        cr4label = customtkinter.CTkLabel(l_frame, text="Performance of job delegated by Nurse Supervisor", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=400)
        cr4 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr4.place(x=650, y=400)

        cr5label = customtkinter.CTkLabel(l_frame, width = 2, text="Compliance with the existing terms and conditions \nas stated in the Memorandum of Agreement (MOA) \nwith documents required for submission", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=450)
        cr5 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr5.place(x=650, y=460)

        cr6label = customtkinter.CTkLabel(l_frame, text="Follows the infection control procedures ensures \nthat Universal Precaution protocols are followed", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=520)
        cr6 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr6.place(x=650, y=520)

        crilabel = customtkinter.CTkLabel(l_frame, text="(On a scale of 1 - 5, 1 being the lowest and 5 the highest rating)", font=('Courier', 18, "bold"),bg_color="transparent", text_color="black").place(x=30, y=590)

        totl = customtkinter.CTkLabel(l_frame, text="Total", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=660)
        tots = customtkinter.CTkLabel(l_frame, text="", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
        tots.place(x=650, y=660)

        aver = customtkinter.CTkLabel(l_frame, text="Average", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=700)
        avera = customtkinter.CTkLabel(l_frame, text="", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
        avera.place(x=650, y=700)


        sol = customtkinter.CTkButton(l_frame,text="count",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command= solve)
        sol.place(x=70, y=750)
        
               
        proc = customtkinter.CTkButton(l_frame,text="Proceed",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=120, height=55, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2', command= allsave)
        proc.place(x=630, y=810)

        can = PIL.Image.open("Assets\\cancel.png")
        checked2 = customtkinter.CTkImage(can,size=(30,30))
        cancel = customtkinter.CTkButton(l_frame, text="", image=checked2, bg_color= 'white',fg_color="white",hover_color= "#8a8987", width= 20,cursor='hand2',command=cancels)
        cancel.place(x=740,y=10)

        aply.configure(state = DISABLED)

        root.bind("<Button-1>", start_drag)
        root.bind("<B1-Motion>", move_app)

        root.mainloop()


    aply = customtkinter.CTkButton(f4_1,text="Rate Data",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=apply)
    aply.place(x=1200, y=700)



    show_data()
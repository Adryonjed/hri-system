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
from ratingForm.exprtdata import *


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

    dl = PIL.Image.open("Assets\\downloads.png")
    dwl = customtkinter.CTkImage(dl,size=(25,25))

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

        dfile = customtkinter.CTkLabel(tableframe, text="Date Filed                             ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dfile.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

        tol = customtkinter.CTkLabel(tableframe, text="Total                                  ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        tol.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

        dayss = customtkinter.CTkLabel(tableframe, text="Average                            ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dayss.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

        dayss = customtkinter.CTkLabel(tableframe, text="Scale                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dayss.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

        aps = customtkinter.CTkLabel(tableframe, text="Action     ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        aps.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)


        for g2 in result:
            

            dfile2 = customtkinter.CTkLabel(f5_2, text="                                         ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=0,padx=35,pady=10,sticky = NSEW)

            tol2 = customtkinter.CTkLabel(f5_2, text="                                    ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol2.grid(row=0, column=1,padx=35,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f5_2, text="                            ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=2,padx=35,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f5_2, text="                        ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=3,padx=35,pady=10,sticky = NSEW)

            ap2 = customtkinter.CTkLabel(f5_2, text="   ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ap2.grid(row=0, column=4,padx=35,pady=10,sticky = NSEW)

            
            jo = customtkinter.CTkLabel(f5_2, text=g2[2],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo.grid(row=i, column=0,padx=5,pady=10,sticky = NSEW)
            jo2= customtkinter.CTkLabel(f5_2, text=g2[15],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
            jo3= customtkinter.CTkLabel(f5_2, text=g2[16],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo3.grid(row=i, column=2,padx=5,pady=10,sticky = NSEW)
            jo3= customtkinter.CTkLabel(f5_2, text=g2[17],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo3.grid(row=i, column=3,padx=5,pady=10,sticky = NSEW)
           
            shoow = customtkinter.CTkButton(f5_2,text="",image= edt, fg_color='#46729c',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=g2[0]:showit(k))
            shoow.grid(row= i, column = 4,pady=5,padx = 3)

            expt = customtkinter.CTkButton(f5_2,text="",image= dwl, fg_color='#9c9346',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=g2[0]:exprtit(k))
            expt.grid(row= i, column = 5,pady=5,padx = 3)

            i = i+1
    
    show_data()

    def showit(s_ide):
        show_edit(s_ide)

    def exprtit(s_ide):
        saveasfile(s_ide)



    def apply():
        root = customtkinter.CTkToplevel()
        root.geometry('800x1000+650+50')
        root.overrideredirect(True)
        root.title("Rating Form")
        root.wm_attributes("-transparentcolor",'#333333')
        root.wait_visibility()
        root.grab_set()


        l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=800,height=1000,corner_radius=30)
        l_frame.pack()

        f2title = customtkinter.CTkFrame(l_frame, width=770, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
        f2title.place(x=15, y=20)

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
            c7 = int(cr7.get())
            c8 = int(cr8.get())
            c9 = int(cr9.get())
            c10 = int(cr10.get())

            ttal = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
            tots.configure(text=str(ttal))
            ttl = str(ttal)

            aver = ttal / 10
            avera.configure(text='{:.2f}'.format(aver))
            average = str(aver)

            if aver == 5.0:
                 scl.configure(text = 'Outstanding')
            elif aver <= 4.9 and aver >= 4.0:
                 scl.configure(text = 'Very Good')
            elif aver <= 3.9 and aver >= 3.0:
                 scl.configure(text = 'Average')
            elif aver <= 2.9 and aver >= 2.0:
                 scl.configure(text = 'Below Average')
            elif aver <= 1.9 and aver >= 1.0:
                 scl.configure(text = 'Poor')
                 


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
            cri7 = str(cr7.get())
            cri8 = str(cr8.get())
            cri9 = str(cr9.get())
            cri10 = str(cr10.get())
            scle  = str(scl.cget("text"))

        
            if (cri1 == "" or cri1 == " ") or (cri2 == "" or cri2 == " ") or (cri3 == "" or cri3 == " ") or (cri4 == "" or cri4 == " ") or (cri5 == "" or cri5 == " ") or (cri6 == "" or cri6 == " ") or (cri7 == "" or cri7 == " ") or (cri8 == "" or cri8 == " ") or (cri9 == "" or cri9 == " ") or (cri10 == "" or cri10 == " "):
                    messagebox.showinfo("Error", "Please fill up the blank entry")
                    return
            else:
                    try:
                        msg = messagebox.askquestion('',"Do you want to add this person?")
                        if msg == 'yes':
                            conn = connection()
                            cursor = conn.cursor()
                            cursor.execute(
                                "INSERT INTO perform VALUES ('""','"+idss+"','"+dfile+"','"+ffname+"','"+ssname+"','"+cri1+"','"+cri2+"','"+cri3+"','"+cri4+"','"+cri5+"','"+cri6+"' ,'"+cri7+"' ,'"+cri8+"' ,'"+cri9+"' ,'"+cri10+"' ,'"+ttl+"','"+average+"','"+scle+"') ")
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


        criteria = customtkinter.CTkLabel(l_frame, text="Criteria", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=270, y=150)

        rating = customtkinter.CTkLabel(l_frame, text="Rate", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=655, y=150)

        cr1label = customtkinter.CTkLabel(l_frame, text="Clear understanding of the signed job description: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=200)
        cr1 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr1.place(x=650, y=200)

        cr2label = customtkinter.CTkLabel(l_frame, text="Possess timelines in the job/Efficiency in assigned job: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=250)
        cr2 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr2.place(x=650, y=250)

        cr3label = customtkinter.CTkLabel(l_frame, text="Meet expectations/targets consistently?: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=300)
        cr3 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr3.place(x=650, y=300)

        cr4label = customtkinter.CTkLabel(l_frame, text="Maintain prescribed quality in work?: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=350)
        cr4 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr4.place(x=650, y=350)

        cr5label = customtkinter.CTkLabel(l_frame, width = 2, text="Follow policies & procedures: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=400)
        cr5 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr5.place(x=650, y=400)

        cr6label = customtkinter.CTkLabel(l_frame, text="Commitment, realiability, dependability: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=450)
        cr6 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr6.place(x=650, y=450)

        cr7label = customtkinter.CTkLabel(l_frame, text="Time Management: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=500)
        cr7 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr7.place(x=650, y=500)

        cr8label = customtkinter.CTkLabel(l_frame, text="Punctuality: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=550)
        cr8 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr8.place(x=650, y=550)

        cr9label = customtkinter.CTkLabel(l_frame, text="Follow rules & regulations of the hospital: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=600)
        cr9 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr9.place(x=650, y=600)

        cr10label = customtkinter.CTkLabel(l_frame, text="Handling work pressure: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=650)
        cr10 = customtkinter.CTkEntry(l_frame,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
        cr10.place(x=650, y=650)

        crilabel = customtkinter.CTkLabel(l_frame, text="(On a scale of 1 - 5, 1 being the lowest and 5 the highest rating)", font=('Courier', 18, "bold"),bg_color="transparent", text_color="black").place(x=30, y=690)

        totl = customtkinter.CTkLabel(l_frame, text="Total", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=760)
        tots = customtkinter.CTkLabel(l_frame, text="", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
        tots.place(x=650, y=760)

        aver = customtkinter.CTkLabel(l_frame, text="Average", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=800)
        avera = customtkinter.CTkLabel(l_frame, text="", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
        avera.place(x=650, y=800)

        scl = customtkinter.CTkLabel(l_frame, text="", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
        scl.place(x=630, y=840)


        sol = customtkinter.CTkButton(l_frame,text="count",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command= solve)
        sol.place(x=70, y=850)
        
               
        proc = customtkinter.CTkButton(l_frame,text="Save Data",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=115, height=50, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command= proceed)
        proc.place(x=495, y=910)

        clo = customtkinter.CTkButton(l_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
        hover_color = '#9e9e9e',cursor='hand2',command= cancels)
        clo.place(x=630, y=910)


        aply.configure(state = DISABLED)


        root.mainloop()


    aply = customtkinter.CTkButton(f4_1,text="Rate Data",fg_color='#46829c',font=('Arial', 20,) ,bg_color= 'transparent', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=apply)
    aply.place(x=1200, y=700)



    show_data()
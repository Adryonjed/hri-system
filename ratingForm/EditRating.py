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
    root.geometry('800x1000+650+70')
    root.overrideredirect(True)
    root.title("Rating Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()

    p_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=800,height=1000,corner_radius=30)
    p_frame.pack()

    f2title = customtkinter.CTkFrame(p_frame, width=770, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=15, y=20)

    tit = customtkinter.CTkLabel(f2title, text="PERFORMANCE EVALUATION RATING", font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text="Rate based on your performance", font=("Arial", 20))
    subtit.place(x=20,y=60)

    ide = tk.StringVar()
    crii1 = tk.StringVar()
    crii2 = tk.StringVar()
    crii3 = tk.StringVar()
    crii4 = tk.StringVar()
    crii5 = tk.StringVar()
    crii6 = tk.StringVar()
    crii7 = tk.StringVar()
    crii8 = tk.StringVar()
    crii9 = tk.StringVar()
    crii10 = tk.StringVar()


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
        if num == 8:
            crii7.set(word)
        if num == 9:
            crii8.set(word)
        if num == 10:
            crii9.set(word)
        if num == 11:
            crii10.set(word)

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
    store(results[11],8)
    store(results[12],9)
    store(results[13],10)
    store(results[14],11)
    conn.commit()
    conn.close()
    
    
    

    nat = datetime.now() 
    now = nat.strftime("%b %d, %Y")
    doblabel = Label(text=now)
  

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
        cri7 = str(cr7.get())
        cri8 = str(cr8.get())
        cri9 = str(cr9.get())
        cri10 = str(cr10.get())
    
        if (cri1 == "" or cri1 == " ") or (cri2 == "" or cri2 == " ") or (cri3 == "" or cri3 == " ") or (cri4 == "" or cri4 == " ") or (cri5 == "" or cri5 == " ") or (cri6 == "" or cri6 == " ") or (cri7 == "" or cri7 == " ") or (cri8 == "" or cri8 == " ") or (cri9 == "" or cri9 == " ") or (cri10 == "" or cri10 == " "):
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
        else:
                try:
                    msg = messagebox.askquestion('',"Do you want to Update this data?")
                    if msg == 'yes':
                        conn = connection()
                        cursor = conn.cursor()
                        cursor.execute("UPDATE perform SET datefile = '"+dfile+"', fname = '"+ffname+"', sname = '"+ssname+"', cr1 = '"+cri1+"', cr2 = '"+cri2+"', cr3 = '"+cri3+"', cr4 = '"+cri4+"', cr5 = '"+cri5+"', cr6 = '"+cri6+"', cr7 = '"+cri7+"', cr8 = '"+cri8+"', cr9 = '"+cri9+"', cr10 = '"+cri10+"', totals = '"+ttl+"', averages = '"+average+"' WHERE ide = '"+idss+"' ")
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



    criteria = customtkinter.CTkLabel(p_frame, text="Criteria", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=270, y=150)

    rating = customtkinter.CTkLabel(p_frame, text="Rate", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=655, y=150)

    cr1label = customtkinter.CTkLabel(p_frame, text="Clear understanding of the signed job description: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=200)
    cr1 = customtkinter.CTkEntry(p_frame, textvariable=crii1,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr1.place(x=650, y=200)

    cr2label = customtkinter.CTkLabel(p_frame, text="Possess timelines in the job/Efficiency in assigned job: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=250)
    cr2 = customtkinter.CTkEntry(p_frame , textvariable=crii2, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr2.place(x=650, y=250)

    cr3label = customtkinter.CTkLabel(p_frame, text="Meet expectations/targets consistently?: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=300)
    cr3 = customtkinter.CTkEntry(p_frame, textvariable=crii3, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr3.place(x=650, y=300)

    cr4label = customtkinter.CTkLabel(p_frame, text="Maintain prescribed quality in work?: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=350)
    cr4 = customtkinter.CTkEntry(p_frame, textvariable=crii4, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr4.place(x=650, y=350)

    cr5label = customtkinter.CTkLabel(p_frame, width = 2, text="Follow policies & procedures: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=400)
    cr5 = customtkinter.CTkEntry(p_frame, textvariable=crii5, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr5.place(x=650, y=400)

    cr6label = customtkinter.CTkLabel(p_frame, text="Commitment, realiability, dependability: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=450)
    cr6 = customtkinter.CTkEntry(p_frame, textvariable=crii6, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr6.place(x=650, y=450)

    cr7label = customtkinter.CTkLabel(p_frame, text="Time Management: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=500)
    cr7 = customtkinter.CTkEntry(p_frame, textvariable=crii7, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr7.place(x=650, y=500)

    cr8label = customtkinter.CTkLabel(p_frame, text="Punctuality: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=550)
    cr8 = customtkinter.CTkEntry(p_frame, textvariable=crii8,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr8.place(x=650, y=550)

    cr9label = customtkinter.CTkLabel(p_frame, text="Follow rules & regulations of the hospital: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=600)
    cr9 = customtkinter.CTkEntry(p_frame, textvariable=crii9, height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr9.place(x=650, y=600)

    cr10label = customtkinter.CTkLabel(p_frame, text="Handling work pressure: ", font=('Courier', 16),bg_color="transparent", text_color="black").place(x=70, y=650)
    cr10 = customtkinter.CTkEntry(p_frame, textvariable=crii10,  height= 35, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',validate='key',validatecommand=(my_valid,'%S'))
    cr10.place(x=650, y=650)

    crilabel = customtkinter.CTkLabel(p_frame, text="(On a scale of 1 - 5, 1 being the lowest and 5 the highest rating)", font=('Courier', 18, "bold"),bg_color="transparent", text_color="black").place(x=30, y=690)

    totl = customtkinter.CTkLabel(p_frame, text="Total", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=760)
    tots = customtkinter.CTkLabel(p_frame, text=results[15], font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
    tots.place(x=650, y=760)

    aver = customtkinter.CTkLabel(p_frame, text="Average", font=('Arial', 18, "bold"),bg_color="transparent", text_color="black").place(x=70, y=800)
    avera = customtkinter.CTkLabel(p_frame, text=results[16], font=('Arial', 18, "bold"),bg_color="transparent", text_color="black")
    avera.place(x=650, y=800)


    sol = customtkinter.CTkButton(p_frame,text="count",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= solve)
    sol.place(x=70, y=850)
        
            
    proc = customtkinter.CTkButton(p_frame,text="Save Data",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= proceed)
    proc.place(x=495, y=910)

    clo = customtkinter.CTkButton(p_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#9e9e9e',cursor='hand2',command= cancels)
    clo.place(x=630, y=910)


    
    root.mainloop()


    


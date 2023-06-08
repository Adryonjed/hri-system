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
from leaveForm.EditLeave import *
from leaveForm.exprtleave import *


def show_user():

    root = customtkinter.CTkToplevel()
    root.geometry('1200x790+500+200')
    root.overrideredirect(True)
    root.title("Leave Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()
      
    


    l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=1200,height=790,corner_radius=30)
    l_frame.pack()

    f2title = customtkinter.CTkFrame(l_frame, width=1170, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=15, y=20)

    tit = customtkinter.CTkLabel(f2title, text="User Settings", font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text="Delete/Update User Account", font=("Arial", 20))
    subtit.place(x=20,y=60)

    def cancels():
        root.destroy()

    f5_2 = customtkinter.CTkScrollableFrame(l_frame, fg_color ="transparent",bg_color ="transparent",width= 1100,height= 500)
    f5_2.place(x=50, y=150)

    ed = PIL.Image.open("Assets\\edit.png")
    edt = customtkinter.CTkImage(ed,size=(25,25))
    dtl = PIL.Image.open("Assets\\delete.png")
    dlt = customtkinter.CTkImage(dtl,size=(25,25))

    def show_data():
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM credentials")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
    

        i = 1

        tableframe = customtkinter.CTkFrame(l_frame,fg_color ="transparent",bg_color ="transparent",width=1200,height=50)
        tableframe.place(x=55,y=150)

        dfile = customtkinter.CTkLabel(tableframe, text="User id                    ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dfile.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

        tol = customtkinter.CTkLabel(tableframe, text="Username                        ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        tol.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

        dayss = customtkinter.CTkLabel(tableframe, text="Email Address                               ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dayss.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)


        aps = customtkinter.CTkLabel(tableframe, text="Action  ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        aps.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)


        for g2 in result:
        

            dfile2 = customtkinter.CTkLabel(f5_2, text="                         ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=0,padx=35,pady=10,sticky = NSEW)

            tol2 = customtkinter.CTkLabel(f5_2, text="                                ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol2.grid(row=0, column=1,padx=35,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f5_2, text="                                              ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=2,padx=35,pady=10,sticky = NSEW)


            ac = customtkinter.CTkLabel(f5_2, text="      ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ac.grid(row=0, column=4,padx=35,pady=10,sticky = NSEW)
            

            jo = customtkinter.CTkLabel(f5_2, text=g2[0],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo.grid(row=i, column=0,padx=5,pady=10,sticky = NSEW)
            jo2= customtkinter.CTkLabel(f5_2, text=g2[1],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
            jo3= customtkinter.CTkLabel(f5_2, text=g2[3],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo3.grid(row=i, column=2,padx = 5,pady=10,sticky = NSEW)
    
            shoow = customtkinter.CTkButton(f5_2,text="",image= edt, fg_color='#46729c',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=g2[0]:showit(k))
            shoow.grid(row= i, column = 3,pady=5,padx = 2)

            delp = customtkinter.CTkButton(f5_2,text="",image= dlt,fg_color='#9c4656',font=('Arial', 20,) ,bg_color= "transparent", width=40, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
            cursor='hand2',command=lambda k=g2[0]:delete(k))
            delp.grid(row= i, column = 4,pady=5,padx = 2)


            i = i+1

        def delete(s_id):

            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM credentials WHERE id = %s",(s_id))
            result = cursor.fetchone() 
            conn.commit()
            conn.close()

            decision = messagebox.askquestion("Warning!!", "Delete this data? " + result[1])
        
            if decision == "yes":
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM credentials WHERE id = %s",(s_id))
                conn.commit()
                conn.close()

                for row in f5_2.grid_slaves():
                    row.grid_forget()
                show_user()

            else:
                pass


        def showit(s_id):
    
            root2 = customtkinter.CTkToplevel()
            root2.geometry('800x1000+650+70')
            root2.overrideredirect(True)
            root2.title("Edit form")
            root2.wm_attributes("-transparentcolor",'#333333')
            root2.wait_visibility()
            root2.grab_set()

            p_frame = customtkinter.CTkFrame(root2, bg_color='#333333', fg_color='white',width=800,height=1000,corner_radius=30)
            p_frame.pack()

            f2title = customtkinter.CTkFrame(p_frame, width=770, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
            f2title.place(x=15, y=20)

            tit = customtkinter.CTkLabel(f2title, text="USER DETAILS", font=("Arial", 30, 'bold'))
            tit.place(x=20,y=20)
            subtit = customtkinter.CTkLabel(f2title, text="Update/Add user Details", font=("Arial", 20))
            subtit.place(x=20,y=60)

            ide = tk.StringVar()
            uname = tk.StringVar()
            upass = tk.StringVar()
            eml = tk.StringVar()
            


            def store(word,num):
                if num == 1:
                    ide.set(word)
                if num == 2:
                    uname.set(word)
                if num == 3:
                    upass.set(word)
                if num == 4:
                    eml.set(word)
                

            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM credentials WHERE id = %s",(s_id))
            results = cursor.fetchone()
            store(results[0],1)
            store(results[1],2)
            store(results[2],3)
            store(results[3],4)
            conn.commit()
            conn.close()

            def cancels2():
                root2.destroy()

            idd = Label(textvariable=ide)

            def update_user():

                idss = str(idd.cget("text"))
                uname = str(usere.get())
                umail = str(emaile.get())
                upasss = str(psse.get())
                
                try:
                    msg = messagebox.askquestion('',"Do you want to Update this data?")
                    if msg == 'yes':
                        conn = connection()
                        cursor = conn.cursor()
                        cursor.execute("UPDATE credentials SET user = '"+uname+"', pass = '"+upasss+"', email = '"+umail+"' WHERE id = '"+idss+"' ")
                        conn.commit()
                        conn.close()
                        root2.destroy()

                    elif msg == 'no':
                        pass
                    else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                        root2.destroy()
                    
                except:
                    messagebox.showinfo("Error", "Data already exist")
                    return
                
                show_user()
                
            def add_user():

                uname = str(usere2.get())
                umail = str(emaile2.get())
                upasss = str(psse2.get())
                
                try:
                    msg = messagebox.askquestion('',"Do you want to Update this data?")
                    if msg == 'yes':
                        conn = connection()
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO credentials VALUES ('""','"+uname+"','"+upasss+"','"+umail+"') ")
                        conn.commit()
                        conn.close()
                        root2.destroy()

                    elif msg == 'no':
                        pass
                    else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                        root2.destroy()
                    
                except:
                    messagebox.showinfo("Error", "Data already exist")
                    return
                
                show_user()

            editl = customtkinter.CTkLabel(p_frame, text="Update User Account", font=('Arial', 20, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=150)

            unm = customtkinter.CTkLabel(p_frame, text="Username :", font=('Arial', 18, 'bold'),bg_color="transparent",text_color='black').place(x=150, y=200)
            usere = customtkinter.CTkEntry(p_frame, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 22),text_color='black',textvariable=uname)
            usere.place(x=310, y=200)

            emaill = customtkinter.CTkLabel(p_frame, text="Email Address :", font=('Arial', 18, 'bold'),bg_color="transparent",text_color='black').place(x=150, y=250)
            emaile = customtkinter.CTkEntry(p_frame,  height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=eml)
            emaile.place(x=310, y=250)

            pssl = customtkinter.CTkLabel(p_frame, text="Password :", font=('Arial', 18, 'bold'),bg_color="transparent",text_color='black').place(x=150, y=300)
            psse = customtkinter.CTkEntry(p_frame,  height= 35, width=350, show = "*", fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',placeholder_text = "Update your Password",placeholder_text_color= "gray")
            psse.place(x=310, y=300)


            proc = customtkinter.CTkButton(p_frame,text="Update",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
            hover_color = '#2a4859',cursor='hand2',command=update_user)
            proc.place(x=575, y=350)


#-------------------------------------------------------------------------


            sign = customtkinter.CTkLabel (p_frame, text="Add User Account", font=('Arial', 20, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=450)

            unm2 = customtkinter.CTkLabel(p_frame, text="Username :", font=('Arial', 18, 'bold'),bg_color="transparent",text_color='black').place(x=150, y=500)
            usere2 = customtkinter.CTkEntry(p_frame, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 22),text_color='black')
            usere2.place(x=310, y=500)

            emaill2 = customtkinter.CTkLabel(p_frame, text="Email Address :", font=('Arial', 18, 'bold'),bg_color="transparent",text_color='black').place(x=150, y=550)
            emaile2 = customtkinter.CTkEntry(p_frame,  height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
            emaile2.place(x=310, y=550)

            pssl2 = customtkinter.CTkLabel(p_frame, text="Password :", font=('Arial', 18, 'bold'),bg_color="transparent",text_color='black').place(x=150, y=600)
            psse2 = customtkinter.CTkEntry(p_frame,  height= 35, width=350, show = "*", fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
            psse2.place(x=310, y=600)

            proc2 = customtkinter.CTkButton(p_frame,text="Add User",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
            hover_color = '#2a4859',cursor='hand2',command=add_user)
            proc2.place(x=555, y=650)


            clo2 = customtkinter.CTkButton(p_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
            hover_color = '#9e9e9e',cursor='hand2',command= cancels2)
            clo2.place(x=630, y=910)



    
            root2.mainloop()
    
    show_data()

    clo = customtkinter.CTkButton(l_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#9e9e9e',cursor='hand2',command= cancels)
    clo.place(x=990, y=710)

    

    root.mainloop()


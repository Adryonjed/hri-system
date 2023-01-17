from imaplib import Commands
from turtle import onclick, position
from matplotlib import image, style
from matplotlib.pyplot import show
from tkinter import *
from db import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from tkinter.ttk import Progressbar
import tkinter as tk
import customtkinter
import time
from tkinter import filedialog
import base64

def performance():
    f3 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8ad4c9")
    f3.place(x=380, y=200)

    

    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', font=('Arial', 12))
    

    sty = ttk.Style()
    sty.theme_use("clam")
    sty.configure("Treeview", rowheight="50",fieldbackground = '#c9c9c7',background = '#c9c9c7', borderwidth = 0)
    sty.configure("Treeview.Heading", font=(None, 20), background="#c9c9c7", borderwidth = 0, relief = "flat")
    sty.map("Treeview.Heading", background = [('active', "#c9c9c7" )])
    sty.map('Treeview', background=[('selected', 'green')])

    fi = tk.StringVar()

    def ms(word,num):
        if num == 1:
            fi.set(word)

    def mouse_select():
        try:
            selected_item = my_tree.selection()[0]
            name = str(my_tree.item(selected_item)['values'][0])
    
            ms(name,1)
        except:
            messagebox.showinfo("Error", "Please select a data row")

    def dclick(e):
        mouse_select()

    mainframe3 = tk.Frame(bg='#dbb2b2')
    mainframe3.place(x=380, y=200)
    mainframe3.pack_propagate(False)


    def deletef():
        for frame in mainframe3.winfo_children():
            frame.destroy()

    def indicate(page):

        deletef()
        page()

    c = tk.StringVar()
    c1 = tk.StringVar()
    c2 = tk.StringVar()
    c3 = tk.StringVar()


    def check():

        find = str(findEntry.get())
        if (find == "" or find == " "):
            messagebox.showinfo("Error", "Select a data or input your first name in the entry")
            return
        else:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM person WHERE id=%s",(findEntry.get()))
            result = cursor.fetchone()
            drow = result[0]
            drow1 = result[1]
            drow2 = result[2]

            if result:
                indicate(check_p)
                c.set(drow)
                c1.set(drow1)
                c2.set(drow2)
            else:
                pass

        


    
    def check_p():
        
        d = StringVar()


        f3_1 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8ad4c9")
        f3_1.place(x=380, y=200)
        f3_1.grid_propagate(0)



        dates = Label(f3_1, text="DATE OF BIRTH : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=800, y=85)
        dobbs = DateEntry(f3_1,width = 23, font = ('arial', 16), year = 2022, month = 6, day = 22, background = 'gray', foreground =  'white', borderwidth = 0, weekendbackground = 'red', bd = 0)
        dt = date(2023,1,1)
        dobbs.set_date(dt)
        dobbs.place(x=950,y=83)




        snlabel = Label(f3_1, text="YOUR ID :", font=('Arial', 15, 'bold'),bg="#d1a78e").place(x=30, y=30)
        res = Label(f3_1, text="", font=('Arial', 15, 'bold'),bg="#d1a78e", textvariable=c)
        res.place(x=140, y=30)

        snlabel = Label(f3_1, text="SURNAME :", font=('Arial', 20, 'bold'),bg="#d1a78e").place(x=500, y=100)
        res1 = Label(f3_1, text="", font=('Arial', 20, 'bold'),bg="#d1a78e", textvariable=c2)
        res1.place(x=670, y=100)

        fnlabel = Label(f3_1, text="FIRSTNAME :", font=('Arial', 20, 'bold'),bg="#d1a78e").place(x=30, y=100)
        res2 = Label(f3_1, text="", font=('Arial', 20, 'bold'),bg="#d1a78e", textvariable=c1)
        res2.place(x=220, y=100)


        def imported():
            f3_2 = customtkinter.CTkFrame(None, fg_color ="#8ad4c9")
            f3_2.place(x=1000, y=400)
            
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM image WHERE id=%s ORDER BY date DESC",(findEntry.get()))
            

            
            i = 1
            
            for g in cursor:

                jo = Label(f3_2, text=g[2],font=('Arial', 50))
                jo.grid(row=i, column=1, ipadx= 10,padx=20)
                
                jo2 = Label(f3_2,  text='imported', font=('Arial', 50),textvariable=g[1])
                jo2.grid(row=i, column=2, ipadx= 10,padx=20)

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

            
            query = 'INSERT IGNORE INTO image (id,date,img) VALUES (%s,%s,%s)'
            cursor.execute(query, args)
            conn.commit()


            imported()

        


    

        
        uplo = customtkinter.CTkButton(f3_1 ,text="Upload",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command= upload)
        uplo.place(x=1200, y=700)

         
        backt = customtkinter.CTkButton(f3_1 ,text="Back",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(performance))
        backt.place(x=1000, y=700)

        imported()

        





    
            

    add3 = customtkinter.CTkButton(f3,text="Check",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(check))
    add3.place(x=1200, y=700)

   
        

    fin2 = Label(f3, text="FIND : ", font=('Arial', 15, 'bold'),bg="#8aafd4").place(x=50, y=700)
    findEntry = customtkinter.CTkEntry(f3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black',textvariable=fi)
    findEntry.place(x=130, y=700)


    my_tree =ttk.Treeview(f3, show="headings", height=12)
    my_tree['columns'] = ("id","name","sur","pos","dept")


    my_tree.column("id", anchor=CENTER, width=287)
    my_tree.column("name", anchor=W, width=287)
    my_tree.column("sur", anchor=W, width=287)
    my_tree.column("pos", anchor=W, width=287)
    my_tree.column("dept", anchor=W, width=287)


    my_tree.heading("id", text="ID", anchor=CENTER)
    my_tree.heading("name", text="NAME", anchor=CENTER)
    my_tree.heading("sur", text="SURNAME", anchor=CENTER)
    my_tree.heading("pos", text="POSITION", anchor=CENTER)
    my_tree.heading("dept", text="DEPARTMENT", anchor=CENTER)

    my_tree.place(x=27, y=27)
    my_tree.bind("<Double-1>", dclick)
    populate()
    refreshTable()  

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
from ratingForm.ratingApply import *

def perform():
    f3 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#d4d4d4",corner_radius=60)
    f3.place(x=380, y=200)
    f3.pack_propagate(False)

    f2title = customtkinter.CTkFrame(f3, width=1450, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=20, y=20)

    tit = customtkinter.CTkLabel(f2title, text="Performance Records", font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text="manage performance records", font=("Arial", 20))
    subtit.place(x=20,y=60)




    def deletef():
        for frame in f3.winfo_children():
            frame.destroy()

    def indicate(page):
        deletef()
        page()

   

    ids = tk.StringVar()




    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------First Frame-----------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------

    f3_1 = customtkinter.CTkScrollableFrame(f3, fg_color ="transparent",bg_color ="transparent", width= 1380,height= 550)
    f3_1.place(x=50, y=200)

    agree = PIL.Image.open("Assets\\green.png")
    are = PIL.Image.open("Assets\\red.png")
    aye = PIL.Image.open("Assets\\yell.png")

    ed = PIL.Image.open("Assets\\view.png")
    edt = customtkinter.CTkImage(ed,size=(25,25))


    
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal")
    result = cursor.fetchall()
    conn.commit()
    conn.close()


    tableframe = customtkinter.CTkFrame(f3,fg_color ="transparent",bg_color ="transparent",width=1200,height=50)
    tableframe.place(x=55,y=210)

    dfile = customtkinter.CTkLabel(tableframe, text="First Name                         ",font=('Arial', 24, 'bold'),bg_color="transparent",text_color="black")
    dfile.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

    tol = customtkinter.CTkLabel(tableframe, text="Last Name                        ",font=('Arial', 24, 'bold'),bg_color="transparent",text_color="black")
    tol.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

    dayss = customtkinter.CTkLabel(tableframe, text="Staff Type           ",font=('Arial', 24, 'bold'),bg_color="transparent",text_color="black")
    dayss.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

    aps = customtkinter.CTkLabel(tableframe, text="Department            ",font=('Arial', 24, 'bold'),bg_color="transparent",text_color="black")
    aps.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

    aps = customtkinter.CTkLabel(tableframe, text="Status               ",font=('Arial', 24, 'bold'),bg_color="transparent",text_color="black")
    aps.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)

    aps = customtkinter.CTkLabel(tableframe, text="Action         ",font=('Arial', 24, 'bold'),bg_color="transparent",text_color="black")
    aps.grid(row=0, column=5,padx=5,pady=10,sticky = NSEW)


    global i

    i = 1

    for g in result:
        
 
        dfile2 = customtkinter.CTkLabel(f3_1, text="                                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dfile2.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

        tol2 = customtkinter.CTkLabel(f3_1, text="                                         ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        tol2.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

        dayss2 = customtkinter.CTkLabel(f3_1, text="                            ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dayss2.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

        ap2 = customtkinter.CTkLabel(f3_1, text="                              ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        ap2.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

        dfile2 = customtkinter.CTkLabel(f3_1, text="                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dfile2.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)

        act2 = customtkinter.CTkLabel(f3_1, text="        ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        act2.grid(row=0, column=5,padx=5,pady=10,sticky = NSEW)

        col1 = customtkinter.CTkLabel(f3_1, text=g[2],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
        col1.grid(row=i, column=0,padx = 5,pady=10,sticky = NSEW)
        col2 = customtkinter.CTkLabel(f3_1, text=g[1],font=('Arial',20),bg_color="transparent",text_color="black",anchor=W)
        col2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
        col3 = customtkinter.CTkLabel(f3_1, text=g[15],font=('Arial',20),bg_color="transparent",text_color="black",anchor=W)
        col3.grid(row=i, column=2,padx = 5,pady=10,sticky = NSEW)
        col4 = customtkinter.CTkLabel(f3_1, text=g[17],font=('Arial',20),bg_color="transparent",text_color="black",anchor=W)
        col4.grid(row=i, column=3,padx = 5,pady=10,sticky = NSEW)

        if g[19] == "Active":
            clrstat = customtkinter.CTkImage(agree,size=(25,15))

        elif g[19] == "Inactive":
            clrstat = customtkinter.CTkImage(are,size=(25,15))
            
        else:
            clrstat = customtkinter.CTkImage(aye,size=(25,15))
            
        col5 = customtkinter.CTkLabel(f3_1, text=g[19], image = clrstat,compound= "left",font=('Arial',20),bg_color="transparent",text_color="black",anchor=W)
        col5.grid(row=i, column=4,padx = 5,pady=10,sticky = NSEW)

        showb2 = customtkinter.CTkButton(f3_1,text="",image= edt, fg_color='#469c8e',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
        hover_color = '#2a4859' , command=lambda k=g[0]:show_per(k))
        showb2.grid(row= i, column = 5,pady=5,padx = 3)

        
        i = i+1


    def show_per(s_id):
        indicate(show_perform(s_id))
        backt = customtkinter.CTkButton(None ,text="Back",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(perform))
        backt.place(x=1400, y=900)



    def searching(event):
        for rows2 in f3_1.grid_slaves():
            rows2.grid_forget()
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personal WHERE department = %s AND status = %s",(findEntry.get(), findEntry3.get()))
        results = cursor.fetchall()
        conn.commit()
        conn.close()

        i = 1

        for array2 in results:

            dfile2 = customtkinter.CTkLabel(f3_1, text="                                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

            tol2 = customtkinter.CTkLabel(f3_1, text="                                         ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol2.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f3_1, text="                            ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

            ap2 = customtkinter.CTkLabel(f3_1, text="                              ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ap2.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

            dfile2 = customtkinter.CTkLabel(f3_1, text="                      ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)

            act2 = customtkinter.CTkLabel(f3_1, text="        ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            act2.grid(row=0, column=5,padx=5,pady=10,sticky = NSEW)

            col1 = customtkinter.CTkLabel(f3_1, text=array2[2],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col1.grid(row=i, column=0,padx = 5,pady=10,sticky = NSEW)
            col2 = customtkinter.CTkLabel(f3_1, text=array2[1],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
            col3 = customtkinter.CTkLabel(f3_1, text=array2[15],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col3.grid(row=i, column=2,padx = 5,pady=10,sticky = NSEW)
            col4 = customtkinter.CTkLabel(f3_1, text=array2[17],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col4.grid(row=i, column=3,padx = 5,pady=10,sticky = NSEW)

            if array2[19] == "Active":
                clrstat = customtkinter.CTkImage(agree,size=(25,15))

            elif array2[19] == "Inactive":
                clrstat = customtkinter.CTkImage(are,size=(25,15))
                
            else:
                clrstat = customtkinter.CTkImage(aye,size=(25,15))

            col5 = customtkinter.CTkLabel(f3_1, text=array2[19], image = clrstat,compound= "left",font=('Arial',20),bg_color="transparent",text_color="black",anchor=W)
            col5.grid(row=i, column=4,padx = 5,pady=10,sticky = NSEW)


            customtkinter.CTkButton(f3_1,text="",image= edt, fg_color='#469c8e',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=array2[0]:show_per(k)).grid(row= i, column = 5,pady=5,padx = 10)

            i = i+1
      

    def searchbar():
        for rows2 in f3_1.grid_slaves():
            rows2.grid_forget()
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personal WHERE department = %s AND firstname like %s OR id like %s",(findEntry.get(),findEntry2.get(),findEntry2.get()))
        results = cursor.fetchall()
        conn.commit()
        conn.close()

        i = 1

        for array2 in results:

            dfile2 = customtkinter.CTkLabel(f3_1, text="                                           ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

            tol2 = customtkinter.CTkLabel(f3_1, text="                                         ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol2.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f3_1, text="                            ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

            ap2 = customtkinter.CTkLabel(f3_1, text="                              ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ap2.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

            dfile2 = customtkinter.CTkLabel(f3_1, text="                      ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)

            act2 = customtkinter.CTkLabel(f3_1, text="        ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            act2.grid(row=0, column=5,padx=5,pady=10,sticky = NSEW)

            col1 = customtkinter.CTkLabel(f3_1, text=array2[2],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col1.grid(row=i, column=0,padx = 5,pady=10,sticky = NSEW)
            col2 = customtkinter.CTkLabel(f3_1, text=array2[1],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
            col3 = customtkinter.CTkLabel(f3_1, text=array2[15],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col3.grid(row=i, column=2,padx = 5,pady=10,sticky = NSEW)
            col4 = customtkinter.CTkLabel(f3_1, text=array2[17],font=('Arial', 20),bg_color="transparent",text_color="black",anchor=W)
            col4.grid(row=i, column=3,padx = 5,pady=10,sticky = NSEW)

            if array2[19] == "Active":
                clrstat = customtkinter.CTkImage(agree,size=(25,15))

            elif array2[19] == "Inactive":
                clrstat = customtkinter.CTkImage(are,size=(25,15))
                
            else:
                clrstat = customtkinter.CTkImage(aye,size=(25,15))

            col5 = customtkinter.CTkLabel(f3_1, text=array2[19], image = clrstat, compound= "left",font=('Arial',20),bg_color="transparent",text_color="black",anchor=W)
            col5.grid(row=i, column=4,padx = 5,pady=10,sticky = NSEW)


            customtkinter.CTkButton(f3_1,text="",image= edt, fg_color='#469c8e',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=array2[0]:show_per(k)).grid(row= i, column = 5,pady=5,padx = 10)

            i = i+1

         
    def refresh():
        perform()

    
    find = customtkinter.CTkLabel(f3, text="Find: ", font=('Arial', 20, 'bold'),bg_color="transparent",text_color="black").place(x=50, y=153)
    
    findEntry = customtkinter.CTkOptionMenu(f3,height= 35, width = 200,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", values=["ADMIN","ANCILLARY", "MEDICAL", "NURSING"], command=searching)
    findEntry.set("")
    findEntry.place(x=110, y=150)
    findEntry.bind("<Key>", searching)


    find2 = customtkinter.CTkLabel(f3, text="Status: ", font=('Arial', 20, 'bold'),bg_color="transparent",text_color="black").place(x=330, y=153)

    findEntry3 = customtkinter.CTkOptionMenu(f3,height= 35, width = 200,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", values=["Active","Inactive","AWOL"], command=searching)
    findEntry3.set("")
    findEntry3.place(x=410, y=150)
    findEntry3.bind("<Key>", searching)


    refr = PIL.Image.open("Assets\\refresh.png")
    ref = customtkinter.CTkImage(refr,size=(30,30))

    refreshh = customtkinter.CTkButton(f3,text="",image = ref, bg_color= 'transparent',fg_color="transparent",hover_color= "#8aafd4", width= 20,cursor='hand2',command=refresh)
    refreshh.place(x=620, y=150)

    search = customtkinter.CTkButton(f3,text="Search",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= 'transparent', width=100, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=searchbar)
    search.place(x=1350, y=150)
    search.bind("<Return>",searchbar)
    
    findEntry2 = customtkinter.CTkEntry(f3,height = 37, width= 400, fg_color='white',border_width = 2 , corner_radius= 10,font=('Arial', 20),text_color='black')
    findEntry2.place(x=940, y=150)



    

    
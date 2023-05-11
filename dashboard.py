from tkinter import *
from database.db import *
from tkinter import ttk
from time import strftime
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import PIL.Image



def dash():
    f1 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#d4d4d4", corner_radius=50)
    f1.place(x=380, y=200)

    f1_1 = customtkinter.CTkFrame(f1, width=300, height=180, fg_color="#67c9be",corner_radius=40)
    f1_1.place(x=30, y=30)

    img = PIL.Image.open("Assets\\peo.png")
    peo = customtkinter.CTkImage(img,size=(40,40))

    ln = customtkinter.CTkLabel(f1_1, text="Total Employees", font=('Arial', 20), bg_color="transparent",text_color="black",image=peo,compound="right")
    ln.place(x=25, y=10)
    
    f1_2 = customtkinter.CTkFrame(f1, width=300, height=180, fg_color="#95c791",corner_radius=40)
    f1_2.place(x=400, y=30)

    img2 = PIL.Image.open("Assets\\dept.png")
    depts = customtkinter.CTkImage(img2,size=(30,30))

    ln2 = customtkinter.CTkLabel(f1_2, text="Total Active ", font=('Arial', 20), bg_color="transparent",text_color="black",image=depts,compound="right")
    ln2.place(x=25, y=10)

    f1_3 = customtkinter.CTkFrame(f1, width=300, height=180, fg_color="#95c791",corner_radius=40)
    f1_3.place(x=775, y=30)

    img3 = PIL.Image.open("Assets\\dept.png")
    depts3 = customtkinter.CTkImage(img3,size=(30,30))

    ln3 = customtkinter.CTkLabel(f1_3, text="Total AWOL ", font=('Arial', 20), bg_color="transparent",text_color="black",image=depts3,compound="right")
    ln3.place(x=25, y=10)

    f1_4 = customtkinter.CTkFrame(f1, width=300, height=180, fg_color="#95c791",corner_radius=40)
    f1_4.place(x=1150, y=30)

    img4 = PIL.Image.open("Assets\\dept.png")
    depts4 = customtkinter.CTkImage(img4,size=(30,30))

    ln4 = customtkinter.CTkLabel(f1_4, text="Total Inactive ", font=('Arial', 20), bg_color="transparent",text_color="black",image=depts4,compound="right")
    ln4.place(x=25, y=10)




    def refreshcount():
        
        conn = connection()
        cursor = conn.cursor()
        em_number = cursor.execute("SELECT * FROM personal")
        customtkinter.CTkLabel(f1_1, text=(em_number), font=('Arial', 70), bg_color="transparent",text_color="black").place(relx=0.5,rely=0.5, anchor=CENTER)
        act_num = cursor.execute("SELECT * FROM personal WHERE status = 'Active' ")
        customtkinter.CTkLabel(f1_2, text=(act_num), font=('Arial', 70), bg_color="transparent",text_color="black").place(relx=0.5,rely=0.5, anchor=CENTER)
        AWOL_num = cursor.execute("SELECT * FROM personal WHERE status = 'AWOL' ")
        customtkinter.CTkLabel(f1_3, text=(AWOL_num), font=('Arial', 70), bg_color="transparent",text_color="black").place(relx=0.5,rely=0.5, anchor=CENTER)
        inac_num = cursor.execute("SELECT * FROM personal WHERE status = 'Inactive' ")
        customtkinter.CTkLabel(f1_4, text=(inac_num), font=('Arial', 70), bg_color="transparent",text_color="black").place(relx=0.5,rely=0.5, anchor=CENTER)



    refreshcount()
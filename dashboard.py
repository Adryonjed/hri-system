from tkinter import *
from db import *
from tkinter import ttk
from time import strftime
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import PIL.Image



def dash():
    f1 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#d4b88a", corner_radius=50)
    f1.place(x=380, y=200)

    f1_1 = customtkinter.CTkFrame(f1, width=300, height=200, fg_color="#67c9be",corner_radius=40)
    f1_1.place(x=30, y=30)

    img = PIL.Image.open("Assets\\peo.png")
    peo = customtkinter.CTkImage(img,size=(40,40))

    ln = customtkinter.CTkLabel(f1_1, text="Total Employees", font=('Arial', 20), bg_color="transparent",text_color="black",image=peo,compound="right")
    ln.place(x=25, y=10)

    
    f1_2 = customtkinter.CTkFrame(f1, width=300, height=200, fg_color="#95c791",corner_radius=40)
    f1_2.place(x=400, y=30)

    img2 = PIL.Image.open("Assets\\dept.png")
    depts = customtkinter.CTkImage(img2,size=(30,30))

    ln2 = customtkinter.CTkLabel(f1_2, text="Total Departments ", font=('Arial', 20), bg_color="transparent",text_color="black",image=depts,compound="right")
    ln2.place(x=25, y=10)



    def refreshcount():
        
        conn = connection()
        cursor = conn.cursor()
        em_number = cursor.execute("SELECT * FROM personal")
        customtkinter.CTkLabel(f1_1, text=(em_number), font=('Arial', 70), bg_color="transparent",text_color="black").place(relx=0.5,rely=0.5, anchor=CENTER)
        dept_num = cursor.execute("SELECT * FROM personal GROUP BY department")
        customtkinter.CTkLabel(f1_2, text=(dept_num), font=('Arial', 70), bg_color="transparent",text_color="black").place(relx=0.5,rely=0.5, anchor=CENTER)



    def my_time():
        time_string = strftime('%I:%M:%S %p \n %A \n %x') 
        l1.config(text=time_string)
        l1.after(1000,my_time) 

    my_font=('times',45,'bold')
    l1=tk.Label(f1,font=my_font,bg="#d4b88a")
    l1.place(x=550, y=300)

    my_time()
    refreshcount()
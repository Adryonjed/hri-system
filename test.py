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
import io



my_w = tk.Tk() # parent window 
my_w.geometry("400x500") # size as width height
my_w.title("www.plus2net.com")  # Adding a title
# database connection 
conn = connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM educ")

# Column headers  row 0
l1=Label(my_w, text='ID') 
l1.grid(row=0,column=1) 

l2=Label(my_w, text='Name') 
l2.grid(row=0,column=2) 

l3=Label(my_w, text='Photo') 
l3.grid(row=0,column=3) 

i=1 # data starts from row 1 
images = [] # to manage garbage collection. 

for student in cursor: 
    stream = io.BytesIO(student[2])
    img=Image.open(stream)
    img = ImageTk.PhotoImage(img)    
    e = Label(my_w, text=student[0]) 
    e.grid(row=i,column=1,ipadx=20) 
    e = Label(my_w, text=student[1]) 
    e.grid(row=i,column=2,ipadx=60) 
    e = Label(my_w, image=img) 
    e.grid(row=i, column=3,ipady=7)  
    images.append(img) # garbage collection 
    i=i+1 
   
my_w.mainloop()
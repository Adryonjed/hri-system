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


def select(app):

        
        sname = str(res1.cget("text"))
        fname = str(res2.cget("text"))
        mname = str(res3.cget("text"))
        ct = str(res6.cget("text"))
        hei = str(res8.cget("text"))
        wei = str(res9.cget("text"))
        tlno = str(res11.cget("text"))
        clno = str(res12.cget("text"))
        email = str(res13.cget("text"))
        pos = str(res14.cget("text"))
        dept = str(res15.cget("text"))
        
        setc(sname,1)
        setc(fname,2)
        setc(mname,3)
        setc(ct,4)
        setc(hei,5)
        setc(wei,6)
        setc(tlno,7)
        setc(clno,8)
        setc(email,9)
        setc(pos,10)
        setc(dept,11)

        show_frame2(f2_3)


modb = customtkinter.CTkButton(sf2,text="Modify",fg_color='#467c9c',text_font=('Arial', 20,) ,bg_color= '#d1a78e', width=160, height=60, border_width=0, corner_radius=10,
hover_color = '#2a4859',cursor='hand2',command=select)
modb.place(x=1200, y=900)

app.mainloop()
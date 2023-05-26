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


def filing():

    root = customtkinter.CTkToplevel()
    root.geometry('800x1000+650+50')
    root.overrideredirect(True)
    root.title("Rating Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()

    f_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=800,height=1000,corner_radius=30)
    f_frame.pack()

    f2title = customtkinter.CTkFrame(f_frame, width=770, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=15, y=20)

    tit = customtkinter.CTkLabel(f2title, text="201 FILING", font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text="Inserting 201 Files (PDF files Only)", font=("Arial", 20))
    subtit.place(x=20,y=60)


    def cancels():
        root.destroy()

    def validate2(u_input):
            
        return u_input.isdigit()
    my_valid2 = f_frame.register(validate2)


    def upl_etd():

      global imgfile

      f_types = [('PDF', '*.pdf')]
      imgfile = filedialog.askopenfilename(filetypes=f_types)
      if imgfile:
        etdpth.set(imgfile)


    def upl_clrnc():

      global imgfile2

      f_types = [('PDF', '*.pdf')]
      imgfile2 = filedialog.askopenfilename(filetypes=f_types)
      if imgfile2:
        clrncpth.set(imgfile2)

    def upl_wc():

      global imgfile3

      f_types = [('PDF', '*.pdf')]
      imgfile3 = filedialog.askopenfilename(filetypes=f_types)
      if imgfile3:
        wcpth.set(imgfile3)

    def upl_hr():

      global imgfile4

      f_types = [('PDF', '*.pdf')]
      imgfile4 = filedialog.askopenfilename(filetypes=f_types)
      if imgfile4:
        hrpth.set(imgfile4)

    def upl_tx():

      global imgfile5

      f_types = [('PDF', '*.pdf')]
      imgfile5 = filedialog.askopenfilename(filetypes=f_types)
      if imgfile5:
        txpth.set(imgfile5)

      
    def addfile():
      
      fob = open(imgfile, 'rb').read()
      fob2 = open(imgfile2, 'rb').read()
      fob3 = open(imgfile3, 'rb').read()
      fob4 = open(imgfile4, 'rb').read()
      fob5 = open(imgfile5, 'rb').read()
      
      msg = messagebox.askquestion('',"Do you want to add this person?")
      if msg == 'yes':
        conn = connection()
        cursor = conn.cursor()
        args = (idl.get(),fn.get(), sn.get(),fob,fob2,fob3,fob4,fob5)
        cursor.execute("INSERT INTO hro (id,fname,sname,edp,clearance,workh,hiring,tax) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",args)
        conn.commit()
        conn.close()
        root.destroy()
      elif msg == 'no':
        pass
      else:
        messagebox.showinfo('Return', 'You will now return to the application screen')
        root.destroy()

    idlabel = customtkinter.CTkLabel(f_frame, text="ID NO. :", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=150)
    idl = customtkinter.CTkEntry(f_frame, height= 35,width=75, fg_color='white',border_width = 2, font=('Arial', 22),corner_radius= 10,text_color='black',validate='key',validatecommand=(my_valid2,'%S'))
    idl.place(x=100, y=200)

    fnlabel = customtkinter.CTkLabel(f_frame, text="FIRSTNAME :", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=350)
    fn = customtkinter.CTkEntry(f_frame, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 22),text_color='black')
    fn.place(x=100, y=300)

    snlabel = customtkinter.CTkLabel(f_frame, text="SURNAME :", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=250)
    sn = customtkinter.CTkEntry(f_frame, height= 35,width=450, fg_color='white',border_width = 2,font=('Arial', 22), corner_radius= 10,text_color='black')
    sn.place(x=100, y=400)


    etd = customtkinter.CTkLabel(f_frame, text="Education/transcripts/diplomas: ", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=450)
    etd_up = customtkinter.CTkButton(f_frame, width=50, height=30, text="Chose a file", command=upl_etd)
    etd_up.place(x=100, y=490)
    etdpth = tk.StringVar()
    etdpath = customtkinter.CTkLabel(f_frame, text="", font=('Courier', 14, 'bold'),bg_color="transparent",text_color="#3a52c9",textvariable=etdpth).place(x=250, y=495)

    clrnc = customtkinter.CTkLabel(f_frame, text="Clearances: ", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=530)
    clrnc_up = customtkinter.CTkButton(f_frame, width=50, height=30, text="Chose a file", command=upl_clrnc)
    clrnc_up.place(x=100, y=570)
    clrncpth = tk.StringVar()
    clrncpath = customtkinter.CTkLabel(f_frame, text="", font=('Courier', 14, 'bold'),bg_color="transparent",text_color="#3a52c9",textvariable=clrncpth).place(x=250, y=575)
    
    wc = customtkinter.CTkLabel(f_frame, text="Work History: ", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=610)
    wc_up = customtkinter.CTkButton(f_frame, width=50, height=30, text="Chose a file", command=upl_wc)
    wc_up.place(x=100, y=650)
    wcpth = tk.StringVar()
    wcpath = customtkinter.CTkLabel(f_frame, text="", font=('Courier', 14, 'bold'),bg_color="transparent",text_color="#3a52c9",textvariable=wcpth).place(x=250, y=655)

    hr = customtkinter.CTkLabel(f_frame, text="Hiring Requirements: ", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=690)
    hr_up = customtkinter.CTkButton(f_frame, width=50, height=30, text="Chose a file", command=upl_hr)
    hr_up.place(x=100, y=730)
    hrpth = tk.StringVar()
    hrpath = customtkinter.CTkLabel(f_frame, text="", font=('Courier', 14, 'bold'),bg_color="transparent",text_color="#3a52c9",textvariable=hrpth).place(x=250, y=735)

    tx = customtkinter.CTkLabel(f_frame, text="Tax Identification: ", font=('Courier', 18, 'bold'),bg_color="transparent",text_color='black').place(x=20, y=770)
    tx_up = customtkinter.CTkButton(f_frame, width=50, height=30, text="Chose a file", command=upl_tx)
    tx_up.place(x=100, y=810)
    txpth = tk.StringVar()
    txpath = customtkinter.CTkLabel(f_frame, text="", font=('Courier', 14, 'bold'),bg_color="transparent",text_color="#3a52c9",textvariable=txpth).place(x=250, y=815)


    proc = customtkinter.CTkButton(f_frame,text="Save Data",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=addfile)
    proc.place(x=495, y=910)

    clo = customtkinter.CTkButton(f_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#9e9e9e',cursor='hand2',command= cancels)
    clo.place(x=630, y=910)



    root.mainloop()
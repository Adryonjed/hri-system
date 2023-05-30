from tkinter import *
from database.db import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from tkinter import filedialog
import csv





def save_data():

    root = customtkinter.CTkToplevel()
    root.geometry('730x500+650+350')
    root.overrideredirect(True)
    root.title("Rating Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()

    p_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=730,height=500,corner_radius=30)
    p_frame.pack()

    f2title = customtkinter.CTkFrame(p_frame, width=690, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=15, y=20)

    tit = customtkinter.CTkLabel(f2title, text="DOWNLOAD EMPLOYEES LIST", font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text="Save it into CSV/Excel File", font=("Arial", 20))
    subtit.place(x=20,y=60)

    

    conn = connection()
    cursor = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()
    cursor4 = conn.cursor()
    cursor5 = conn.cursor()
    cursor.execute("SELECT id, surname, firstname, sex, staff, position FROM personal")
    cursor2.execute("SELECT id, surname, firstname, sex, staff, position FROM personal WHERE department = 'ADMIN' ")
    cursor3.execute("SELECT id, surname, firstname, sex, staff, position FROM personal WHERE department = 'ANCILLARY' ")
    cursor4.execute("SELECT id, surname, firstname, sex, staff, position FROM personal WHERE department = 'MEDICAL' ")
    cursor5.execute("SELECT id, surname, firstname, sex, staff, position FROM personal WHERE department = 'NURSING' ")
    result = cursor.fetchall()
    result2 = cursor2.fetchall()
    result3 = cursor3.fetchall()
    result4 = cursor4.fetchall()
    result5 = cursor5.fetchall()
    conn.commit()
    conn.close()

    def cancels():
        root.destroy()


    def saveit(result):

        file = filedialog.asksaveasfilename(filetypes = [("CSV file",'*.csv')],defaultextension='.pdf',title= "Save a CSV file",initialfile="all Employees.csv",initialdir='C:\\Users\\ferna\\Downloads')
        with open(file, 'a',newline='') as f:
            w = csv.writer (f, dialect='excel')
            for record in result:
                w.writerow(record)
    
    def saveit2(result2):

        file = filedialog.asksaveasfilename(filetypes = [("CSV file",'*.csv')],defaultextension='.pdf',title= "Save a CSV file",initialfile="admin employees.csv",initialdir='C:\\Users\\ferna\\Downloads')
        with open(file, 'a',newline='') as f:
            w = csv.writer (f, dialect='excel')
            for record in result2:
                w.writerow(record)


    def saveit3(result3):

        file = filedialog.asksaveasfilename(filetypes = [("CSV file",'*.csv')],defaultextension='.pdf',title= "Save a CSV file",initialfile="ancillary employees.csv",initialdir='C:\\Users\\ferna\\Downloads')
        with open(file, 'a',newline='') as f:
            w = csv.writer (f, dialect='excel')
            for record in result3:
                w.writerow(record)

    def saveit4(result4):

        file = filedialog.asksaveasfilename(filetypes = [("CSV file",'*.csv')],defaultextension='.pdf',title= "Save a CSV file",initialfile="medical Employees.csv",initialdir='C:\\Users\\ferna\\Downloads')
        with open(file, 'a',newline='') as f:
            w = csv.writer (f, dialect='excel')
            for record in result4:
                w.writerow(record)

    def saveit5(result5):

        file = filedialog.asksaveasfilename(filetypes = [("CSV file",'*.csv')],defaultextension='.pdf',title= "Save a CSV file",initialfile="nursing employees.csv",initialdir='C:\\Users\\ferna\\Downloads')
        with open(file, 'a',newline='') as f:
            w = csv.writer (f, dialect='excel')
            for record in result5:
                w.writerow(record)







    alle = customtkinter.CTkLabel(p_frame, text="All Employees", font=('Arial', 14, 'bold'),text_color= "black",bg_color="transparent").place(x=55,y=220)
    sol = customtkinter.CTkButton(p_frame,text="Save as CSV",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=110, height=40, border_width=0, corner_radius=5,
    hover_color = '#2a4859',cursor='hand2', command=lambda: saveit(result))
    sol.place(x=50, y=250)

    alla = customtkinter.CTkLabel(p_frame, text="Admin Employees", font=('Arial', 14, 'bold'),text_color= "black",bg_color="transparent").place(x=175,y=290)
    sol2 = customtkinter.CTkButton(p_frame,text="Save as CSV",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=110, height=40, border_width=0, corner_radius=5,
    hover_color = '#2a4859',cursor='hand2', command=lambda: saveit2(result2))
    sol2.place(x=180, y=250)

    allan = customtkinter.CTkLabel(p_frame, text="Ancillary Employees", font=('Arial', 14, 'bold'),text_color= "black",bg_color="transparent").place(x=300,y=220)
    sol3 = customtkinter.CTkButton(p_frame,text="Save as CSV",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=110, height=40, border_width=0, corner_radius=5,
    hover_color = '#2a4859',cursor='hand2', command=lambda: saveit3(result3))
    sol3.place(x=310, y=250)

    
    allm = customtkinter.CTkLabel(p_frame, text="Medical Employees", font=('Arial', 14, 'bold'),text_color= "black",bg_color="transparent").place(x=430,y=290)
    sol4 = customtkinter.CTkButton(p_frame,text="Save as CSV",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=110, height=40, border_width=0, corner_radius=5,
    hover_color = '#2a4859',cursor='hand2', command=lambda: saveit4(result4))
    sol4.place(x=440, y=250)

    alln = customtkinter.CTkLabel(p_frame, text="Nursing Employees", font=('Arial', 14, 'bold'),text_color= "black",bg_color="transparent").place(x=560,y=220)
    sol5 = customtkinter.CTkButton(p_frame,text="Save as CSV",fg_color='#789c46',font=('Arial', 16,) ,bg_color= 'transparent', width=110, height=40, border_width=0, corner_radius=5,
    hover_color = '#2a4859',cursor='hand2', command=lambda: saveit5(result5))
    sol5.place(x=570, y=250)
        

    clo = customtkinter.CTkButton(p_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#9e9e9e',cursor='hand2',command= cancels)
    clo.place(x=560, y=410)


    
    root.mainloop()
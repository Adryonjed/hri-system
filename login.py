from tkinter import *
from database.db import *
from PIL import ImageTk
from time import strftime
import tkinter as tk
from tkinter import ttk
import customtkinter
import PIL.Image
from tkinter import messagebox



root = tk.Tk()
root.title("Login form")
root.geometry('925x500+500+200')
root.configure(bg='#4972b3')
root.resizable(False,False)




def login():

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM credentials WHERE user = %s AND pass = %s", (user.get(),pcode.get()))
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    if result:
        root.destroy()
        import main
        
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


dl= PIL.Image.open("Assets\\logo.png")
dlt = customtkinter.CTkImage(dl,size=(350,350))
ol5 = customtkinter.CTkLabel(root, text='', image = dlt).place(x=40, y=50)


frame= customtkinter.CTkFrame(root, width=350, height=350, bg_color="transparent",fg_color='white', corner_radius=50)
frame.place(x=470, y=70)
heading=customtkinter.CTkLabel(frame, text='Sign in', text_color='#57a1f8', bg_color='transparent', fg_color='transparent', font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=120, y=5)
#########
user = customtkinter.CTkEntry(frame, height= 30,width=300, fg_color='transparent',border_width = 0, bg_color="transparent", font=('Microsoft YaHei UI Light',14,'bold'),placeholder_text = "Username",placeholder_text_color= "gray",text_color='black')
user.place(x=30, y=80)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

pcode= customtkinter.CTkEntry (frame, height= 30,width=300, fg_color='transparent',border_width = 0, show = "*", bg_color="transparent", font=('Microsoft YaHei UI Light',14,'bold'),placeholder_text = "Password",placeholder_text_color= "gray",text_color='black')
pcode.place(x=30, y=150)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

addto = customtkinter.CTkButton(frame,text="Log In",fg_color='#46829c',font=('Microsoft YaHei UI Light', 20,) ,bg_color= 'transparent', width=260, height=35, border_width=0, corner_radius=5,
    hover_color = '#2a4859',cursor='hand2',command=login).place(x=40, y=215)

root.mainloop()
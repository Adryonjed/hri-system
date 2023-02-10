from tkinter import *
from db import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
import tkinter as tk
import customtkinter
from tkinter import filedialog
import base64
from PIL import ImageTk, Image
import PIL.Image
import math
from datetime import datetime
from time import strftime

def performance():
    f3 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8ad4c9",corner_radius=60)
    f3.place(x=380, y=200)

    

    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', font=('Arial', 12))
    

    sty = ttk.Style()
    sty.theme_use('clam')
    sty.configure("Treeview", rowheight="50",fieldbackground ='#dbd5d5',background = '#dbd5d5', borderwidth = 0,relief = 'flat')
    sty.configure("Treeview.Heading", font=(None, 20), background="#8f8d8d", borderwidth = 0, relief = "flat")
    sty.map("Treeview.Heading", background = [('active', "#8f8d8d")])
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

    mainframe3 = tk.Frame(f3,bg='#dbb2b2')
    mainframe3.place(x=380, y=200)
    mainframe3.pack_propagate(False)


    def deletef():
        for frame in mainframe3.winfo_children():
            frame.destroy()

    def indicate(page):

        deletef()
        page()

    ids = tk.StringVar()
    fname = tk.StringVar()
    sname = tk.StringVar()



    def check():

        find = str(find2Entry.get())
        if (find == "" or find == " "):
            messagebox.showinfo("Error", "Select a data or input your ID No.")
            return
        else:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM personal WHERE id=%s",(find2Entry.get()))
            result = cursor.fetchone()
            drow = result[0]
            drow1 = result[1]
            drow2 = result[2]

            if result:
                indicate(check_p)
                ids.set(drow)
                sname.set(drow1)
                fname.set(drow2)
            else:
                pass

        


    
    def check_p():

        f3_1 = customtkinter.CTkFrame(f3, width=1500, height=820, fg_color ="#8ad4c9",bg_color="#aee0e8",corner_radius=50)
        f3_1.place(x=0, y=0)

        snlabel = Label(f3_1, text="YOUR ID :", font=('Arial', 15, 'bold'),bg="#8ad4c9").place(x=30, y=30)
        res = Label(f3_1, text="", font=('Arial', 15, 'bold'),bg="#8ad4c9", textvariable=ids)
        res.place(x=140, y=30)

        snlabel = Label(f3_1, text="SURNAME :", font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=500, y=100)
        res1 = Label(f3_1, text="", font=('Arial', 20, 'bold'),bg="#8ad4c9", textvariable=sname)
        res1.place(x=670, y=100)

        fnlabel = Label(f3_1, text="FIRSTNAME :", font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=30, y=100)
        res2 = Label(f3_1, text="", font=('Arial', 20, 'bold'),bg="#8ad4c9", textvariable=fname)
        res2.place(x=220, y=100)

        
        
        f3_2 = customtkinter.CTkFrame(f3_1, fg_color ="transparent")
        f3_2.place(x=240, y=250)

        
        

        def shoow():

            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT datepass, quality, quantity, timeliness, average, remarks FROM rating WHERE id=%s ORDER BY datepass DESC",(find2Entry.get()))
            result = cursor.fetchall()
                        
            i = 0
            for g in result:

                for j in range(len(g)):
                    jo = Label(f3_2, text=g[j],font=('Arial', 14),background="#8ad4c9")
                    jo.grid(row=i, column=j,padx=30,pady=10)


                delp = customtkinter.CTkButton(f3_2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
                cursor='hand2',command=lambda k=g[0]:delete(k))
                delp.grid(row= i, column = 7,pady=10,padx = 50)

                i = i+1

                if i == 4:
                    break
                

            conn.commit()
            conn.close()
        shoow()

        def delete(d_datepass):

            
            decision = messagebox.askquestion("Warning!!", "Delete this data? ")
        
            if decision == "yes":
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM rating WHERE  datepass=%s",(d_datepass))
                conn.commit()
                conn.close()

                for row in f3_2.grid_slaves():
                    row.grid_forget()
                shoow()
            else:
                messagebox.showinfo("Error", "Sorry an error occured")


            

        def ups():
            root = customtkinter.CTkToplevel()
            root.geometry('800x400')
            root.overrideredirect(True)
            root.wm_attributes("-transparentcolor",'gray')
            

            def start_drag(e):
                e.widget.offset = (e.x, e.y)

            def move_app(e):
                # calculate the top-left corner of window based on the saved offset
                root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')

            def validate(u_input): 
                return u_input.isdigit()
            my_valid = root.register(validate)



            frow = customtkinter.CTkFrame(root, width=800,height=400,fg_color="#84a98c")
            frow.place(x=0,y=0)

            bgg = customtkinter.CTkFrame(root, width=800,height=60,fg_color="#283618")
            bgg.place(x=0,y=0)

            lavs = customtkinter.CTkLabel(bgg,text="RATING INPUT",font=('Arial', 40, 'bold'),bg_color="#283618", text_color='white').place(x=250,y=8)

            doblabel = Label(frow, text="Date taken:", font=('Courier', 14, 'bold'),bg="#84a98c").place(x=20, y=83)
            dta= DateEntry(frow, height= 25, width=10, font = ('arial', 18),date_pattern='mm/dd/y', background='gray', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
            dt = date(2023,1,1)
            dta.set_date(dt)
            dta.place(x=150, y= 80)

            qual = customtkinter.CTkEntry(frow,height= 40, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
            qual.place(x=130,y=150)

            quan = customtkinter.CTkEntry(frow,height= 40, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
            quan.place(x=280,y=150)

            til = customtkinter.CTkEntry(frow,height= 40, width=50, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
            til.place(x=440,y=150)


            def calc():

                global tots

                quali = int(qual.get())
                quant = int(quan.get())
                timel = int(til.get())
                sub = 0
                total = 0

                sub =  quali + quant + timel
                total =math.floor(sub / 3)
                

                tots = customtkinter.CTkLabel(frow, text= total, font=('Arial', 32))
                tots.place (x=580,y=155)

                global remarks

                if tots.cget("text") == 5:
                    remarks = customtkinter.CTkLabel(frow, text='OUTSTANDING', font=('Arial', 32))
                    remarks.place(x=220,y=250)
                elif tots.cget("text") == 4:
                    remarks = customtkinter.CTkLabel(frow, text='VERY SATISFACTORY', font=('Arial', 32))
                    remarks.place(x=220,y=250)
                elif tots.cget("text") == 3:
                    remarks = customtkinter.CTkLabel(frow, text='SATISFACTORY', font=('Arial', 32))
                    remarks.place(x=220,y=250)
                elif tots.cget("text") == 2:
                    remarks = customtkinter.CTkLabel(frow, text='UNSATISFACTORY', font=('Arial', 32))
                    remarks.place(x=220,y=250)
                elif tots.cget("text") == 1:
                    remarks = customtkinter.CTkLabel(frow, text='POOR', font=('Arial', 32))
                    remarks.place(x=220,y=250)
                else:
                    pass

        

            def proceeds():

                ids = str(res.cget("text"))
                rem = str(remarks.cget('text'))
                qua = str(qual.get())
                quann = str(quan.get())
                timell = str(til.get())
                totals = str(tots.cget("text"))
                dtake = str(dta.get_date())

                conn = connection()
                cursor = conn.cursor()
                cursor.execute(
                        "INSERT INTO rating VALUES ('""','"+ids+"','"+dtake+"','"+qua+"','"+quann+"','"+timell+"','"+totals+"','"+rem+"') ")
                conn.commit()
                conn.close()


                shoow()
                root.destroy()

            def cancels():
                root.destroy()


            lavs = Label(frow,text="5 - Outstanding\n4 - Very Satisfactory\n3 - Satisfactory\n2 - unsatisfactory\n1 - Poor",font=('Arial', 12, 'bold'),justify=LEFT,background="#84a98c", foreground='white').place(x=20,y=280)

            sol = customtkinter.CTkButton(frow,text="Solve",fg_color='#9c7846',font=('Arial', 20) ,bg_color= '#84a98c', width=100, height=50, border_width=0, corner_radius=10,
            hover_color = '#2a4859',cursor='hand2',command=calc)
            sol.place(x=600, y=300)

            
            pro = PIL.Image.open("Assets\\exit.png")
            checked2 = customtkinter.CTkImage(pro,size=(40,40))
            proceed= customtkinter.CTkButton(frow, text="", image=checked2, bg_color= '#84a98c',fg_color="#84a98c",hover_color= "#84a98c", width= 20,cursor='hand2',command=proceeds)
            proceed.place(x=710, y=300)

            can = PIL.Image.open("Assets\\cancel.png")
            checked2 = customtkinter.CTkImage(can,size=(40,40))
            cancel = customtkinter.CTkButton(bgg, text="", image=checked2, bg_color= '#283618',fg_color="#283618",hover_color= "#283618", width= 20,cursor='hand2',command=cancels)
            cancel.place(x=735,y=5)







            bgg.bind("<Button-1>", start_drag)
            bgg.bind("<B1-Motion>", move_app)

            root.mainloop()




        


        uptd = customtkinter.CTkButton(f3_1,text="Add Data",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=ups)
        uptd.place(x=1200, y=700)

         
        backt = customtkinter.CTkButton(f3_1 ,text="Back",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(performance))
        backt.place(x=1000, y=700)

        shoow()





    def read2():
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, firstname, surname, position, department FROM personal WHERE surname like %s",(find2Entry.get()))
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        
        return results


    def searching():
        for rows2 in my_tree.get_children():
            my_tree.delete(rows2)
        
        for array2 in read2():
            my_tree.insert(parent='', index='end', iid=array2, text="", values=(array2), tag="orow")

        

    def refresh():
        populate()
        refreshTable()




    search = customtkinter.CTkButton(f3,text="Search",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=100, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=searching)
    search.place(x=350, y=27)

    refr = PIL.Image.open("Assets\\refresh.png")
    ref = customtkinter.CTkImage(refr,size=(30,30))

    search2 = customtkinter.CTkButton(f3,text="",image = ref, bg_color= '#8ad4c9',fg_color="#8ad4c9",hover_color= "#8ad4c9", width= 20,cursor='hand2',command=refresh)
    search2.place(x=450, y=27)

        
    add3 = customtkinter.CTkButton(f3,text="Check",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=check)
    add3.place(x=1200, y=700)

   
        
    find2 = Label(f3, text="FIND : ", font=('Arial', 18, 'bold'),bg="#8ad4c9").place(x=50, y=30)
    find2Entry = customtkinter.CTkEntry(f3,height = 37, width=200, fg_color='white',border_width = 0 ,font=('Arial', 20),text_color='black',textvariable=fi)
    find2Entry.place(x=130, y=28)


    my_tree =ttk.Treeview(f3, show="headings", height=11)
    my_tree['columns'] = ("id","name","sur","pos","dept")


    my_tree.column("id", anchor=CENTER, width=287)
    my_tree.column("name", anchor=CENTER, width=287)
    my_tree.column("sur", anchor=CENTER, width=287)
    my_tree.column("pos", anchor=CENTER, width=287)
    my_tree.column("dept", anchor=CENTER, width=287)
    my_tree.heading("id", text="ID", anchor=CENTER)
    my_tree.heading("name", text="NAME", anchor=CENTER)
    my_tree.heading("sur", text="SURNAME", anchor=CENTER)
    my_tree.heading("pos", text="POSITION", anchor=CENTER)
    my_tree.heading("dept", text="DEPARTMENT", anchor=CENTER)
    my_tree.place(x=27, y=90)

    my_tree.bind("<Double-1>", dclick)
    populate()
    refreshTable()  
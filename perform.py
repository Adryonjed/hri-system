from pkgutil import read_code
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


def performance():
    f3 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8ad4c9",corner_radius=60)
    f3.place(x=380, y=200)

    

    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read2():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', font=('Arial', 12))
    

    sty = ttk.Style()
    sty.theme_use('clam')
    sty.configure("Treeview", rowheight="50",fieldbackground ='#dbd5d5',background = '#dbd5d5', borderwidth = 0,relief = 'flat')
    sty.configure("Treeview.Heading", font=(None, 20), background="#8f8d8d", borderwidth = 0, relief = "flat")
    sty.map("Treeview.Heading", background = [('active', "#8f8d8d")])
    sty.map('Treeview', background=[('selected', 'green')])




    def deletef():
        for frame in f3.winfo_children():
            frame.destroy()

    def indicate(page):

        deletef()
        page()

    ids = tk.StringVar()
    fname = tk.StringVar()
    sname = tk.StringVar()

#-------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------First Frame-----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------

    
    
    def history():

        global name, drow, drow1, drow2

        selected_item = my_tree.selection()[0]
        name = str(my_tree.item(selected_item)['values'][0])
        if name != name:
            messagebox.showinfo("Error", "Select a data or input your ID no.")
            return         
        else:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM personal WHERE id=%s",(name))
            result = cursor.fetchone()
            drow = result[0]
            drow1 = result[1]
            drow2 = result[2]

            if result:
                indicate(show_history)
                ids.set(drow)
                sname.set(drow1)
                fname.set(drow2)
            else:
                pass

    def show_history():

        f3_1 = customtkinter.CTkFrame(f3, width=1500, height=820, fg_color ="#8ad4c9",bg_color="#aee0e8",corner_radius=50)
        f3_1.place(x=0, y=0)

        snlabel = Label(f3_1, text="YOUR ID : " + str(drow), font=('Arial', 15, 'bold'),bg="#8ad4c9").place(x=30, y=30)

        fnlabel = Label(f3_1, text="FIRSTNAME : " + drow2, font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=30, y=100)
       
        snlabel = Label(f3_1, text="SURNAME : " + drow1, font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=500, y=100)


        nat = datetime.now() 
        now = nat.strftime("%b/%d/%y")
        doblabel = Label(f3_1,text=now, font=('Courier', 20, 'bold'),bg="#8ad4c9")
        doblabel.place(x=30, y=170)

        
        f3_2 = customtkinter.CTkFrame(f3_1, fg_color ="transparent",bg_color ="transparent")
        f3_2.place(x=240, y=250)

        

        def shoow():
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ids, datepass FROM image WHERE id=%s ORDER BY datepass DESC",(name))
            result = cursor.fetchall()


            i = 0
    
            for g in result:

                jo = Label(f3_2, text=g[1],font=('Arial', 14),background="#8ad4c9")
                jo.grid(row=i, column=1,padx=30,pady=10)
                jo2= Label(f3_2, text="Passed A Document",font=('Arial', 14),background="#8ad4c9",textvariable=g[0])
                jo2.grid(row=i, column=2,padx=30,pady=10)

                delp = customtkinter.CTkButton(f3_2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
                cursor='hand2',command=lambda k=g[0]:delete(k))
                delp.grid(row= i, column = 3,pady=10,padx = 30)

                delp = customtkinter.CTkButton(f3_2,text="view",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
                cursor='hand2',command=lambda k=g[0]:view(k))
                delp.grid(row= i, column = 4,pady=10,padx = 30)

                delp = customtkinter.CTkButton(f3_2,text="save",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= "#8ad4c9", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
                cursor='hand2',command=lambda k=g[0]:save(k))
                delp.grid(row= i, column = 5,pady=10,padx = 30)

                i = i+1

                if i == 4:
                    break
                

            conn.commit()
            conn.close()
        shoow()

        def delete(s_ids):

            
            decision = messagebox.askquestion("Warning!!", "Delete this data? ")
        
            if decision == "yes":
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM image WHERE  ids =%s",(s_ids))
                conn.commit()
                conn.close()

                for row in f3_2.grid_slaves():
                    row.grid_forget()
                shoow()
            else:
                pass

        def view(s_ids):
            root = customtkinter.CTkToplevel()
            root.geometry('800x1000')
            root.overrideredirect(True)
            root.wm_attributes("-transparentcolor",'gray')
            root.grab_set()
            

            def start_drag(e):
                e.widget.offset = (e.x, e.y)

            def move_app(e):
                # calculate the top-left corner of window based on the saved offset
                root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')

        
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM image WHERE ids=%s",(s_ids))
            result = cursor.fetchone()
            conn.commit()
            conn.close()

            img = PIL.Image.open(io.BytesIO(result[3]))
            imga = customtkinter.CTkImage(img,size=(300,600))

            fram = customtkinter.CTkFrame(root, bg_color='gray', fg_color='white',width=800,height=1000,corner_radius=30)
            fram.pack()
            imahe = customtkinter.CTkLabel(fram, text='', image=imga)
            imahe.place(x=250,y=0)

            def cancels():
                root.destroy()

            can = PIL.Image.open("Assets\\cancel.png")
            checked2 = customtkinter.CTkImage(can,size=(30,30))
            cancel = customtkinter.CTkButton(fram, text="", image=checked2, bg_color= 'white',fg_color="white",hover_color= "#8a8987", width= 20,cursor='hand2',command=cancels)
            cancel.place(x=740,y=10)


            fram.bind("<Button-1>", start_drag)
            fram.bind("<B1-Motion>", move_app)
            root.mainloop()

        def save(s_ids):

            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM image WHERE ids=%s",(s_ids))
            result = cursor.fetchone()
            conn.commit()
            conn.close()

            img = PIL.Image.open(io.BytesIO(result[3]))
            imga = customtkinter.CTkImage(img,size=(300,600))

            files = filedialog.asksaveasfilename(filetypes=[('JPG', '*.jpg'),('PNG', '*.png')],defaultextension=".png",initialdir="C:\\Users\\ferna\\Downloads\\",initialfile="docu.jpg",title="Save a File",confirmoverwrite=True)
            if files:
                img.save(files)
            else:
                messagebox.showinfo("Error", "No File has been saved")


        def upload():

            global file
            f_types = [('JPG', '*.jpg'),('PNG', '*.png')]
            file = filedialog.askopenfilename(filetypes=f_types)

            if file:
                fob = open(file, 'rb').read()
                conn = connection()
                cursor = conn.cursor()
                args = (ids.get(),doblabel.cget("text"),fob)
                
                cursor.execute("INSERT INTO image (id,datepass,img) VALUES (%s,%s,%s)",args)
                conn.commit()
                conn.close()
            else:
                messagebox.showinfo("Error", "No File Selected")
            shoow()



        uptd = customtkinter.CTkButton(f3_1,text="Add Data",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=upload)
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
    hover_color = '#2a4859',cursor='hand2',command=history)
    add3.place(x=1200, y=700)

   
        
    find2 = Label(f3, text="FIND : ", font=('Arial', 18, 'bold'),bg="#8ad4c9").place(x=50, y=30)
    find2Entry = customtkinter.CTkEntry(f3,height = 37, width=200, fg_color='white',border_width = 0 ,font=('Arial', 20),text_color='black')
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

    def dclick(e):
        history()

    my_tree.bind("<Double-1>", dclick)
    populate()
    refreshTable()  
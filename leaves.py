from tkinter import *
from database.db import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
import PIL.Image
from tkcalendar import DateEntry
from tkinter import filedialog
import io



def leave():
   f4 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8a9dd4")
   f4.place(x=380, y=200)
   ln = Label(f4, text="Total Employees", font=('Arial', 20), background="#86babd")
   ln.place(x=50, y=10)

   def deletef():
      for frame in f4.winfo_children():
         frame.destroy()

   def indicate (page):
      deletef()
      page()


   
   def refreshTable():
      for data in my_tree.get_children():
         my_tree.delete(data)

      for array in read():
         my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

      my_tree.tag_configure('orow', font=('Arial', 12))

   

   def history():

      global name,ide, fname,sname,pos,dept

      selected_item = my_tree.selection()[0]
      name = str(my_tree.item(selected_item)['values'][0])

      if name != name:
         messagebox.showinfo("Error", "Select a data or input your ID no.")
         return
      else:
         conn = connection()
         cursor = conn.cursor()
         cursor.execute("SELECT id, firstname, surname, position, department FROM personal WHERE id=%s",(name))
         result = cursor.fetchone()
         ide = result[0]
         fname = result[1]
         sname = result[2]
         pos = result[3]
         dept = result[4]
         indicate(show_leave)
      

   def show_leave():


      f4_1 = customtkinter.CTkFrame(f4, width=1500, height=820, fg_color ="#8ad4c9",bg_color="#aee0e8",corner_radius=50)
      f4_1.place(x=0, y=0)

      snlabel = Label(f4_1, text="YOUR ID : " + str(ide), font=('Arial', 15, 'bold'),bg="#8ad4c9").place(x=30, y=30)

      fnlabel = Label(f4_1, text="FIRSTNAME : " + fname , font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=70, y=100)

      snlabel = Label(f4_1, text="SURNAME : " + sname, font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=70, y=150)
   
      poslabel = Label(f4_1, text="POSITION : " + pos, font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=700, y=100)

      poslabel = Label(f4_1, text="DEPARTMENT : " + pos, font=('Arial', 20, 'bold'),bg="#8ad4c9").place(x=700, y=150)

      
      

      nat = datetime.now() 
      now = nat.strftime("%b %d, %Y")
      doblabel = Label(f4_1,text=now, font=('Arial', 20, 'bold'),bg="#8ad4c9")
      doblabel.place(x=1200, y=30)

       
      f5_2 = customtkinter.CTkScrollableFrame(f4_1, fg_color ="#8ad4c9",bg_color ="transparent",width=1200,height=350)
      f5_2.place(x=120, y=250)

      def show_data():
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("SELECT datefile, types, days, reco FROM leaves WHERE ids=%s ORDER BY datefile DESC",(name))
            result = cursor.fetchall()
            conn.commit()
            conn.close()

            i = 1

            tableframe = customtkinter.CTkFrame(f4_1,fg_color ="transparent",bg_color ="transparent",width=1200,height=50)
            tableframe.place(x=130,y=250)
            dfile = customtkinter.CTkLabel(tableframe, text="    Date Filed    ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

            tol = customtkinter.CTkLabel(tableframe, text="                  Type of Leave                    ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

            dayss = customtkinter.CTkLabel(tableframe, text=" Days ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

            aps = customtkinter.CTkLabel(tableframe, text="       Approval     ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            aps.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

            aps = customtkinter.CTkLabel(tableframe, text="                   ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            aps.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)

    
            for g in result:
                
                dtr=datetime.strftime(g[0],'%b/%d/%Y')

                dfile2 = customtkinter.CTkLabel(f5_2, text="                  ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
                dfile2.grid(row=0, column=0,padx=35,pady=10,sticky = NSEW)

                tol2 = customtkinter.CTkLabel(f5_2, text="                                                    ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
                tol2.grid(row=0, column=1,padx=35,pady=10,sticky = NSEW)

                dayss2 = customtkinter.CTkLabel(f5_2, text="      ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
                dayss2.grid(row=0, column=2,padx=35,pady=10,sticky = NSEW)

                ap2 = customtkinter.CTkLabel(f5_2, text="                  ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
                ap2.grid(row=0, column=3,padx=35,pady=10,sticky = NSEW)
                

                jo = customtkinter.CTkLabel(f5_2, text=dtr,font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black")
                jo.grid(row=i, column=0,padx=5,pady=10,sticky = NSEW)
                jo2= customtkinter.CTkLabel(f5_2, text=g[1],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
                jo2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
                jo3= customtkinter.CTkLabel(f5_2, text=g[2],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black")
                jo3.grid(row=i, column=2,padx=5,pady=10,sticky = NSEW)
                jo4= customtkinter.CTkLabel(f5_2, text=g[3],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black")
                jo4.grid(row=i, column=3,padx=5,pady=10,sticky = NSEW)

                dell = customtkinter.CTkButton(f5_2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= "transparent", width=90, height=35, border_width=0, corner_radius=10,hover_color = '#2a4859',
                cursor='hand2',command=lambda k=g[0]:delete(k))
                dell.grid(row= i, column = 4,pady=10,padx = 30)
         
                i = i+1

                if i == 7:
                    break
                

            
      show_data()

      def delete(s_datefile):

            
            decision = messagebox.askquestion("Warning!!", "Delete this data? ")
        
            if decision == "yes":
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM leaves WHERE  datefile =%s",(s_datefile))
                conn.commit()
                conn.close()

                for row in f5_2.grid_slaves():
                    row.grid_forget()
                show_data()
            else:
                pass


      def apply():
         root = customtkinter.CTkToplevel()
         root.geometry('1200x700')
         root.overrideredirect(True)
         root.wm_attributes("-transparentcolor",'#333333')
         root.grab_set()

         def start_drag(e):
            e.widget.offset = (e.x, e.y)

         def move_app(e):
            root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')


         l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=1200,height=700,corner_radius=30)
         l_frame.pack()


         def cancels():
            root.destroy()
            aply.configure(state = NORMAL)

         def solve(): 
            global days

            diff_days=(ltoentry.get_date() - lfromentry.get_date()).days
            total.configure(text=str(diff_days) + ' Days')
            days = str(diff_days)


         def upl_mc():

            global imgfile, imgs

            f_types = [('JPG', '*.jpg'),('PNG', '*.png')]
            imgfile = filedialog.askopenfilename(filetypes=f_types)
            photo = PIL.Image.open(imgfile)
            imgs = customtkinter.CTkImage(photo,size=(70,100))

            def mc_view():
               view_f = customtkinter.CTkToplevel()
               view_f.geometry('800x1000')
               view_f.overrideredirect(True)
               view_f.wm_attributes("-transparentcolor",'gray')
               view_f.grab_set()


               def start_drag2(e):
                e.widget.offset = (e.x, e.y)

               def move_app2(e):
         
                  view_f.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')

               imgview = customtkinter.CTkImage(photo,size=(700,900))

               view_frame = customtkinter.CTkFrame(view_f, bg_color='gray', fg_color='white',width=800,height=1000,corner_radius=30)
               view_frame.pack()

               imahe = customtkinter.CTkLabel(view_frame, text='', image=imgview)
               imahe.place(x=40,y=50)

               def cancels():
                  view_f.destroy()

               can = PIL.Image.open("Assets\\cancel.png")
               checked2 = customtkinter.CTkImage(can,size=(30,30))
               cancel = customtkinter.CTkButton(view_frame, text="", image=checked2, bg_color= 'white',fg_color="white",hover_color= "#8a8987", width= 20,cursor='hand2',command=cancels)
               cancel.place(x=740,y=10)

               view_frame.bind("<Button-1>", start_drag2)
               view_frame.bind("<B1-Motion>", move_app2)
               view_f.mainloop()

            vie = customtkinter.CTkButton(l_frame,text="",image=imgs,width=70,height=100, cursor='hand2',bg_color="transparent", fg_color="transparent", command=mc_view)
            vie.place(x=570, y=450)

         def imgsave():

            if imgfile:
                fob = open(imgfile, 'rb').read()
                conn = connection()
                cursor = conn.cursor()
                args = (ide,doblabel.cget("text"),fob)
                
                cursor.execute("INSERT INTO medcert (idd,datefile,img) VALUES (%s,%s,%s)",args)
                conn.commit()
                conn.close()
            else:
                messagebox.showinfo("Error", "No File Selected")
   

         def proceed():

            idss = str(ide)
            dfile = str(dofentry.get_date())
            typ = str(tyle.get())
            froo =  str(lfromentry.get_date())
            too =  str(ltoentry.get_date())
            comm = str(cmt.get())
            reco = str(rec.get())
            vsp = str(vspltb.get("1.0","end-1c"))
            ics = str(icsltb.get("1.0","end-1c"))
            bw = str(lbwtb.get("1.0","end-1c"))
            stl = str(stud.get())
            ops = str(oth.get())
      
            if (typ == "" or typ == " ") or (froo == "" or froo == " ") or (too == "" or too == " ") or (comm == "" or comm == " ") or (reco == "" or reco == " "):
                  messagebox.showinfo("Error", "Please fill up the blank entry")
                  return
            else:
                  try:
                     msg = messagebox.askquestion('',"Do you want to add this person?")
                     if msg == 'yes':
                        conn = connection()
                        cursor = conn.cursor()
                        cursor.execute(
                           "INSERT INTO leaves VALUES ('""','"+idss+"','"+dfile+"','"+typ+"','"+froo+"','"+too+"','"+days+"','"+comm+"','"+reco+"','"+vsp+"','"+ics+"','"+bw+"','"+stl+"','"+ops+"') ")
                        conn.commit()
                        conn.close()

                        root.destroy()
                        aply.configure(state = NORMAL)
                     elif msg == 'no':
                        pass
                     else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                        root.destroy()
                        aply.configure(state = NORMAL)
                  except:
                       messagebox.showinfo("Error", "Data already exist")
                       return
            show_data()

         def allsave():
            imgsave()
            proceed()



         dof = customtkinter.CTkLabel(l_frame, text="Date Filing: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=50)
         dofentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
         dofentry.set_date(nat)
         dofentry.place(x=150,y=50)

         tol = customtkinter.CTkLabel(l_frame, text="Type of Leave: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=102)
         tyle = tk.StringVar()
         st = customtkinter.CTkOptionMenu(l_frame,height= 35, width = 400,fg_color='#b8b8b8',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = '#a19e9d',text_color = "black",variable = tyle, values=["Vacation Leave", "Mandatory/Forced Leave", "Sick Leave", "Maternity Leave", "Paternity Leave", "Special Previlege Leave", "Solo Parent Leave", "Study Leave", "10-Day VAWC Leave", "Rehabilitaion Leave", "Special Leave Benefits for Women", "Special Emergency","Adoption"])
         st.place(x=190, y= 100)
         st.set("")

         nool = customtkinter.CTkLabel(l_frame, text="Number of Working days applied for", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=200)

         lfrom = customtkinter.CTkLabel(l_frame, text="From: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=252)
         lfromentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
         lfromentry.set_date(nat)
         lfromentry.place(x=100, y= 250)

         lto = customtkinter.CTkLabel(l_frame, text="To: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=250, y=252)
         ltoentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
         ltoentry.set_date(nat)
         ltoentry.place(x=305, y= 250)

         total = Label(l_frame, text="Days", font=('Arial', 16, 'bold'),bg="white")
         total.place(x=480, y=252)

         comm = customtkinter.CTkLabel(l_frame, text="Commutation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=100)
         cmt = tk.StringVar()
         opcm1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Requested", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Requested",bg_color ="white",variable=cmt, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 150)
         opcm2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Not Requested",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Not Requested",bg_color ="white",variable=cmt, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 150)
         cmt.set(None)

         recom = customtkinter.CTkLabel(l_frame, text="Recommendation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=200)
         rec = tk.StringVar()
         opre1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Approve", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Approve",bg_color="transparent",variable=rec, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 250)
         opre2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Decline",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Decline",bg_color="transparent",variable=rec, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 250)
         rec.set(None)

         vspl = customtkinter.CTkLabel(l_frame, text="In case of Vacation/Special Privilege Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=350)
         vspltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
         vspltb.place(x=50, y= 390)

         icsl = customtkinter.CTkLabel(l_frame, text="In case of Sick Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=450)
         icsltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
         icsltb.place(x=50, y= 490)

         lbw = customtkinter.CTkLabel(l_frame, text="In case of Special Leave Benefits for Women:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=550)
         lbwtb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
         lbwtb.place(x=50, y= 590)

         csl = customtkinter.CTkLabel(l_frame, text="In case of Study Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=350)
         stud = tk.StringVar()
         opcsl1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Completion of Master's Degree", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color="transparent",variable=stud, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 380)
         opcsl2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="BAR/Board Examination Review",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color="transparent",variable=stud, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 410)
         stud.set(None)

         op = customtkinter.CTkLabel(l_frame, text="Other purpose:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=450)
         oth = tk.StringVar()
         op1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Monetization of Leave Credits", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color="transparent",variable=oth, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 480)
         op2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Terminal Leave",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color="transparent",variable=oth, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 510)
         oth.set(None)

         sol = customtkinter.CTkButton(l_frame,text="count",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
         hover_color = '#2a4859',cursor='hand2',command= solve)
         sol.place(x=480, y=300)

         upl = customtkinter.CTkButton(l_frame,text="Upload",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
         hover_color = '#2a4859',cursor='hand2',command= upl_mc)
         upl.place(x=480, y=490)

         

         proc = customtkinter.CTkButton(l_frame,text="Proceed",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
         hover_color = '#2a4859',cursor='hand2',command= allsave)
         proc.place(x=900, y=625)

         can = PIL.Image.open("Assets\\cancel.png")
         checked2 = customtkinter.CTkImage(can,size=(30,30))
         cancel = customtkinter.CTkButton(l_frame, text="", image=checked2, bg_color= 'white',fg_color="white",hover_color= "#8a8987", width= 20,cursor='hand2',command=cancels)
         cancel.place(x=1135,y=15)

         aply.configure(state = DISABLED)

         root.bind("<Button-1>", start_drag)
         root.bind("<B1-Motion>", move_app)

         root.mainloop()


      aply = customtkinter.CTkButton(f4_1,text="Apply for leave",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=apply)
      aply.place(x=1200, y=700)

      
      backt = customtkinter.CTkButton(f4_1 ,text="Back",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(leave))
      backt.place(x=1000, y=700)

      show_data()

   

   sty = ttk.Style()
   sty.theme_use('clam')
   sty.configure("Treeview", rowheight="50",fieldbackground ='#dbd5d5',background = '#dbd5d5', borderwidth = 0,relief = 'flat')
   sty.configure("Treeview.Heading", font=(None, 20), background="#8f8d8d", borderwidth = 0, relief = "flat")
   sty.map("Treeview.Heading", background = [('active', "#8f8d8d")])
   sty.map('Treeview', background=[('selected', 'green')])

   my_tree =ttk.Treeview(f4, show="headings", height=11)
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
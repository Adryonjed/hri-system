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
from leaveForm.EditLeave import *
from leaveForm.exprtleave import *


def show_leave(s_id):
      
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal WHERE id=%s",(s_id))
    result = cursor.fetchone()
    ide = result[0]
    fname = result[2]
    sname = result[1]
    conn.commit()
    conn.close()
    


    f4_1 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#d4d4d4",bg_color="transparent",corner_radius=50)
    f4_1.place(x=380, y=200)

    nat = datetime.now() 
    now = nat.strftime("%b %d, %Y")

    f2title = customtkinter.CTkFrame(f4_1, width=1450, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
    f2title.place(x=20, y=20)

    tit = customtkinter.CTkLabel(f2title, text=result[2], font=("Arial", 30, 'bold'))
    tit.place(x=20,y=20)
    subtit = customtkinter.CTkLabel(f2title, text=result[1] + " - " + result[17], font=("Arial", 20))
    subtit.place(x=20,y=60)
    doblabel = customtkinter.CTkLabel(f2title,text=now, font=('Arial', 16, 'bold'))
    doblabel.place(x=1330, y=20)


    f5_2 = customtkinter.CTkScrollableFrame(f4_1, fg_color ="#d4d4d4",bg_color ="transparent",width= 1380,height= 500)
    f5_2.place(x=50, y=150)

    ed = PIL.Image.open("Assets\\edit.png")
    edt = customtkinter.CTkImage(ed,size=(25,25))

    dl = PIL.Image.open("Assets\\downloads.png")
    dwl = customtkinter.CTkImage(dl,size=(25,25))

    def show_data():
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ide, datefile, types, day, reco FROM leaves WHERE ids=%s ORDER BY datefile DESC",(s_id))
        result = cursor.fetchall()
        conn.commit()
        conn.close()


        i = 1

        tableframe = customtkinter.CTkFrame(f4_1,fg_color ="transparent",bg_color ="transparent",width=1200,height=50)
        tableframe.place(x=55,y=150)

        dfile = customtkinter.CTkLabel(tableframe, text="Date Filed                    ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dfile.grid(row=0, column=0,padx=5,pady=10,sticky = NSEW)

        tol = customtkinter.CTkLabel(tableframe, text="Type of Leave                                             ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        tol.grid(row=0, column=1,padx=5,pady=10,sticky = NSEW)

        dayss = customtkinter.CTkLabel(tableframe, text="Days                 ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        dayss.grid(row=0, column=2,padx=5,pady=10,sticky = NSEW)

        aps = customtkinter.CTkLabel(tableframe, text="Approval                ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        aps.grid(row=0, column=3,padx=5,pady=10,sticky = NSEW)

        aps = customtkinter.CTkLabel(tableframe, text="Action  ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
        aps.grid(row=0, column=4,padx=5,pady=10,sticky = NSEW)


        for g2 in result:
            
            dtr=datetime.strftime(g2[1],'%b/%d/%Y')

            dfile2 = customtkinter.CTkLabel(f5_2, text="                              ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dfile2.grid(row=0, column=0,padx=35,pady=10,sticky = NSEW)

            tol2 = customtkinter.CTkLabel(f5_2, text="                                                               ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            tol2.grid(row=0, column=1,padx=35,pady=10,sticky = NSEW)

            dayss2 = customtkinter.CTkLabel(f5_2, text="                 ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            dayss2.grid(row=0, column=2,padx=35,pady=10,sticky = NSEW)

            ap2 = customtkinter.CTkLabel(f5_2, text="                 ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ap2.grid(row=0, column=3,padx=35,pady=10,sticky = NSEW)

            ac = customtkinter.CTkLabel(f5_2, text="      ",font=('Arial', 26, 'bold'),bg_color="transparent",text_color="black")
            ac.grid(row=0, column=4,padx=35,pady=10,sticky = NSEW)
            

            jo = customtkinter.CTkLabel(f5_2, text=dtr,font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo.grid(row=i, column=0,padx=5,pady=10,sticky = NSEW)
            jo2= customtkinter.CTkLabel(f5_2, text=g2[2],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo2.grid(row=i, column=1,padx = 5,pady=10,sticky = NSEW)
            jo3= customtkinter.CTkLabel(f5_2, text=g2[3],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo3.grid(row=i, column=2,padx=5,pady=10,sticky = NSEW)
            jo4= customtkinter.CTkLabel(f5_2, text=g2[4],font=('Arial', 18, 'bold'),bg_color="transparent",text_color="black",anchor=W)
            jo4.grid(row=i, column=3,padx=5,pady=10,sticky = NSEW)

            shoow = customtkinter.CTkButton(f5_2,text="",image= edt, fg_color='#46729c',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=g2[0]:showit(k))
            shoow.grid(row= i, column = 4,pady=5,padx = 2)

            expt = customtkinter.CTkButton(f5_2,text="",image= dwl, fg_color='#9c9346',font=('Arial', 20,) ,bg_color= 'transparent', width=40, height=35, border_width=0, corner_radius=10,
            hover_color = '#2a4859' , command=lambda k=g2[0]:exprtit(k))
            expt.grid(row= i, column = 5,pady=5,padx = 2)

            i = i+1
    
    show_data()

    def showit(s_ide):
        show_apply(s_ide)

    def exprtit(s_ide):
        saveasfile(s_ide)


    def apply():
        root = customtkinter.CTkToplevel()
        root.geometry('1200x790+500+200')
        root.overrideredirect(True)
        root.title("Leave Form")
        root.wm_attributes("-transparentcolor",'#333333')
        root.wait_visibility()
        root.grab_set()


        l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=1200,height=790,corner_radius=30)
        l_frame.pack()

        f2title = customtkinter.CTkFrame(l_frame, width=1170, height=100, fg_color ="#4976bf",corner_radius=30,bg_color="transparent")
        f2title.place(x=15, y=20)

        tit = customtkinter.CTkLabel(f2title, text="LEAVE APPLICATION", font=("Arial", 30, 'bold'))
        tit.place(x=20,y=20)
        subtit = customtkinter.CTkLabel(f2title, text="Apply for Leave", font=("Arial", 20))
        subtit.place(x=20,y=60)


        def cancels():
            root.destroy()
            aply.configure(state = NORMAL)

        def solve(): 
            global days

            diff_days=(ltoentry.get_date() - lfromentry.get_date()).days
            total.configure(text=str(diff_days) + ' Days')
            days = str(diff_days)


        def proceed():

            idss = str(ide)
            ffname = str(fname)
            ssname = str(sname)
            dfile = str(dofentry.get_date())
            typ = str(tyle.get())
            froo =  str(lfromentry.get_date())
            too =  str(ltoentry.get_date())
            vsp = str(vspltb.get("1.0","end-1c"))
            ics = str(icsltb.get("1.0","end-1c"))
            ifp = str(medcert.get())
            bw = str(bbw.get())
            sts = str(stts.get("1.0","end-1c"))
            comm = str(cmt.get())
            reco = str(rec.get())
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
                                "INSERT INTO leaves VALUES ('""','"+idss+"','"+dfile+"','"+ffname+"','"+ssname+"','"+typ+"','"+froo+"','"+too+"','"+days+"','"+comm+"','"+reco+"','"+vsp+"','"+ics+"','"+ifp+"','"+bw+"','"+sts+"','"+stl+"','"+ops+"') ")
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


        dof = customtkinter.CTkLabel(l_frame, text="Date Filing: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=140)
        dofentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
        dofentry.set_date(nat)
        dofentry.place(x=150,y=140)

        tol = customtkinter.CTkLabel(l_frame, text="Type of Leave: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=202)
        tyle = tk.StringVar()
        st = customtkinter.CTkOptionMenu(l_frame,height= 35, width = 400,fg_color='#b8b8b8',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = '#a19e9d',text_color = "black",variable = tyle, values=["Vacation Leave", "Mandatory/Forced Leave", "Sick Leave", "Paternity Leave", "Special Previlege Leave", "Solo Parent Leave", "Study Leave", "10-Day VAWC Leave", "Rehabilitaion Leave", "Special Leave Benefits for Women", "Special Emergency","Adoption"])
        st.place(x=190, y= 200)
        st.set("")

        nool = customtkinter.CTkLabel(l_frame, text="Number of Working days applied for:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=260)

        lfrom = customtkinter.CTkLabel(l_frame, text="From: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=30, y=300)
        lfromentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
        lfromentry.set_date(nat)
        lfromentry.place(x=100, y= 300)

        lto = customtkinter.CTkLabel(l_frame, text="To: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=260, y=300)
        ltoentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
        ltoentry.set_date(nat)
        ltoentry.place(x=305, y= 300)

        total = Label(l_frame, text="Days", font=('Arial', 16, 'bold'),bg="white")
        total.place(x=480, y=300)

        sol = customtkinter.CTkButton(l_frame,text="count",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command= solve)
        sol.place(x=480, y=350)

        vspl = customtkinter.CTkLabel(l_frame, text="In case of Vacation/Special Privilege Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=410)
        vspltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
        vspltb.place(x=50, y= 450)

        att = customtkinter.CTkLabel(l_frame, text="In Case Attended a Seminar:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=510)
        stts = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
        stts.place(x=50, y= 550)

        icsl = customtkinter.CTkLabel(l_frame, text="In case of Sick Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=610)
        icsltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
        icsltb.place(x=50, y= 650)

        med = customtkinter.CTkLabel(l_frame, text="Passed a Medical Certificate:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=50, y=710)
        medcert = tk.StringVar()
        medcert1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Yes", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value="Yes",bg_color="transparent",variable=medcert, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=80,y= 750)
        medcert2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="No",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value="No",bg_color="transparent",variable=medcert, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=180,y= 750)
        medcert.set(None)

        comm = customtkinter.CTkLabel(l_frame, text="Commutation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=200)
        cmt = tk.StringVar()
        opcm1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Requested", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Requested",bg_color ="white",variable=cmt, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 250)
        opcm2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Not Requested",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Not Requested",bg_color ="white",variable=cmt, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 250)
        cmt.set(None)

        recom = customtkinter.CTkLabel(l_frame, text="Recommendation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=300)
        rec = tk.StringVar()
        opre1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Approved", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Approved",bg_color="transparent",variable=rec, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 350)
        opre2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Declined",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Declind",bg_color="transparent",variable=rec, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 350)
        rec.set(None)

        csl = customtkinter.CTkLabel(l_frame, text="In case of Study Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=410)
        stud = tk.StringVar()
        opcsl1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Completion of Master's Degree", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value="Completion of Masters Degree",bg_color="transparent",variable=stud, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 450)
        opcsl2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="BAR/Board Examination Review",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='BAR/Board Examination Review',bg_color="transparent",variable=stud, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 480)
        stud.set(None)

        op = customtkinter.CTkLabel(l_frame, text="Other purpose:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=510)
        oth = tk.StringVar()
        op1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Monetization of Leave Credits", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Monetization of Leave Credits',bg_color="transparent",variable=oth, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 550)
        op2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Terminal Leave",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Terminal Leave',bg_color="transparent",variable=oth, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 580)
        oth.set(None)

        lbw = customtkinter.CTkLabel(l_frame, text="In case of Special Leave Benefits for Women:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700,y=610)
        bbw = tk.StringVar()
        lbwtb = customtkinter.CTkOptionMenu(l_frame,height= 35, width = 400,fg_color='#b8b8b8',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = '#a19e9d',text_color = "black",variable = bbw, values=["Maternity Leave", "VAWC", "gynecological disorder"])
        lbwtb.place(x=750, y= 650)
        bbw.set("")
        

        proc = customtkinter.CTkButton(l_frame,text="Save Data",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=115, height=50, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command= proceed)
        proc.place(x=855, y=710)

        clo = customtkinter.CTkButton(l_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
        hover_color = '#9e9e9e',cursor='hand2',command= cancels)
        clo.place(x=990, y=710)

        aply.configure(state = DISABLED)

        root.mainloop()

    aply = customtkinter.CTkButton(f4_1,text="Apply for leave",fg_color='#46829c',font=('Arial', 20,) ,bg_color= 'transparent', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=apply)
    aply.place(x=1200, y=700)



    show_data()
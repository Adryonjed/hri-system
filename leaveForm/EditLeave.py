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




def show_apply(s_ide):
    root = customtkinter.CTkToplevel()
    root.geometry('1200x790+500+200')
    root.overrideredirect(True)
    root.title("Leave Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()



    l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=1200,height=790,corner_radius=30)
    l_frame.pack()

    ides = tk.StringVar()

    def id(word,num):
        if num == 1:
            ides.set(word)

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leaves WHERE ide = %s",(s_ide))
    results = cursor.fetchone()
    id(results[0],1)

    nat = datetime.now() 
    now = nat.strftime("%b %d, %Y")
    doblabel = Label(text=now)
  
    def cancels():
        root.destroy()
        

    def solve(): 
        global days

        diff_days=(ltoentry.get_date() - lfromentry.get_date()).days
        total.configure(text=str(diff_days) + ' Days')
        days = str(diff_days)



    idd = Label(textvariable=ides)


    def proceed():

        idss = str(idd.cget("text"))
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
        recc = str(rec.get())
        stl = str(stud.get())
        ops = str(oth.get())

    
        if (typ == "" or typ == " ") or (froo == "" or froo == " ") or (too == "" or too == " ") or (comm == "" or comm == " ") or (recc == "" or recc == " "):
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
        else:
                try:
                    msg = messagebox.askquestion('',"Do you want to add this person?")
                    if msg == 'yes':
                        conn = connection()
                        cursor = conn.cursor()
                        cursor.execute("UPDATE leaves SET datefile = '"+dfile+"', types = '"+typ+"', fromdate  = '"+froo+"', todate = '"+too+"', day = '"+days+"', commu = '"+comm+"', reco = '"+recc+"', vspl = '"+vsp+"', sl = '"+ics+"', conditions = '"+ifp+"', lbw = '"+bw+"' , sem = '"+sts+"' , studl = '"+stl+"' , others = '"+ops+"' WHERE ide = '"+idss+"' ")
                        conn.commit()
                        conn.close()

                        root.destroy()
                        
                    elif msg == 'no':
                        pass
                    else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                        root.destroy()
                       
                except:
                    messagebox.showinfo("Error", "Data already exist")
                    return
        


    dof = customtkinter.CTkLabel(l_frame, text="Date Filing: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=50)
    dofentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
    dofentry.set_date(results[2])
    dofentry.place(x=150,y=50)

    tol = customtkinter.CTkLabel(l_frame, text="Type of Leave: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=102)
    tyle = tk.StringVar()
    st = customtkinter.CTkOptionMenu(l_frame,height= 35, width = 400,fg_color='#b8b8b8',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = '#a19e9d',text_color = "black",variable = tyle, values=["Vacation Leave", "Mandatory/Forced Leave", "Sick Leave", "Maternity Leave", "Paternity Leave", "Special Previlege Leave", "Solo Parent Leave", "Study Leave", "10-Day VAWC Leave", "Rehabilitaion Leave", "Special Leave Benefits for Women", "Special Emergency","Adoption"])
    st.place(x=190, y= 100)
    st.set(results[3])

    nool = customtkinter.CTkLabel(l_frame, text="Number of Working days applied for:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=165)

    lfrom = customtkinter.CTkLabel(l_frame, text="From: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=212)
    lfromentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
    lfromentry.set_date(results[4])
    lfromentry.place(x=100, y= 210)

    lto = customtkinter.CTkLabel(l_frame, text="To: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=250, y=212)
    ltoentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
    ltoentry.set_date(results[5])
    ltoentry.place(x=305, y= 210)

    total = Label(l_frame, text=str(results[6]) + " Days", font=('Arial', 16, 'bold'),bg="white")
    total.place(x=480, y=212)

    sol = customtkinter.CTkButton(l_frame,text="count",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= solve)
    sol.place(x=480, y=250)

    vspl = customtkinter.CTkLabel(l_frame, text="In case of Vacation/Special Privilege Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=300)
    vspltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
    vspltb.place(x=50, y= 340)

    icsl = customtkinter.CTkLabel(l_frame, text="In case of Sick Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=400)
    icsltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent",fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
    icsltb.place(x=50, y= 440)

    med = customtkinter.CTkLabel(l_frame, text="If Sick leave, Passed a Medical Certificate:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=500)
    medcert = tk.StringVar()
    medcert1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Yes", radiobutton_height= 20, radiobutton_width= 20, border_width_checked = 10, border_width_unchecked= 5, value="Yes",bg_color="transparent",variable=medcert, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=50,y= 530)
    medcert2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="No",radiobutton_height= 20, radiobutton_width= 20, border_width_checked = 10, border_width_unchecked= 5, value="No",bg_color="transparent",variable=medcert, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=140,y= 530)
    medcert.set(results[11])

    lbw = customtkinter.CTkLabel(l_frame, text="In case of Special Leave Benefits for Women:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=560)
    bbw = tk.StringVar()
    lbwtb = customtkinter.CTkOptionMenu(l_frame,height= 35, width = 400,fg_color='#b8b8b8',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = '#a19e9d',text_color = "black",variable = bbw, values=["Maternity Leave", "VAWC", "gynecological disorder"])
    lbwtb.place(x=50, y= 600)
    bbw.set(results[12])

    att = customtkinter.CTkLabel(l_frame, text="In Case Attended a Seminar:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=650)
    stts = customtkinter.CTkTextbox(l_frame,height= 50, width = 400,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
    stts.place(x=50, y= 690)

    comm = customtkinter.CTkLabel(l_frame, text="Commutation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=100)
    cmt = tk.StringVar()
    opcm1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Requested", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Requested",bg_color ="white",variable=cmt, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 150)
    opcm2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Not Requested",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Not Requested",bg_color ="white",variable=cmt, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 150)
    cmt.set(results[7])

    recom = customtkinter.CTkLabel(l_frame, text="Recommendation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=200)
    rec = tk.StringVar()
    opre1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Approve", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Approve",bg_color="transparent",variable=rec, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 250)
    opre2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Decline",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Decline",bg_color="transparent",variable=rec, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 250)
    rec.set(results[8])

    csl = customtkinter.CTkLabel(l_frame, text="In case of Study Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=350)
    stud = tk.StringVar()
    opcsl1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Completion of Master's Degree", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color="transparent",variable=stud, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 380)
    opcsl2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="BAR/Board Examination Review",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color="transparent",variable=stud, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 410)
    stud.set(results[14])

    op = customtkinter.CTkLabel(l_frame, text="Other purpose:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=450)
    oth = tk.StringVar()
    op1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Monetization of Leave Credits", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color="transparent",variable=oth, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 480)
    op2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Terminal Leave",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color="transparent",variable=oth, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 510)
    oth.set(results[15])
    

    proc = customtkinter.CTkButton(l_frame,text="Save Data",fg_color='#4b6bab',font=('Arial', 20,) ,bg_color= 'transparent', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= proceed)
    proc.place(x=855, y=690)

    clo = customtkinter.CTkButton(l_frame,text="Close",fg_color='transparent',font=('Arial', 20,) ,bg_color= 'transparent',text_color='black', width=115, height=50, border_width=0, corner_radius=10,
    hover_color = '#9e9e9e',cursor='hand2',command= cancels)
    clo.place(x=990, y=690)



    root.mainloop()

    


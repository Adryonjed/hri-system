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




def show_apply(s_ids):
    root = customtkinter.CTkToplevel()
    root.geometry('1200x700')
    root.overrideredirect(True)
    root.title("Leave Form")
    root.wm_attributes("-transparentcolor",'#333333')
    root.wait_visibility()
    root.grab_set()


    def start_drag(e):
        e.widget.offset = (e.x, e.y)

    def move_app(e):
        root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')


    l_frame = customtkinter.CTkFrame(root, bg_color='#333333', fg_color='white',width=1200,height=700,corner_radius=30)
    l_frame.pack()

    idss = tk.StringVar()

    def id(word,num):
        if num == 1:
            idss.set(word)

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ide, ids, datefile, types, fromdate, todate, commu, reco,studl, others FROM leaves WHERE ide = %s",(s_ids))
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


    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medcert WHERE id = %s",(s_ids))
    imgres = cursor.fetchone()
    conn.commit()
    conn.close()

    imga = PIL.Image.open(io.BytesIO(imgres[3]))
    imgs = customtkinter.CTkImage(imga,size=(70,100))


    def upl_mc():

        global imgfile, photo, imahe
        f_types = [('JPG', '*.jpg'),('PNG', '*.png')]
        imgfile = filedialog.askopenfilename(filetypes=f_types)
        photo = PIL.Image.open(imgfile)
        img = customtkinter.CTkImage(photo,size=(70,100))
        imgv= customtkinter.CTkImage(photo,size=(700,900))
        
        vie.configure(image=img)
        imahe.configure(image=imgv)

    def mc_view():

        global photo, imahe

        view_f = customtkinter.CTkToplevel()
        view_f.geometry('800x1000')
        view_f.overrideredirect(True)
        view_f.wm_attributes("-transparentcolor",'gray')
        view_f.grab_set()


        def start_drag2(e):
            e.widget.offset = (e.x, e.y)

        def move_app2(e):
    
            view_f.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}')

        imgview = customtkinter.CTkImage(imga,size=(700,900))

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

        

    def imgsave():

        idd = Label(textvariable=idss)
        ides = str(idd.cget("text"))

        if imgfile:
            fob = open(imgfile, 'rb').read()
            conn = connection()
            cursor = conn.cursor()
            args = (fob,ides)
            
            cursor.execute("UPDATE medcert SET img=%s WHERE id = %s",args)
            conn.commit()
            conn.close()
        else:
            messagebox.showinfo("Error", "No File Selected")

    


    def proceed():

        idd = Label(textvariable=idss)
        ides = str(idd.cget("text"))

        dfile = str(dofentry.get_date())
        typ = str(tyle.get())
        froo =  str(lfromentry.get_date())
        too =  str(ltoentry.get_date())
        comm = str(cmt.get())
        recc = str(rec.get())
        vsp = str(vspltb.get("1.0","end-1c"))
        ics = str(icsltb.get("1.0","end-1c"))
        bw = str(lbwtb.get("1.0","end-1c"))
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
                        cursor.execute("UPDATE leaves SET datefile = '"+dfile+"', types = '"+typ+"', fromdate  = '"+froo+"', todate = '"+too+"', day = '"+days+"', commu = '"+comm+"', reco = '"+recc+"', vspl = '"+vsp+"', sl = '"+ics+"', lbw = '"+bw+"' , studl = '"+stl+"' , others = '"+ops+"' WHERE ide = '"+ides+"' ")
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
        

    def allsave():
        imgsave()
        proceed()


    



    dof = customtkinter.CTkLabel(l_frame, text="Date Filing: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=50)
    dofentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
    dofentry.set_date(results[2])
    dofentry.place(x=150,y=50)

    tol = customtkinter.CTkLabel(l_frame, text="Type of Leave: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=102)
    tyle = tk.StringVar()
    st = customtkinter.CTkOptionMenu(l_frame,height= 35, width = 400,fg_color='#b8b8b8',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = '#a19e9d',text_color = "black",variable = tyle, values=["Vacation Leave", "Mandatory/Forced Leave", "Sick Leave", "Maternity Leave", "Paternity Leave", "Special Previlege Leave", "Solo Parent Leave", "Study Leave", "10-Day VAWC Leave", "Rehabilitaion Leave", "Special Leave Benefits for Women", "Special Emergency","Adoption"])
    st.place(x=190, y= 100)
    st.set(results[3])

    nool = customtkinter.CTkLabel(l_frame, text="Number of Working days applied for", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=200)

    lfrom = customtkinter.CTkLabel(l_frame, text="From: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=252)
    lfromentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
    lfromentry.set_date(results[4])
    lfromentry.place(x=100, y= 250)

    lto = customtkinter.CTkLabel(l_frame, text="To: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=250, y=252)
    ltoentry = DateEntry(l_frame, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
    ltoentry.set_date(results[5])
    ltoentry.place(x=305, y= 250)

    total = Label(l_frame, text="Days", font=('Arial', 16, 'bold'),bg="white")
    total.place(x=480, y=252)

    comm = customtkinter.CTkLabel(l_frame, text="Commutation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=100)
    cmt = tk.StringVar()
    opcm1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Requested", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Requested",bg_color ="white",variable=cmt, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 150)
    opcm2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Not Requested",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Not Requested",bg_color ="white",variable=cmt, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 150)
    cmt.set(results[6])

    recom = customtkinter.CTkLabel(l_frame, text="Recommendation:", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=200)
    rec = tk.StringVar()
    opre1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Approve", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Approve",bg_color="transparent",variable=rec, cursor='hand2', font=('Courier', 16, 'bold'),text_color='#171414').place(x=700,y= 250)
    opre2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Decline",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value="Decline",bg_color="transparent",variable=rec, cursor='hand2',font=('Courier', 16, 'bold'),text_color='#171414').place(x=870,y= 250)
    rec.set(results[7])

    vspl = customtkinter.CTkLabel(l_frame, text="In case of Vacation/Special Privilege Leave:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=20,y=350)
    vspltb = customtkinter.CTkTextbox(l_frame,height= 50, width = 400 ,border_width=2,bg_color="transparent", fg_color="white", text_color="black",font=('Arial', 16),scrollbar_button_color="#616161",scrollbar_button_hover_color="#616161")
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
    stud.set(results[8])

    op = customtkinter.CTkLabel(l_frame, text="Other purpose:", font=('Arial', 18, 'bold'),text_color= "black",bg_color="transparent").place(x=700, y=450)
    oth = tk.StringVar()
    op1 = customtkinter.CTkRadioButton(l_frame,border_color="#5c5c5c", text="Monetization of Leave Credits", radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color="transparent",variable=oth, cursor='hand2', font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 480)
    op2 = customtkinter.CTkRadioButton(l_frame, border_color="#5c5c5c",text="Terminal Leave",radiobutton_height= 25, radiobutton_width= 25, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color="transparent",variable=oth, cursor='hand2',font=('Arial', 16, 'bold'),text_color='#171414').place(x=750,y= 510)
    oth.set(results[9])

    sol = customtkinter.CTkButton(l_frame,text="count",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= solve)
    sol.place(x=480, y=300)

    upl = customtkinter.CTkButton(l_frame,text="Upload",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= 'transparent', width=80, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= upl_mc)
    upl.place(x=480, y=490)

    vie = customtkinter.CTkButton(l_frame,text="",image=imgs,width=70,height=100, cursor='hand2',bg_color="transparent", fg_color="transparent", command=mc_view)
    vie.place(x=570, y=450)

    
    proc = customtkinter.CTkButton(l_frame,text="Proceed",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command= allsave)
    proc.place(x=900, y=625)

    can = PIL.Image.open("Assets\\cancel.png")
    checked2 = customtkinter.CTkImage(can,size=(30,30))
    cancel = customtkinter.CTkButton(l_frame, text="", image=checked2, bg_color= 'white',fg_color="white",hover_color= "#8a8987", width= 20,cursor='hand2',command=cancels)
    cancel.place(x=1135,y=15)



    root.bind("<Button-1>", start_drag)
    root.bind("<B1-Motion>", move_app)

    root.mainloop()

    


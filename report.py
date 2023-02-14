from tkinter import *
from db import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from tkinter import filedialog
import base64
from PIL import ImageTk, Image
import PIL.Image
import math
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import GOV_LEGAL





def report():
    f5 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8ad4c9",corner_radius=60)
    f5.place(x=380, y=200)

    

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


    def dclick(e):
        show()


    def deletef():
        for frame in f5.winfo_children():
            frame.destroy()

    def indicate(page):

        deletef()
        page()


   #===================personal

    p_sname = tk.StringVar()
    p_fname = tk.StringVar()
    p_mname = tk.StringVar()
    p_dob = tk.StringVar()
    p_pob = tk.StringVar()
    p_sex = tk.StringVar()
    p_civ = tk.StringVar()
    p_height = tk.IntVar()
    p_weight = tk.IntVar()
    p_bt = tk.StringVar()
    p_citi = tk.StringVar()
    p_ifdc = tk.StringVar()
    p_coun = tk.StringVar()
    p_email = tk.StringVar()
    p_pos = tk.StringVar()
    p_stat = tk.StringVar()
    p_dept = tk.StringVar()


    #===================numbers

    n_gsis = tk.StringVar()
    n_pag = tk.StringVar()
    n_phil = tk.StringVar()
    n_sss = tk.StringVar()
    n_tin = tk.StringVar()
    n_ae = tk.StringVar()
    n_tel = tk.StringVar()
    n_cel = tk.StringVar()

    #===================residential address


    r_ra1 = tk.StringVar()
    r_ra2 = tk.StringVar()
    r_ra3 = tk.StringVar()
    r_ra4 = tk.StringVar()
    r_ra5 = tk.StringVar()
    r_ra6 = tk.StringVar()
    r_ra7 = tk.StringVar()

    #===================permanent address

    p_pa1 = tk.StringVar()
    p_pa2 = tk.StringVar()
    p_pa3 = tk.StringVar()
    p_pa4 = tk.StringVar()
    p_pa5 = tk.StringVar()
    p_pa6 = tk.StringVar()
    p_pa7 = tk.StringVar()


    #===================Spouse

    s_sname = tk.StringVar()
    s_fname = tk.StringVar()
    s_mname = tk.StringVar()
    s_occup = tk.StringVar()
    s_ebn = tk.StringVar()
    s_ba = tk.StringVar()
    s_tele = tk.StringVar()

    #===================family

    f_fsn = tk.StringVar()
    f_ffn = tk.StringVar()
    f_fmn = tk.StringVar()
    f_mmn = tk.StringVar()
    f_msn = tk.StringVar()
    f_mfn = tk.StringVar()
    f_mn = tk.StringVar()

    #===================elementary


    e_school = tk.StringVar()
    e_bdc = tk. StringVar()
    e_fro = tk. StringVar()
    e_to = tk. StringVar()
    e_hig = tk. StringVar()
    e_yg = tk. StringVar()
    e_sa = tk. StringVar()

    #===================highschool

    h_school = tk.StringVar()
    h_bdc = tk. StringVar()
    h_fro = tk. StringVar()
    h_to = tk. StringVar()
    h_hig = tk. StringVar()
    h_yg = tk. StringVar()
    h_sa = tk. StringVar()

    #===================vocational


    v_school = tk.StringVar()
    v_bdc = tk. StringVar()
    v_fro = tk. StringVar()
    v_to = tk. StringVar()
    v_hig = tk. StringVar()
    v_yg = tk. StringVar()
    v_sa = tk. StringVar()

    #===================college

    c_school = tk.StringVar()
    c_bdc = tk. StringVar()
    c_fro = tk. StringVar()
    c_to = tk. StringVar()
    c_hig = tk. StringVar()
    c_yg = tk. StringVar()
    c_sa = tk. StringVar()

    #===================Graduate studies

    g_school = tk.StringVar()
    g_bdc = tk. StringVar()
    g_fro = tk. StringVar()
    g_to = tk. StringVar()
    g_hig = tk. StringVar()
    g_yg = tk. StringVar()
    g_sa = tk. StringVar()

    ids = tk.StringVar()

    def id(word,num):
        if num == 1:
            ids.set(word)

    def per(word,num):
        if num == 1:
            p_sname.set(word)
        if num == 2:
            p_fname.set(word)
        if num == 3:
            p_mname.set(word)
        if num == 4:
            p_dob.set(word)
        if num == 5:
            p_pob.set(word)
        if num == 6:
            p_sex.set(word)
        if num == 7:
            p_civ.set(word)
        if num == 8:
            p_height.set(word)
        if num == 9:
            p_weight.set(word)
        if num == 10:
            p_bt.set(word)
        if num == 11:
            p_citi.set(word)
        if num == 12:
            p_ifdc.set(word)
        if num == 13:
            p_coun.set(word)
        if num == 14:
            p_email.set(word)
        if num == 15:
            p_pos.set(word)
        if num == 16:
            p_stat.set(word)
        if num == 17:
            p_dept.set(word)


    def numbs(word,num):
        if num == 1:
            n_gsis.set(word)
        if num == 2:
            n_pag.set(word)
        if num == 3:
            n_phil.set(word)
        if num == 4:
            n_sss.set(word)
        if num == 5:
            n_tin.set(word)
        if num == 6:
            n_ae.set(word)
        if num == 7:
            n_tel.set(word)
        if num == 8:
            n_cel.set(word)



    def resad(word,num):
        if num == 1:
            r_ra1.set(word)
        if num == 2:
            r_ra2.set(word)
        if num == 3:
            r_ra3.set(word)
        if num == 4:
            r_ra4.set(word)
        if num == 5:
            r_ra5.set(word)
        if num == 6:
            r_ra6.set(word)
        if num == 7:
            r_ra7.set(word)

    def perad(word,num):
        if num == 1:
            p_pa1.set(word)
        if num == 2:
            p_pa2.set(word)
        if num == 3:
            p_pa3.set(word)
        if num == 4:
            p_pa4.set(word)
        if num == 5:
            p_pa5.set(word)
        if num == 6:
            p_pa6.set(word)
        if num == 7:
            p_pa7.set(word)

    def spous(word,num):
        if num == 1:
            s_sname.set(word)
        if num == 2:
            s_fname.set(word)
        if num == 3:
            s_mname.set(word)
        if num == 4:
            s_occup.set(word)
        if num == 5:
            s_ebn.set(word)
        if num == 6:
            s_ba.set(word)
        if num == 7:
            s_tele.set(word)

    def fam(word,num):
        if num == 1:
            f_fsn.set(word)
        if num == 2:
            f_ffn.set(word)
        if num == 3:
            f_fmn.set(word)
        if num == 4:
            f_mmn.set(word)
        if num == 5:
            f_msn.set(word)
        if num == 6:
            f_mfn.set(word)
        if num == 7:
            f_mn.set(word)

    def elem(word,num):
        if num == 1:
            e_school.set(word)
        if num == 2:
            e_bdc.set(word)
        if num == 3:
            e_fro.set(word)
        if num == 4:
            e_to.set(word)
        if num == 5:
            e_hig.set(word)
        if num == 6:
            e_yg.set(word)
        if num == 7:
            e_sa.set(word)

    def high(word,num):
        if num == 1:
            h_school.set(word)
        if num == 2:
            h_bdc.set(word)
        if num == 3:
            h_fro.set(word)
        if num == 4:
            h_to.set(word)
        if num == 5:
            h_hig.set(word)
        if num == 6:
            h_yg.set(word)
        if num == 7:
            h_sa.set(word)

    def voca(word,num):
        if num == 1:
            v_school.set(word)
        if num == 2:
            v_bdc.set(word)
        if num == 3:
            v_fro.set(word)
        if num == 4:
            v_to.set(word)
        if num == 5:
            v_hig.set(word)
        if num == 6:
            v_yg.set(word)
        if num == 7:
            v_sa.set(word)

    def col(word,num):
        if num == 1:
            c_school.set(word)
        if num == 2:
            c_bdc.set(word)
        if num == 3:
            c_fro.set(word)
        if num == 4:
            c_to.set(word)
        if num == 5:
            c_hig.set(word)
        if num == 6:
            c_yg.set(word)
        if num == 7:
            c_sa.set(word)

    def grad(word,num):
        if num == 1:
            g_school.set(word)
        if num == 2:
            g_bdc.set(word)
        if num == 3:
            g_fro.set(word)
        if num == 4:
            g_to.set(word)
        if num == 5:
            g_hig.set(word)
        if num == 6:
            g_yg.set(word)
        if num == 7:
            g_sa.set(word)
   
    def show():

        selected_item = my_tree.selection()[0]
        name = str(my_tree.item(selected_item)['values'][0])

        if name != name:
            messagebox.showinfo("Error", "Select a data or input your ID no.")
            return


        else:
        
            conn = connection()
            cursor = conn.cursor()
            cursor2 = conn.cursor()
            cursor3 = conn.cursor()
            cursor4 = conn.cursor()
            cursor5 = conn.cursor()
            cursor6 = conn.cursor()
            cursor7 = conn.cursor()
            cursor8 = conn.cursor()
            cursor9 = conn.cursor()
            cursor10 = conn.cursor()
            cursor11 = conn.cursor()
            cursor.execute("SELECT * FROM personal WHERE id=%s",(name))
            cursor2.execute("SELECT * FROM numbers WHERE id=%s",(name))
            cursor3.execute("SELECT * FROM residential WHERE id=%s",(name))
            cursor4.execute("SELECT * FROM permanent WHERE id=%s",(name))
            cursor5.execute("SELECT * FROM spouse WHERE id=%s",(name))
            cursor6.execute("SELECT * FROM family WHERE id=%s",(name))
            cursor7.execute("SELECT * FROM elementary WHERE id=%s",(name))
            cursor8.execute("SELECT * FROM highschool WHERE id=%s",(name))
            cursor9.execute("SELECT * FROM vocational WHERE id=%s",(name))
            cursor10.execute("SELECT * FROM college WHERE id=%s",(name))
            cursor11.execute("SELECT * FROM graduate WHERE id=%s",(name))
            result = cursor.fetchone()
            result2 = cursor2.fetchone()
            result3 = cursor3.fetchone()
            result4 = cursor4.fetchone()
            result5 = cursor5.fetchone()
            result6 = cursor6.fetchone()
            result7 = cursor7.fetchone()
            result8 = cursor8.fetchone()
            result9 = cursor9.fetchone()
            result10 = cursor10.fetchone()
            result11 = cursor11.fetchone()

            dtr=datetime.strftime(result[4],'%b/%d/%Y')
        
            id(result[0],1)
            per(result[1],1)
            per(result[2],2)
            per(result[3],3)
            per(dtr,4)
            per(result[5],5)
            per(result[6],6)
            per(result[7],7)
            per(result[8],8)
            per(result[9],9)
            per(result[10],10)
            per(result[11],11)
            per(result[12],12)
            per(result[13],13)
            per(result[14],14)
            per(result[15],15)
            per(result[16],16)
            per(result[17],17)

            numbs(result2[1],1)
            numbs(result2[2],2)
            numbs(result2[3],3)
            numbs(result2[4],4)
            numbs(result2[5],5)
            numbs(result2[6],6)
            numbs(result2[7],7)
            numbs(result2[8],8)

            resad(result3[1],1)
            resad(result3[2],2)
            resad(result3[3],3)
            resad(result3[4],4)
            resad(result3[5],5)
            resad(result3[6],6)
            resad(result3[7],7)

            perad(result4[1],1)
            perad(result4[2],2)
            perad(result4[3],3)
            perad(result4[4],4)
            perad(result4[5],5)
            perad(result4[6],6)
            perad(result4[7],7)

            spous(result5[1],1)
            spous(result5[2],2)
            spous(result5[3],3)
            spous(result5[4],4)
            spous(result5[5],5)
            spous(result5[6],6)
            spous(result5[7],7)

            fam(result6[1],1)
            fam(result6[2],2)
            fam(result6[3],3)
            fam(result6[4],4)
            fam(result6[5],5)
            fam(result6[6],6)
            fam(result6[7],7)

            elem(result7[1],1)
            elem(result7[2],2)
            elem(result7[3],3)
            elem(result7[4],4)
            elem(result7[5],5)
            elem(result7[6],6)
            elem(result7[7],7)

            high(result8[1],1)
            high(result8[2],2)
            high(result8[3],3)
            high(result8[4],4)
            high(result8[5],5)
            high(result8[6],6)
            high(result8[7],7)

            voca(result9[1],1)
            voca(result9[2],2)
            voca(result9[3],3)
            voca(result9[4],4)
            voca(result9[5],5)
            voca(result9[6],6)
            voca(result9[7],7)

            col(result10[1],1)
            col(result10[2],2)
            col(result10[3],3)
            col(result10[4],4)
            col(result10[5],5)
            col(result10[6],6)
            col(result10[7],7)

            grad(result11[1],1)
            grad(result11[2],2)
            grad(result11[3],3)
            grad(result11[4],4)
            grad(result11[5],5)
            grad(result11[6],6)
            grad(result11[7],7)

            indicate(show_e)

    def show_e():

        f2_2 = customtkinter.CTkFrame(f5, width=1500, height=820, fg_color ="transparent")
        f2_2.place(x=0, y=0)
        f2_2.pack_propagate(0)
        cv2 = Canvas(f2_2,background='#ffffff',highlightthickness=0)
        cv2.pack(side =LEFT,fill=BOTH, expand=1)
        sb2= customtkinter.CTkScrollbar(f2_2, orientation= VERTICAL, border_spacing = 3,fg_color = '#aee0e8', command=cv2.yview)
        sb2.pack(side=RIGHT, fill=Y)
        cv2.configure(yscrollcommand=sb2.set)
        cv2.bind('<Configure>', lambda e:cv2.configure(scrollregion = cv2.bbox('all')))

        sf2 = customtkinter.CTkFrame(cv2, width=1500, height=2000 ,fg_color ="transparent")
        cv2.create_window((0,0), window=sf2, anchor="nw")

        sf2.bind("<MouseWheel>", lambda event: cv2.yview_scroll(-int(event.delta/100), "units"))

        photo = PIL.Image.open("Assets\\Picture1.png")
        nphoto = customtkinter.CTkImage(photo,size=(1485,1860))
        j = customtkinter.CTkLabel(sf2,text="", image=nphoto)
        j.place(x=0, y=0)
        j.bind("<MouseWheel>", lambda event: cv2.yview_scroll(-int(event.delta/100), "units"))


         

        back2 = customtkinter.CTkButton(sf2,text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#ffffff', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(report))
        back2.place(x=1000, y=1900)


   #-------------------------------------------------------------------------------------------------------------------------------------#
   #-------------------------------------------------------PERSONAL INFO-----------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#

        snshow = Label(sf2, text="", font=('Courier', 16, 'bold'),bg="#ffffff", textvariable=p_sname).place(x=300, y=220)

        fnshow = Label(sf2, text="", font=('Courier', 16, 'bold'),bg="#ffffff", textvariable=p_fname).place(x=300, y=260)

        mnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=p_mname).place(x=300,y=295)

        dobshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=p_dob).place(x=320,y=350)

        pobshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=p_pob).place(x=320,y=405)

        chk = PIL.Image.open("Assets\\chke.png")
        checked = customtkinter.CTkImage(chk,size=(25,25))
        sexshow = customtkinter.CTkLabel(sf2, text= "", image=checked)

        if p_sex.get() == "male":
            sexshow.place(x=298,y=445)
        elif  p_sex.get() == "female":
            sexshow.place(x=432,y=445)
        else:
            pass

        chk2 = PIL.Image.open("Assets\\chke.png")
        checked2 = customtkinter.CTkImage(chk2,size=(25,23))
        civshow = customtkinter.CTkLabel(sf2, text= "", image=checked2)

        if p_civ.get() == "Single":
            civshow.place(x=298,y=485)
        elif  p_civ.get() == "Married":
            civshow.place(x=432,y=485)
        elif  p_civ.get() == "Widowed":
            civshow.place(x=298,y=510)
        elif  p_civ.get() == "Seperated":
            civshow.place(x=432,y=510)
        elif  p_civ.get() == "Other/s":
            civshow.place(x=298,y=535)
        else:
            pass

        hshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=p_height).place(x=320,y=580)
        wshow = Label(sf2, text = "", font=('Courier',13,'bold'),bg="#ffffff",textvariable=p_weight).place(x=320,y=614)
        btshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=p_bt).place(x=320,y=660)
        gsshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=n_gsis).place(x=320,y=700)
        pagshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=n_pag).place(x=320,y=745)
        phshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=n_phil).place(x=320,y=784)
        ssshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=n_sss).place(x=320,y=820)
        tinshow = Label(sf2, text = "", font=('Courier',13,'bold'),bg="#ffffff",textvariable=n_tin).place(x=320,y=856)
        aeshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=n_ae).place(x=320,y=890)

        chk3 = PIL.Image.open("Assets\\chke.png")
        checked3 = customtkinter.CTkImage(chk3,size=(25,25))
        citzshow = customtkinter.CTkLabel(sf2, text= "", image=checked3)

        if p_citi.get() == "Filipino":
            citzshow.place(x=935,y=345)
        elif  p_citi.get() == "Dual Citizenship":
            citzshow.place(x=1126,y=345)
        else:
            pass

        chk4 = PIL.Image.open("Assets\\chke.png")
        checked4 = customtkinter.CTkImage(chk4,size=(25,25))
        optshow = customtkinter.CTkLabel(sf2, text= "", image=checked4)
        
        if p_ifdc.get() == "By Birth":
            optshow.place(x=1160,y=370)
        elif  p_ifdc.get() == "By Naturalization":
            optshow.place(x=1262,y=370)
        else:
            pass

        counshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=p_coun).place(x=935,y=445)

        res1show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=r_ra1).place(x=910,y=486)
        res2show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=r_ra2).place(x=1262,y=486)
        res3show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=r_ra3).place(x=910,y=529)
        res4show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=r_ra4).place(x=1262,y=529)
        res5show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=r_ra5).place(x=910,y=572)
        res6show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=r_ra6).place(x=1262,y=572)
        res7show = Label(sf2, text = "", font=('Courier',13,'bold'),bg="#ffffff",justify='center',textvariable=r_ra7).place(x=910,y=615)

        per1show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=p_pa1).place(x=910,y=645)
        per2show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=p_pa2).place(x=1262,y=645)
        per3show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=p_pa3).place(x=910,y=693)
        per4show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=p_pa4).place(x=1262,y=693)
        per5show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=p_pa5).place(x=910,y=738)
        per6show = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",justify='center',textvariable=p_pa6).place(x=1262,y=738)
        per7show = Label(sf2, text = "", font=('Courier',13,'bold'),bg="#ffffff",justify='center',textvariable=p_pa7).place(x=910,y=784)

        telshow = Label(sf2, text = "", font=('Courier',14,'bold'),bg="#ffffff",justify='center',textvariable=n_tel).place(x=910,y=820)
        celshow = Label(sf2, text = "", font=('Courier',14,'bold'),bg="#ffffff",justify='center',textvariable=n_cel).place(x=910,y=856)
        emailshow = Label(sf2, text = "", font=('Courier',14,'bold'),bg="#ffffff",justify='center',textvariable=p_email).place(x=910,y=890)

        spsnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_sname).place(x=290,y=958)
        spfnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_fname).place(x=290,y=995)
        spmnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_mname).place(x=290,y=1032)
        spocshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_occup).place(x=290,y=1069)
        spebnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_ebn).place(x=290,y=1106)
        spbashow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_ba).place(x=290,y=1143)
        sptelshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=s_tele).place(x=290,y=1180)
        fsnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_fsn).place(x=290,y=1217)
        ffnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_ffn).place(x=290,y=1254)
        fmnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_fmn).place(x=290,y=1291)
        mmnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_mmn).place(x=290,y=1328)
        msnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_msn).place(x=290,y=1365)
        mfnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_mfn).place(x=290,y=1402)
        mnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=f_mn).place(x=290,y=1439)

        enosshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_school).place(x=282,y=1585)
        ebdcshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_bdc).place(x=573,y=1585)
        efromshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_fro).place(x=960,y=1585)
        etoshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_to).place(x=1070,y=1585)
        ehishow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_hig).place(x=1175,y=1585)
        eygshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_yg).place(x=1280,y=1585)
        esashow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=e_sa).place(x=1400,y=1585)

        hnosshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_school).place(x=282,y=1627)
        hbdcshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_bdc).place(x=573,y=1627)
        hfromshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_fro).place(x=960,y=1627)
        htoshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_to).place(x=1070,y=1627)
        hhishow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_hig).place(x=1175,y=1627)
        hygshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_yg).place(x=1280,y=1627)
        hsashow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=h_sa).place(x=1400,y=1627)

        vnosshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_school).place(x=282,y=1669)
        vbdcshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_bdc).place(x=573,y=1669)
        vfromshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_fro).place(x=960,y=1669)
        vtoshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_to).place(x=1070,y=1669)
        vhishow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_hig).place(x=1175,y=1669)
        vygshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_yg).place(x=1280,y=1669)
        vsashow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=v_sa).place(x=1400,y=1669)

        cnosshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_school).place(x=282,y=1705)
        cbdcshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_bdc).place(x=573,y=1705)
        cfromshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_fro).place(x=960,y=1705)
        ctoshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_to).place(x=1070,y=1705)
        chishow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_hig).place(x=1175,y=1705)
        cygshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_yg).place(x=1280,y=1705)
        csashow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=c_sa).place(x=1400,y=1705)

        gnosshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_school).place(x=282,y=1743)
        gbdcshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_bdc).place(x=573,y=1743)
        gfromshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_fro).place(x=960,y=1743)
        gtoshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_to).place(x=1070,y=1743)
        ghishow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_hig).place(x=1175,y=1743)
        gygshow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_yg).place(x=1280,y=1743)
        gsashow = Label(sf2, text = "", font=('Courier',12,'bold'),bg="#ffffff",textvariable=g_sa).place(x=1400,y=1743)

        gsashow = customtkinter.CTkLabel(sf2, text = "NOT APPLICABLE HERE\nINSTEAD WRITE IT", font=('Arial',32,'bold'),bg_color="transparent",text_color="#7a7979").place(x=950,y=1180)
    



    def read2():
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, firstname, surname, position, department FROM personal WHERE surname like %s OR firstname like %s OR id like %s",(findEntry.get(),findEntry.get(),findEntry.get()))
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




    search = customtkinter.CTkButton(f5,text="Search",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=100, height=40, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=searching)
    search.place(x=350, y=27)

    refr = PIL.Image.open("Assets\\refresh.png")
    ref = customtkinter.CTkImage(refr,size=(30,30))

    search2 = customtkinter.CTkButton(f5,text="",image = ref, bg_color= '#8ad4c9',fg_color="#8ad4c9",hover_color= "#8ad4c9", width= 20,cursor='hand2',command=refresh)
    search2.place(x=450, y=27)

        
    add3 = customtkinter.CTkButton(f5,text="Check",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8ad4c9', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=show)
    add3.place(x=1200, y=700)

   
        
    find = Label(f5, text="FIND : ", font=('Arial', 18, 'bold'),bg="#8ad4c9").place(x=50, y=30)
    findEntry = customtkinter.CTkEntry(f5,height = 37, width=200, fg_color='white',border_width = 0 ,font=('Arial', 20),text_color='black')
    findEntry.place(x=130, y=28)


    my_tree =ttk.Treeview(f5, show="headings", height=11)
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
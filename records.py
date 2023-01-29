from tkinter import *
from db import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from tkcalendar import DateEntry
from datetime import date
import tkinter as tk
from tkinter import ttk
import customtkinter




def record():
    f2 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8aafd4",corner_radius=50)
    f2.place(x=380, y=200)
    f2.pack_propagate(False)


    def deletef():
        for frame in f2.winfo_children():
            frame.destroy()

    def indicate (page):
        deletef()
        page()


    def validate(u_input): 
        return u_input.isdigit()
    my_valid = f2.register(validate) 


    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

        my_tree.tag_configure('orow', font=('Arial', 12))
        

    fi = tk.StringVar()
    
    c = tk.StringVar()
    c1 = tk.StringVar()
    c2 = tk.StringVar()
    c3 = tk.StringVar()
    c4 = tk.StringVar()
    c5 = tk.StringVar()
    c6 = tk.StringVar()
    c7 = tk.StringVar()
    c8 = tk.StringVar()
    c9 = tk.StringVar()
    c10 = tk.StringVar()
    c11 = tk.StringVar()
    c12 = tk.StringVar()
    c13 = tk.StringVar()
    c14 = tk.StringVar()
    c15 = tk.StringVar()
    c16 = tk.StringVar()

    tc1 = tk.StringVar()
    tc2 = tk.StringVar()
    tc3 = tk.StringVar()
    tc4 = tk.StringVar()
    tc5 = tk.StringVar()
    tc6 = tk.StringVar()
    tc7 = tk.StringVar()
    tc8 = tk.StringVar()
    tc9 = tk.StringVar()
    tc10 = tk.StringVar()
    tc11 = tk.StringVar()
    tc12 = tk.StringVar()
    tc13 = tk.StringVar()
    tc14 = tk.StringVar()
    tc15 = tk.StringVar()


    def ms(word,num):
        if num == 1:
            fi.set(word)

    def setc(word,num):
        if num == 1:
            tc1.set(word)
        if num == 2:
            tc2.set(word)
        if num == 3:
            tc3.set(word)
        if num == 4:
            tc6.set(word)
        if num == 5:
            tc8.set(word)
        if num == 6:
            tc9.set(word)
        if num == 7:
            tc11.set(word)
        if num == 8:
            tc12.set(word)
        if num == 9:
            tc13.set(word)
        if num == 10:
            tc14.set(word)
        if num == 11:
            tc15.set(word)
            
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    result = cursor.fetchone()
    
    def show():
        find = str(findEntry.get())

        if find == "" or find == " ":
            messagebox.showinfo("Error", "Select a data or input your ID no.")
            return
        else:
        
            conn = connection()
            cursor = conn.cursor()
            cursor2 = conn.cursor()
            cursor.execute("SELECT * FROM person WHERE id=%s",(findEntry.get()))
            cursor2.execute("SELECT * FROM educ WHERE id=%s ", (findEntry.get()))
            result = cursor.fetchone()
            result2 = cursor2.fetchone()
            drow = result[0]
            drow1 = result[1]
            drow2 = result[2]
            drow3 = result[3]
            drow4 = result[4]
            drow5 = result[5]
            drow6 = result[6]
            drow7 = result[7]
            drow8 = result[8]
            drow9 = result[9]
            drow10 = result[10]
            drow11 = result[11]
            drow12 = result[12]
            drow13 = result[13]
            drow14 = result[14]
            drow15 = result[15]
            erow1 = result2[1]
        
            if result:
                indicate(show_e)
                c.set(drow)
                c1.set(drow1)
                c2.set(drow2)
                c3.set(drow3)
                c4.set(drow4)
                c5.set(drow5)
                c6.set(drow6)
                c7.set(drow7)
                c8.set(drow8)
                c9.set(drow9)
                c10.set(drow10)
                c11.set(drow11)
                c12.set(drow12)
                c13.set(drow13)
                c14.set(drow14)
                c15.set(drow15)
                c16.set(erow1)
            else:
                pass


    def mouse_select():
        try:
            selected_item = my_tree.selection()[0]
            name = str(my_tree.item(selected_item)['values'][0])
    
            ms(name,1)
        
        except:
            messagebox.showinfo("Error", "Please select a data row")

    

  

    sty = ttk.Style()
    sty.theme_use('clam')
    sty.configure("Treeview", rowheight="50",fieldbackground ='#dbd5d5',background = '#dbd5d5', borderwidth = 0,relief = 'flat')
    sty.configure("Treeview.Heading", font=(None, 20), background="#8f8d8d", borderwidth = 0, relief = "flat")
    sty.map("Treeview.Heading", background = [('active', "#8f8d8d")])
    sty.map('Treeview', background=[('selected', 'green')])


    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------entering data-----------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#

    def add_e():

        f2_1 = customtkinter.CTkFrame(f2, width=1500, height=820)
        f2_1.place(x=0, y=0)
        f2_1.pack_propagate(0)
        cv = Canvas(f2_1,background='#dbb2b2',highlightthickness=0)
        cv.pack(side =LEFT,fill=BOTH, expand=1)
        sb = customtkinter.CTkScrollbar(f2_1, orientation= VERTICAL, border_spacing = 3,fg_color = 'white', command=cv.yview)
        sb.pack(side=RIGHT, fill=Y)
        cv.configure(yscrollcommand=sb.set)
        cv.bind('<Configure>', lambda e:cv.configure(scrollregion = cv.bbox('all')))

        sf = customtkinter.CTkFrame(cv, width=1500, height=2000 ,fg_color ="#8ed1ba",corner_radius=50)
        cv.create_window((0,0), window=sf, anchor="nw")

        def mousewheel(event):
            cv.yview_scroll(-1*(event.delta/500), "units")

        cv.bind("<MouseWheel>",mousewheel)


        def add():
            sname = str(sn.get())
            fname = str(fnEntry.get())
            mname = str(mnEntry.get())
            ct = str(ctEntry.get())
            hei = str(htEntry.get())
            wei = str(wtEntry.get())
            bt = str(btt.get())
            tlno = str(tEntry.get())
            clno = str(cEntry.get())
            email = str(eEntry.get())
            dobb =  str(dobentry.get_date())
            sex = str(rb.get())
            cs = str(cb.get())
            pos = str(poEntry.get())
            dept = str(deEntry.get())
            elem = str(elEntry.get())

            if (sname == "" or sname == " ") or (fname == "" or  fname == " ") or (mname == "" or mname == " ") or (ct == "" or ct == " ") or (hei == "" or hei == " ") or (wei == "" or wei == " ") or (bt == "" or bt == " ") or (tlno == "" or tlno == " ") or (clno == "" or clno == " ") or (email == "" or email == " ") or (dobb == "" or dobb == " ") or (sex == "" or sex == " ") or (cs == "" or cs == " ") or (pos == "" or pos == " ") or (dept == "" or dept == " ") or (elem == "" or elem == " "):
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
            else:
                try:
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO person VALUES ('""','"+fname+"','"+mname+"','"+sname+"','"+sex+"','"+dobb+"','"+ct+"','"+cs+"','"+hei+"','"+wei+"','"+bt+"','"+tlno+"','"+clno+"','"+email+"','"+pos+"','"+dept+"') ")
                    cursor.execute(
                        "INSERT INTO educ VALUES ('""','"+elem+"') ")
                    conn.commit()
                    conn.close()
                    msg = messagebox.askquestion('',"Do you want to add this person?")
                    if msg == 'yes':
                        sn.delete(0,'end')
                        fnEntry.delete(0,'end')
                        mnEntry.delete(0,'end')
                        ctEntry.delete(0,'end')
                        htEntry.delete(0,'end')
                        wtEntry.delete(0,'end')
                        btt.set("")
                        tEntry.delete(0,'end')
                        cEntry.delete(0,'end')
                        eEntry.delete(0,'end')
                        dobentry.set_date(dt)
                        rb.set(None)
                        cb.set("")
                        poEntry.delete(0,'end')
                        eEntry.delete(0,'end')
                        deEntry.delete(0,'end')
                        elEntry.delete(0,'end')
                        indicate(record)
                    else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                except:
                    
                    messagebox.showinfo("Error", "Inventory already exist")
                    return
            
           

                


            refreshTable()


        back = customtkinter.CTkButton(sf, text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#8ed1ba', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(record))
        back.place(x=1000, y=1800)

        addto = customtkinter.CTkButton(sf,text="Attach",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8ed1ba', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=add)
        addto.place(x=1200, y=1800)

    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------PERSONAL INFO-----------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#

        titleabel = Label(sf, text="PERSONAL DATA SHEET", font=('Arial', 22, 'bold'),bg="#8ed1ba")
        titleabel.place(x=690, y=10, anchor= N)

        sublabel = Label(sf, text="PERSONAL INFORMATION ", font=('Arial', 18, 'bold'),bg="#8ed1ba")
        sublabel.place(x=30, y=50)

        snlabel = Label(sf, text="1.SURNAME :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=100)
        sn = customtkinter.CTkEntry(sf, height= 35,width=450, fg_color='white',border_width = 2, corner_radius= 10,placeholder_text = "Name extension (Jr.,Sr.)",font=('Arial', 22),placeholder_text_color= "gray",text_color='black')
        sn.place(x=280, y=100)

        fnlabel = Label(sf, text="  FIRSTNAME :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=150)
        fnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0, font=('Arial', 22),text_color='black')
        fnEntry.place(x=280, y=150)

        mnlabel = Label(sf, text="  MIDDLENAME :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=200)
        mnEntry = customtkinter.CTkEntry(sf,  height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        mnEntry.place(x=280, y=200)

        doblabel = Label(sf, text="2.DATE OF BIRTH :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=252)
        dobentry = DateEntry(sf, height= 35, width=15, font = ('arial', 22), year=2019, month=6, day=22,background='gray', foreground='white', borderwidth=0, weekendbackground ="red",bd = 0)
        dt = date(2023,1,1)
        dobentry.set_date(dt)
        dobentry.place(x=280, y= 250)

        poblabel = Label(sf, text="3.PLACE OF BIRTH :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=302)
        pobEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        pobEntry.place(x=280, y=300)

        sexlabel = Label(sf, text="4.SEX : ", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=350)
        rb = tk.StringVar()
        stat1 = customtkinter.CTkRadioButton(sf, text="Male", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='male',bg_color ="#8ed1ba",variable=rb, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black').place(x=280,y= 350)
        stat2 = customtkinter.CTkRadioButton(sf, text="Female",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='female',bg_color ="#8ed1ba",variable=rb, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black').place(x=380,y= 350)
        rb.set(None)

        statuslabel = Label(sf, text="5.CIVIL STATUS :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=400)
        civ = tk.StringVar()
        st = customtkinter.CTkOptionMenu(sf,height= 35, width = 300,fg_color='white',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = 'white',button_hover_color = 'gray',text_color = "black",variable = civ, values=["Single", "Married", "Widowed", "Seperated", "Other/s"])
        st.place(x=280, y= 400)
        st.set("")

        hlabel = Label(sf, text="6.HEIGHT (cm) :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=450)
        htEntry = customtkinter.CTkEntry(sf,height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        htEntry.place(x=280, y=450)

        wlabel = Label(sf, text="7.WEIGHT (kg) :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=500)
        wtEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        wtEntry.place(x=280, y=500)

        btlabel = Label(sf, text="8.BLOOD TYPE :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=550)
        blo = tk.StringVar()
        bt = customtkinter.CTkOptionMenu(sf,height= 35, width = 300,fg_color='white',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color ='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = 'white',button_hover_color = 'gray',text_color = "black", variable = blo, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        bt.place(x=280, y= 550)
        bt.set("")

        gslabel = Label(sf, text="9.GSIS ID NO. :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=600)
        gsEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        gsEntry.place(x=280, y=600)

        paglabel = Label(sf, text="10.PAG-IBIG ID NO. :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=650)
        pagEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        pagEntry.place(x=280, y=650)

        phlabel = Label(sf, text="11.PHILHEALTH NO. :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=700)
        phEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        phEntry.place(x=280, y=700)

        sslabel = Label(sf, text="12.SSS NO. :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=750)
        ssEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        ssEntry.place(x=280, y=750)

        tilabel = Label(sf, text="13.TIN NO. :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=800)
        tiEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        tiEntry.place(x=280, y=800)

        aelabel = Label(sf, text="14.AGENCY EMPLOYEE NO.:", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=850)
        aeEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        aeEntry.place(x=280, y=850)

        tlabel = Label(sf, text="TEL NO. : ", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=900)
        tEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        tEntry.place(x=280, y=900)

        clabel = Label(sf, text="CEL NO. : ", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=20, y=950)
        cEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
        cEntry.place(x=280, y=950)



        def fr():
            optlabel.place_forget()
            ct5.place_forget()
            ct6.place_forget()
            coulabel.place_forget()
            couEntry.place_forget()

        def gt():
            optlabel.place_configure(x=900, y=300)
            ct5.place_configure(x=1050,y= 350)
            ct6.place_configure(x=1190,y= 350)
            coulabel.place_configure(x=850, y=397)
            couEntry.place_configure(x=1025, y=395)
           

        ctlabel = Label(sf, text="15.CITIZENSHIP :", font=('Courier', 18, 'bold'),bg="#8ed1ba").place(x=750, y=250)
        rb2 = tk.StringVar()
        ct3 = customtkinter.CTkRadioButton(sf, text="Filipino", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color ="#8ed1ba",variable=rb2, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black',command=fr).place(x=990,y= 250)
        ct4 = customtkinter.CTkRadioButton(sf, text="Dual Citizenship",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color ="#8ed1ba",variable=rb2, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black',command=gt).place(x=1130,y= 250)
        rb2.set(None)

        optlabel = Label(sf, text="if Dual Citizenship:", font=('Courier', 15, 'bold'),bg="#8ed1ba")
        optlabel.place(x=900, y=300)
        opt2 = tk.StringVar()
        ct5 = customtkinter.CTkRadioButton(sf, text="By Birth", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='By Birth',bg_color ="#8ed1ba",variable=opt2, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black')
        ct5.place(x=1050,y= 350)
        ct6 = customtkinter.CTkRadioButton(sf, text="By Naturalization",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='By Naturalization',bg_color ="#8ed1ba",variable=opt2, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black')
        ct6.place(x=1190,y= 350)
        opt2.set(None)

        coulabel = Label(sf, text="your Country :", font=('Courier', 14, 'bold'),bg="#8ed1ba")
        coulabel.place(x=850, y=397)
        couEntry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        couEntry.place(x=1025, y=395)


        ralabel = Label(sf, text="16.RESIDENTIAL ADDRESS :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=750, y=450)
        ra1label = Label(sf, text="HouseBlock/Lot No.", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=930, y=510)
        raEntry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        raEntry.place(x=900, y=480)

        ra2label = Label(sf, text="Street", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=1270, y=510)
        ra2Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra2Entry.place(x=1180, y=480)

        ra3label = Label(sf, text="Subdivision/Village", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=925, y=570)
        ra3Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra3Entry.place(x=900, y=540)

        ra4label = Label(sf, text="Barangay", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=1260, y=570)
        ra4Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra4Entry.place(x=1180, y=540)

        ra5label = Label(sf, text="City/Municipality", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=930, y=630)
        ra5Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra5Entry.place(x=900, y=600)

        ra6label = Label(sf, text="Province", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=1260, y=630)
        ra6Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra6Entry.place(x=1180, y=600)

        ra7label = Label(sf, text="ZIP CODE :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=785, y=665)
        ra7Entry = customtkinter.CTkEntry(sf,height= 35, width=125, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra7Entry.place(x=900, y=660)

        palabel = Label(sf, text="17.PERMANENT ADDRESS :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=750, y=700)
        pa1label = Label(sf, text="HouseBlock/Lot No.", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=930, y=760)
        paEntry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        paEntry.place(x=900, y=730)

        pa2label = Label(sf, text="Street", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=1270, y=760)
        pa2Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        pa2Entry.place(x=1180, y=730)

        pa3label = Label(sf, text="Subdivision/Village", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=925, y=820)
        pa3Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        pa3Entry.place(x=900, y=790)

        pa4label = Label(sf, text="Barangay", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=1260, y=820)
        pa4Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        pa4Entry.place(x=1180, y=790)

        pa5label = Label(sf, text="City/Municipality", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=930, y=880)
        pa5Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        pa5Entry.place(x=900, y=850)

        pa6label = Label(sf, text="Province", font=('Courier', 12, 'bold'),bg="#8ed1ba").place(x=1260, y=880)
        pa6Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        pa6Entry.place(x=1180, y=850)

        pa7label = Label(sf, text="ZIP CODE :", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=785, y=915)
        ra7Entry = customtkinter.CTkEntry(sf,height= 35, width=125, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ra7Entry.place(x=900, y=910)

        elabel = Label(sf, text="18.EMAIL ADDRESS: ", font=('Courier', 14, 'bold'),bg="#8ed1ba").place(x=753, y=950)
        eEntry = customtkinter.CTkEntry(sf,height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        eEntry.place(x=950, y=950)


    #-------------------------------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------------------FAMILY BG------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#


        fblabel = Label(sf, text="FAMILY BACKGROUND", font=('Courier', 18, 'bold'),bg="#8ed1ba").place(x=30, y=1000)

        spolabel = Label(sf, text="19. SPOUSE'S SURNAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        spoEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        spoEntry.place(x=230, y=1050)

        fspolabel = Label(sf, text="FIRST NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        fspoEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        fspoEntry.place(x=230, y=1100)

        mspolabel = Label(sf, text="MIIDDLE NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        mspoEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        mspoEntry.place(x=230, y=1150)

        oclabel = Label(sf, text="OCCUPATION : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        ocEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ocEntry.place(x=230, y=1200)

        ebmlabel = Label(sf, text="EMPLOYEE/\nBUSINESS NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        ebmEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ebmEntry.place(x=230, y=1250)

        balabel = Label(sf, text="BUSINESS ADDRESS: ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        baEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        baEntry.place(x=230, y=1300)

        telelabel = Label(sf, text="TELEPHONE NO. : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        teleEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        teleEntry.place(x=230, y=1350)

        fsnlabel = Label(sf, text="20. FATHER'S SURNAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        fsnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        fsnEntry.place(x=950, y=1050)

        ffnlabel = Label(sf, text="FIRST NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        ffnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        ffnEntry.place(x=950, y=1100)

        fmnlabel = Label(sf, text="MIIDDLE NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        fmnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        fmnEntry.place(x=950, y=1150)

        mmnlabel = Label(sf, text="21. MOTHER'S MAIDEN NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        mmnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        mmnEntry.place(x=950, y=1200)

        msnlabel = Label(sf, text="SURNAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        msnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        msnEntry.place(x=950, y=1250)

        mfnlabel = Label(sf, text="FIRST NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        baEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        baEntry.place(x=950, y=1300)

        mlabel = Label(sf, text="MIDDLE NAME : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1052)
        mEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 0 ,font=('Arial', 22),text_color='black')
        mEntry.place(x=950, y=1350)

         

    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------EDUC BACKGROUND-----------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#


        
        eblabel = Label(sf, text="EDUCATIONAL BACKGROUND", font=('Arial', 17, 'bold'),bg="#8ed1ba")
        eblabel.place(x=30, y=1400)

        elabel = Label(sf, text="ELEMENTARY : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1450)
        ensEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        ensEntry.place(x=200, y=1500)

        bdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        bdcEntry.place(x=620, y=1500)

        froEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        froEntry.place(x=940, y=1500)

        toEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        toEntry.place(x=1030, y=1500)

        hiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hiEntry.place(x=1120, y=1500)

        ygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        ygEntry.place(x=1240, y=1500)

        saEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        saEntry.place(x=1360, y=1500)


        hslabel = Label(sf, text="HIGHSCHOOL : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1450)
        hsnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hsnsEntry.place(x=200, y=1550)

        hsbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hsbdcEntry.place(x=620, y=1550)

        hsfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hsfroEntry.place(x=940, y=1550)

        hstoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hstoEntry.place(x=1030, y=1550)

        hshiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hshiEntry.place(x=1120, y=1550)

        hsygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hsygEntry.place(x=1240, y=1550)

        hssaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        hssaEntry.place(x=1360, y=1550)


        vtlabel = Label(sf, text="VOCATIONAL/\nTRADE COURSE : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1450)
        vtnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vtnsEntry.place(x=200, y=1600)

        vtbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vtbdcEntry.place(x=620, y=1600)

        vtfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vtfroEntry.place(x=940, y=1600)

        vttoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vttoEntry.place(x=1030, y=1600)

        vthiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vthiEntry.place(x=1120, y=1600)

        vtygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vtygEntry.place(x=1240, y=1600)

        vtsaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        vtsaEntry.place(x=1360, y=1600)


        clabel = Label(sf, text="COLLEGE : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1450)
        cnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        cnsEntry.place(x=200, y=1650)

        cbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        cbdcEntry.place(x=620, y=1650)

        cfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        cfroEntry.place(x=940, y=1650)

        ctoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        ctoEntry.place(x=1030, y=1650)

        chiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        chiEntry.place(x=1120, y=1650)

        cygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        cygEntry.place(x=1240, y=1650)

        csaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        csaEntry.place(x=1360, y=1650)

        gslabel = Label(sf, text="GRADUATE STUDIES : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=1450)
        gsnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gsnsEntry.place(x=200, y=1700)

        gsbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gsbdcEntry.place(x=620, y=1700)

        gsfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gsfroEntry.place(x=940, y=1700)

        gstoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gstoEntry.place(x=1030, y=1700)

        gshiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gshiEntry.place(x=1120, y=1700)

        gsygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gsygEntry.place(x=1240, y=1700)

        gssaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 0, font=('Arial', 16,),text_color='black')
        gssaEntry.place(x=1360, y=1700)



        




       


       






      

   

        """
    
        polabel = Label(sf, text="POSITION : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=800, y=235)
        poEntry = customtkinter.CTkEntry(sf, width=400, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black')
        poEntry.place(x=950, y=233)

        deabel = Label(sf, text="DEPARTMENT : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=800, y=285)
        deEntry = customtkinter.CTkEntry(sf, width=400, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black')
        deEntry.place(x=950, y=283)

    





"""

    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------showing data------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#
        
    def show_e():

        f2_2 = customtkinter.CTkFrame(f2, width=1500, height=820, fg_color ="#8ed1ba")
        f2_2.place(x=0, y=0)
        f2_2.pack_propagate(0)
        cv2 = Canvas(f2_2,background='#dbb2b2',highlightthickness=0)
        cv2.pack(side =LEFT,fill=BOTH, expand=1)
        sb2= customtkinter.CTkScrollbar(f2_2, orientation= VERTICAL, border_spacing = 3,fg_color = 'white', command=cv2.yview)
        sb2.pack(side=RIGHT, fill=Y)
        cv2.configure(yscrollcommand=sb2.set)
        cv2.bind('<Configure>', lambda e:cv2.configure(scrollregion = cv2.bbox('all')))

        sf2 = customtkinter.CTkFrame(cv2, width=1500, height=1000 ,fg_color ="#d1a78e")
        cv2.create_window((0,0), window=sf2, anchor="nw")

        def mousewheel(event):
            cv2.yview_scroll(-1*(event.delta/500), "units")

        cv2.bind("<MouseWheel>",mousewheel)



        def select():

            sname = str(res1.cget("text"))
            fname = str(res2.cget("text"))
            mname = str(res3.cget("text"))
            ct = str(res6.cget("text"))
            hei = str(res8.cget("text"))
            wei = str(res9.cget("text"))
            tlno = str(res11.cget("text"))
            clno = str(res12.cget("text"))
            email = str(res13.cget("text"))
            pos = str(res14.cget("text"))
            dept = str(res15.cget("text"))
            
            setc(sname,1)
            setc(fname,2)
            setc(mname,3)
            setc(ct,4)
            setc(hei,5)
            setc(wei,6)
            setc(tlno,7)
            setc(clno,8)
            setc(email,9)
            setc(pos,10)
            setc(dept,11)
            indicate(modify_e)

            

        back2 = customtkinter.CTkButton(sf2,text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#d1a78e', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(record))
        back2.place(x=1000, y=900)

        modb = customtkinter.CTkButton(sf2,text="Modify",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#d1a78e', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=select)
        modb.place(x=1200, y=900)


        pilabel = Label(sf2, text="PERSONAL INFORMATION ", font=('Arial', 20, 'bold'),bg="#d1a78e")
        pilabel.place(x=30, y=25)

        snlabel = Label(sf2, text="YOUR ID : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=1230, y=85)
        res = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c)
        res.place(x=1320, y=85)

        snlabel = Label(sf2, text="SURNAME : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=85)
        res1 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c3)
        res1.place(x=160, y=83)

        fnlabel = Label(sf2, text="FIRSTNAME : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=135)
        res2 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c1)
        res2.place(x=160, y=133)

        mnlabel = Label(sf2, text="MIDDLENAME : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=185)
        res3 = Label(sf2,text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c2)
        res3.place(x=160, y=183)

        sexlabel = Label(sf2, text="SEX : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=800, y=135)
        res4 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c4)
        res4.place(x=950,y= 135)

        doblabel = Label(sf2, text="DATE OF BIRTH : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=800, y=85)
        res5 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c5)
        res5.place(x=950, y= 83)

        ctlabel = Label(sf2, text="CITIZENSHIP : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=235)
        res6 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c6)
        res6.place(x=160, y=233)

        statuslabel = Label(sf2, text="CIVIL STATUS : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=800, y=185)
        res7 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c7)
        res7.place(x=950, y= 183)

        hlabel = Label(sf2, text="HEIGHT (m) : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=285)
        res8 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c8)
        res8.place(x=160, y=283)

        wlabel = Label(sf2, text="WEIGHT (kg) : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=335)
        res9 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c9)
        res9.place(x=160, y=333)

        btlabel = Label(sf2, text="BLOOD TYPE : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=385)
        res10 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c10)
        res10.place(x=160, y= 383)


        tlabel = Label(sf2, text="TEL NO. : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=435)
        res11 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c11)
        res11.place(x=160, y=433)

        clabel = Label(sf2, text="CEL NO. : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=485)
        res12 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c12)
        res12.place(x=160, y=483)

        elabel = Label(sf2, text="EMAIL : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=30, y=535)
        res13 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c13)
        res13.place(x=160, y=533)

        polabel = Label(sf2, text="POSITION : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=800, y=235)
        res14 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c14)
        res14.place(x=950, y=233)

        deabel = Label(sf2, text="DEPARTMENT : ", font=('Arial', 12, 'bold'),bg="#d1a78e").place(x=800, y=285)
        res15 = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c15)
        res15.place(x=950, y=283)

        elabel = Label(sf2, text="ELEMENTARY : ", font=('Arial', 12, 'bold'),bg="#8ed1ba").place(x=30, y=650)
        elEntry = Label(sf2, text="", font=('Arial', 12, 'bold'),bg="#d1a78e", textvariable=c16)
        elEntry.place(x=200, y=650)


        
    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------updating data------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#

        
    def modify_e():


        f2_3 = customtkinter.CTkFrame(f2, width=1500, height=820, fg_color ="#8ed1ba")
        f2_3.place(x=0, y=0)
        f2_3.pack_propagate(0)
        cv3= Canvas(f2_3,background='#dbb2b2',highlightthickness=0,)
        cv3.pack(side =LEFT,fill=BOTH, expand=1)
        sb3 = customtkinter.CTkScrollbar(f2_3, orientation= VERTICAL, border_spacing = 3,fg_color = 'white', command=cv3.yview)
        sb3.pack(side=RIGHT, fill=Y)
        cv3.configure(yscrollcommand=sb3.set)
        cv3.bind('<Configure>', lambda e:cv3.configure(scrollregion = cv3.bbox('all')))

        sf3 = customtkinter.CTkFrame(cv3, width=1500, height=1000 ,fg_color ="#b780c2")
        cv3.create_window((0,0), window=sf3, anchor="nw")


        def mousewheel(event):
            cv3.yview_scroll(-1*(event.delta/500), "units")

        cv3.bind("<MouseWheel>",mousewheel)

        

        def update():
        
            selected_item = my_tree.selection()[0]
            jed = str(my_tree.item(selected_item)['values'][0])
        
            sname = str(sn2.get())
            fname = str(fnEntry2.get())
            mname = str(mnEntry2.get())
            ct = str(ctEntry2.get())
            hei = str(htEntry2.get())
            wei = str(wtEntry2.get())
            bt = str(btt2.get())
            tlno = str(tEntry2.get())
            clno = str(cEntry2.get())
            email = str(eEntry2.get())
            dobb =  str(dobentry2.get_date())
            sex = str(rb2.get())
            cs = str(cb2.get())
            pos = str(poEntry2.get())
            dept = str(deEntry2.get())

            if (sname == "" or sname == " ") or (fname == "" or  fname == " ") or (mname == "" or mname == " ") or (ct == "" or ct == " ") or (hei == "" or hei == " ") or (wei == "" or wei == " ") or (bt == "" or bt == " ") or (tlno == "" or tlno == " ") or (clno == "" or clno == " ") or (email == "" or email == " ") or (dobb == "" or dobb == " ") or (sex == "" or sex == " ") or (cs == "" or cs == " ") or (pos == "" or pos == " ") or (dept == "" or dept == " "):
                messagebox.showinfo("Error", "Please fill up the blank entry")
                return
            else:
                try:
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE person SET firstname='"+fname+"', middlename='"+mname+"', lastname='"+sname+"', sex='"+sex+"', DOB='"+dobb+"', citizenship='"+ct+"',civilstatus='"+cs+"',height='"+hei+"',weight='"+wei+"',bloodtype='"+bt+"',tellno='"+tlno+"',cellno='"+clno+"',email='"+email+"',position='"+pos+"',department='"+dept+"' WHERE id='"+jed+"' ")
                    conn.commit()
                    conn.close()
                    msg = messagebox.askquestion('',"Do you want to Update this Information?")
                    if msg == 'yes':
                        sn2.delete(0,'end')
                        fnEntry2.delete(0,'end')
                        mnEntry2.delete(0,'end')
                        ctEntry2.delete(0,'end')
                        htEntry2.delete(0,'end')
                        wtEntry2.delete(0,'end')
                        btt2.set("")
                        tEntry2.delete(0,'end')
                        cEntry2.delete(0,'end')
                        eEntry2.delete(0,'end')
                        dobentry2.set_date(dt)
                        rb2.set(None)
                        cb2.set("")
                        poEntry2.delete(0,'end')
                        eEntry2.delete(0,'end')
                        deEntry2.delete(0,'end')
                        indicate(record)
                    else:
                        messagebox.showinfo('Return', 'You will now return to the application screen')
                except:
                    messagebox.showinfo("Error", "Inventory already exist")
                    return

            refreshTable()
        
        back3 = customtkinter.CTkButton(sf3,text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#b780c2', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(show_e))
        back3.place(x=1000, y=900)

        uptd = customtkinter.CTkButton(sf3,text="Update",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#b780c2', width=160, height=60, border_width=0, corner_radius=10,
        hover_color = '#2a4859',cursor='hand2',command=update)
        uptd.place(x=1200, y=900)


        pilabel2 = Label(sf3, text="UPDATING INFORMATION ", font=('Arial', 17, 'bold'),bg="#b780c2")
        pilabel2.place(x=30, y=25)

        snlabel2 = Label(sf3, text="SURNAME : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=85)
        sn2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0,font=('Arial', 16,),text_color='black',textvariable=tc1)
        sn2.place(x=160, y=83)

        fnlabel2 = Label(sf3, text="FIRSTNAME : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=135)
        fnEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black',textvariable=tc2)
        fnEntry2.place(x=160, y=133)

        mnlabel2 = Label(sf3, text="MIDDLENAME : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=185)
        mnEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black',textvariable=tc3)
        mnEntry2.place(x=160, y=183)

        sexlabel2 = Label(sf3, text="SEX : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=800, y=135)
        rb2 =StringVar()
        r12 = customtkinter.CTkRadioButton(sf3, text="Male",border_width_checked = 7, border_width_unchecked= 5, value='male',bg_color="#b780c2",variable=rb2,cursor='hand2', font=('arial', 14),text_color='black').place(x=950,y= 135)
        r22 = customtkinter.CTkRadioButton(sf3, text="Female",border_width_checked = 7, border_width_unchecked= 5, value='female',bg_color="#b780c2",variable=rb2,cursor='hand2',font=('arial', 14),text_color='black').place(x=1050,y= 135)
        rb2.set(result[4])

        doblabel2 = Label(sf3, text="DATE OF BIRTH : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=800, y=85)
        dobentry2 = DateEntry(sf3, width=23, font = ('arial', 16), year=2019, month=6, day=22,background='gray', foreground='white', borderwidth=0, weekendbackground ="red",bd = 0)
        dt = date(2023,1,1)
        dobentry2.set_date(result[5])
        dobentry2.place(x=950, y= 83)

        ctlabel2 = Label(sf3, text="CITIZENSHIP : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=235)
        ctEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black',textvariable=tc6)
        ctEntry2.place(x=160, y=233)

        statuslabel2 = Label(sf3, text="CIVIL STATUS : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=800, y=185)
        cb2 = tk.StringVar()
        st2 = customtkinter.CTkOptionMenu(sf3,width = 300,fg_color='white',font=('arial', 14),dropdown_font = ('arial', 14),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = 'white',button_hover_color = 'gray',text_color = "black",variable = cb2, values=["Single", "Married", "Widowed", "Seperated", "Other/s"])
        st2.place(x=950, y= 183)
        st2.set(result[7])

        hlabel2 = Label(sf3, text="HEIGHT (m) : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=285)
        htEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=tc8)
        htEntry2.place(x=160, y=283)

        wlabel2 = Label(sf3, text="WEIGHT (kg) : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=335)
        wtEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=tc9)
        wtEntry2.place(x=160, y=333)

        btlabel2 = Label(sf3, text="BLOOD TYPE : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=385)
        btt2 = tk.StringVar()
        bt2 = customtkinter.CTkOptionMenu(sf3,width = 300,fg_color='white',font=('arial', 14),dropdown_font = ('arial', 14),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = 'white',button_hover_color = 'gray',text_color = "black",variable = btt2, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        bt2.place(x=160, y= 383)
        bt2.set(result[10])

        tlabel2 = Label(sf3, text="TEL NO. : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=435)
        tEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=tc11)
        tEntry2.place(x=160, y=433)

        clabel2 = Label(sf3, text="CEL NO. : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=485)
        cEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=tc12)
        cEntry2.place(x=160, y=483)

        elabel2 = Label(sf3, text="EMAIL : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=30, y=535)
        eEntry2 = customtkinter.CTkEntry(sf3, width=500, fg_color='white',border_width = 0 ,font=('Arial', 16),text_color='black',textvariable=tc13)
        eEntry2.place(x=160, y=533)


        polabel2 = Label(sf3, text="POSITION : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=800, y=235)
        poEntry2 = customtkinter.CTkEntry(sf3, width=400, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black',textvariable=tc14)
        poEntry2.place(x=950, y=233)

        deabel2 = Label(sf3, text="DEPARTMENT : ", font=('Arial', 12, 'bold'),bg="#b780c2").place(x=800, y=285)
        deEntry2 = customtkinter.CTkEntry(sf3, width=400, fg_color='white',border_width = 0 ,font=('Arial', 16,),text_color='black',textvariable=tc15)
        deEntry2.place(x=950, y=283)
        


    #-------------------------------------------------------------------------------------------------------------------------------------#
    #---------------------------------------------------------function--------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#

    

        
    def delete():

        find2 = str(findEntry.get())

        if find2 == "" or find2 == " ":
             messagebox.showinfo("Error", "Please select a Data")
    
        selected_item = my_tree.selection()[0] 
        decision = messagebox.askquestion("Warning!!", "Delete the selected data? " + (my_tree.item(selected_item)['values'][2]))
    
        if decision != "yes":
            return 
        else:
            selected_item = my_tree.selection()[0] 
            deleteData = str(my_tree.item(selected_item)['values'][0])
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM person WHERE id ='"+str(deleteData)+"'")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Sorry an error occured")
                return


        refreshTable()
        
    #-------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------buttons------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------------------------------------------#


    addb = customtkinter.CTkButton(f2,text="add Employee",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(add_e))
    addb.place(x=1200, y=710)

    showb = customtkinter.CTkButton(f2,text="Show Data",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=show)
    showb.place(x=1000, y=710)

    delb = customtkinter.CTkButton(f2,text="Delete",fg_color='#9c4656',font=('Arial', 20,) ,bg_color= '#8aafd4', width=160, height=60, border_width=0, corner_radius=10,
    hover_color = '#2a4859',cursor='hand2',command=delete)
    delb.place(x=800, y=710)


    find = Label(f2, text="FIND : ", font=('Arial', 18, 'bold'),bg="#8aafd4").place(x=50, y=30)
    findEntry = customtkinter.CTkEntry(f2,height = 37, width=200, fg_color='white',border_width = 0 ,font=('Arial', 20),text_color='black',textvariable=fi)
    findEntry.place(x=130, y=28)




    my_tree =ttk.Treeview(f2, show="headings", height=11)
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
        mouse_select()

    my_tree.bind("<Double-1>", dclick)
    
    populate()
    refreshTable()

    
def leave():
    f4 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8a9dd4")
    f4.place(x=380, y=200)
    ln = Label(f4, text="Total Employees", font=('Arial', 20), background="#86babd")
    ln.place(x=50, y=10)
    

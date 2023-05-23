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
import io
from PIL import ImageGrab
from tkinter import filedialog
from PIL import Image, ImageTk
from dashboard import*

   

def add_e():

   f2_1 = customtkinter.CTkFrame(None, width=1500, height=820)
   f2_1.place(x=380, y=200)
   f2_1.pack_propagate(0)
   cv = Canvas(f2_1,background='#d4d4d4',highlightthickness=0)
   cv.pack(side =LEFT,fill=BOTH, expand=1)
   sb = customtkinter.CTkScrollbar(f2_1, orientation= VERTICAL, border_spacing = 2,fg_color = '#aee0e8', command= cv.yview)
   sb.pack(side=RIGHT, fill=Y)
   cv.configure(yscrollcommand=sb.set)
   cv.bind('<Configure>', lambda e:cv.configure(scrollregion = cv.bbox('all')))

   sf = customtkinter.CTkFrame(cv, width=1500, height=2300 ,fg_color ="#d4d4d4",corner_radius=50)
   cv.create_window((0,0), window=sf, anchor="nw")

   sf.bind("<MouseWheel>", lambda event: cv.yview_scroll(-int(event.delta/100), "units"))


   def deletef():
      for frame in f2_1.winfo_children():
         frame.destroy()

   def indicate(page):
      deletef()
      page()


   def validate(u_input): 
      return u_input.isdigit()
   my_valid = f2_1.register(validate)

   
      


   def add():

      #=====personal
      sname = str(sn.get())
      fname = str(fnEntry.get())
      mname = str(mnEntry.get())
      dob = str(dobentry.get_date())
      pob = str(pobEntry.get())
      sex = str(sexx.get())
      civil = str(civ.get())
      hei = str(htEntry.get())
      wei = str(wtEntry.get())
      blood = str(blo.get())
      ctiz = str(ctz.get())
      ifdu = str(opt2.get())
      count = str(couEntry.get())
      email = str(eEntry.get())
      staff = str(staEntry.get())
      posi = str(poEntry.get())
      dept = str(deEntry.get())
      stus = str(tus.get())
      sal = str(sg.get())
      con_fro = str(lfrom.get_date())
      con_to = str(lto.get_date())
      perm_start = str(lstart.get_date())

      #=====numbers
      gsis = str(gsEntry.get())
      pagi = str(pagEntry.get())
      phil = str(phEntry.get())
      sss = str(ssEntry.get())
      tin = str(tiEntry.get())
      agem = str(aeEntry.get())
      tele = str(tEntry.get())
      cell = str(cEntry.get())

      #=====residential address
      res1 = str(raEntry.get())
      res2 = str(ra2Entry.get())
      res3 = str(ra3Entry.get())
      res4 = str(ra4Entry.get())
      res5 = str(ra5Entry.get())
      res6 = str(ra6Entry.get())
      res7 = str(ra7Entry.get())
      

      #=====permanent address
      per1 = str(pa1Entry.get())
      per2 = str(pa2Entry.get())
      per3 = str(pa3Entry.get())
      per4 = str(pa4Entry.get())
      per5 = str(pa5Entry.get())
      per6 = str(pa6Entry.get())
      per7 = str(pa7Entry.get())


      #=====spouse
      sposn = str(spoEntry.get())
      spofn = str(fspoEntry.get())
      spomn = str(mspoEntry.get())
      spooc = str(ocEntry.get())
      spoebn = str(ebmEntry.get())
      spoba = str(baEntry.get())
      spotel = str(teleEntry.get())
      
      #=====family
      fsn = str(fsnEntry.get())
      ffn = str(ffnEntry.get())
      fmn = str(fmnEntry.get())
      mmn = str(mmnEntry.get())
      msn = str(msnEntry.get())
      mfn = str(mfnEntry.get())
      mmd = str(mEntry.get())

      #=====elementary
      ens = str(ensEntry.get())
      ebdc = str(bdcEntry.get())
      efrom = str(froEntry.get())
      eto = str(toEntry.get())
      ehigh = str(hiEntry.get())
      eyg = str(ygEntry.get())
      esa = str(saEntry.get())

      #=====highschool
      hsns = str(hsnsEntry.get())
      hsbdc = str(hsbdcEntry.get())
      hsfrom = str(hsfroEntry.get())
      hsto = str(hstoEntry.get())
      hshigh = str(hshiEntry.get())
      hsyg = str(hsygEntry.get())
      hssa = str(hssaEntry.get())

      #=====vocational
      vtns = str(vtnsEntry.get())
      vtbdc = str(vtbdcEntry.get())
      vtfrom = str(vtfroEntry.get())
      vtto = str(vttoEntry.get())
      vthigh = str(vthiEntry.get())
      vtyg = str(vtygEntry.get())
      vtsa = str(vtsaEntry.get())

      #=====college
      cns = str(cnsEntry.get())
      cbdc = str(cbdcEntry.get())
      cfrom = str(cfroEntry.get())
      cto = str(ctoEntry.get())
      chigh = str(chiEntry.get())
      cyg = str(cygEntry.get())
      csa = str(csaEntry.get())


      #=====graduate studies
      gns = str(gsnsEntry.get())
      gbdc = str(gsbdcEntry.get())
      gfrom = str(gsfroEntry.get())
      gto = str(gstoEntry.get())
      ghigh = str(gshiEntry.get())
      gyg = str(gsygEntry.get())
      gsa = str(gssaEntry.get())



      if (sname == "" or sname == " ") or (fname == "" or  fname == " ") or (mname == "" or mname == " ") or (pob == "" or pob == " ") or (sex == None or sex == "None") or (civil == "" or civil == " ") or (hei == "" or hei == " ") or (blood == "" or blood == " ") or (posi == "" or posi == " ") or (staff == "" or staff == " ") or (agem == "" or agem == " ") or (ctiz == None or ctiz == "None") or (dept == "" or dept == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return
      else:
            try:
               msg = messagebox.askquestion('',"Do you want to add this person?")
               if msg == 'yes':
                  conn = connection()
                  cursor = conn.cursor()
                  cursor.execute(
                     "INSERT INTO personal VALUES ('""','"+sname+"','"+fname+"','"+mname+"','"+dob+"','"+pob+"','"+sex+"','"+civil+"','"+hei+"','"+wei+"','"+blood+"','"+ctiz+"','"+ifdu+"','"+count+"','"+email+"','"+staff+"','"+posi+"','"+dept+"','"+sal+"','"+stus+"','"+con_fro+"','"+con_to+"','"+perm_start+"') ")
                  cursor.execute(
                     "INSERT INTO numbers VALUES ('""','"+gsis+"','"+pagi+"','"+phil+"','"+sss+"','"+tin+"','"+agem+"','"+tele+"','"+cell+"') ")
                  cursor.execute(
                     "INSERT INTO residential VALUES ('""','"+res1+"','"+res2+"','"+res3+"','"+res4+"','"+res5+"','"+res6+"','"+res7+"') ")
                  cursor.execute(
                     "INSERT INTO permanent VALUES ('""','"+per1+"','"+per2+"','"+per3+"','"+per4+"','"+per5+"','"+per6+"','"+per7+"') ")
                  cursor.execute(
                     "INSERT INTO spouse VALUES ('""','"+sposn+"','"+spofn+"','"+spomn+"','"+spooc+"','"+spoebn+"','"+spoba+"','"+spotel+"') ")
                  cursor.execute(
                     "INSERT INTO family VALUES ('""','"+fsn+"','"+ffn+"','"+fmn+"','"+mmn+"','"+msn+"','"+mfn+"','"+mmd+"') ")
                  cursor.execute(
                     "INSERT INTO elementary VALUES ('""','"+ens+"','"+ebdc+"','"+efrom+"','"+eto+"','"+ehigh+"','"+eyg+"','"+esa+"') ")
                  cursor.execute(
                     "INSERT INTO highschool VALUES ('""','"+hsns+"','"+hsbdc+"','"+hsfrom+"','"+hsto+"','"+hshigh+"','"+hsyg+"','"+hssa+"') ")
                  cursor.execute(
                     "INSERT INTO vocational VALUES ('""','"+vtns+"','"+vtbdc+"','"+vtfrom+"','"+vtto+"','"+vthigh+"','"+vtyg+"','"+vtsa+"') ")
                  cursor.execute(
                     "INSERT INTO college VALUES ('""','"+cns+"','"+cbdc+"','"+cfrom+"','"+cto+"','"+chigh+"','"+cyg+"','"+csa+"') ")
                  cursor.execute(
                     "INSERT INTO graduate VALUES ('""','"+gns+"','"+gbdc+"','"+gfrom+"','"+gto+"','"+ghigh+"','"+gyg+"','"+gsa+"') ")
                  conn.commit()
                  conn.close()
                  for entry in (sn,fnEntry,mnEntry,pobEntry,htEntry,wtEntry,gsEntry,pagEntry,phEntry,tiEntry,aeEntry,tEntry,cEntry,couEntry,raEntry,ra2Entry,ra3Entry,ra4Entry,ra5Entry,ra6Entry,ra7Entry,pa1Entry,pa2Entry,pa3Entry,pa4Entry,pa5Entry,pa6Entry,pa7Entry,eEntry,spoEntry,fspoEntry,mspoEntry,ocEntry,ebmEntry,baEntry,teleEntry,fsnEntry,ffnEntry,fmnEntry,mmnEntry,msnEntry,mfnEntry,mEntry,ensEntry,bdcEntry,froEntry,toEntry,hiEntry,ygEntry,saEntry,hsnsEntry,hsbdcEntry,hsfroEntry,hstoEntry,hshiEntry,hsygEntry,hssaEntry,vtnsEntry,vtbdcEntry,vtfroEntry,vttoEntry,vthiEntry,vtygEntry,vtsaEntry,cnsEntry,cbdcEntry,cfroEntry,ctoEntry,chiEntry,cygEntry,csaEntry,gsnsEntry,gsbdcEntry,gsfroEntry,gstoEntry,gshiEntry,gsygEntry,gssaEntry):
                     entry.delete(0,'end')
                  dobentry.set_date(dt)
                  sexx.set(None)
                  civ.set(None)
                  ctz.set(None)
                  opt2.set(None)
                  indicate(dash)
               elif msg == 'no':
                  pass
               else:
                  messagebox.showinfo('Return', 'You will now return to the application screen')
                  indicate(dash)
            except:
               
               messagebox.showinfo("Error", "Data already exist")
               return
            
   def upl_mc():

      global imgfile, photo

      f_types = [('JPG', '*.jpg'),('PNG', '*.png')]
      imgfile = filedialog.askopenfilename(filetypes=f_types)
      photo = PIL.Image.open(imgfile)

      imgs = customtkinter.CTkImage(photo,size=(140,140))
      imgs2 = customtkinter.CTkImage(photo,size=(250,250))

      profile = customtkinter.CTkLabel(sf, text="", image= imgs)
      profile.place(x=1230, y=100)

      profile2 = customtkinter.CTkLabel(sf, text="", image= imgs2)
      profile2.place(x=1120, y=1800)

   def addimg():
      if imgfile:
            fob = open(imgfile, 'rb').read()
            conn = connection()
            cursor = conn.cursor()
            args = (sn.get(), fnEntry.get(),fob)
            cursor.execute("INSERT INTO profile (fname,sname,img) VALUES (%s,%s,%s)",args)
            conn.commit()
            conn.close()
      else:
            messagebox.showinfo("Error", "No File Saved")

   def allsave():
       addimg()
       add()

   back = customtkinter.CTkButton(sf, text="Back",fg_color='#9c465d',font=('Arial', 20,) ,bg_color= '#d4d4d4', width=160, height=60, border_width=0, corner_radius=10,
   hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(dash))
   back.place(x=1000, y=2200)

   addto = customtkinter.CTkButton(sf,text="Attach",fg_color='#46829c',font=('Arial', 20,) ,bg_color= '#d4d4d4', width=160, height=60, border_width=0, corner_radius=10,
   hover_color = '#2a4859',cursor='hand2',command=allsave)
   addto.place(x=1200, y=2200)

#-------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------PERSONAL INFO-----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#

   titleabel = Label(sf, text="PERSONAL DATA SHEET", font=('Arial', 22, 'bold'),bg="#d4d4d4")
   titleabel.place(x=690, y=10, anchor= N)

   line = customtkinter.CTkFrame(sf, height=40,width=1485, fg_color="#aeafb0").place(x=0,y=50)
   sublabel = Label(sf, text="PERSONAL INFORMATION ", font=('Arial', 18, 'bold'),bg="#aeafb0")
   sublabel.place(x=30, y=55)

   pro_up = customtkinter.CTkButton(sf, width=50, height=30, command=upl_mc, text="Chose Image file")
   pro_up.place(x=1060, y=200)

   phott = customtkinter.CTkLabel(sf, text="PHOTO", font=('Arial', 20, 'bold'),bg_color="transparent",text_color="#9c9c9c").place(x=1230, y=150)

   
   snlabel = Label(sf, text="1.SURNAME :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=100)
   sn = customtkinter.CTkEntry(sf, height= 35,width=450, fg_color='white',border_width = 2, corner_radius= 10,placeholder_text = "Name extension (Jr.,Sr.)",font=('Arial', 22),placeholder_text_color= "gray",text_color='black')
   sn.place(x=280, y=100)

   fnlabel = Label(sf, text="  FIRSTNAME :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=150)
   fnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 22),text_color='black')
   fnEntry.place(x=280, y=150)

   mnlabel = Label(sf, text="  MIDDLENAME :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=200)
   mnEntry = customtkinter.CTkEntry(sf,  height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   mnEntry.place(x=280, y=200)

   doblabel = Label(sf, text="2.DATE OF BIRTH :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=252)
   dobentry = DateEntry(sf, height= 35, width=15, font = ('arial', 22),date_pattern='mm/dd/y', background='gray', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
   dt = date(2023,1,1)
   dobentry.set_date(dt)
   dobentry.place(x=280, y= 250)

   poblabel = Label(sf, text="3.PLACE OF BIRTH :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=302)
   pobEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pobEntry.place(x=280, y=300)

   sexlabel = Label(sf, text="4.SEX : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=350)
   sexx = tk.StringVar()
   stat1 = customtkinter.CTkRadioButton(sf, text="Male", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='male',bg_color ="#d4d4d4",variable=sexx, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black').place(x=280,y= 350)
   stat2 = customtkinter.CTkRadioButton(sf, text="Female",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='female',bg_color ="#d4d4d4",variable=sexx, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black').place(x=380,y= 350)
   sexx.set(None)

   statuslabel = Label(sf, text="5.CIVIL STATUS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=400)
   civ = tk.StringVar()
   st = customtkinter.CTkOptionMenu(sf,height= 35, width = 300,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black",variable = civ, values=["Single", "Married", "Widowed", "Seperated", "Other/s"])
   st.place(x=280, y= 400)
   st.set("")

   hlabel = Label(sf, text="6.HEIGHT (cm) :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=450)
   htEntry = customtkinter.CTkEntry(sf,height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   htEntry.place(x=280, y=450)

   wtlabel = Label(sf, text="7.WEIGHT (kg) :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=500)
   wtEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   wtEntry.place(x=280, y=500)

   btlabel = Label(sf, text="8.BLOOD TYPE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=550)
   blo = tk.StringVar()
   bt = customtkinter.CTkOptionMenu(sf,height= 35, width = 300,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color ='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", variable = blo, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
   bt.place(x=280, y= 550)
   bt.set("")

   gslabel = Label(sf, text="9.GSIS ID NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=600)
   gsEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   gsEntry.place(x=280, y=600)

   paglabel = Label(sf, text="10.PAG-IBIG ID NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=650)
   pagEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   pagEntry.place(x=280, y=650)

   phlabel = Label(sf, text="11.PHILHEALTH NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=700)
   phEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   phEntry.place(x=280, y=700)

   sslabel = Label(sf, text="12.SSS NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=750)
   ssEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   ssEntry.place(x=280, y=750)

   tilabel = Label(sf, text="13.TIN NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=800)
   tiEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   tiEntry.place(x=280, y=800)

   aelabel = Label(sf, text="14.AGENCY EMPLOYEE NO.:", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=850)
   aeEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   aeEntry.place(x=280, y=850)

   tlabel = Label(sf, text="15.TELEPHONE NO. : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=900)
   tEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   tEntry.place(x=280, y=900)

   clabel = Label(sf, text="16.CELLPHONE NO. : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=950)
   cEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   cEntry.place(x=280, y=950)

   tuslabel = Label(sf, text="STATUS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=100)
   tus = tk.StringVar()
   tus = customtkinter.CTkOptionMenu(sf,height= 35, width = 250,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black",variable = tus, values=["Active", "Inactive", "AWOL"])
   tus.place(x=920, y=100)
   tus.set("")

   fnlabel = Label(sf, text="SALARY GRADE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=150)
   sg = customtkinter.CTkEntry(sf, height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 22),text_color='black')
   sg.place(x=920, y=150)

   def fr():
      for gr in (optlabel,ct5,ct6,coulabel,couEntry):
         gr.place_forget()
      opt2.set(None)
      couEntry.delete(0,'end')

   def gt():
      optlabel.place_configure(x=900, y=300)
      ct5.place_configure(x=1050,y= 350)
      ct6.place_configure(x=1190,y= 350)
      coulabel.place_configure(x=850, y=397)
      couEntry.place_configure(x=1025, y=395)
      

   ctlabel = Label(sf, text="17.CITIZENSHIP :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=250)
   ctz = tk.StringVar()
   ct3 = customtkinter.CTkRadioButton(sf, text="Filipino", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color ="#d4d4d4",variable=ctz, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black',command=fr).place(x=990,y= 250)
   ct4 = customtkinter.CTkRadioButton(sf, text="Dual Citizenship",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color ="#d4d4d4",variable=ctz, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black',command=gt).place(x=1130,y= 250)
   ctz.set(None)

   optlabel = Label(sf, text="if Dual Citizenship:", font=('Courier', 15, 'bold'),bg="#d4d4d4")
   optlabel.place(x=900, y=300)
   opt2 = tk.StringVar()
   ct5 = customtkinter.CTkRadioButton(sf, text="By Birth", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='By Birth',bg_color ="#d4d4d4",variable=opt2, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black')
   ct5.place(x=1050,y= 350)
   ct6 = customtkinter.CTkRadioButton(sf, text="By Naturalization",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='By Naturalization',bg_color ="#d4d4d4",variable=opt2, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black')
   ct6.place(x=1190,y= 350)
   opt2.set(None)

   coulabel = Label(sf, text="your Country :", font=('Courier', 14, 'bold'),bg="#d4d4d4")
   coulabel.place(x=850, y=397)
   couEntry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   couEntry.place(x=1025, y=395)


   ralabel = Label(sf, text="18.RESIDENTIAL ADDRESS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=450)
   ra1label = Label(sf, text="HouseBlock/Lot No.", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=510)
   raEntry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   raEntry.place(x=900, y=480)

   ra2label = Label(sf, text="Street", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1270, y=510)
   ra2Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ra2Entry.place(x=1180, y=480)

   ra3label = Label(sf, text="Subdivision/Village", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=925, y=570)
   ra3Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ra3Entry.place(x=900, y=540)

   ra4label = Label(sf, text="Barangay", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=570)
   ra4Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ra4Entry.place(x=1180, y=540)

   ra5label = Label(sf, text="City/Municipality", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=630)
   ra5Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ra5Entry.place(x=900, y=600)

   ra6label = Label(sf, text="Province", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=630)
   ra6Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ra6Entry.place(x=1180, y=600)

   ra7label = Label(sf, text="ZIP CODE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=785, y=665)
   ra7Entry = customtkinter.CTkEntry(sf,height= 35, width=125, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   ra7Entry.place(x=900, y=660)

   palabel = Label(sf, text="19.PERMANENT ADDRESS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=700)
   pa1label = Label(sf, text="HouseBlock/Lot No.", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=760)
   pa1Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pa1Entry.place(x=900, y=730)

   pa2label = Label(sf, text="Street", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1270, y=760)
   pa2Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pa2Entry.place(x=1180, y=730)

   pa3label = Label(sf, text="Subdivision/Village", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=925, y=820)
   pa3Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pa3Entry.place(x=900, y=790)

   pa4label = Label(sf, text="Barangay", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=820)
   pa4Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pa4Entry.place(x=1180, y=790)

   pa5label = Label(sf, text="City/Municipality", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=880)
   pa5Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pa5Entry.place(x=900, y=850)

   pa6label = Label(sf, text="Province", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=880)
   pa6Entry = customtkinter.CTkEntry(sf,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   pa6Entry.place(x=1180, y=850)

   pa7label = Label(sf, text="ZIP CODE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=785, y=915)
   pa7Entry = customtkinter.CTkEntry(sf,height= 35, width=125, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   pa7Entry.place(x=900, y=910)

   elabel = Label(sf, text="20.EMAIL ADDRESS: ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=753, y=950)
   eEntry = customtkinter.CTkEntry(sf,height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   eEntry.place(x=950, y=950)


#-------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------FAMILY BG------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#


   line2 = customtkinter.CTkFrame(sf, height=40,width=1485, fg_color="#aeafb0").place(x=0,y=1000)
   fblabel = Label(sf, text="FAMILY BACKGROUND", font=('Arial', 18, 'bold'),bg="#aeafb0").place(x=30, y=1005)

   

   spolabel = Label(sf, text="21.SPOUSE'S SURNAME: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1052)
   spoEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   spoEntry.place(x=230, y=1050)

   fspolabel = Label(sf, text="   FIRST NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1100)
   fspoEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   fspoEntry.place(x=230, y=1100)

   mspolabel = Label(sf, text="   MIIDDLE NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1150)
   mspoEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   mspoEntry.place(x=230, y=1150)

   oclabel = Label(sf, text="   OCCUPATION : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1200)
   ocEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ocEntry.place(x=230, y=1200)

   ebmlabel = Label(sf, text="EMPLOYEE/\nBUSINESS NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4",justify= LEFT).place(x=48, y=1250)
   ebmEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ebmEntry.place(x=230, y=1250)

   balabel = Label(sf, text="   BUSINESS ADDRESS: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1305)
   baEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   baEntry.place(x=230, y=1300)

   telelabel = Label(sf, text="   TELEPHONE NO. : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1350)
   teleEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   teleEntry.place(x=230, y=1350)

   fsnlabel = Label(sf, text="22.FATHER'S SURNAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1052)
   fsnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   fsnEntry.place(x=950, y=1050)

   ffnlabel = Label(sf, text="   FIRST NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1100)
   ffnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   ffnEntry.place(x=950, y=1100)

   fmnlabel = Label(sf, text="   MIIDDLE NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1150)
   fmnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   fmnEntry.place(x=950, y=1150)

   mmnlabel = Label(sf, text="23.MOTHER'S MAIDEN NAME: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1200)
   mmnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   mmnEntry.place(x=950, y=1200)

   msnlabel = Label(sf, text="   SURNAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1250)
   msnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   msnEntry.place(x=950, y=1250)

   mfnlabel = Label(sf, text="   FIRST NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1300)
   mfnEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   mfnEntry.place(x=950, y=1300)

   mlabel = Label(sf, text="   MIDDLE NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1350)
   mEntry = customtkinter.CTkEntry(sf, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
   mEntry.place(x=950, y=1350)

   

#-------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------EDUC BACKGROUND-----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#


   

   line3 = customtkinter.CTkFrame(sf, height=40,width=1485, fg_color="#aeafb0").place(x=0,y=1400)
   eblabel = Label(sf, text="EDUCATIONAL BACKGROUND", font=('Arial', 17, 'bold'),bg="#aeafb0").place(x=30, y=1405)

   lvllabel = Label(sf, text="Level", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=50, y=1450)
   NOSlabel = Label(sf, text="Name of School", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=310, y=1450)
   BEDClabel = Label(sf, text="Basic Education/Degree/Course", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=620, y=1450)
   POAlabel = Label(sf, text="Period of Attendance", font=('Courier', 10, 'bold'),bg="#d4d4d4").place(x=935, y=1450)
   frotolabel = Label(sf, text="From      To", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=947, y=1475)
   hillabel = Label(sf, text="Highest Level/\nUnits Earned\n(if not graduated)",justify= CENTER, font=('Courier', 9, 'bold'),bg="#d4d4d4").place(x=1105 , y=1445)
   YGGlabel = Label(sf, text="Year\nGraduated", font=('Courier', 11, 'bold'),bg="#d4d4d4").place(x=1245, y=1450)
   SAlabel = Label(sf, text="Scholarship/\nAcademic Honors\nReceived", font=('Courier', 10, 'bold'),bg="#d4d4d4").place(x=1345, y=1445)


   elabel = Label(sf, text="ELEMENTARY : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1500)
   ensEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   ensEntry.place(x=200, y=1500)

   bdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   bdcEntry.place(x=620, y=1500)

   froEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   froEntry.place(x=940, y=1500)

   toEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   toEntry.place(x=1030, y=1500)

   hiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   hiEntry.place(x=1120, y=1500)

   ygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   ygEntry.place(x=1240, y=1500)

   saEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   saEntry.place(x=1360, y=1500)


   hslabel = Label(sf, text="HIGHSCHOOL : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1550)
   hsnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   hsnsEntry.place(x=200, y=1550)

   hsbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   hsbdcEntry.place(x=620, y=1550)

   hsfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   hsfroEntry.place(x=940, y=1550)

   hstoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   hstoEntry.place(x=1030, y=1550)

   hshiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   hshiEntry.place(x=1120, y=1550)

   hsygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   hsygEntry.place(x=1240, y=1550)

   hssaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   hssaEntry.place(x=1360, y=1550)


   vtlabel = Label(sf, text="VOCATIONAL/\nTRADE COURSE : ",justify = LEFT, font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1600)
   vtnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   vtnsEntry.place(x=200, y=1600)

   vtbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   vtbdcEntry.place(x=620, y=1600)

   vtfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   vtfroEntry.place(x=940, y=1600)

   vttoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   vttoEntry.place(x=1030, y=1600)

   vthiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   vthiEntry.place(x=1120, y=1600)

   vtygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   vtygEntry.place(x=1240, y=1600)

   vtsaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   vtsaEntry.place(x=1360, y=1600)


   clabel = Label(sf, text="COLLEGE : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1650)
   cnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   cnsEntry.place(x=200, y=1650)

   cbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   cbdcEntry.place(x=620, y=1650)

   cfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   cfroEntry.place(x=940, y=1650)

   ctoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   ctoEntry.place(x=1030, y=1650)

   chiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   chiEntry.place(x=1120, y=1650)

   cygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   cygEntry.place(x=1240, y=1650)

   csaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   csaEntry.place(x=1360, y=1650)

   gslabel = Label(sf, text="GRADUATE STUDIES: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1700)
   gsnsEntry = customtkinter.CTkEntry(sf,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   gsnsEntry.place(x=200, y=1700)

   gsbdcEntry = customtkinter.CTkEntry(sf,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   gsbdcEntry.place(x=620, y=1700)

   gsfroEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   gsfroEntry.place(x=940, y=1700)

   gstoEntry = customtkinter.CTkEntry(sf,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   gstoEntry.place(x=1030, y=1700)

   gshiEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black')
   gshiEntry.place(x=1120, y=1700)

   gsygEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   gsygEntry.place(x=1240, y=1700)

   gssaEntry = customtkinter.CTkEntry(sf,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black')
   gssaEntry.place(x=1360, y=1700)


   roelabel = Label(sf, text="EMPLOYEE DETAILS", font=('Arial', 17, 'bold'),bg="#d4d4d4")
   roelabel.place(x=30, y=1750)



   polabel = Label(sf, text="POSITION :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=1800)
   poEntry = tk.StringVar()
   po = customtkinter.CTkOptionMenu(sf,height= 35, width = 350,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color ='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", variable = poEntry, values=["Permanent", "Contractual","Casual" ,"On the Job", "Volunteer"])
   po.place(x=160, y=1800)
   po.set("")

   stalabel = Label(sf, text="STAFF TYPE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=570, y=1800)
   staEntry = tk.StringVar()
   sta = customtkinter.CTkOptionMenu(sf,height= 35, width = 350,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color ='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", variable = staEntry, values=["Registered Nurse", "LPN", "Midwife", "Caregivers", "Pediatric nursing",  "Practitioner", "Pharmacist","Radiologist", "Cardiologist", "Pathologist" ,"Dietitian", "Pediatrician", "Orthopedic", "General surgeons", "Pulmonologists", "Anesthesiologists", "Gynecologists", "Therapist", "hospice workers", "Social workers", "Cook", "Housekeeper", "Driver", "Porter", "Maintenance Worker", "COH", "CON" , "COD", "Assistant", "Secretary", "IT technician", "IT Administrator"])
   sta.place(x=600, y=1850)
   sta.set("")

   deptlabel = Label(sf, text="STATION :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=570, y=1920)
   deEntry = tk.StringVar()
   de = customtkinter.CTkOptionMenu(sf,height= 35, width = 350,fg_color='#a2a3a2',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color ='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", variable = deEntry, values=["ADMIN","ANCILLARY", "MEDICAL", "NURSING"])
   de.place(x=600, y=1970)
   de.set("")

   nool = customtkinter.CTkLabel(sf, text="If Contractual (time of contract):", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=1870)

   lfrom = customtkinter.CTkLabel(sf, text="From: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=40, y=1922)
   lfrom = DateEntry(sf, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
   lfrom.set_date(dt)
   lfrom.place(x=100, y= 1920)

   lto = customtkinter.CTkLabel(sf, text="To: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=270, y=1922)
   lto = DateEntry(sf, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
   lto.set_date(dt)
   lto.place(x=305, y= 1920)

   started = customtkinter.CTkLabel(sf, text="If Permanent (when it started):", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=20, y=1970)

   lstarted = customtkinter.CTkLabel(sf, text="Start: ", font=('Arial', 20, 'bold'),text_color= "black",bg_color="transparent").place(x=40, y=2022)
   lstart = DateEntry(sf, height= 25, width=10, font = ('arial', 16),date_pattern='mm/dd/y', background='#808080', foreground='white', borderwidth=5, weekendbackground ="red",bd = 0)
   lstart.set_date(dt)
   lstart.place(x=100, y= 2020)




  

   


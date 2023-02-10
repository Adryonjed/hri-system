from tkinter import *
from db import *
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
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import GOV_LEGAL









def record():
   f2 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8aafd4",corner_radius=50,bg_color="transparent")
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


   def ms(word,num):
      if num == 1:
         fi.set(word)

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
      find = str(findEntry.get())

      if find == "" or find == " ":
         messagebox.showinfo("Error", "Select a data or input your ID no.")
         return

      elif findEntry.get() != findEntry.get():
         messagebox.showinfo("Error", "NO DATA")
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
         cursor.execute("SELECT * FROM personal WHERE id=%s",(findEntry.get()))
         cursor2.execute("SELECT * FROM numbers WHERE id=%s",(findEntry.get()))
         cursor3.execute("SELECT * FROM residential WHERE id=%s",(findEntry.get()))
         cursor4.execute("SELECT * FROM permanent WHERE id=%s",(findEntry.get()))
         cursor5.execute("SELECT * FROM spouse WHERE id=%s",(findEntry.get()))
         cursor6.execute("SELECT * FROM family WHERE id=%s",(findEntry.get()))
         cursor7.execute("SELECT * FROM elementary WHERE id=%s",(findEntry.get()))
         cursor8.execute("SELECT * FROM highschool WHERE id=%s",(findEntry.get()))
         cursor9.execute("SELECT * FROM vocational WHERE id=%s",(findEntry.get()))
         cursor10.execute("SELECT * FROM college WHERE id=%s",(findEntry.get()))
         cursor11.execute("SELECT * FROM graduate WHERE id=%s",(findEntry.get()))
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
      cv = Canvas(f2_1,background='#d4d4d4',highlightthickness=0)
      cv.pack(side =LEFT,fill=BOTH, expand=1)
      sb = customtkinter.CTkScrollbar(f2_1, orientation= VERTICAL, border_spacing = 3,fg_color = '#d4d4d4', command=cv.yview)
      sb.pack(side=RIGHT, fill=Y)
      cv.configure(yscrollcommand=sb.set)
      cv.bind('<Configure>', lambda e:cv.configure(scrollregion = cv.bbox('all')))

      sf = customtkinter.CTkFrame(cv, width=1500, height=2000 ,fg_color ="#d4d4d4",corner_radius=50)
      cv.create_window((0,0), window=sf, anchor="nw")

      def mousewheel(event):
         cv.yview_scroll(-1*(event.delta/500), "units")

      cv.bind("<MouseWheel>",mousewheel)


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
         posi = str(poEntry.get())
         stat = str(stEntry.get())
         dept = str(deEntry.get()) 

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



         



         if (sname == "" or sname == " ") or (fname == "" or  fname == " ") or (mname == "" or mname == " ") or (pob == "" or pob == " ") or (sex == None or sex == "None") or (civil == "" or civil == " ") or (hei == "" or hei == " ") or (blood == "" or blood == " ") or (posi == "" or posi == " ") or (stat == "" or stat == " ") or (agem == "" or agem == " ") or (ctiz == None or ctiz == "None") or (dept == "" or dept == " "):
               messagebox.showinfo("Error", "Please fill up the blank entry")
               return
         else:
               try:
                  msg = messagebox.askquestion('',"Do you want to add this person?")
                  if msg == 'yes':
                     conn = connection()
                     cursor = conn.cursor()
                     cursor.execute(
                        "INSERT INTO personal VALUES ('""','"+sname+"','"+fname+"','"+mname+"','"+dob+"','"+pob+"','"+sex+"','"+civil+"','"+hei+"','"+wei+"','"+blood+"','"+ctiz+"','"+ifdu+"','"+count+"','"+email+"','"+posi+"','"+stat+"','"+dept+"') ")
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
                     indicate(record)
                  elif msg == 'no':
                     messagebox.showinfo('Return', 'You will now return to the application screen')
                     indicate(record)
                  else:
                     messagebox.showinfo('Return', 'You will now return to the application screen')
               except:
                  
                  messagebox.showinfo("Error", "Inventory already exist")
                  return
         
         
         refreshTable()


      back = customtkinter.CTkButton(sf, text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#d4d4d4', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(record))
      back.place(x=1000, y=1900)

      addto = customtkinter.CTkButton(sf,text="Attach",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#d4d4d4', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=add)
      addto.place(x=1200, y=1900)

   #-------------------------------------------------------------------------------------------------------------------------------------#
   #-------------------------------------------------------PERSONAL INFO-----------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#

      titleabel = Label(sf, text="PERSONAL DATA SHEET", font=('Arial', 22, 'bold'),bg="#d4d4d4")
      titleabel.place(x=690, y=10, anchor= N)

      sublabel = Label(sf, text="PERSONAL INFORMATION ", font=('Arial', 18, 'bold'),bg="#d4d4d4")
      sublabel.place(x=30, y=50)

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


      fblabel = Label(sf, text="FAMILY BACKGROUND", font=('Courier', 18, 'bold'),bg="#d4d4d4").place(x=30, y=1000)

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


      
      eblabel = Label(sf, text="EDUCATIONAL BACKGROUND", font=('Arial', 17, 'bold'),bg="#d4d4d4")
      eblabel.place(x=30, y=1400)

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

      polabel = Label(sf, text="POSITION : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=40, y=1800)
      poEntry = customtkinter.CTkEntry(sf, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 16,),text_color='black')
      poEntry.place(x=160, y=1800)

      stlabel = Label(sf, text="STATUS: ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=520, y=1800)
      stEntry = customtkinter.CTkEntry(sf, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
      stEntry.place(x=610, y=1800)


      deabel = Label(sf, text="DEPARTMENT : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=980, y=1800)
      deEntry = customtkinter.CTkEntry(sf, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black')
      deEntry.place(x=1120, y=1800)


   #-------------------------------------------------------------------------------------------------------------------------------------#
   #-------------------------------------------showing data------------------------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#
      
   def show_e():

      f2_2 = customtkinter.CTkFrame(f2, width=1500, height=820, fg_color ="transparent")
      f2_2.place(x=0, y=0)
      f2_2.pack_propagate(0)
      cv2 = Canvas(f2_2,background='#ffffff',highlightthickness=0)
      cv2.pack(side =LEFT,fill=BOTH, expand=1)
      sb2= customtkinter.CTkScrollbar(f2_2, orientation= VERTICAL, border_spacing = 3,fg_color = 'white', command=cv2.yview)
      sb2.pack(side=RIGHT, fill=Y)
      cv2.configure(yscrollcommand=sb2.set)
      cv2.bind('<Configure>', lambda e:cv2.configure(scrollregion = cv2.bbox('all')))

      sf2 = customtkinter.CTkFrame(cv2, width=1500, height=2000 ,fg_color ="transparent")
      cv2.create_window((0,0), window=sf2, anchor="nw")

      def mousewheel(event):
         cv2.yview_scroll(-1*(event.delta/500), "units")

      cv2.bind("<MouseWheel>",mousewheel)

      photo = PIL.Image.open("Assets\\Picture1.png")
      nphoto = customtkinter.CTkImage(photo,size=(1485,1860))
      j = customtkinter.CTkLabel(sf2,text="", image=nphoto)
      j.place(x=0, y=0)




      def select():
         indicate(modify_e)

         

      back2 = customtkinter.CTkButton(sf2,text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#ffffff', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(record))
      back2.place(x=1000, y=1900)

      modb = customtkinter.CTkButton(sf2,text="Modify",fg_color='#467c9c',font=('Arial', 20,) ,bg_color= '#ffffff', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=select)
      modb.place(x=1200, y=1900)


   #-------------------------------------------------------------------------------------------------------------------------------------#
   #-------------------------------------------------------PERSONAL INFO-----------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#

      snshow = Label(sf2, text="", font=('Courier', 16, 'bold'),bg="#ffffff", textvariable=p_sname).place(x=300, y=220)

      fnshow = Label(sf2, text="", font=('Courier', 16, 'bold'),bg="#ffffff", textvariable=p_fname).place(x=300, y=260)

      mnshow = Label(sf2, text = "", font=('Courier',16,'bold'),bg="#ffffff",textvariable=p_mname).place(x=300,y=300)

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
   
   #-------------------------------------------------------------------------------------------------------------------------------------#
   #-------------------------------------------updating data------------------------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#

      
   def modify_e():



      f2_3 = customtkinter.CTkFrame(f2, width=1500, height=820, fg_color ="#d4d4d4")
      f2_3.place(x=0, y=0)
      f2_3.pack_propagate(0)
      cv3= Canvas(f2_3,background='#d4d4d4',highlightthickness=0,)
      cv3.pack(side =LEFT,fill=BOTH, expand=1)
      sb3 = customtkinter.CTkScrollbar(f2_3, orientation= VERTICAL, border_spacing = 3,fg_color = '#d4d4d4', command=cv3.yview)
      sb3.pack(side=RIGHT, fill=Y)
      cv3.configure(yscrollcommand=sb3.set)
      cv3.bind('<Configure>', lambda e:cv3.configure(scrollregion = cv3.bbox('all')))

      sf3 = customtkinter.CTkFrame(cv3, width=1500, height=2000 ,fg_color ="#d4d4d4")
      cv3.create_window((0,0), window=sf3, anchor="nw")

      def validate2(u_input): 
         return u_input.isdigit()
      my_valid2 = sf3.register(validate2)


      def mousewheel(event):
         cv3.yview_scroll(-1*(event.delta/500), "units")

      cv3.bind("<MouseWheel>",mousewheel)

      idd = Label(textvariable=ids)
      
      conn = connection()
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM personal WHERE id= %s",(idd.cget("text")))
      result = cursor.fetchone()
  
      
      def update():

         idd = Label(textvariable=ids)
         ide = str(idd.cget("text"))
      
      
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
         posi = str(poEntry.get())
         stat = str(stEntry.get())
         dept = str(deEntry.get()) 

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

         if (sname == "" or sname == " ") or (fname == "" or  fname == " ") or (mname == "" or mname == " ") or (pob == "" or pob == " ") or (sex == None or sex == "None") or (civil == "" or civil == " ") or (hei == "" or hei == " ") or (blood == "" or blood == " ") or (posi == "" or posi == " ") or (stat == "" or stat == " ") or (agem == "" or agem == " ") or (ctiz == None or ctiz == "None") or (dept == "" or dept == " "):
               messagebox.showinfo("Error", "Please fill up the blank entry")
               return
         else:
               try:
                  msg = messagebox.askquestion('',"Do you want to Update this Information?")
                  if msg == 'yes':
                     conn = connection()
                     cursor = conn.cursor()
                     cursor.execute("UPDATE personal SET surname = '"+sname+"', firstname = '"+fname+"', middlename = '"+mname+"', DOB = '"+dob+"', POB = '"+pob+"' , sex = '"+sex+"', civil = '"+civil+"', height = '"+hei+"', weight = '"+wei+"', bloodtype = '"+blood+"', citizenship = '"+ctiz+"', ifDC = '"+ifdu+"', country = '"+count+"', email = '"+email+"', position = '"+posi+"', status = '"+stat+"', department = '"+dept+"' WHERE id='"+ide+"'")
                     cursor.execute("UPDATE numbers SET gsis = '"+gsis+"', pagibig = '"+pagi+"', philhealth = '"+phil+"', sss = '"+sss+"', tin = '"+tin+"', agency = '"+agem+"', telephone = '"+tele+"', cellphone = '"+cell+"' WHERE id='"+ide+"' ")
                     cursor.execute("UPDATE residential SET houseblock = '"+res1+"', street = '"+res2+"', subd  = '"+res3+"', brgy = '"+res4+"', city = '"+res5+"', province = '"+res6+"', zip = '"+res7+"' WHERE id='"+ide+"' ")
                     cursor.execute("UPDATE permanent SET houseblock = '"+per1+"', street = '"+per2+"', subd  = '"+per3+"', brgy = '"+per4+"', city = '"+per5+"', province = '"+per6+"', zip = '"+per7+"' WHERE id='"+ide+"'")
                     cursor.execute("UPDATE spouse SET surname = '"+sposn+"', firstname = '"+spofn+"', middlename  = '"+spomn+"', occupation = '"+spooc+"', businessname = '"+spoebn+"', businessadd = '"+spoba+"', telephone = '"+spotel+"' WHERE id='"+ide+"' ")
                     cursor.execute("UPDATE family SET fathersn = '"+fsn+"', fatherfn = '"+ffn+"', fathermn  = '"+fmn+"', mothermn = '"+mmn+"', mothersn = '"+msn+"', motherfn = '"+mfn+"', mothermmn = '"+mmd+"' WHERE id='"+ide+"' ")
                     cursor.execute("UPDATE elementary SET school = '"+ens+"', degree = '"+ebdc+"', froms  = '"+efrom+"', tos = '"+eto+"', units = '"+ehigh+"', graduated = '"+eyg+"', acads = '"+esa+"' WHERE id='"+ide+"'")
                     cursor.execute("UPDATE highschool SET school = '"+hsns+"', degree = '"+hsbdc+"', froms  = '"+hsfrom+"', tos = '"+hsto+"', units = '"+hshigh+"', graduated = '"+hsyg+"', acads = '"+hssa+"'WHERE id='"+ide+"'  ")
                     cursor.execute("UPDATE vocational SET school = '"+vtns+"', degree = '"+vtbdc+"', froms  = '"+vtfrom+"', tos = '"+vtto+"', units = '"+vthigh+"', graduated = '"+vtyg+"', acads = '"+vtsa+"' WHERE id='"+ide+"' ")
                     cursor.execute("UPDATE college SET school = '"+cns+"', degree = '"+cbdc+"', froms  = '"+cfrom+"', tos = '"+cto+"', units = '"+chigh+"', graduated = '"+cyg+"', acads = '"+csa+"' WHERE id='"+ide+"' ")
                     cursor.execute("UPDATE graduate SET school = '"+gns+"', degree = '"+gbdc+"', froms  = '"+gfrom+"', tos = '"+gto+"', units = '"+ghigh+"', graduated = '"+gyg+"', acads = '"+gsa+"' WHERE id='"+ide+"' ")
                     conn.commit()
                     conn.close()
                     for entry in (sn,fnEntry,mnEntry,pobEntry,htEntry,wtEntry,gsEntry,pagEntry,phEntry,tiEntry,aeEntry,tEntry,cEntry,couEntry,raEntry,ra2Entry,ra3Entry,ra4Entry,ra5Entry,ra6Entry,ra7Entry,pa1Entry,pa2Entry,pa3Entry,pa4Entry,pa5Entry,pa6Entry,pa7Entry,eEntry,spoEntry,fspoEntry,mspoEntry,ocEntry,ebmEntry,baEntry,teleEntry,fsnEntry,ffnEntry,fmnEntry,mmnEntry,msnEntry,mfnEntry,mEntry,ensEntry,bdcEntry,froEntry,toEntry,hiEntry,ygEntry,saEntry,hsnsEntry,hsbdcEntry,hsfroEntry,hstoEntry,hshiEntry,hsygEntry,hssaEntry,vtnsEntry,vtbdcEntry,vtfroEntry,vttoEntry,vthiEntry,vtygEntry,vtsaEntry,cnsEntry,cbdcEntry,cfroEntry,ctoEntry,chiEntry,cygEntry,csaEntry,gsnsEntry,gsbdcEntry,gsfroEntry,gstoEntry,gshiEntry,gsygEntry,gssaEntry):
                        entry.delete(0,'end')
                     sexx.set(None)
                     civ.set(None)
                     ctz.set(None)
                     opt2.set(None)
                     indicate(record)
                     
                  elif msg == 'no':
                     pass
                  else:
                     messagebox.showinfo('Return', 'You will now return to the application screen')
               except:
                  messagebox.showinfo("Error", "Inventory already exist")
                  return

         refreshTable()
      
      back3 = customtkinter.CTkButton(sf3,text="Back",fg_color='#469c91',font=('Arial', 20,) ,bg_color= '#d4d4d4', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=lambda: indicate(show_e))
      back3.place(x=1000, y=1900)

      uptd = customtkinter.CTkButton(sf3,text="Update",fg_color='#9c7846',font=('Arial', 20,) ,bg_color= '#d4d4d4', width=160, height=60, border_width=0, corner_radius=10,
      hover_color = '#2a4859',cursor='hand2',command=update)
      uptd.place(x=1200, y=1900)


      titleabel = Label(sf3, text="PERSONAL DATA SHEET", font=('Arial', 22, 'bold'),bg="#d4d4d4")
      titleabel.place(x=690, y=10, anchor= N)

      sublabel = Label(sf3, text="PERSONAL INFORMATION ", font=('Arial', 18, 'bold'),bg="#d4d4d4")
      sublabel.place(x=30, y=50)

      snlabel = Label(sf3, text="1.SURNAME :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=100)
      sn = customtkinter.CTkEntry(sf3, height= 35,width=450, fg_color='white',border_width = 2, corner_radius= 10,placeholder_text = "Name extension (Jr.,Sr.)",font=('Arial', 22),placeholder_text_color= "gray",text_color='black',textvariable=p_sname)
      sn.place(x=280, y=100)

      fnlabel = Label(sf3, text="  FIRSTNAME :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=150)
      fnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 22),text_color='black',textvariable=p_fname)
      fnEntry.place(x=280, y=150)

      mnlabel = Label(sf3, text="  MIDDLENAME :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=200)
      mnEntry = customtkinter.CTkEntry(sf3,  height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_mname)
      mnEntry.place(x=280, y=200)

      doblabel = Label(sf3, text="2.DATE OF BIRTH :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=252)
      dobentry = DateEntry(sf3, height= 35, width=15, font = ('arial', 22),date_pattern='mm/dd/y', background='gray', foreground='white', borderwidth=2, weekendbackground ="red",bd = 0)
      dobentry.set_date(result[4])
      dobentry.place(x=280, y= 250)

      poblabel = Label(sf3, text="3.PLACE OF BIRTH :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=302)
      pobEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pob)
      pobEntry.place(x=280, y=300)

      sexlabel = Label(sf3, text="4.SEX : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=350)
      sexx = tk.StringVar()
      stat1 = customtkinter.CTkRadioButton(sf3, text="Male", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='male',bg_color ="#d4d4d4",variable=sexx, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black').place(x=280,y= 350)
      stat2 = customtkinter.CTkRadioButton(sf3, text="Female",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='female',bg_color ="#d4d4d4",variable=sexx, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black').place(x=380,y= 350)
      sexx.set(result[6])

      statuslabel = Label(sf3, text="5.CIVIL STATUS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=400)
      civ = tk.StringVar()
      st = customtkinter.CTkOptionMenu(sf3,height= 35, width = 300,fg_color='#868786',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color='white',dropdown_text_color = 'black',dropdown_hover_color = 'green',button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black",variable = civ, values=["Single", "Married", "Widowed", "Seperated", "Other/s"])
      st.place(x=280, y= 400)
      st.set(result[7])

      hlabel = Label(sf3, text="6.HEIGHT (cm) :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=450)
      htEntry = customtkinter.CTkEntry(sf3,height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid2,'%S'),text_color='black',textvariable=p_height)
      htEntry.place(x=280, y=450)

      wtlabel = Label(sf3, text="7.WEIGHT (kg) :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=500)
      wtEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid2,'%S'),text_color='black',textvariable=p_weight)
      wtEntry.place(x=280, y=500)

      btlabel = Label(sf3, text="8.BLOOD TYPE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=550)
      blo = tk.StringVar()
      bt = customtkinter.CTkOptionMenu(sf3,height= 35, width = 300,fg_color='#868786',font=('Arial', 22),dropdown_font = ('Courier', 16),dropdown_fg_color ='white',dropdown_text_color = 'black',dropdown_hover_color = 'green', button_color = '#a2a3a2',button_hover_color = 'gray',text_color = "black", variable = blo, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
      bt.place(x=280, y= 550)
      bt.set(result[10])

      gslabel = Label(sf3, text="9.GSIS ID NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=600)
      gsEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid2,'%S'),text_color='black',textvariable=n_gsis)
      gsEntry.place(x=280, y=600)

      paglabel = Label(sf3, text="10.PAG-IBIG ID NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=650)
      pagEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid2,'%S'),text_color='black',textvariable=n_pag)
      pagEntry.place(x=280, y=650)

      phlabel = Label(sf3, text="11.PHILHEALTH NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=700)
      phEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=n_phil)
      phEntry.place(x=280, y=700)

      sslabel = Label(sf3, text="12.SSS NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=750)
      ssEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=n_sss)
      ssEntry.place(x=280, y=750)

      tilabel = Label(sf3, text="13.TIN NO. :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=800)
      tiEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=n_tin)
      tiEntry.place(x=280, y=800)

      aelabel = Label(sf3, text="14.AGENCY EMPLOYEE NO.:", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=850)
      aeEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=n_ae)
      aeEntry.place(x=280, y=850)

      tlabel = Label(sf3, text="15.TELEPHONE NO. : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=900)
      tEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=n_tel)
      tEntry.place(x=280, y=900)

      clabel = Label(sf3, text="16.CELLPHONE NO. : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=20, y=950)
      cEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=n_cel)
      cEntry.place(x=280, y=950)



      def fr():
         optlabel.place_forget()
         ct5.place_forget()
         ct6.place_forget()
         coulabel.place_forget()
         couEntry.place_forget()
         opt2.set(None)
         couEntry.delete(0,'end')

      def gt():
         optlabel.place_configure(x=900, y=300)
         ct5.place_configure(x=1050,y= 350)
         ct6.place_configure(x=1190,y= 350)
         coulabel.place_configure(x=850, y=397)
         couEntry.place_configure(x=1025, y=395)
         

      ctlabel = Label(sf3, text="17.CITIZENSHIP :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=250)
      ctz = tk.StringVar()
      ct3 = customtkinter.CTkRadioButton(sf3, text="Filipino", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='Filipino',bg_color ="#d4d4d4",variable=ctz, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black',command=fr).place(x=990,y= 250)
      ct4 = customtkinter.CTkRadioButton(sf3, text="Dual Citizenship",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='Dual Citizenship',bg_color ="#d4d4d4",variable=ctz, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black',command=gt).place(x=1130,y= 250)
      ctz.set(result[11])

      optlabel = Label(sf3, text="if Dual Citizenship:", font=('Courier', 15, 'bold'),bg="#d4d4d4")
      optlabel.place(x=900, y=300)
      opt2 = tk.StringVar()
      ct5 = customtkinter.CTkRadioButton(sf3, text="By Birth", radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='By Birth',bg_color ="#d4d4d4",variable=opt2, cursor='hand2', font=('Courier', 16, 'bold'),text_color='black')
      ct5.place(x=1050,y= 350)
      ct6 = customtkinter.CTkRadioButton(sf3, text="By Naturalization",radiobutton_height= 30, radiobutton_width= 30, border_width_checked = 10, border_width_unchecked= 5, value='By Naturalization',bg_color ="#d4d4d4",variable=opt2, cursor='hand2',font=('Courier', 16, 'bold'),text_color='black')
      ct6.place(x=1190,y= 350)
      opt2.set(result[12])

      coulabel = Label(sf3, text="your Country :", font=('Courier', 14, 'bold'),bg="#d4d4d4")
      coulabel.place(x=850, y=397)
      couEntry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_coun)
      couEntry.place(x=1025, y=395)


      ralabel = Label(sf3, text="18.RESIDENTIAL ADDRESS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=450)
      ra1label = Label(sf3, text="HouseBlock/Lot No.", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=510)
      raEntry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=r_ra1)
      raEntry.place(x=900, y=480)

      ra2label = Label(sf3, text="Street", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1270, y=510)
      ra2Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=r_ra2)
      ra2Entry.place(x=1180, y=480)

      ra3label = Label(sf3, text="Subdivision/Village", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=925, y=570)
      ra3Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=r_ra3)
      ra3Entry.place(x=900, y=540)

      ra4label = Label(sf3, text="Barangay", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=570)
      ra4Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=r_ra4)
      ra4Entry.place(x=1180, y=540)

      ra5label = Label(sf3, text="City/Municipality", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=630)
      ra5Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=r_ra5)
      ra5Entry.place(x=900, y=600)

      ra6label = Label(sf3, text="Province", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=630)
      ra6Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=r_ra6)
      ra6Entry.place(x=1180, y=600)

      ra7label = Label(sf3, text="ZIP CODE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=785, y=665)
      ra7Entry = customtkinter.CTkEntry(sf3,height= 35, width=125, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=r_ra7)
      ra7Entry.place(x=900, y=660)

      palabel = Label(sf3, text="19.PERMANENT ADDRESS :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=750, y=700)
      pa1label = Label(sf3, text="HouseBlock/Lot No.", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=760)
      pa1Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pa1)
      pa1Entry.place(x=900, y=730)

      pa2label = Label(sf3, text="Street", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1270, y=760)
      pa2Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pa2)
      pa2Entry.place(x=1180, y=730)

      pa3label = Label(sf3, text="Subdivision/Village", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=925, y=820)
      pa3Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pa3)
      pa3Entry.place(x=900, y=790)

      pa4label = Label(sf3, text="Barangay", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=820)
      pa4Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pa4)
      pa4Entry.place(x=1180, y=790)

      pa5label = Label(sf3, text="City/Municipality", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=930, y=880)
      pa5Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pa5)
      pa5Entry.place(x=900, y=850)

      pa6label = Label(sf3, text="Province", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=1260, y=880)
      pa6Entry = customtkinter.CTkEntry(sf3,height= 35, width=250, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_pa6)
      pa6Entry.place(x=1180, y=850)

      pa7label = Label(sf3, text="ZIP CODE :", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=785, y=915)
      pa7Entry = customtkinter.CTkEntry(sf3,height= 35, width=125, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=p_pa7)
      pa7Entry.place(x=900, y=910)

      elabel = Label(sf3, text="20.EMAIL ADDRESS: ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=753, y=950)
      eEntry = customtkinter.CTkEntry(sf3,height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_email)
      eEntry.place(x=950, y=950)


   #-------------------------------------------------------------------------------------------------------------------------------------#
   #----------------------------------------------------------FAMILY BG------------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#


      fblabel = Label(sf3, text="FAMILY BACKGROUND", font=('Courier', 18, 'bold'),bg="#d4d4d4").place(x=30, y=1000)

      spolabel = Label(sf3, text="21.SPOUSE'S SURNAME: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1052)
      spoEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=s_sname)
      spoEntry.place(x=230, y=1050)

      fspolabel = Label(sf3, text="   FIRST NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1100)
      fspoEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=s_fname)
      fspoEntry.place(x=230, y=1100)

      mspolabel = Label(sf3, text="   MIIDDLE NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1150)
      mspoEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=s_mname)
      mspoEntry.place(x=230, y=1150)

      oclabel = Label(sf3, text="   OCCUPATION : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1200)
      ocEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=s_occup)
      ocEntry.place(x=230, y=1200)

      ebmlabel = Label(sf3, text="EMPLOYEE/\nBUSINESS NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4",justify= LEFT).place(x=48, y=1250)
      ebmEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=s_ebn)
      ebmEntry.place(x=230, y=1250)

      balabel = Label(sf3, text="   BUSINESS ADDRESS: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1305)
      baEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=s_ba)
      baEntry.place(x=230, y=1300)

      telelabel = Label(sf3, text="   TELEPHONE NO. : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=20, y=1350)
      teleEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=s_tele)
      teleEntry.place(x=230, y=1350)

      fsnlabel = Label(sf3, text="22.FATHER'S SURNAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1052)
      fsnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_fsn)
      fsnEntry.place(x=950, y=1050)

      ffnlabel = Label(sf3, text="   FIRST NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1100)
      ffnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_ffn)
      ffnEntry.place(x=950, y=1100)

      fmnlabel = Label(sf3, text="   MIIDDLE NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1150)
      fmnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_fmn)
      fmnEntry.place(x=950, y=1150)

      mmnlabel = Label(sf3, text="23.MOTHER'S MAIDEN NAME: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1200)
      mmnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_mmn)
      mmnEntry.place(x=950, y=1200)

      msnlabel = Label(sf3, text="   SURNAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1250)
      msnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_msn)
      msnEntry.place(x=950, y=1250)

      mfnlabel = Label(sf3, text="   FIRST NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1300)
      mfnEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_mfn)
      mfnEntry.place(x=950, y=1300)

      mlabel = Label(sf3, text="   MIDDLE NAME : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=700, y=1350)
      mEntry = customtkinter.CTkEntry(sf3, height= 35, width=450, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=f_mn)
      mEntry.place(x=950, y=1350)

      

   #-------------------------------------------------------------------------------------------------------------------------------------#
   #-----------------------------------------------------EDUC BACKGROUND-----------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#


      
      eblabel = Label(sf3, text="EDUCATIONAL BACKGROUND", font=('Arial', 17, 'bold'),bg="#d4d4d4")
      eblabel.place(x=30, y=1400)

      lvllabel = Label(sf3, text="Level", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=50, y=1450)
      NOSlabel = Label(sf3, text="Name of School", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=310, y=1450)
      BEDClabel = Label(sf3, text="Basic Education/Degree/Course", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=620, y=1450)
      POAlabel = Label(sf3, text="Period of Attendance", font=('Courier', 10, 'bold'),bg="#d4d4d4").place(x=935, y=1450)
      frotolabel = Label(sf3, text="From      To", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=947, y=1475)
      hillabel = Label(sf3, text="Highest Level/\nUnits Earned\n(if not graduated)",justify= CENTER, font=('Courier', 9, 'bold'),bg="#d4d4d4").place(x=1105 , y=1445)
      YGGlabel = Label(sf3, text="Year\nGraduated", font=('Courier', 11, 'bold'),bg="#d4d4d4").place(x=1245, y=1450)
      SAlabel = Label(sf3, text="Scholarship/\nAcademic Honors\nReceived", font=('Courier', 10, 'bold'),bg="#d4d4d4").place(x=1345, y=1445)


      elabel = Label(sf3, text="ELEMENTARY : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1500)
      ensEntry = customtkinter.CTkEntry(sf3,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=e_school)
      ensEntry.place(x=200, y=1500)

      bdcEntry = customtkinter.CTkEntry(sf3,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=e_bdc)
      bdcEntry.place(x=620, y=1500)

      froEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=e_fro)
      froEntry.place(x=940, y=1500)

      toEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=e_to)
      toEntry.place(x=1030, y=1500)

      hiEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=e_hig)
      hiEntry.place(x=1120, y=1500)

      ygEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=e_yg)
      ygEntry.place(x=1240, y=1500)

      saEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=e_sa)
      saEntry.place(x=1360, y=1500)


      hslabel = Label(sf3, text="HIGHSCHOOL : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1550)
      hsnsEntry = customtkinter.CTkEntry(sf3,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=h_school)
      hsnsEntry.place(x=200, y=1550)

      hsbdcEntry = customtkinter.CTkEntry(sf3,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=h_bdc)
      hsbdcEntry.place(x=620, y=1550)

      hsfroEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=h_fro)
      hsfroEntry.place(x=940, y=1550)

      hstoEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=h_to)
      hstoEntry.place(x=1030, y=1550)

      hshiEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=h_hig)
      hshiEntry.place(x=1120, y=1550)

      hsygEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=h_yg)
      hsygEntry.place(x=1240, y=1550)

      hssaEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=h_sa)
      hssaEntry.place(x=1360, y=1550)


      vtlabel = Label(sf3, text="VOCATIONAL/\nTRADE COURSE : ",justify = LEFT, font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1600)
      vtnsEntry = customtkinter.CTkEntry(sf3,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=v_school)
      vtnsEntry.place(x=200, y=1600)

      vtbdcEntry = customtkinter.CTkEntry(sf3,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=v_bdc)
      vtbdcEntry.place(x=620, y=1600)

      vtfroEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=v_fro)
      vtfroEntry.place(x=940, y=1600)

      vttoEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=v_to)
      vttoEntry.place(x=1030, y=1600)

      vthiEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=v_hig)
      vthiEntry.place(x=1120, y=1600)

      vtygEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=v_yg)
      vtygEntry.place(x=1240, y=1600)

      vtsaEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=v_sa)
      vtsaEntry.place(x=1360, y=1600)


      clabel = Label(sf3, text="COLLEGE : ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1650)
      cnsEntry = customtkinter.CTkEntry(sf3,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=c_school)
      cnsEntry.place(x=200, y=1650)

      cbdcEntry = customtkinter.CTkEntry(sf3,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=c_bdc)
      cbdcEntry.place(x=620, y=1650)

      cfroEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=c_fro)
      cfroEntry.place(x=940, y=1650)

      ctoEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=c_to)
      ctoEntry.place(x=1030, y=1650)

      chiEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=c_hig)
      chiEntry.place(x=1120, y=1650)

      cygEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=c_yg)
      cygEntry.place(x=1240, y=1650)

      csaEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=c_sa)
      csaEntry.place(x=1360, y=1650)

      gslabel = Label(sf3, text="GRADUATE STUDIES: ", font=('Courier', 12, 'bold'),bg="#d4d4d4").place(x=25, y=1700)
      gsnsEntry = customtkinter.CTkEntry(sf3,  height= 35, width=400, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=g_school)
      gsnsEntry.place(x=200, y=1700)

      gsbdcEntry = customtkinter.CTkEntry(sf3,  height= 35, width=300, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=g_bdc)
      gsbdcEntry.place(x=620, y=1700)

      gsfroEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=g_fro)
      gsfroEntry.place(x=940, y=1700)

      gstoEntry = customtkinter.CTkEntry(sf3,  height= 35, width=70, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=g_to)
      gstoEntry.place(x=1030, y=1700)

      gshiEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),text_color='black',textvariable=g_hig)
      gshiEntry.place(x=1120, y=1700)

      gsygEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=g_yg)
      gsygEntry.place(x=1240, y=1700)

      gssaEntry = customtkinter.CTkEntry(sf3,  height= 35, width=100, fg_color='white',border_width = 2, corner_radius= 10, font=('Arial', 16,),validate='key',validatecommand=(my_valid,'%S'),text_color='black',textvariable=g_sa)
      gssaEntry.place(x=1360, y=1700)


      roelabel = Label(sf3, text="EMPLOYEE DETAILS", font=('Arial', 17, 'bold'),bg="#d4d4d4")
      roelabel.place(x=30, y=1750)

      polabel = Label(sf3, text="POSITION : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=40, y=1800)
      poEntry = customtkinter.CTkEntry(sf3, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 16,),text_color='black',textvariable=p_pos)
      poEntry.place(x=160, y=1800)

      stlabel = Label(sf3, text="STATUS: ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=520, y=1800)
      stEntry = customtkinter.CTkEntry(sf3, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_stat)
      stEntry.place(x=610, y=1800)


      deabel = Label(sf3, text="DEPARTMENT : ", font=('Courier', 14, 'bold'),bg="#d4d4d4").place(x=980, y=1800)
      deEntry = customtkinter.CTkEntry(sf3, height= 35, width=350, fg_color='white',border_width = 2, corner_radius= 10,font=('Arial', 22),text_color='black',textvariable=p_dept)
      deEntry.place(x=1120, y=1800)



      


   #-------------------------------------------------------------------------------------------------------------------------------------#
   #---------------------------------------------------------function--------------------------------------------------------------------#
   #-------------------------------------------------------------------------------------------------------------------------------------#

   

      
   def delete():
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
               cursor.execute("DELETE FROM personal WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM numbers WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM residential WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM permanent WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM spouse WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM family WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM elementary WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM highschool WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM vocational WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM college WHERE id ='"+str(deleteData)+"'")
               cursor.execute("DELETE FROM graduate WHERE id ='"+str(deleteData)+"'")
               conn.commit()
               conn.close()
         except:
               messagebox.showinfo("Error", "Sorry an error occured")
               return


      refreshTable()

   def read2():
      conn = connection()
      cursor = conn.cursor()
      cursor.execute("SELECT id, firstname, surname, position, department FROM personal WHERE surname like %s",(findEntry.get()))
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

   search = customtkinter.CTkButton(f2,text="Search",fg_color='#469c8e',font=('Arial', 20,) ,bg_color= '#8aafd4', width=100, height=40, border_width=0, corner_radius=10,
   hover_color = '#2a4859',cursor='hand2',command=searching)
   search.place(x=350, y=27)

   refr = PIL.Image.open("Assets\\refresh.png")
   ref = customtkinter.CTkImage(refr,size=(30,30))

   search2 = customtkinter.CTkButton(f2,text="",image = ref, bg_color= '#8aafd4',fg_color="#8aafd4",hover_color= "#8aafd4", width= 20,cursor='hand2',command=refresh)
   search2.place(x=450, y=27)





   my_tree = ttk.Treeview(f2, show="headings", height=11)
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
   f2.bind('<Return>', refresh)
   
   populate()
   refreshTable()

   
def leave():
   f4 = customtkinter.CTkFrame(None, width=1500, height=820, fg_color ="#8a9dd4")
   f4.place(x=380, y=200)
   ln = Label(f4, text="Total Employees", font=('Arial', 20), background="#86babd")
   ln.place(x=50, y=10)
    

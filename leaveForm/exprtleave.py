from tkinter import *
from database.db import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import PIL.Image
from time import strftime
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import io
from tkinter import filedialog
from PIL import ImageGrab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4

    

def saveasfile(s_ide):

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leaves WHERE ide=%s",(s_ide))
    result = cursor.fetchone()
    conn.commit()
    conn.close()

    ids = result[1]

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal WHERE id=%s",(ids))
    results = cursor.fetchone()

    dtr=datetime.strftime(result[2],'%b %d, %Y')
    fro=datetime.strftime(result[6],'%b/%d/%Y')
    too=datetime.strftime(result[7],'%b/%d/%Y')


    file = filedialog.asksaveasfilename(filetypes = [("PDF file",'*.pdf')],defaultextension='.pdf',title= "Save a PDF file",initialfile="default.pdf",initialdir='C:\\Users\\ferna\\Downloads')
    c = canvas.Canvas(file,pagesize= letter)
    c.translate(inch,inch)

    
    
    c.drawCentredString(3.18*inch, 9.33*inch,'Roxas Memorial Provincial Hospital',c.setFont("Helvetica-Bold", 20))
    c.drawCentredString(3.18*inch, 9.10*inch,'Arnaldo Boulevard, Roxas City, Capiz',c.setFont("Helvetica", 13))
    c.drawCentredString(3.18*inch, 8.80*inch,'Application for Leave',c.setFont("Helvetica", 16))
    c.drawCentredString(3.18*inch, 8.60*inch,'C.Y - 2022',c.setFont("Helvetica", 12))
    c.drawImage("Assets\\logo.png",-0.2*inch, 8.85*inch,height=60,width=60)
    c.drawImage("Assets\\capizlogo.png",5.75*inch, 8.75*inch,height=70,width=70)


    c.drawCentredString(3.18*inch, 8.25*inch,result[3] + " " + result[4],c.setFont("Helvetica-Bold", 17))
    c.drawCentredString(3.18*inch, 8*inch,results[15],c.setFont("Helvetica", 14))

    c.drawString(-0.7*inch, 7.70*inch,"Date Filed - " + dtr,c.setFontSize(size=12))


    c.drawString(-0.5*inch, 7.30*inch,"Type of Leave: ",c.setFont("Helvetica-Bold", 14))
    c.drawString(0.2*inch, 7*inch,result[5],c.setFont("Helvetica", 14))

    c.drawString(3.5*inch, 7.30*inch,"Number of Working days applied for: ",c.setFont("Helvetica-Bold", 12))
    c.drawString(3.9*inch, 7*inch,"From: "+ fro  ,c.setFont("Helvetica", 12))
    c.drawString(3.9*inch, 6.75*inch,"To: " + too ,c.setFont("Helvetica", 12))
    c.drawString(5.8*inch, 6.85*inch,str(result[8]) + " Days",c.setFont("Helvetica-Bold", 12))
    

    c.drawString(-0.5*inch, 6.50*inch,"Commutation: ",c.setFont("Helvetica-Bold", 14))
    c.drawString(0.2*inch, 6.20*inch,result[9],c.setFont("Helvetica", 14))

    c.drawString(3.5*inch, 6.50*inch,"Recommendation: ",c.setFont("Helvetica-Bold", 14))
    c.drawString(3.9*inch, 6.20*inch,result[10],c.setFont("Helvetica", 14))


    c.drawString(-0.5*inch, 5.40*inch,"In case of Vacation/Special Privilege Leave: ",c.setFont("Helvetica-Bold", 12))
    c.drawString(0.2*inch, 5.10*inch,result[11],c.setFont("Helvetica", 14))

    c.drawString(-0.5*inch, 4.60*inch,"In Case Attended a Seminar:",c.setFont("Helvetica-Bold", 12))
    c.drawString(0.2*inch, 4.30*inch,result[15],c.setFont("Helvetica", 14))

    c.drawString(-0.5*inch, 3.80*inch,"In case of Sick Leave: ",c.setFont("Helvetica-Bold", 12))
    c.drawString(0.2*inch, 3.50*inch,result[12],c.setFont("Helvetica", 14))

    c.drawString(-0.2*inch, 3.20*inch,"If Sick leave, Passed a Medical Certificate:",c.setFont("Helvetica-Bold", 12))
    c.drawString(0.6*inch, 2.90*inch,result[13],c.setFont("Helvetica", 14))



    c.drawString(3.5*inch, 5.40*inch,"In case of Special Leave Benefits for Women: ",c.setFont("Helvetica-Bold", 12))
    c.drawString(3.9*inch, 5.10*inch,result[14],c.setFont("Helvetica", 14))

    c.drawString(3.5*inch, 4.60*inch,"In case of Study Leave: ",c.setFont("Helvetica-Bold", 12))
    c.drawString(3.9*inch, 4.30*inch,result[16],c.setFont("Helvetica", 14))

    c.drawString(3.5*inch, 3.80*inch,"Other purposes: ",c.setFont("Helvetica-Bold", 12))
    c.drawString(3.9*inch, 3.50*inch,result[17],c.setFont("Helvetica", 14))



    c.drawString(-0.5*inch, 0.5*inch,"Employee's Signature",c.setFont("Helvetica", 12))

    c.drawString(5*inch, 0.5*inch,"Dept.Head Signature",c.setFont("Helvetica", 12))


    


    
    
    

    c.showPage()
    c.save()
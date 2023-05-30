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
    cursor.execute("SELECT * FROM perform WHERE ide=%s",(s_ide))
    result = cursor.fetchone()
    
    conn.commit()
    conn.close()

    ids = result[1]

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal WHERE id=%s",(ids))
    results = cursor.fetchone()


    file = filedialog.asksaveasfilename(filetypes = [("PDF file",'*.pdf')],defaultextension='.pdf',title= "Save a PDF file",initialfile="default.pdf",initialdir='C:\\Users\\ferna\\Downloads')
    c = canvas.Canvas(file,pagesize= letter)
    c.translate(inch,inch)

    
    
    c.drawCentredString(3.18*inch, 9.33*inch,'Roxas Memorial Provincial Hospital',c.setFont("Helvetica-Bold", 20))
    c.drawCentredString(3.18*inch, 9.10*inch,'Arnaldo Boulevard, Roxas City, Capiz',c.setFont("Helvetica", 13))
    c.drawCentredString(3.18*inch, 8.80*inch,'Performance evaluation Sheet',c.setFont("Helvetica", 16))
    c.drawCentredString(3.18*inch, 8.60*inch,'C.Y - 2022',c.setFont("Helvetica", 12))
    c.drawImage("Assets\\logo.png",-0.2*inch, 8.85*inch,height=60,width=60)
    c.drawImage("Assets\\capizlogo.png",5.75*inch, 8.75*inch,height=70,width=70)
    


    c.drawCentredString(3.18*inch, 8.25*inch,result[3] + " " + result[4],c.setFont("Helvetica-Bold", 17))
    c.drawCentredString(3.18*inch, 8*inch,results[15],c.setFont("Helvetica", 14))

    c.drawString(-0.7*inch, 7.70*inch,"Date Filed - " + result[2],c.setFontSize(size=12))

    c.drawString(1.15*inch, 7.25*inch,"Criterias",c.setFont("Helvetica-Bold", 14))

    c.drawString(-0.5*inch, 6.80*inch,"Clear understanding of the signed job description: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 6.40*inch,"Possess timelines in the job/Efficiency in assigned job: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 6*inch,"Meet expectations/targets consistently?: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 5.60*inch,"Maintain prescribed quality in work?: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 5.20*inch,"Follow policies & procedures: ",c.setFont("Helvetica", 12))

    c.drawString(-0.5*inch, 4.80*inch,"Commitment, realiability, dependability: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 4.40*inch,"Time Management: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 4*inch,"Punctuality: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 3.60*inch,"Follow rules & regulations of the hospital: ",c.setFont("Helvetica", 12))
    c.drawString(-0.5*inch, 3.20*inch,"Handling work pressure: ",c.setFont("Helvetica", 12))

    c.drawString(5.8*inch, 7.25*inch,"Rates",c.setFont("Helvetica-Bold", 14))

    c.drawString(6*inch, 6.80*inch,str(result[5]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 6.40*inch,str(result[6]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 6*inch,str(result[7]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 5.60*inch,str(result[8]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 5.20*inch,str(result[9]),c.setFont("Helvetica", 12))

    c.drawString(6*inch, 4.80*inch,str(result[10]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 4.40*inch,str(result[11]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 4*inch,str(result[12]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 3.60*inch,str(result[13]),c.setFont("Helvetica", 12))
    c.drawString(6*inch, 3.20*inch,str(result[14]),c.setFont("Helvetica", 12))

    c.drawString(-0.5*inch, 2*inch,"Total Rate ",c.setFont("Helvetica-Bold", 14))
    c.drawString(-0.5*inch, 1.5*inch,"Avarage ",c.setFont("Helvetica-Bold", 14))

    c.drawString(6*inch, 2*inch,str(result[15]),c.setFont("Helvetica-Bold", 14))
    c.drawString(6*inch, 1.5*inch,str(result[16]),c.setFont("Helvetica-Bold", 14))
    c.drawCentredString(6.15*inch, 1.2*inch,result[17],c.setFont("Helvetica-Bold", 14))


    c.drawString(-0.5*inch, 0.1*inch,"Employee's Signature",c.setFont("Helvetica", 12))

    c.drawString(5*inch, 0.1*inch,"Dept.Head Signature",c.setFont("Helvetica", 12))


    
    
    

    c.showPage()
    c.save()
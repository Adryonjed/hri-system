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


    file = filedialog.asksaveasfilename(filetypes = [("PDF file",'*.pdf')],defaultextension='.pdf',title= "Save a PDF file",initialfile="default.pdf",initialdir='C:\\Users\\ferna\\Downloads')
    c = canvas.Canvas(file,pagesize= letter)
    c.translate(inch,inch)

    
    
    c.drawString(0.90*inch, 9.33*inch,'Roxas Memorial Provincial Hospital',c.setFont("Helvetica-Bold", 20))
    c.drawString(1.80*inch, 8.97*inch,'Performance evaluation Sheet',c.setFont("Helvetica", 15))
    c.drawImage("Assets\\logo.png",-0.2*inch, 8.85*inch,height=60,width=60)
    c.drawImage("Assets\\capizlogo.png",5.8*inch, 8.75*inch,height=70,width=70)


    c.drawString(1.9*inch, 8.25*inch,result[3] + " " + result[4],c.setFont("Helvetica-Bold", 16))

    c.drawString(-0.7*inch, 7.75*inch,"Date Filed - " + result[2],c.setFontSize(size=12))

    c.drawString(1.15*inch, 7.25*inch,"Criterias",c.setFont("Helvetica-Bold", 14))

    c.drawString(-0.5*inch, 6.50*inch,"Clear understanding of the signed job description: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 6*inch,"Possess timelines in the job/Efficiency in assigned job: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 5.50*inch,"Meet expectations/targets consistently?: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 5*inch,"Maintain prescribed quality in work?: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 4.50*inch,"Follow policies & procedures: ",c.setFont("Helvetica", 14))

    c.drawString(-0.5*inch, 4*inch,"Commitment, realiability, dependability: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 3.50*inch,"Time Management: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 3*inch,"Punctuality: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 2.50*inch,"Follow rules & regulations of the hospital: ",c.setFont("Helvetica", 14))
    c.drawString(-0.5*inch, 2*inch,"Handling work pressure: ",c.setFont("Helvetica", 14))

    c.drawString(5.8*inch, 7.25*inch,"Rates",c.setFont("Helvetica-Bold", 14))

    c.drawString(6*inch, 6.50*inch,str(result[5]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 6*inch,str(result[6]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 5.50*inch,str(result[7]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 5*inch,str(result[8]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 4.50*inch,str(result[9]),c.setFont("Helvetica", 14))

    c.drawString(6*inch, 4*inch,str(result[10]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 3.50*inch,str(result[11]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 3*inch,str(result[12]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 2.50*inch,str(result[13]),c.setFont("Helvetica", 14))
    c.drawString(6*inch, 2*inch,str(result[14]),c.setFont("Helvetica", 14))

    c.drawString(-0.5*inch, 1*inch,"Total Rate ",c.setFont("Helvetica-Bold", 14))
    c.drawString(-0.5*inch, 0.50*inch,"Avarage ",c.setFont("Helvetica-Bold", 14))

    c.drawString(6*inch, 1*inch,str(result[15]),c.setFont("Helvetica-Bold", 14))
    c.drawString(6*inch, 0.50*inch,str(result[16]),c.setFont("Helvetica-Bold", 14))
    c.drawString(5.70*inch, 0*inch,result[17],c.setFont("Helvetica-Bold", 14))


    
    
    

    c.showPage()
    c.save()
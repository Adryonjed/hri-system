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
from reportlab.lib.pagesizes import GOV_LEGAL

    

def saveasfile(s_id):

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
    cursor.execute("SELECT * FROM personal WHERE id=%s",(s_id))
    cursor2.execute("SELECT * FROM numbers WHERE id=%s",(s_id))
    cursor3.execute("SELECT * FROM residential WHERE id=%s",(s_id))
    cursor4.execute("SELECT * FROM permanent WHERE id=%s",(s_id))
    cursor5.execute("SELECT * FROM spouse WHERE id=%s",(s_id))
    cursor6.execute("SELECT * FROM family WHERE id=%s",(s_id))
    cursor7.execute("SELECT * FROM elementary WHERE id=%s",(s_id))
    cursor8.execute("SELECT * FROM highschool WHERE id=%s",(s_id))
    cursor9.execute("SELECT * FROM vocational WHERE id=%s",(s_id))
    cursor10.execute("SELECT * FROM college WHERE id=%s",(s_id))
    cursor11.execute("SELECT * FROM graduate WHERE id=%s",(s_id))
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
    conn.commit()
    conn.close()


    file = filedialog.asksaveasfilename(filetypes = [("PDF file",'*.pdf')],defaultextension='.pdf',title= "Save a PDF file",initialfile="default.pdf",initialdir='C:\\Users\\ferna\\Downloads')
    c = canvas.Canvas(file,pagesize=GOV_LEGAL)
    c.translate(inch,inch)
    c.setFont("Helvetica", 10)
    c.drawImage("Assets\\PDS.jpg",-1*inch,-1.00*inch,height=938,width=612)

    #personal info
    
    c.drawString(0.8*inch, 10.33*inch, result[1])
    c.drawString(0.8*inch, 10.05*inch, result[2])
    c.drawString(0.8*inch, 9.77*inch, result[3])
    dtr=datetime.strftime(result[4],'%b/%d/%Y')
    c.drawString(0.8*inch, 9.40*inch,dtr)
    c.drawString(0.8*inch, 9.05*inch, result[5])

    if result[6] == 'male':
        c.drawImage("Assets\\chk.jpg",0.7*inch, 8.74*inch,height=10,width=10)
    if result[6] == 'female':
        c.drawImage("Assets\\chk.jpg",1.47*inch, 8.74*inch,height=10,width=10)


    if result[7] == "Single":
        c.drawImage("Assets\\chk.jpg",0.7*inch, 8.47*inch,height=10,width=10)
    if result[7] == "Married":
        c.drawImage("Assets\\chk.jpg",1.47*inch, 8.47*inch,height=10,width=10)
    if result[7] == "Widowed":
        c.drawImage("Assets\\chk.jpg",0.7*inch, 8.30*inch,height=10,width=10)
    if result[7] == "Seperated":
        c.drawImage("Assets\\chk.jpg",1.47*inch, 8.30*inch,height=10,width=10)
    if result[7] == "Other/s":
        c.drawImage("Assets\\chk.jpg",0.7*inch, 8.13*inch,height=10,width=10)

    c.drawString(0.8*inch, 7.82*inch, str(result[8]))
    c.drawString(0.8*inch, 7.57*inch, str(result[9]))
    c.drawString(0.8*inch, 7.28*inch, result[10])

    #numbers

    c.drawString(0.8*inch, 6.95*inch, str(result2[1]))
    c.drawString(0.8*inch, 6.65*inch, str(result2[2]))
    c.drawString(0.8*inch, 6.38*inch, str(result2[3]))
    c.drawString(0.8*inch, 6.11*inch, str(result2[4]))
    c.drawString(0.8*inch, 5.87*inch, str(result2[5]))
    c.drawString(0.8*inch, 5.6*inch, str(result2[6]))

    #citizenship

    if result[11] == 'Filipino':
        c.drawImage("Assets\\chk.jpg",4.35*inch, 9.45*inch,height=10,width=10)
    if result[11] == 'Dual Citizenship':
        c.drawImage("Assets\\chk.jpg",5.45*inch, 9.45*inch,height=10,width=10)
        
    if result[12] == 'By Birth':
        c.drawImage("Assets\\chk.jpg",5.65*inch, 9.25*inch,height=10,width=10)
    if result[12] == 'By Naturalization':
        c.drawImage("Assets\\chk.jpg",6.23*inch, 9.25*inch,height=10,width=10)
    
    c.drawString(4.35*inch, 8.74*inch, result[13])

    #residential

    c.drawString(3.7*inch, 8.47*inch, result3[1])
    c.drawString(5.65*inch, 8.47*inch, result3[2])
    c.drawString(3.7*inch, 8.17*inch, result3[3])
    c.drawString(5.65*inch, 8.17*inch, result3[4])
    c.drawString(3.7*inch, 7.87*inch, result3[5])
    c.drawString(5.65*inch, 7.87*inch, result3[6])
    c.drawString(3.7*inch, 7.57*inch, str(result3[7]))

    #permanent

    c.drawString(3.7*inch, 7.37*inch, result4[1])
    c.drawString(5.65*inch, 7.37*inch, result4[2])
    c.drawString(3.7*inch, 7.03*inch, result4[3])
    c.drawString(5.65*inch, 7.03*inch, result4[4])
    c.drawString(3.7*inch, 6.73*inch, result4[5])
    c.drawString(5.65*inch, 6.73*inch, result4[6])
    c.drawString(3.7*inch, 6.37*inch, str(result4[7]))

    #cell and telephone

    c.drawString(3.7*inch, 6.11*inch, str(result2[7]))
    c.drawString(3.7*inch, 5.87*inch, str(result2[8]))

    #email

    c.drawString(3.7*inch, 5.66*inch, result[14])

    #spouse

    c.drawString(0.8*inch, 5.17*inch, result5[1])
    c.drawString(0.8*inch, 4.89*inch, result5[2])
    c.drawString(0.8*inch, 4.61*inch, result5[3])
    c.drawString(0.8*inch, 4.35*inch, result5[4])
    c.drawString(0.8*inch, 4.12*inch, result5[5])
    c.drawString(0.8*inch, 3.85*inch, result5[6])
    c.drawString(0.8*inch, 3.57*inch, str(result5[7]))

    #family

    c.drawString(0.8*inch, 3.3*inch, result6[1])
    c.drawString(0.8*inch, 3.04*inch, result6[2])
    c.drawString(0.8*inch, 2.78*inch, result6[3])
    c.drawString(0.8*inch, 2.52*inch, result6[4])
    c.drawString(0.8*inch, 2.26*inch, result6[5])
    c.drawString(0.8*inch, 2*inch, result6[6])
    c.drawString(0.8*inch, 1.74*inch, result6[7])

    #elementary

    c.drawString(0.63*inch, 0.8*inch, result7[1],c.setFontSize(size=5))
    c.drawString(2.3*inch, 0.8*inch, result7[2])
    c.drawString(4.35*inch, 0.8*inch, str(result7[3]),c.setFontSize(size=12))
    c.drawString(5.08*inch, 0.8*inch, str(result7[4]))
    c.drawString(5.65*inch, 0.8*inch, str(result7[5]))
    c.drawString(6.26*inch, 0.8*inch, str(result7[6]))
    c.drawString(7.01*inch, 0.8*inch, str(result7[7]))

    #highschool

    c.drawString(0.63*inch, 0.5*inch, result8[1],c.setFontSize(size=5))
    c.drawString(2.3*inch, 0.5*inch, result8[2])
    c.drawString(4.35*inch, 0.5*inch, str(result8[3]),c.setFontSize(size=12))
    c.drawString(5.08*inch, 0.5*inch, str(result8[4]))
    c.drawString(5.65*inch, 0.5*inch, str(result8[5]))
    c.drawString(6.26*inch, 0.5*inch, str(result8[6]))
    c.drawString(7.01*inch, 0.5*inch, str(result8[7]))
    
    #vocational

    c.drawString(0.63*inch, 0.22*inch, result9[1],c.setFontSize(size=5))
    c.drawString(2.3*inch, 0.22*inch, result9[2])
    c.drawString(4.35*inch, 0.22*inch, str(result9[3]),c.setFontSize(size=12))
    c.drawString(5.08*inch, 0.22*inch, str(result9[4]))
    c.drawString(5.65*inch, 0.22*inch, str(result9[5]))
    c.drawString(6.26*inch, 0.22*inch, str(result9[6]))
    c.drawString(7.01*inch, 0.22*inch, str(result9[7]))

    #college

    c.drawString(0.63*inch, -0.07*inch, result10[1],c.setFontSize(size=5))
    c.drawString(2.3*inch, -0.07*inch, result10[2])
    c.drawString(4.35*inch, -0.07*inch, str(result10[3]),c.setFontSize(size=12))
    c.drawString(5.08*inch, -0.07*inch, str(result10[4]))
    c.drawString(5.65*inch, -0.07*inch, str(result10[5]))
    c.drawString(6.26*inch, -0.07*inch, str(result10[6]))
    c.drawString(7.01*inch, -0.07*inch, str(result10[7]))

    #graduate

    c.drawString(0.63*inch, -0.33*inch, result10[1],c.setFontSize(size=5))
    c.drawString(2.3*inch, -0.33*inch, result10[2])
    c.drawString(4.35*inch, -0.33*inch, str(result10[3]),c.setFontSize(size=12))
    c.drawString(5.08*inch, -0.33*inch, str(result10[4]))
    c.drawString(5.65*inch, -0.33*inch, str(result10[5]))
    c.drawString(6.26*inch, -0.33*inch, str(result10[6]))
    c.drawString(7.01*inch, -0.33*inch, str(result10[7]))
    
    
    

    c.showPage()
    c.save()
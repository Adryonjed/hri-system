from cProfile import label
from imaplib import Commands
from matplotlib import image, style
from matplotlib.pyplot import show
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk



def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='ewe',
    )
    return conn

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, firstname, surname, position, department FROM person ORDER BY firstname")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    
    return results

def populate():
    my_tree = ttk.Treeview()
    for rows in my_tree.get_children():
        my_tree.delete(rows)

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    for result in results:
        my_tree.insert(parent='', index=len(results), iid=result, text='',
                              values=(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15]))
    
def join():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person LEFT JOIN educ ON person.id = educ.id")
    conn.commit()
    conn.close()





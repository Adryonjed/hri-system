from cProfile import label
from imaplib import Commands
from matplotlib import image, style
from matplotlib.pyplot import show
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import customtkinter



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
    cursor.execute("SELECT * FROM firstt ORDER BY name")
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
    cursor.execute("SELECT * FROM firstt")
    results = cursor.fetchall()
    conn.commit()
    conn.close()

    for result in results:
        my_tree.insert(parent='', index=len(results), iid=result, text='',
                              values=(result[0], result[1], result[2], result[3]))
                              
                              
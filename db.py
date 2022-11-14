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
    cursor.execute("SELECT name, email, position, department FROM firstt ORDER BY name")
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
                              values=(result[0], result[1], result[2], result[3],result[4],result[5]))
                              
                              
def populate2():
    my_tree2 = ttk.Treeview()
    for rows in my_tree2.get_children():
        my_tree2.delete(rows)

    conn2 = connection()
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT * FROM firstt")
    results2 = cursor2.fetchall()
    conn2.commit()
    conn2.close()

    for result in results2:
        my_tree2.insert(parent='', index=len(results2), iid=result, text='',
                              values=(result[0], result[1], result[2], result[3],result[4],result[5]))
                              
                              
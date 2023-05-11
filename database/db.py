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
        db='hris',
    )
    return conn







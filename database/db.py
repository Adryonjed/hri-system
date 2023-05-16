import pymysql
from tkinter import *
import tkinter as tk



def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='hris',
    )
    return conn







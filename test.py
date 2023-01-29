import tkinter as tk

from tkinter import *

#------------------------------------

def addBox():
    print ("ADD")

    # I use len(all_entries) to get nuber of next free column
    next_row = len(all_entries)


    # add entry in second row
    ent = Entry(frame_for_boxes)
    ent.grid(row=next_row, column=1)

    all_entries.append( ent )

#------------------------------------

def showEntries():

    for  ent in (all_entries):
        print ( ent.get())

#------------------------------------

all_entries = []

root = Tk()

showButton = Button(root, text='Show all text', command=showEntries)
showButton.pack()

addboxButton = Button(root, text='<Add Time Input>', fg="Red", command=addBox)
addboxButton.pack()

frame_for_boxes = Frame(root)
frame_for_boxes.pack()

root.mainloop()
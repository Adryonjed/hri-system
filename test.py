
# import modules
import tkinter as tk
  
# object of tkinter
# and background set for light grey
master = tk.Tk()
master.configure(bg='light grey')
  
# create label
l = tk.Label(master,
             text="Welcome to geeksforgeeks",
             bg="red")
  
# apply cget()
print("Label text: ", l.cget("text"))
  
l.pack()
master.mainloop()
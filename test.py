import tkinter as tk

def toggle_switch():
    global is_on
    is_on = not is_on
    update_switch()

def update_switch():
    if is_on:
        frams.pack()
    else:
        frams.pack_forget()
        

root = tk.Tk()

is_on = False


rames = tk.Frame(root, width=100,height=10, bg="black")
rames.pack()

switch_button = tk.Button(rames, text="Off", bg="red", command=toggle_switch)
switch_button.pack()


frams = tk.Frame(rames, width=100,height=100, bg="red")

switch_button2 = tk.Button(root, text="Off", bg="blue")
switch_button2.pack()

root.mainloop()

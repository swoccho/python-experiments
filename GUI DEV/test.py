import tkinter as tk
from tkinter import ttk
def greet():
     print("hello world")


root = tk.Tk()
root.title("hello world" )

greet_button = ttk.Button(root,text="greet " ,command=greet)
greet_button.pack(side="left",fill= "x" ,expand=True)

quit_button = ttk.Button(root,text="Quit" , command=root.destroy)
quit_button.pack(side="right",fill="x",expand=True)


root.mainloop()

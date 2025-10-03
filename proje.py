
import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Hello")

window.config(bg="#090cec")

tk.Label(window,text=" Hello world !!!!!").grid(row=1,column=0,padx=10,pady=10)

window.mainloop()            

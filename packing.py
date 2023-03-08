import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

rectangulo_1 = tk.Label(root, text="Rectángulo 1", bg="green", fg="white")
rectangulo_1.pack(ipadx=10, ipady=10, fill="x")

rectangulo_2 = tk.Label(root, text="Rectángulo 2", bg="red", fg="white")
rectangulo_2.pack(ipadx=10, ipady=10)


root.mainloop()
import tkinter as tk 
from tkinter import ttk

def saludar():
    print ("conchale")

root = tk.Tk()

saludar_btn = ttk.Button(root, text = "Saludar", command=saludar)
saludar_btn.pack(side="left", fill="y", expand="False")

cerrar_btn = ttk.Button(root, text = "Salir", command=root.destroy)
cerrar_btn.pack(side="left")

root.mainloop()
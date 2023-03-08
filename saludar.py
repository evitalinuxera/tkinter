import tkinter as tk 
from tkinter import ttk

def saludar():
    print (f"Hola, {nombre_usuario.get() or 'mundo'}!")

root = tk.Tk()

nombre_usuario = tk.StringVar()

nombre_lbl = ttk.Label(root, text="Nombre: ")
nombre_lbl.pack(side="left", padx=(0, 10))

nombre = ttk.Entry(root, width="15", textvariable=nombre_usuario)
nombre.pack(side="left")
nombre.focus()

saludar_btn = ttk.Button(root, text="Saludar", command=saludar)
saludar_btn.pack(side="left")

salir_btn = ttk.Button(root, text="Salir", command=root.destroy)
salir_btn.pack(side="right")

root.mainloop()
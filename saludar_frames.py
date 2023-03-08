import tkinter as tk 
from tkinter import ttk

def saludar():
    print (f"Hola, {nombre_usuario.get() or 'mundo'}!")

# Ventana Ppal
root = tk.Tk()

nombre_usuario = tk.StringVar()

# Frame superior con el Entry
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

nombre_lbl = ttk.Label(input_frame, text="Nombre: ")
nombre_lbl.pack(side="left", padx=(0, 10))

nombre = ttk.Entry(input_frame, width="15", textvariable=nombre_usuario)
nombre.pack(side="left")
nombre.focus()

# Frame inferior con los botones
botones_frame = ttk.Frame(root, padding=(20, 10))
botones_frame.pack(fill="both")

saludar_btn = ttk.Button(botones_frame, text="Saludar", command=saludar)
saludar_btn.pack(side="left", fill="x", expand="True")

salir_btn = ttk.Button(botones_frame, text="Salir", command=root.destroy)
salir_btn.pack(side="right", fill="x", expand="True")

root.mainloop()
import tkinter as tk 
from tkinter import ttk

def saludar():
    print (f"Hola, {nombre_usuario.get() or 'mundo'}!")

# Ventana Ppal
root = tk.Tk()
root.title("Saludador")
root.columnconfigure(0, weight=1)

nombre_usuario = tk.StringVar()

# Frame superior con el Entry
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")

nombre_lbl = ttk.Label(input_frame, text="Nombre: ")
nombre_lbl.grid(row=0, column=0, padx=(0, 10))

nombre = ttk.Entry(input_frame, width="15", textvariable=nombre_usuario)
nombre.grid(row=0, column=1)
nombre.focus()

# Frame inferior con los botones
botones_frame = ttk.Frame(root, padding=(20, 10))
botones_frame.grid(row=1, column=0, sticky="EW")

botones_frame.columnconfigure(0, weight=1)
botones_frame.columnconfigure(1, weight=1)

saludar_btn = ttk.Button(botones_frame, text="Saludar", command=saludar)
saludar_btn.grid(row=0, column=0, sticky="EW")

salir_btn = ttk.Button(botones_frame, text="Salir", command=root.destroy)
salir_btn.grid(row=0, column=1, sticky="EW")

root.mainloop()
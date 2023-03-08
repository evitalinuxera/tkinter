import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Label widget")

# Solo el Label
# label = ttk.Label(root,text="Hola", padding=20)
# label.config(font=("Ubuntu", 20))
# label.pack()

# Label con imagen
# Hay que instalar Pillow con apt
# Son estos paquetes
# python3-pil.imagetk python3-pil

imagen = Image.open("gulf_logo.png").resize((64, 64))
foto = ImageTk.PhotoImage(imagen)
label = ttk.Label(root, text="El mejor aceite", image=foto, padding=5, compound="right")
label.pack()

# Hacer un label variable
# Acá uso string pero se puede usar
# IntVar, BooleanVar, DoubleVar
# saludo = tk.StringVar()
# label = ttk.Label(root, padding=10, textvariable=saludo)
# saludo.set("Hola, nueva cadena")

root.mainloop()
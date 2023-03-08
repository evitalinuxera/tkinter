import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

texto = tk.Text(root, height=8)
texto.grid(row=0, column=0, sticky="ew")
texto.insert("1.0", "Ingrese el comentario acá...")

# Hay que agregarle una scrollbar aparte
texto_scroleado = ttk.Scrollbar(root, orient="vertical", command=texto.yview)
texto_scroleado.grid(row=0, column=1, sticky="ns")
texto["yscrollcommand"] = texto_scroleado.set

root.mainloop()
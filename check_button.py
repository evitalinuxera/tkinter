import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

# La manera simple
# checkBtn = ttk.Checkbutton(root, text="Chequeado")
# checkBtn.pack()
#
# checkBtn["state"] = "normal"

opcion_seleccionada = tk.StringVar()

def imprimir_seleccion():
    print (opcion_seleccionada.get())

checkBtn = ttk.Checkbutton(
    root,
    text="Ejemplo de check",
    variable=opcion_seleccionada,
    command=imprimir_seleccion,
    onvalue="Chequeado",
    offvalue="Deschequeado"
)

checkBtn.pack()

root.mainloop()
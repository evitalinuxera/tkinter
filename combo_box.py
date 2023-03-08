import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

dia_de_la_semana = tk.StringVar()
diaCombo = ttk.Combobox(root, textvariable=dia_de_la_semana)
diaCombo["values"] = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
diaCombo["state"] = "readonly" # Esto es para que no se agreguen valores. 
# para que se pueda agregar se pone la opcion "normal"
diaCombo.pack()

def handle_seleccion(event):
    print("Hoy es", dia_de_la_semana.get())
    print("Pero lo vamos a cambiar por Viernes.")
    dia_de_la_semana.set("Viernes")
    print(diaCombo.current()) # Devuelve el índice de la lista
    print(dia_de_la_semana.get()) #Devuelve el elemento de la lista

# Asocio el widget/evento con la función
diaCombo.bind("<<ComboboxSelected>>", handle_seleccion)

root.mainloop()

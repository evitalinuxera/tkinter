import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

variable_guardada = tk.StringVar()

opcion_uno = ttk.Radiobutton(
    root,
    text="Opción 1",
    variable=variable_guardada,
    value="Primera Opción"
)

opcion_dos = ttk.Radiobutton(
    root,
    text="Opción 2",
    variable=variable_guardada,
    value="Segunda Opción"
)

opcion_tres = ttk.Radiobutton(
    root,
    text="Opción 3",
    variable=variable_guardada,
    value="Tercera Posición"
)

opcion_uno.pack()
opcion_dos.pack()
opcion_tres.pack()

root.mainloop()
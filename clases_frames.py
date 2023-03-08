import tkinter as tk 
from tkinter import ttk

# Clase para la ventana
class SaludarApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("App que saluda")

        InputFrame(self).pack()


# Clase para el frame
class InputFrame(ttk.Frame):
    def __init__(self, contenedor):
        super().__init__(contenedor)

        self.entrada_nombre = tk.StringVar()

        nombre_lbl=ttk.Label(self, text="Ingrese nombre: ")
        nombre_ent = ttk.Entry(self, textvariable=self.entrada_nombre)
        mandar_btn = ttk.Button(self, 
        text="Saludar", command=self.saludar)

        nombre_lbl.pack(side="left")
        nombre_ent.pack(side="left")
        mandar_btn.pack(side="left")

    def saludar(self):
        print(f"Hola, {self.entrada_nombre.get()}!")

# Loop ppal
root = SaludarApp()
root.mainloop()
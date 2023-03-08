import tkinter as tk 
from tkinter import ttk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x300")
        self.title("Aplicación")
        Frame_gral(self).grid(row=0, column=0, sticky="NESW")

class Frame_gral(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        cartel = ttk.Label(self, text="Garlopa")
        cartel.grid(row=0, column=0, padx=(15,15), pady=(30, 0))
        






root = Aplicacion()
root.mainloop()
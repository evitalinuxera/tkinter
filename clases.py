import tkinter as tk 
from tkinter import ttk

class HolaMundo(tk.Tk):
    # Se crea esta clase copia de la tk.Tk
    # y se mete el método __init__ con 
    # self, así todo lo puedo referir a 
    # self en lugar de a root como antes
    def __init__(self):
        super().__init__()

        self.title("Hola")
        ttk.Label(self, text="La hago grande para que se vea, hola, putes").pack()

root = HolaMundo()
root.mainloop()
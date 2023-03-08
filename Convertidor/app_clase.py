import tkinter as tk 
from tkinter import ttk 

class ConvertidorDistancias(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Convertidor de distancias")
        self.frame = ttk.Frame(self, padding=(60, 30))
        self.geometry("300x200")
        self.frame.grid()

class MetrosPies(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.valor_pies = tk.StringVar()
        self.valor_metros = tk.StringVar()

    


root = ConvertidorDistancias()

root.mainloop()
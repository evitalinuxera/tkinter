import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ttk.Label(root, text="San Martín, padre de la Patria", padding=20).pack()

# Si no se pone el fill, el separador sale de un solo pixel
# por default y no se ve un pomo
ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root, text="Belgrano, capo total", padding=20).pack()

root.mainloop()
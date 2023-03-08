import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

def handle_cambio_scale(event):
    print(scale.get())

valor_actual = tk.DoubleVar()

scale = ttk.Scale(
    root, 
    orient="horizontal",
    from_=0,
    to=10,
    command=handle_cambio_scale,
    variable=valor_actual
)
scale.pack(fill="x")

root.mainloop()

print(valor_actual.get())
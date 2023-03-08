import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

valor_inicial = tk.StringVar(value=20)
varSpn = ttk.Spinbox(
    root,
    from_=0,
    # En lugar de from_ y to se pueden mandar valores fijos como
    # por ejemplo
    # values=(5, 10, 15, 20)
    to=30,
    textvariable=valor_inicial,
    wrap=False # wrap es para que sea continuo
)

varSpn.pack()

# Para traer el valor 
print(varSpn.get())

root.mainloop()
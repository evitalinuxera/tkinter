import tkinter as tk 
from tkinter import ttk
import tkinter.font as font

# Armo la ventana
# y configuro la fuente

root = tk.Tk()
root.title("Convertidor de distancias")
font.nametofont("TkDefaultFont").configure(size=12)

# Declaro la(s) variable(s) y funciones
valor_en_metros = tk.StringVar()
valor_en_pies = tk.StringVar(value="Acá se mostrará la conversión")

def calcular_pies(*args):
    try:
        metros = float(valor_en_metros.get())
        pies = metros * 3.28084
        # print (f"{metros} metros es igual a {pies: .3f} pies.")
        valor_en_pies.set(f"{pies: .3f}")

    except ValueError:
        pass

# Armo el frame ppal
main = ttk.Frame(root, padding=(10, 15))
main.grid()

# Esta es para que el contenido siempre quede
# en el centro 
# También podría haber metido una medida fija
# en el geometry de la ventana root y ahí no 
# se estiraba usando resize=False
root.columnconfigure(0, weight=1)

# Declaro los widgets
metrosLbl = ttk.Label(main, text="Metros: ")
metrosEnt = ttk.Entry(main, width=10, textvariable=valor_en_metros, font=("Monospace", 15))
piesLbl = ttk.Label(main, text="Pies: ")
piesRes = ttk.Label(main, textvariable=valor_en_pies)
convBtn = ttk.Button(main, text="Convertir", command=calcular_pies)

# Ubico los widgets en la grilla
metrosLbl.grid(column=0, row=0, sticky="w")
metrosEnt.grid(column=1, row=0, sticky="ew")
metrosEnt.focus()
piesLbl.grid(column=0, row=1, sticky="w")
piesRes.grid(column=1, row=1, sticky="ew")
convBtn.grid(column=0, row=2, columnspan=2, sticky="ew")

# Para poner una MISMA propiedad a todo un grupo de widgets
# se usa esta infame propiedad
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

# Acá van los bindings al teclado
# uno para la tecla ENTER principal
# y otro para el enter del NumPad
root.bind("<Return>", calcular_pies)
root.bind("KP_Enter", calcular_pies)

# Loop ppal
root.mainloop()
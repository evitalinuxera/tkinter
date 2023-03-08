import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Ejemplos de widgets")

# Armar el widget
texto = tk.Text(root, height=8)
texto.pack()

# Llenarlo con texto
# 
# Ojota, 1.0 es 
# línea 1
# posición 0
# No hay línea 0
texto.insert("1.0", "Inserte su comentario acá...")

# Hacerlo no disponible
# texto["state"] = "disable" 
# 
# Hacerlo disponible se usa "normal"

# Para traer el texto que ingresaron
# se pone (desde, hasta)
# en el ejemplo está "todo el texto"
contenido = texto.get("1.0", "end")
print (contenido)


root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widget Examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

pl = tk.StringVar(value=programming_languages)
# ojo que este es tk, no ttk
pl_select = tk.Listbox(root, listvariable=pl, height=6)
pl_select.pack(padx=10, pady=10)

pl_select["selectmode"] = "extended"  # Allows multiple selection, "browse" is the counterpart (yeah, I know it's a bad name!)
# Otros dicen que se puede usar "multiple". En Huayra 6 con MATE no me anduvo la selección múltiple.

def handle_selection_change(event):
    selected_indices = pl_select.curselection()
    for i in selected_indices:
        print(pl_select.get(i))


pl_select.bind("<<ListboxSelect>>", handle_selection_change)
root.mainloop()
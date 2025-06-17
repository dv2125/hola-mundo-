import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Hola Mundo")
ventana.geometry("300x150")

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Hola Mundo!")

boton = tk.Button(
    ventana,
    text="Saludar",
    command=mostrar_mensaje,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
boton.pack(expand=True)

ventana.mainloop()
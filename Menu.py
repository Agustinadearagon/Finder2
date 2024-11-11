# menú.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
from tkinter import filedialog

def ejecutar_script(script):
    """ Ejecuta un script Python de manera segura """
    try:
        subprocess.run(["python", script], check=True)
        messagebox.showinfo("Éxito", f"El script {script} se ejecutó correctamente.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo {script} no se encontró.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", f"Hubo un problema ejecutando el script {script}.")

def crear_ventana():
    """ Configura la ventana principal de la aplicación """
    ventana = tk.Tk()
    ventana.title("Menú de Herramientas")
    ventana.geometry("600x500")

    # Botones para ejecutar los scripts
    botones = [
        ("Ejecutar Sirla", "scripts/sirla.py"),
        ("Ejecutar Hacha", "scripts/hacha.py"),
        ("Convertir Archivos", "scripts/conversor.py"),
        ("Buscar Archivos", "scripts/Finder.py")
    ]

    for texto, script in botones:
        boton = tk.Button(ventana, text=texto, command=lambda s=script: ejecutar_script(s))
        boton.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()

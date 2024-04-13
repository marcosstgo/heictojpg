import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def open_heic():
    file_path = filedialog.askopenfilename(filetypes=[("HEIC files", "*.heic")])
    if file_path:
        input_path.set(file_path)

def save_jpg():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    if file_path:
        output_path.set(file_path)

def convert_heic_to_jpg():
    heic_path = os.path.abspath(input_path.get())
    jpg_path = os.path.abspath(output_path.get())
    if not heic_path or not jpg_path:
        messagebox.showerror("Error", "Por favor selecciona un archivo HEIC y especifica la ubicación para guardar el JPG.")
        return
    magick_path = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'
    try:
        subprocess.run([magick_path, 'convert', heic_path, jpg_path], check=True)
        messagebox.showinfo("Éxito", "El archivo se ha convertido exitosamente!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Falló la conversión del archivo: {e}")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"No se encontró el ejecutable de ImageMagick: {e}")

# Configuración de la GUI
root = tk.Tk()
root.title("Convertidor de HEIC a JPG")
root.config(bg="#333333")  # Color de fondo de la ventana

# Variables para las rutas de archivo
input_path = tk.StringVar()
output_path = tk.StringVar()

# Estilos
style = {"font": ("Arial", 12), "bg": "#333333", "fg": "#ffffff"}
button_style = {"font": ("Arial", 12), "bg": "#0078D7", "fg": "#ffffff", "padx": 10, "pady": 5}

# Widgets
tk.Label(root, text="Selecciona el archivo HEIC:", **style).pack(pady=(10, 0))
entry_heic = tk.Entry(root, textvariable=input_path, width=50, **style)
entry_heic.pack(pady=(5, 10))

tk.Button(root, text="Buscar", command=open_heic, **button_style).pack()

tk.Label(root, text="Guardar el JPG como:", **style).pack(pady=(10, 0))
entry_jpg = tk.Entry(root, textvariable=output_path, width=50, **style)
entry_jpg.pack(pady=(5, 10))

tk.Button(root, text="Guardar como", command=save_jpg, **button_style).pack()

tk.Button(root, text="Convertir", command=convert_heic_to_jpg, **button_style).pack(pady=(10, 20))

root.mainloop()

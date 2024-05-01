import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

def open_heic():
    file_paths = filedialog.askopenfilenames(
        title="Seleccionar archivos",
        filetypes=[("Image files", "*.heic *.HEIC *.jfif *.JFIF")]
    )
    if file_paths:
        # Unimos las rutas y convertimos las extensiones a minúsculas
        normalized_paths = [path.lower() for path in file_paths]
        input_path.set(";".join(normalized_paths))

def save_jpg():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_path.set(folder_path)

def convert_heic_to_jpg():
    file_paths = input_path.get().split(";")
    folder_jpg = output_path.get()
    if not file_paths or not folder_jpg:
        messagebox.showerror("Error", "Por favor selecciona los archivos y especifica la carpeta para guardar los JPGs.")
        return

    progress_bar['maximum'] = len(file_paths)
    progress_bar['value'] = 0
    root.update_idletasks()

    magick_path = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'
    errors = []

    for file_path in file_paths:
        file_extension = os.path.splitext(file_path)[1]
        if file_extension in [".heic", ".HEIC"]:
            jpg_path = os.path.join(folder_jpg, os.path.basename(file_path).replace(".heic", ".jpg").replace(".HEIC", ".jpg"))
        elif file_extension in [".jfif", ".JFIF"]:
            jpg_path = os.path.join(folder_jpg, os.path.basename(file_path).replace(".jfif", ".jpg").replace(".JFIF", ".jpg"))
        
        try:
            subprocess.run([magick_path, file_path, jpg_path], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            errors.append(f"Falló la conversión del archivo {file_path}: {e}")
        progress_bar['value'] += 1
        root.update_idletasks()

    if errors:
        messagebox.showerror("Error en la conversión", "\n".join(errors))
    else:
        messagebox.showinfo("Éxito", "Todos los archivos se han convertido exitosamente!")

# Configuración de la GUI
root = tk.Tk()
root.title("HEIC y JFIF a JPG | @m4rcos | v1.1")
root.config(bg="#333333")

# Variables para las rutas de archivo
input_path = tk.StringVar()
output_path = tk.StringVar()

# Estilos
style = {"font": ("Arial", 12), "bg": "#333333", "fg": "#ffffff"}
button_style = {
    "font": ("Arial", 12), 
    "bg": "#0078D7", 
    "fg": "#ffffff", 
    "padx": 10, 
    "pady": 5
}


# Widgets
tk.Label(root, text="Selecciona los archivos HEIC o JFIF:", **style).pack(pady=(10, 0))
entry_heic = tk.Entry(root, textvariable=input_path, width=50, **style)
entry_heic.pack(pady=(5, 10))

tk.Button(root, text="Buscar", command=open_heic, **button_style).pack()

tk.Label(root, text="Guardar los JPGs en la carpeta:", **style).pack(pady=(10, 0))
entry_jpg = tk.Entry(root, textvariable=output_path, width=50, **style)
entry_jpg.pack(pady=(5, 10))

tk.Button(root, text="Seleccionar carpeta", command=save_jpg, **button_style).pack()

tk.Button(root, text="Convertir", command=convert_heic_to_jpg, **button_style).pack(pady=(10, 5))

# Barra de progreso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=(5, 20))

root.mainloop()

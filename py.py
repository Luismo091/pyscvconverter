import tkinter as tk
from tkinter import filedialog
import csv


def convertir_archivo():
    # Abrir el archivo de texto
    ruta_archivo = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        # Crear el nombre de archivo para el archivo CSV
        nombre_archivo_csv = ruta_archivo[:-4] + ".csv"

        # Leer el archivo de texto
        with open(ruta_archivo, 'r') as archivo_txt:
            lineas = archivo_txt.readlines()

        # Escribir los datos en el archivo CSV
        with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for linea in lineas:
                datos = linea.strip().split()  # Separar los datos por espacios
                escritor_csv.writerow(datos)

        # Mostrar un mensaje de éxito
        resultado_label.config(
            text="Archivo convertido con éxito: " + nombre_archivo_csv)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor TXT a CSV")

# Botón para seleccionar el archivo de texto
boton_archivo = tk.Button(
    ventana, text="Seleccionar archivo TXT", command=convertir_archivo)
boton_archivo.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()

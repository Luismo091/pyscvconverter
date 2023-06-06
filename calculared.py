import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox


def procesar_archivo():
    archivo_entrada = filedialog.askopenfilename(
        title="Seleccionar archivo de entrada", filetypes=[("Archivos de texto", "*.txt")])
    if archivo_entrada:
        try:
            fechas_nacimiento = []
            with open(archivo_entrada, 'r') as archivo:
                for linea in archivo:
                    fecha = datetime.strptime(linea.strip(), '%d/%m/%Y')
                    fechas_nacimiento.append(fecha)

            fechas_actuales = [datetime.now()
                               for _ in range(len(fechas_nacimiento))]
            edades = [(fecha_actual.year - fecha_nacimiento.year)
                      for fecha_nacimiento, fecha_actual in zip(fechas_nacimiento, fechas_actuales)]

            archivo_salida = filedialog.asksaveasfilename(
                title="Guardar archivo de salida", defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
            if archivo_salida:
                with open(archivo_salida, 'w', newline='') as archivo_csv:
                    writer = csv.writer(archivo_csv)
                    writer.writerow(["Edad"])
                    writer.writerows(zip(edades))

                messagebox.showinfo(
                    "Proceso completado", "El archivo de salida se ha generado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning(
            "Advertencia", "No se seleccionó ningún archivo de entrada.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de edades")
ventana.geometry("300x200")

# Crear etiqueta y botón de procesar archivo
etiqueta = tk.Label(ventana, text="Seleccione el archivo de entrada")
etiqueta.pack(pady=10)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar_archivo)
boton_procesar.pack(pady=10)

# Ejecutar el bucle de la interfaz
ventana.mainloop()

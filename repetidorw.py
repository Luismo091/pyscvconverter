import csv
import tkinter as tk
from tkinter import messagebox, filedialog

def exportar_a_csv(valores):
    guardar_path = filedialog.asksaveasfilename(defaultextension=".csv")
    if guardar_path:
        with open(guardar_path, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(["Valor"])
            for valor, repeticiones in valores.items():
                for _ in range(repeticiones):
                    writer.writerow([valor])
        messagebox.showinfo("Exportación exitosa", "Los valores se han exportado correctamente.")

def agregar_valor():
    valor = valor_entry.get().strip()
    repeticiones = repeticiones_entry.get().strip()
    
    if valor and repeticiones:
        try:
            repeticiones = int(repeticiones)
            if repeticiones < 1:
                raise ValueError
            valores[valor] = repeticiones
            valores_listbox.insert(tk.END, f"{valor}: {repeticiones}")
            valor_entry.delete(0, tk.END)
            repeticiones_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "La cantidad de repeticiones debe ser un número entero mayor o igual a 1.")
    else:
        messagebox.showerror("Error", "Por favor, ingresa un valor y la cantidad de repeticiones.")

def eliminar_valor():
    seleccion = valores_listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        valor = valores_listbox.get(indice).split(":")[0].strip()
        del valores[valor]
        valores_listbox.delete(indice)
    else:
        messagebox.showerror("Error", "Por favor, selecciona un valor de la lista para eliminar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Exportador CSV")
ventana.geometry("400x300")

# Crear los elementos de la interfaz
valor_label = tk.Label(ventana, text="Valor:")
valor_label.pack()

valor_entry = tk.Entry(ventana)
valor_entry.pack()

repeticiones_label = tk.Label(ventana, text="Repeticiones:")
repeticiones_label.pack()

repeticiones_entry = tk.Entry(ventana)
repeticiones_entry.pack()

agregar_boton = tk.Button(ventana, text="Agregar", command=agregar_valor)
agregar_boton.pack()

valores_listbox = tk.Listbox(ventana)
valores_listbox.pack()

eliminar_boton = tk.Button(ventana, text="Eliminar", command=eliminar_valor)
eliminar_boton.pack()

exportar_boton = tk.Button(ventana, text="Exportar a CSV", command=lambda: exportar_a_csv(valores))
exportar_boton.pack()

# Diccionario para almacenar los valores y sus repeticiones
valores = {}

# Iniciar el programa
ventana.mainloop()

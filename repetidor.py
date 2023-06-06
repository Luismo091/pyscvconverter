import csv

def repetir_valor(numero, valor):
    return valor * int(numero)

# Nombre del archivo de entrada
archivo_entrada = "datos.txt"

# Nombre del archivo CSV de salida
archivo_salida = "resultado.csv"

# Abrir el archivo de entrada en modo lectura
with open(archivo_entrada, 'r') as archivo:
    # Crear un lector CSV
    lector = csv.reader(archivo, delimiter=',')

    # Crear una lista para almacenar los datos repetidos
    datos_repetidos = []

    # Leer cada línea del archivo
    for linea in lector:
        # Obtener el número y el valor de la línea actual
        numero = linea[0]
        valor = linea[1]

        # Repetir el valor según el número proporcionado
        valor_repetido = repetir_valor(numero, valor)

        # Agregar el valor repetido a la lista de datos repetidos
        datos_repetidos.append(valor_repetido)

# Abrir el archivo CSV de salida en modo escritura
with open(archivo_salida, 'w', newline='') as archivo_csv:
    # Crear un escritor CSV
    escritor = csv.writer(archivo_csv)

    # Escribir los datos repetidos en el archivo CSV
    for dato in datos_repetidos:
        escritor.writerow([dato])

print("Los datos repetidos se han exportado correctamente a", archivo_salida)

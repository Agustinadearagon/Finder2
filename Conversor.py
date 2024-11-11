# conversor.py
import pandas as pd
import os

def convertir_a_txt(archivo):
    """ Convierte un archivo CSV o Excel a formato TXT """
    try:
        if archivo.endswith(".csv"):
            df = pd.read_csv(archivo)
        elif archivo.endswith((".xls", ".xlsx")):
            df = pd.read_excel(archivo)
        else:
            raise ValueError("Formato de archivo no compatible")

        nombre_salida = os.path.splitext(archivo)[0] + ".txt"
        df.to_csv(nombre_salida, sep=';', index=False)
        print(f"Archivo convertido a {nombre_salida}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

def ejecutar():
    """ Función principal de ejecución """
    archivo = input("Ingrese el nombre del archivo a convertir: ")
    convertir_a_txt(archivo)

if __name__ == "__main__":
    ejecutar()

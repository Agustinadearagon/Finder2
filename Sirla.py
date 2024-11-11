# Sirla.py
import os
import pandas as pd

def leer_datos(archivo):
    """ Lee un archivo CSV y devuelve un DataFrame """
    try:
        return pd.read_csv(archivo)
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        return None

def procesar_datos(df):
    """ Procesa el DataFrame para obtener resultados """
    try:
        # Aquí va el procesamiento específico
        df['Resultado'] = df['Valor'] * 2  # Ejemplo de procesamiento
        return df
    except KeyError:
        print("Error: El DataFrame no contiene las columnas esperadas.")
        return None

def guardar_resultados(df, archivo_salida):
    """ Guarda el DataFrame procesado en un archivo CSV """
    try:
        df.to_csv(archivo_salida, index=False)
        print(f"Resultados guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def ejecutar():
    """ Función principal para ejecutar el script """
    archivo = input("Ingrese el nombre del archivo CSV: ")
    if os.path.exists(archivo):
        df = leer_datos(archivo)
        if df is not None:
            df = procesar_datos(df)
            if df is not None:
                archivo_salida = 'resultados_sirla.csv'
                guardar_resultados(df, archivo_salida)
    else:
        print(f"El archivo {archivo} no existe.")

if __name__ == "__main__":
    ejecutar()

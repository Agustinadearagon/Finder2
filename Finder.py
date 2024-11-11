# Finder.py
import os

def buscar_archivos(directorio, extension):
    """ Busca archivos con una extensión específica en un directorio """
    try:
        archivos_encontrados = [f for f in os.listdir(directorio) if f.endswith(extension)]
        return archivos_encontrados
    except FileNotFoundError:
        print(f"El directorio {directorio} no fue encontrado.")
        return []

def ejecutar():
    """ Función principal para buscar archivos """
    directorio = input("Ingrese el directorio donde buscar: ")
    extension = input("Ingrese la extensión del archivo (por ejemplo, .txt): ")
    archivos = buscar_archivos(directorio, extension)
    if archivos:
        print(f"Archivos encontrados: {', '.join(archivos)}")
    else:
        print("No se encontraron archivos.")

if __name__ == "__main__":
    ejecutar()

# hacha.py
import os

def cortar_archivo(archivo, partes):
    """ Divide un archivo en partes iguales """
    try:
        tamaño_archivo = os.path.getsize(archivo)
        tamaño_parte = tamaño_archivo // partes
        with open(archivo, 'rb') as f:
            for i in range(partes):
                with open(f'{archivo}_parte_{i + 1}', 'wb') as salida:
                    salida.write(f.read(tamaño_parte))
        print(f"Archivo {archivo} dividido en {partes} partes.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error al cortar el archivo: {e}")

def ejecutar():
    """ Función principal de ejecución """
    archivo = input("Ingrese el nombre del archivo a cortar: ")
    partes = int(input("Ingrese el número de partes: "))
    cortar_archivo(archivo, partes)

if __name__ == "__main__":
    ejecutar()

# Finder2
# readme.py
import os

def generar_readme():
    """ Genera un archivo README básico para el proyecto """
    contenido = """
    # Proyecto Herramientas

    Este proyecto contiene varias herramientas útiles para procesamiento de archivos.

    ## Scripts:
    - **menú.py**: Interfaz principal del programa.
    - **Sirla.py**: Procesamiento de datos desde archivos CSV.
    - **Hacha.py**: Divide archivos grandes en partes.
    - **Conversor.py**: Convierte archivos CSV o Excel a formato TXT.
    - **Finder.py**: Busca archivos en un directorio con una extensión específica.
    
    ## Uso:
    - Ejecutar los scripts desde el menú principal o directamente desde la terminal.
    """
    with open("README.md", 'w') as f:
        f.write(contenido)
    print("README.md generado exitosamente.")

if __name__ == "__main__":
    generar_readme()

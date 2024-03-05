# Importaciones

import os

rutaCarpeta = 'C:/Users/ALEJANDRO/Desktop/AppContadorCarpeta/pythonContadorCarpeta/CarpetaArchivos'


def contar_archivos_en_carpeta(carpeta):
    total_archivos = 0
    for ruta, carpetas, archivos in os.walk(carpeta):
        total_archivos += len(archivos)
    return total_archivos


def main():
    carpeta = rutaCarpeta
    total_archivos = contar_archivos_en_carpeta(carpeta)
    ruta_txt = os.path.abspath(os.path.join(os.getcwd(), "../", "../", "total_archivos.txt"))
    with open(ruta_txt, "w") as archivo_txt:
        archivo_txt.write(f"El total de archivos {total_archivos}")


if __name__ == "__main__":
    main()

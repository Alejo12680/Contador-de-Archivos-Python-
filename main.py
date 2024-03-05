# Importaciones

import os

rutaCarpeta = 'C:/Users/ALEJANDRO/Desktop/AppContadorCarpeta/pythonContadorCarpeta/CarpetaArchivos'


def contar_archivos_en_carpeta(carpeta):
    total_archivos = 0
    total_subcarpetas = 0
    for ruta, carpetas, archivos in os.walk(carpeta):
        total_archivos += len(archivos)
        total_subcarpetas += len(carpetas)
    return total_archivos, total_subcarpetas


def main():
    carpeta = rutaCarpeta
    total_archivos, total_subcarpetas = contar_archivos_en_carpeta(carpeta)
    ruta_txt = os.path.abspath(os.path.join(os.getcwd(), "../", "../", "Contador.txt"))
    with open(ruta_txt, "w") as archivo_txt:
        archivo_txt.write(f"El total de Archivos: {total_archivos}, El total de Subcarpetas: {total_subcarpetas}")


if __name__ == "__main__":
    main()

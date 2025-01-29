import os
import re

RUTA_ORIGEN = './paginas'
RUTA_DESTINO = './paginas_limpias'


os.makedirs(RUTA_DESTINO, exist_ok=True)


def guardarTexto(texto: str, nombre_archivo: str) -> None:
    """
    Guarda el texto en un archivo.

    Args:
        texto (str): El texto a guardar.
        nombre_archivo (str): El nombre del archivo.
    """
    with open(os.path.join(RUTA_DESTINO, nombre_archivo), 'w', encoding='utf-8') as f:
        f.write(texto)


def limparTexto(texto: str, file: str) -> None:
    """
    Limpia el texto eliminando saltos de línea innecesarios y guarda el resultado.

    Args:
        texto (str): El texto a limpiar.
        file (str): El nombre del archivo.
    """
    texto = re.sub(r" \n", " ", texto)
    guardarTexto(texto, file)


def main():
    """
    Función principal del programa.
    Recorre los archivos de texto en la ruta de origen, los limpia y los guarda en la ruta de destino.
    """
    for root, _, files in os.walk(RUTA_ORIGEN):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    texto = f.read()
                    limparTexto(texto, file)


if __name__ == '__main__':
    main()

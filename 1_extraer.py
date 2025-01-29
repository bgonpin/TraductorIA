import PyPDF2
import os


def crearTxt(numero: int, texto: str) -> bool:
    """
    Crea un archivo de texto con el contenido dado.

    Args:
        numero (int): El número de página para el nombre del archivo.
        texto (str): El texto a escribir en el archivo.

    Returns:
        bool: True si el archivo se creó correctamente.
    """
    with open(f'./paginas/{numero}.txt', 'w', encoding='utf-8') as f:
        f.write(texto)
    return True


def extraerTexto(pdf: str) -> str:
    """
    Extrae el texto de un archivo PDF y lo guarda en archivos de texto individuales.

    Args:
        pdf (str): La ruta al archivo PDF.

    Returns:
        str: El texto concatenado de todas las páginas del PDF.
    """
    texto = ''
    contador = 1
    with open(pdf, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            texto_pagina = page.extract_text()
            crearTxt(contador, texto_pagina)
            texto += texto_pagina
            contador += 1
    return texto


def main():
    """
    Función principal del programa.
    Extrae el texto de un PDF y lo guarda en archivos de texto.
    """
    pdf = 'a-christmas-carol-charles-dickens.pdf'
    extraerTexto(pdf)


if __name__ == '__main__':
    main()

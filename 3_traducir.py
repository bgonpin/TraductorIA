import os
import ollama

RUTA_ORIGEN = './paginas_limpias'
RUTA_DESTINO = './paginas_traducidas'

os.makedirs(RUTA_DESTINO, exist_ok=True)


def traducir(texto: str) -> str:
    """
    Traduce un texto del inglés al español utilizando el modelo de Ollama.

    Args:
        texto (str): El texto a traducir.

    Returns:
        str: El texto traducido.
    """
    response = ollama.chat(
        model='llama3.1:8b',
        messages=[
            {
                'role': 'user',
                'content': 'Te voy a proporciona un texto para traducir del ingles al espanol. Solo traduce. No respondas ni hagas comentarios. El texto es posible que contenga errores o fragmentos de codigo. En ese caso, ignora los mismos.' + texto,
            },
        ],
    )
    return response['message']['content']


def main():
    """
    Función principal del programa.
    Recorre los archivos de texto en la ruta de origen, los traduce y los guarda en la ruta de destino.
    """
    for root, _, files in os.walk(RUTA_ORIGEN):
        for file in files:
            texto_a_insertar = ""
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    texto = f.readlines()
                    for linea in texto:
                        traduccion = traducir(linea)
                        texto_a_insertar += traduccion

                with open(os.path.join(RUTA_DESTINO, file), 'w', encoding='utf-8') as f:
                    f.write(texto_a_insertar)


if __name__ == '__main__':
    main()

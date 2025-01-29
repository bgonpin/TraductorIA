import fitz
import os

RUTA_DESTINO_IMAGENES = './imagen_pdf'

os.makedirs(RUTA_DESTINO_IMAGENES, exist_ok=True)


def extraerImagenesPdf(pdf: str) -> None:
    """
    Extrae las imágenes de un archivo PDF y las guarda como archivos PNG.

    Args:
        pdf (str): La ruta al archivo PDF.
    """
    pdf_document = fitz.open(pdf)
    for page_index in range(len(pdf_document)):
        page = pdf_document[page_index]
        image_list = page.get_images()
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_data = base_image["image"]
            if len(image_list) > 1:
                nombre_archivo = f"imagen_{page_index}_{image_index}.png"
            else:
                nombre_archivo = f"imagen_{page_index}.png"
            ruta_archivo = os.path.join(RUTA_DESTINO_IMAGENES, nombre_archivo)
            with open(ruta_archivo, "wb") as fp:
                fp.write(image_data)


def main():
    """
    Función principal del programa.
    Extrae las imágenes de un PDF específico.
    """
    extraerImagenesPdf("Deep Reinforcement Learning with Python (2024).pdf")


if __name__ == "__main__":
    main()

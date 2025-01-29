# 🎨 Traductor IA 🤖

Este proyecto es un traductor que utiliza inteligencia artificial.

## 📝 Descripción

Este proyecto toma un archivo PDF como entrada, extrae el texto, lo limpia, lo traduce y extrae las imágenes.

## 🚀 Uso

1.  Ejecutar `1_extraer.py` para extraer el texto del PDF.
2.  Ejecutar `2_limpiar.py` para limpiar el texto extraído.
3.  Ejecutar `3_traducir.py` para traducir el texto limpio.
4.  Ejecutar `4_extraer_imagenes.py` para extraer las imágenes del PDF.

## 🗂️ Estructura del proyecto

*   `1_extraer.py`: Script para extraer el texto del PDF.
*   `2_limpiar.py`: Script para limpiar el texto extraído.
*   `3_traducir.py`: Script para traducir el texto limpio.
*   `4_extraer_imagenes.py`: Script para extraer las imágenes del PDF.
*   `paginas/`: Directorio que contiene los archivos de texto extraídos del PDF.
*   `paginas_limpias/`: Directorio que contiene los archivos de texto limpios.
*   `paginas_traducidas/`: Directorio que contiene los archivos de texto traducidos.
*   `a-christmas-carol-charles-dickens.pdf`: Archivo PDF de ejemplo.
*   `ollama-python-main.tar.gz`: Archivo comprimido con el modelo de lenguaje.

## ⚙️ Dependencias

*   Python 3.6 o superior
*   `PyPDF2`
*   `requests`
*   `beautifulsoup4`
*   `transformers`
*   `torch`
*   `sentencepiece`
*   `accelerate`
*   `ollama`

## 🛠️ Instalación

1.  Clonar el repositorio.
2.  Instalar las dependencias con `pip install -r requirements.txt`.
3.  Descargar el modelo de lenguaje `ollama-python-main.tar.gz` y descomprimirlo.
4.  Ejecutar `ollama serve` para iniciar el servidor de ollama.

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, crea un pull request con tus cambios.

## 📜 Licencia

Este proyecto está bajo la licencia MIT.

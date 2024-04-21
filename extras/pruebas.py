import re
from bs4 import BeautifulSoup

def contar_imagenes(texto):


    # Analizar el HTML usando BeautifulSoup
    soup = BeautifulSoup(texto, 'html.parser')

    # Encontrar todas las etiquetas <img>
    imagenes = soup.find_all('img')

    # Contar el número de imágenes
    numero_imagenes = len(imagenes)

    # Ignorar las imágenes que no tienen el atributo src
    for imagen in imagenes:
        if not imagen.get('src'):
            numero_imagenes -= 1

    return numero_imagenes













import re

def tiene_alt(texto):
    """
    Verifica si el texto contiene atributos 'alt' en las etiquetas de imagen.

    Args:
        texto: El texto HTML que se va a analizar.

    Returns:
        True si al menos una etiqueta de imagen tiene un atributo 'alt', False de lo contrario.
    """
    # Expresión regular para buscar atributos 'alt' en etiquetas de imagen
    regex = re.compile(r'<img\s+.*?alt="(.*?)"', re.IGNORECASE)

    # Buscar todas las coincidencias en el texto
    matches = regex.findall(texto)

    # Si hay al menos una coincidencia, retornar True
    if matches:
        return True
    else:
        return False

def contar_signos_exclamacion(texto_html):
    """
    Cuenta el número de signos de admiración en el contenido de un texto HTML.

    Args:
        texto_html: El texto HTML en el que se van a contar los signos de admiración.

    Returns:
        El número de signos de admiración en el contenido del texto HTML.
    """
    # Analizar el HTML utilizando BeautifulSoup
    soup = BeautifulSoup(texto_html, 'html.parser')

    # Obtener el contenido del texto sin etiquetas HTML ni comentarios
    contenido = soup.get_text()

    # Contar los signos de admiración en el contenido
    return contenido.count('!')

def tiene_mayusculas(texto_html, umbral=10):
    """
    Verifica si hay muchas mayúsculas en un texto HTML.

    Args:
        texto_html: El texto HTML en el que se va a verificar la presencia de mayúsculas.
        umbral: El umbral para determinar si hay "muchas" mayúsculas.

    Returns:
        True si hay más de 'umbral' mayúsculas, False de lo contrario.
    """
    # Analizar el HTML utilizando BeautifulSoup
    soup = BeautifulSoup(texto_html, 'html.parser')

    # Obtener el contenido visible del texto
    contenido_visible = soup.get_text()

    # Contar las mayúsculas en el contenido visible
    return sum(1 for c in contenido_visible if c.isupper()) > umbral
def imagenes_grandes(texto_html):
    soup = BeautifulSoup(texto_html, 'html.parser')

    # Verificar si hay imágenes grandes
    imagenes = soup.find_all('img')
    for imagen in imagenes:
        if 'width' in imagen.attrs and 'height' in imagen.attrs:
            if int(imagen['width']) > 600 or int(imagen['height']) > 600:
                recomendaciones.append("Evitar imágenes grandes, ya que pueden aumentar la tasa de spam.")
    adjuntos = soup.find_all('a', href=True)
    for adjunto in adjuntos:
        if any(extension in adjunto['href'] for extension in ['.doc', '.pdf', '.xls', '.zip']):
            recomendaciones.append("Evitar archivos adjuntos, ya que pueden aumentar la tasa de spam.")
        palabras_sospechosas = {
        "dinero": "Evita el uso de términos relacionados con dinero en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "suerte": "Evita el uso de términos relacionados con la suerte en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "precio": "Evita el uso de términos relacionados con precios en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "oferta": "Evita el uso de términos relacionados con ofertas en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "rebajas": "Evita el uso de términos relacionados con rebajas en exceso, ya que pueden hacer que el correo se catalogue como spam."
        # Agrega más palabras y recomendaciones según sea necesario
    }

    # Lista para almacenar palabras sospechosas detectadas y sus recomendaciones
    resultados = []

    # Analizar el HTML utilizando BeautifulSoup
    soup = BeautifulSoup(texto_html, 'html.parser')

    # Obtener el contenido visible del texto
    contenido_visible = soup.get_text()

    # Buscar palabras sospechosas en el contenido visible
    for palabra, recomendacion in palabras_sospechosas.items():
        if palabra in contenido_visible.lower():
            resultados.append((palabra, recomendacion))

    # Verificar enlaces raros
    enlaces = soup.find_all('a', href=True)
    for enlace in enlaces:
        if "%" in enlace['href'] or "$" in enlace['href']:
            resultados.append((enlace['href'], "Evita enlaces raros, ya que pueden hacer que el correo se catalogue como spam."))

    return resultados
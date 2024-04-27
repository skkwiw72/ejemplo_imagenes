from django.shortcuts import render
from email.mime.image import MIMEImage
import random
import time
import mimetypes
import pandas as pd
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


import re
import smtplib
import dns.resolver
import pandas as pd


import io
def html_to_text(file_html):
    # Leer el contenido del archivo HTML como texto
    html_text = file_html.read().decode("utf-8")  # Decodificar el contenido como texto UTF-8
    return html_text

@login_required
def verificadorspam(request):
    return render(request, 'verificadorspam.html')

def detectar_spam(texto_html):
    recomendaciones = {
        "imagenes": "EL uso de imagenes puede indicar spam",
        "Sin alt": "Algunas imágenes no tienen atributo 'alt', lo cual puede afectar la accesibilidad y ser considerado spam.",
        "Exclamaciones": "Exceso de signos de exclamación puede ser considerado spam.",
        "Mayusculas": "Exceso de mayúsculas puede ser considerado spam."
    }

    # Contar imágenes
    def contar_imagenes(texto):
        soup = BeautifulSoup(texto, 'html.parser')
        imagenes = soup.find_all('img')
        numero_imagenes = len(imagenes)
        for imagen in imagenes:
            if not imagen.get('src'):
                numero_imagenes -= 1
        return numero_imagenes

    # Verificar si tiene atributos 'alt' en las imágenes
    def tiene_alt(texto):
        regex = re.compile(r'<img\s+.*?alt="(.*?)"', re.IGNORECASE)
        matches = regex.findall(texto)
        return bool(matches)

    # Contar signos de exclamación
    def contar_signos_exclamacion(texto_html):
        soup = BeautifulSoup(texto_html, 'html.parser')
        contenido = soup.get_text()
        return contenido.count('!')

    # Verificar mayúsculas
    def tiene_mayusculas(texto_html, umbral=5):
        soup = BeautifulSoup(texto_html, 'html.parser')
        contenido_visible = soup.get_text(separator=" ")
        contenido_sin_etiquetas = BeautifulSoup(contenido_visible, 'html.parser').get_text(separator=" ")
        return sum(1 for c in contenido_sin_etiquetas if c.isupper()) > umbral

    # Llamadas a funciones
    num_imagenes = contar_imagenes(texto_html)
    if num_imagenes > 1:
       recomendaciones["No imagenes"] = "Hay más de una imagen en el correo."
    if not tiene_alt(texto_html):
        recomendaciones["Sin alt"]
    num_exclamaciones = contar_signos_exclamacion(texto_html)
    if num_exclamaciones > 3:
        recomendaciones["Exclamaciones"]
    if tiene_mayusculas(texto_html):
        recomendaciones["Mayusculas"]

    return recomendaciones

def imagenes_grandes_y_adjuntos(texto_html):
    recomendaciones = []
    soup = BeautifulSoup(texto_html, 'html.parser')
    imagenes = soup.find_all('img')
    for imagen in imagenes:
        if 'width' in imagen.attrs and 'height' in imagen.attrs:
            if int(imagen['width']) > 600 or int(imagen['height']) > 600:
                recomendaciones.append("Evitar imágenes grandes, ya que pueden aumentar la tasa de spam.")
    adjuntos = soup.find_all('a', href=True)
    for adjunto in adjuntos:
        if any(extension in adjunto['href'] for extension in ['.doc', '.pdf', '.xls', '.zip']):
            recomendaciones.append("Evitar archivos adjuntos, ya que pueden aumentar la tasa de spam.")
    return recomendaciones

def palabras_sospechosas_y_enlaces_raros(texto_html):
    recomendaciones = []
    palabras_sospechosas = {
        "dinero": "Evita el uso de términos relacionados con dinero en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "suerte": "Evita el uso de términos relacionados con la suerte en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "precio": "Evita el uso de términos relacionados con precios en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "oferta": "Evita el uso de términos relacionados con ofertas en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "rebajas": "Evita el uso de términos relacionados con rebajas en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "explota": "Evitar usar este verbo en correos electrónicos, ya que puede sonar agresivo o engañoso.",
        "ventas online": "Utilizar un término más específico como \"aumenta tus ventas online\" o \"potencia tu negocio online\".",
        "mayor tráfico": "Utilizar un término más específico como \"aumenta el tráfico a tu web\" o \"mejora tu posicionamiento SEO\".",
        "vende más": "Utilizar un término más específico como \"aumenta tus ventas\" o \"consigue más clientes\".",
        """100% satisfecho""": "Evitar usar este tipo de afirmaciones absolutas, ya que pueden sonar poco creíbles.",
        "sin riesgos": "Evitar usar este tipo de afirmaciones, ya que pueden sonar poco creíbles.",
        "únete a millones de personas": "Evitar usar este tipo de afirmaciones genéricas, ya que no son muy convincentes.",
        "satisfacción garantizada": "Evitar usar este tipo de afirmaciones absolutas, ya que pueden sonar poco creíbles.",
        "esto no es spam": "No es necesario mencionar que el correo electrónico no es spam, ya que esto puede hacer que parezca sospechoso.",
        "gratis": "Utilizar esta palabra con moderación, ya que puede sonar demasiado bueno para ser verdad.",
        "visa": "Evitar mencionar marcas específicas de tarjetas de crédito.",
        "mastercard": "Evitar mencionar marcas específicas de tarjetas de crédito.",
        "paypal": "Evitar mencionar marcas específicas de métodos de pago.",
        "oportunidad": "Utilizar un término más específico como \"aprovecha esta oportunidad\" o \"no pierdas esta oportunidad\".",
        "no pierdas": "Utilizar un término más específico como \"no pierdas esta oportunidad\" o \"aprovecha esta oferta\".",
        "exclusivo": "Utilizar esta palabra con moderación, ya que puede sonar poco creíble.",
        "urgente": "Evitar usar esta palabra unless it is truly urgent.",
        "última oportunidad": "Evitar usar esta palabra con demasiada frecuencia, ya que puede perder su efecto.",
        "oferta increíble": "Evitar usar este tipo de superlativos, ya que pueden sonar poco creíbles.",
        "no te lo pierdas": "Utilizar un término más específico como \"aprovecha esta oportunidad\" o \"no pierdas esta oferta\".",
        "actúa ahora": "Utilizar una llamada a la acción más específica, como \"haz clic aquí\" o \"compra ahora\".",
        "adelgaza": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "aceptamos tarjetas de crédito": "Evitar mencionar métodos de pago en el asunto del correo electrónico.",
        "haz clic en este enlace": "Utilizar una llamada a la acción más específica, como \"haz clic aquí\" o \"visita nuestro sitio web\".",
        "compra ahora mismo": "Utilizar una llamada a la acción más específica, como \"compra ahora\" o \"no pierdas esta oferta\".",
        "compra ya": "Utilizar una llamada a la acción más específica, como \"compra ahora\" o \"no pierdas esta oferta\".",
        "unidades limitadas": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "milagroso": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "resultados garantizados": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "sin esfuerzo": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "rejuvenece": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
"aumenta": "Utilizar un término más específico como \"aumenta tus ventas\" o \"mejora tu rendimiento\".",
"mejora": "Utilizar un término más específico como \"mejora tu salud\" o \"mejora tu vida\".",
"potente": "Evitar usar este tipo de superlativos, ya que pueden sonar poco creíbles.",
"secreto": "Evitar usar este tipo de palabras, ya que pueden sonar poco confiables.",
"revolucionario": "Evitar usar este tipo de superlativos, ya que pueden sonar poco creíbles.",
"lotería": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"sorteo": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"premio": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"ganador": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"felicidades": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"reclama tu premio": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"última oportunidad para ganar": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
"inversión": "Utilizar un término más específico como \"invierte en tu futuro\" o \"inicia tu propio negocio\".",
"negocio": "Utilizar un término más específico como \"emprendedor\" o \"inicia tu propio negocio\".",
"fortuna": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
"millonario": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
"rápido": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
"fácil": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
"sin riesgo": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
"gana dinero desde casa": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
"trabaja desde casa": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
"¡atención!": "Evitar usar este tipo de palabras en el asunto del correo electrónico.",
"importante": "Evitar usar este tipo de palabras en el asunto del correo electrónico.",
"confidencial": "Evitar usar este tipo de palabras en el asunto del correo electrónico.",
"gratis": "Utilizar esta palabra con moderación, ya que puede sonar demasiado bueno para ser verdad.",
"suscríbete": "Utilizar una llamada a la acción más específica, como \"suscríbete a nuestra newsletter\" o \"recibe ofertas exclusivas\".",
"haz clic aquí": "Utilizar una llamada a la acción más específica, como \"haz clic aquí\" o \"visita nuestro sitio web\".",
"oferta por tiempo limitado": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
"oferta válida hasta agotar existencias": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading."
    }
    soup = BeautifulSoup(texto_html, 'html.parser')
    contenido_visible = soup.get_text()
    for palabra, recomendacion in palabras_sospechosas.items():
        if palabra in contenido_visible.lower():
            recomendaciones.append((palabra, recomendacion))
    enlaces = soup.find_all('a', href=True)
    for enlace in enlaces:
        if "%" in enlace['href'] or "$" in enlace['href']:
            recomendaciones.append((enlace['href'], "Evita enlaces raros, ya que pueden hacer que el correo se catalogue como spam."))
    return recomendaciones











####################################################
def detectar_palabras_sospechosas(texto_correo):
    recomendaciones = []

    palabras_sospechosas = {
        "dinero": "Evita el uso de términos relacionados con dinero en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "suerte": "Evita el uso de términos relacionados con la suerte en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "precio": "Evita el uso de términos relacionados con precios en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "oferta": "Evita el uso de términos relacionados con ofertas en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "rebajas": "Evita el uso de términos relacionados con rebajas en exceso, ya que pueden hacer que el correo se catalogue como spam.",
        "explota": "Evitar usar este verbo en correos electrónicos, ya que puede sonar agresivo o engañoso.",
        "ventas online": "Utilizar un término más específico como \"aumenta tus ventas online\" o \"potencia tu negocio online\".",
        "mayor tráfico": "Utilizar un término más específico como \"aumenta el tráfico a tu web\" o \"mejora tu posicionamiento SEO\".",
        "vende más": "Utilizar un término más específico como \"aumenta tus ventas\" o \"consigue más clientes\".",
        """100% satisfecho""": "Evitar usar este tipo de afirmaciones absolutas, ya que pueden sonar poco creíbles.",
        "sin riesgos": "Evitar usar este tipo de afirmaciones, ya que pueden sonar poco creíbles.",
        "únete a millones de personas": "Evitar usar este tipo de afirmaciones genéricas, ya que no son muy convincentes.",
        "satisfacción garantizada": "Evitar usar este tipo de afirmaciones absolutas, ya que pueden sonar poco creíbles.",
        "esto no es spam": "No es necesario mencionar que el correo electrónico no es spam, ya que esto puede hacer que parezca sospechoso.",
        "gratis": "Utilizar esta palabra con moderación, ya que puede sonar demasiado bueno para ser verdad.",
        "visa": "Evitar mencionar marcas específicas de tarjetas de crédito.",
        "mastercard": "Evitar mencionar marcas específicas de tarjetas de crédito.",
        "paypal": "Evitar mencionar marcas específicas de métodos de pago.",
        "oportunidad": "Utilizar un término más específico como \"aprovecha esta oportunidad\" o \"no pierdas esta oportunidad\".",
        "no pierdas": "Utilizar un término más específico como \"no pierdas esta oportunidad\" o \"aprovecha esta oferta\".",
        "exclusivo": "Utilizar esta palabra con moderación, ya que puede sonar poco creíble.",
        "urgente": "Evitar usar esta palabra unless it is truly urgent.",
        "última oportunidad": "Evitar usar esta palabra con demasiada frecuencia, ya que puede perder su efecto.",
        "oferta increíble": "Evitar usar este tipo de superlativos, ya que pueden sonar poco creíbles.",
        "no te lo pierdas": "Utilizar un término más específico como \"aprovecha esta oportunidad\" o \"no pierdas esta oferta\".",
        "actúa ahora": "Utilizar una llamada a la acción más específica, como \"haz clic aquí\" o \"compra ahora\".",
        "adelgaza": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "aceptamos tarjetas de crédito": "Evitar mencionar métodos de pago en el asunto del correo electrónico.",
        "haz clic en este enlace": "Utilizar una llamada a la acción más específica, como \"haz clic aquí\" o \"visita nuestro sitio web\".",
        "compra ahora mismo": "Utilizar una llamada a la acción más específica, como \"compra ahora\" o \"no pierdas esta oferta\".",
        "compra ya": "Utilizar una llamada a la acción más específica, como \"compra ahora\" o \"no pierdas esta oferta\".",
        "unidades limitadas": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "milagroso": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "resultados garantizados": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "sin esfuerzo": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "rejuvenece": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "aumenta": "Utilizar un término más específico como \"aumenta tus ventas\" o \"mejora tu rendimiento\".",
        "mejora": "Utilizar un término más específico como \"mejora tu salud\" o \"mejora tu vida\".",
        "potente": "Evitar usar este tipo de superlativos, ya que pueden sonar poco creíbles.",
        "secreto": "Evitar usar este tipo de palabras, ya que pueden sonar poco confiables.",
        "revolucionario": "Evitar usar este tipo de superlativos, ya que pueden sonar poco creíbles.",
        "lotería": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "sorteo": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "premio": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "ganador": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "felicidades": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "reclama tu premio": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "última oportunidad para ganar": "Evitar usar este tipo de palabras en correos electrónicos, ya que pueden sonar como spam.",
        "inversión": "Utilizar un término más específico como \"invierte en tu futuro\" o \"inicia tu propio negocio\".",
        "negocio": "Utilizar un término más específico como \"emprendedor\" o \"inicia tu propio negocio\".",
        "fortuna": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
        "millonario": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
        "rápido": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
        "fácil": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
        "sin riesgo": "Evitar usar este tipo de palabras, ya que pueden sonar poco creíbles.",
        "gana dinero desde casa": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "trabaja desde casa": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "¡atención!": "Evitar usar este tipo de palabras en el asunto del correo electrónico.",
        "importante": "Evitar usar este tipo de palabras en el asunto del correo electrónico.",
        "confidencial": "Evitar usar este tipo de palabras en el asunto del correo electrónico.",
        "gratis": "Utilizar esta palabra con moderación, ya que puede sonar demasiado bueno para ser verdad.",
        "suscríbete": "Utilizar una llamada a la acción más específica, como \"suscríbete a nuestra newsletter\" o \"recibe ofertas exclusivas\".",
        "haz clic aquí": "Utilizar una llamada a la acción más específica, como \"haz clic aquí\" o \"visita nuestro sitio web\".",
        "oferta por tiempo limitado": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading.",
        "oferta válida hasta agotar existencias": "Evitar usar este tipo de claims in a spam email, as it may be considered misleading."
    }

    for palabra, recomendacion in palabras_sospechosas.items():
        if palabra in texto_correo.lower():
            recomendaciones.append((palabra, recomendacion))

    return recomendaciones
def detectar_spam_correo(texto_correo):
    recomendaciones = {
        "Exclamaciones": "Exceso de signos de exclamación puede ser considerado spam.",
        "Mayusculas": "Exceso de mayúsculas puede ser considerado spam."
    }

    # Contar signos de exclamación
    def contar_signos_exclamacion(texto):
        return texto.count('!')

    # Verificar mayúsculas
    def tiene_mayusculas(texto, umbral=5):
        return sum(1 for c in texto if c.isupper()) > umbral

    # Llamadas a funciones
    num_exclamaciones = contar_signos_exclamacion(texto_correo)
    if num_exclamaciones > 3:
        recomendaciones["Exclamaciones"]

    if tiene_mayusculas(texto_correo):
        recomendaciones["Mayusculas"]

    return recomendaciones

# Uso de la función
def searchspam(request):
    if request.method == 'POST':
        file_html = request.FILES.get('codigo_html')
        html_correo = request.POST.get('htmlcorreo')

        
        if file_html:
            print(file_html)
            texto_html = html_to_text(file_html)
            print(texto_html)
            recomendaciones_spam = detectar_spam(texto_html)
            recomendaciones_imagenes_adjuntos = imagenes_grandes_y_adjuntos(texto_html)
            recomendaciones_palabras_enlaces = palabras_sospechosas_y_enlaces_raros(texto_html)
            
            # Combina todas las recomendaciones en una lista única
            recomendaciones_totales = list(recomendaciones_spam.values()) + recomendaciones_imagenes_adjuntos + recomendaciones_palabras_enlaces
            
            # Haz lo que necesites con las recomendaciones, por ejemplo, devolverlas como parte del contexto de renderizado
            print(recomendaciones_totales)
            resultados = pd.DataFrame(recomendaciones_totales, columns=['Recomendaciones'])
        if html_correo:
            recomendaciones_palabras_sospechosas = detectar_palabras_sospechosas(html_correo)
            print(recomendaciones_palabras_sospechosas)
            recomendaciones_spama = detectar_spam_correo(html_correo)
            recomendaciones_totales = list(recomendaciones_spama.values()) + recomendaciones_palabras_sospechosas
            resultados = pd.DataFrame(recomendaciones_totales, columns=['Recomendaciones'])
            
            
             
    return render(request, 'results2spam.html', {'resultados': resultados})
            
            
    





           
            
























@login_required
def MailVerifier(request):
    return render(request, 'MailVerifier.html')
def check(addressToVerify):
    fromAddress = 'corn@bt.com'
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    
    # Syntax check
    match = re.match(regex, addressToVerify)
    if match is None:
        return False

    # Check if the address is a Gmail address
    if 'gmail.com' not in addressToVerify:
        print(f'\033[31m{{+}} Email: {addressToVerify} is NOT a Gmail address.\033[00m')
        return False

    try:
        # Get domain for DNS lookup
        splitAddress = addressToVerify.split('@')
        domain = str(splitAddress[1])

        # MX record lookup
        records = dns.resolver.resolve(domain, 'MX')
        mxRecord = str(records[0].exchange)

        # SMTP lib setup
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(server.local_hostname)
        server.mail(fromAddress)
        code, message = server.rcpt(str(addressToVerify))
        server.quit()

        # Assume SMTP response 250 is success
        if code == 250:
            print('\033[31m{+} Email: '+addressToVerify+' is valid! :)\033[00m')
            return True
        else:
            return False
    except Exception as e:
        print(f'\033[31mError verifying {addressToVerify}: {str(e)}\033[00m')
        return False
@login_required
def creador_plantillas(request):
    return render(request, 'creador_plantillas.html')
@csrf_exempt
def default(request):
    return render(request, 'default.html')      



















































def search_mail_verifier(request):
    if request.method == 'POST':
        valid_emails = []
        email_addresses = []
        print("huedhuw")
        
        file = request.FILES.get('exampleInputFile')
        print(file)


        correos = str(request.POST.get('correos'))
        print(correos)
        if len(correos) == 0:
            print(1)

            if file.name.endswith('.txt'):

                print(2)

                for line in file:
                    decoded_line = line.decode('utf-8')
                    decoded_line1 = decoded_line.strip()
                    print(decoded_line1)
                    
                    if check(decoded_line1):
                        print(383823)
                        email_addresses.append(decoded_line1)
                        print(email_addresses)
                resultados = pd.DataFrame(email_addresses, columns=['Valid_Emails'])
                print(resultados)
                return render(request, 'results2.html', {'resultados': resultados})
            if file.name.endswith('.csv'):
                print(3)
                df = pd.read_csv(file)
                print(df)
                for email in df['Email']:
                    if check(email):
                        email_addresses.append(email)
                resultados = pd.DataFrame(email_addresses, columns=['Valid_Emails'])
                print(resultados)
                return render(request, 'results2.html', {'resultados': resultados})
            if file.name.endswith('.xlsx'):
                print(4)
                df = pd.read_excel(file)
                print(df)
                for email in df['Email']:
                    if check(email):
                        email_addresses.append(email)
                resultados = pd.DataFrame(email_addresses, columns=['Valid_Emails'])
                print(resultados)
                return render(request, 'results2.html', {'resultados': resultados})
                    

            # Verifica cada dirección de correo electrónico
                
            else:
                 return HttpResponse("El archivo no es de texto, xlsx o csv")
            # Crea un DataFrame de Pandas con las direcciones de correo electrónico válidas
                
                





        else:
             email_addresses =correos.split(" ")
                    
        # Verifica cada dirección de correo electrónico
             valid_emails = [email for email in email_addresses if check(email)]

        # Crea un DataFrame de Pandas con las direcciones de correo electrónico válidas
             resultados = pd.DataFrame(valid_emails, columns=['Valid_Emails'])
             print(resultados)
             return render(request, 'results2.html', {'resultados': resultados})

    return render(request, 'MailVerifier.html')

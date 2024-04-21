from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from selenium.webdriver.chrome.service import Service
import keyboard

# Create your views here.


def mailsender(request):
    return render(request, 'mail_sender.html')
from email.mime.image import MIMEImage
import random
import time
import mimetypes
import pandas as pd
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import os

def generar_numero_desde_texto(texto_rango):
    # Dividir el texto del rango en los límites inferior y superior
    limites = texto_rango.split('-')
    limite_inferior = int(limites[0])
    limite_superior = int(limites[1])
    # Generar y devolver un número aleatorio dentro del rango
    return random.randint(limite_inferior, limite_superior)

def html_to_text(html_content):
    # Crear un objeto BeautifulSoup a partir del contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Obtener el texto del documento HTML
    text = soup.get_text()
    return text

def enviomail(request):

    if request.method == 'POST':
        print(1)
        
        intervalo_str = request.POST.get('intervalo', '') 

# Convertir a entero si el valor no está vacío, de lo contrario, establecer en 0
        intervalo = int(intervalo_str) if intervalo_str else 0
        aleatorio_str = request.POST.get('aleatorio', '') 
        # Convertir a entero si el valor no está vacío, de lo contrario, establecer en 0
        aleatorio = str(aleatorio_str) if aleatorio_str else 0

        # Obtener el valor de cliledsend de la solicitud POST
        cliledsend_str = request.POST.get('cliledsend', '') 
        print(2)
        # Convertir a entero si el valor no está vacío, de lo contrario, establecer en 0
        cliledsend = int(cliledsend_str) if cliledsend_str else 0
        
        
        contraseñas = []
        cuentas = []
        
        emails = []
        emails_subject = []
        email_adresses = []
        print(3)
        for i in range(1, 6):
            usuario = str(request.POST.get(f"correoid{i}"))
            contraseña = str(request.POST.get(f'contraseña{i}'))
            if usuario and contraseña:
                print(4)
                contraseñas.append(contraseña)
                cuentas.append(usuario)

        for i in range(1, 6):
            print(5)
            asuntocliled = str(request.POST.get(f"asunto{i}"))
            mensaje = str(request.POST.get(f'mensaje{i}'))
            codigo_html = str(request.POST.get(f'codigo_html{i}'))
            file_html = request.FILES.get(f'archivo_html{i}')
            if file_html:
                print(6)
                textos_html = html_to_text(file_html)
                emails.append(textos_html)
            if codigo_html:
                emails.append(codigo_html)
            if asuntocliled:
                emails_subject.append(asuntocliled)
            if mensaje:
                emails.append(mensaje)

        direcciones_correo = str(request.POST.get('correos'))
        file_correo = request.FILES.get('correos_archivo')
        print(7)

        if direcciones_correo:
            direcciones_correo_lista = direcciones_correo.split()
            print("7 y medio")
            print(cuentas)
            print(contraseñas)
            print(cuentas)
            print(contraseñas)
            print(cuentas)
        else:
            df = pd.read_excel(file_correo)
            direcciones_correo_lista = df['correo'].tolist()
            print(3323)

        
            print(323)
        indice_cuenta = 0    
        for correo_destino in direcciones_correo_lista:
            indice_sujetos = random.randint(0, len(emails_subject) - 1)

            indice_mail = random.randint(0, len(emails) - 1)
            
            indice_cuenta = indice_cuenta +1
            if indice_cuenta == len(cuentas):
                indice_cuenta = 0
            contraseña_actual = contraseñas[indice_cuenta-1]

            
           
            mime_message = MIMEMultipart()
            mime_message["From"] = cuentas[indice_cuenta-1]
            mime_message["To"] = correo_destino
            mime_message["Subject"] = emails_subject[indice_sujetos]
            html_message = MIMEText(emails[indice_mail], 'html')
            mime_message.attach(html_message)
            image = request.FILES.get('imagen_cabecera')
            image2 = request.FILES.get('imagen_titular')
            print(9)
            
            if image:
                
                image_mime_type, _ = mimetypes.guess_type(image.name)
                image_mime = MIMEImage(image.read(), _subtype=image_mime_type)
                image_mime.add_header('Content-ID', '<header>')
                mime_message.attach(image_mime)
            if image2:
                image2_mime_type, _ = mimetypes.guess_type(image2.name)
                
                image2_mime = MIMEImage(image2.read(), _subtype=image2_mime_type)
                image2_mime.add_header('Content-ID', '<title>')
                mime_message.attach(image2_mime)


                        
                        
                        
            smtp = SMTP("smtp.gmail.com", 587)
            with smtp:
                        
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(cuentas[indice_cuenta-1], contraseña_actual)
                smtp.sendmail(cuentas[indice_cuenta-1], correo_destino, mime_message.as_string())
                email_adresses.append(correo_destino)
                print("\nEmail sent to: " + correo_destino + " from: " + cuentas[indice_cuenta])
                print(10)
                if intervalo:
                    print(12)
                    time.sleep(intervalo)
                if aleatorio:
                    print(13)
                    numero_aleatorio = generar_numero_desde_texto(aleatorio)
                    time.sleep(numero_aleatorio)
                    print(numero_aleatorio)
                    print(numero_aleatorio)

                if cliledsend:
                    print("cliledsend")
                    tiempo_limite_segundos = cliledsend * 60
                    
                    cantidad_correos = len(direcciones_correo_lista)
                    numero_random = random.randint(-20, 20)

                  
                    tiempo_intervalo = tiempo_limite_segundos/cantidad_correos
                    tiempo_intervalo = tiempo_intervalo + numero_random
                    time.sleep(tiempo_intervalo)
    resultados = pd.DataFrame( email_adresses, columns=['Correos Enviados'])
    print(resultados)
    return render(request, 'results2.html', {'resultados': resultados})
























"""mensajelista =[]
        
        cuentas = int(request.POST.get(f"asunto{i}"))
        numeros = str(request.POST.get(f'mensaje{i}'))
        odigo_html = str(request.POST.get(f'codigo_html{i}'))
        file_html = 
        adjunto1 = request.FILES.get('adjunto1')
        adjunto2 = request.FILES.get('adjunto2')
        adjunto3 = request.FILES.get('adjunto3')
        adjunto4 = request.FILES.get('adjunto4')
        archivo_telefono = request.FILES.get('adjunto4')
        numeros = str(request.POST.get('numeros'))
        country_code = str(request.POST.get('country_code'))

        for i in range(1, 21):
            

            mensaje = str(request.POST.get(f'mensaje{i}'))
            if mensaje:
                mensajelista.append(mensaje)"""












def whatsapp(request):
    return render(request, 'whatsapp.html')



import os
from django.conf import settings



def dividir_lista(numeros_amandar, cuentas):
    longitud_sublista = len(numeros_amandar) // cuentas
    residuo = len(numeros_amandar) % cuentas
    inicio = 0
    sublistas =[]
    
    for i in range(cuentas):
        fin = inicio + longitud_sublista + (1 if i < residuo else 0)
        sublistas.append(numeros_amandar[inicio:fin])
        inicio = fin
    return sublistas



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException
















































@csrf_exempt
def envio_whatsapp(request):
    if request.method == 'POST':
        rutas_imagenes = []
        rutas_adjuntos = []
        
        # Obtenemos las rutas de las imágenes
        imagen1 = request.POST.get("adjunto1")
        if imagen1:
            rutas_imagenes.append(imagen1)

        imagen2 = request.POST.get("adjunto2")
        if imagen2:
            rutas_imagenes.append(imagen2)

        imagen3 = request.POST.get("adjunto3")
        if imagen3:
            rutas_imagenes.append(imagen3)

        video = request.POST.get("adjunto4")
        if video:
            rutas_imagenes.append(video)

        # Obtenemos las rutas de los archivos adjuntos
        adjunto1 = request.POST.get("adjunto1c")
        if adjunto1:
            rutas_adjuntos.append(adjunto1)

        adjunto2 = request.POST.get("adjunto2c")
        if adjunto2:
            rutas_adjuntos.append(adjunto2)

        adjunto3 = request.POST.get("adjunto3c")
        if adjunto3:
            rutas_adjuntos.append(adjunto3)

        adjunto4 = request.POST.get("adjunto4c")
        if adjunto4:
            rutas_adjuntos.append(adjunto4)
            
            
            
            
            
        carpeta = request.POST.get("carpeta")
        contacto =  request.POST.get("contacto")
        numeros = request.POST.get("numeros")
        numeros_archivo = request.FILES.get('archivo_telefono')
        if numeros:
            numeros_lista = numeros.split()
            
        else:
            df = pd.read_excel(numeros_archivo)
            numeros_lista = df['numeros'].tolist()
        selected_country_code = request.POST.get('countryCodeSelect')
        if selected_country_code:
            numeros_lista = [selected_country_code + elemento for elemento in numeros_lista]
        intervalo = request.POST.get('intervalowts')
        aleatorio = request.POST.get('aleatoriowts')
        cliledsend = request.POST.get('cliledsendwts')
        intervalo = str(intervalo) if intervalo else '0'
        aleatorio = str(aleatorio) if aleatorio else '0'
        cliledsend = str(cliledsend) if cliledsend else '0'
        cuentaswts = int(request.POST.get('cuentas'))
        lista_de_mensajes = []
        for i in range(1, 21):
            print(5)
            
            mensaje = str(request.POST.get(f'mensaje{i}'))
         
            if mensaje:
                
                lista_de_mensajes.append(mensaje)
                
        
        numeros_amandar = int(len(numeros_lista))
        numeros_amandar = numeros_amandar / cuentaswts
        sublistas = dividir_lista(numeros_lista,cuentaswts)
        print(sublistas)
    # Lista para almacenar las instancias de los controladores
        drivers = []
        elementos_necesarios = []
        # Abrir el navegador tres veces
        print(6)
        for cuenta in range(cuentaswts):
        
        # Definir opciones del navegador
            options = webdriver.ChromeOptions()
            chromedriver_path = "C:/Users/Cliled/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe"

            service = Service(executable_path=chromedriver_path)
        
        # Inicializar el controlador de Chrome
            driver = webdriver.Chrome(service = service, options=options)
        
        # Acceder a una URL (ejemplo)
            driver.get("https://web.whatsapp.com/")
        
        # Agregar el controlador a la lista
            drivers.append(driver)




        for i in range(int(numeros_amandar)):
            for index, driver in enumerate(drivers, start=1):
                print(f"Interactuando con el controlador {index}")
    # Aquí puedes realizar operaciones específicas para cada controlador
    # Por ejemplo, puedes realizar acciones diferentes dependiendo del índice del controlador
                if index == 1:
                    print("esperaning")
                    time.sleep(60)
                    print("funciona")
                    botonnuevochar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._ajv7:nth-child(4) > ._ajv6 > span"))
                    )
                    botonnuevochar.click()
                    time.sleep(2)
                    primera_lista = sublistas[0]
                    print(primera_lista)
                    objeto = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".\_ai07 .selectable-text"))
                    )
                    
                    objeto.send_keys(primera_lista[i])
                    print("corrco")

                    

                    nuevochat = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._ak72:nth-child(2) > ._ak8l"))
                    )
                    nuevochat.click()
                    time.sleep(2)
                    print("porfinen fa")
                    keyboard.write("Imágenes")
                    keyboard.write("Imágenes")
                    keyboard.send("enter")
                    
                   
                    
                    print("porfinaaaaaaa")

                    if len(rutas_imagenes) > 0:
                    #boton de imagen 
                        parent_element = WebDriverWait(driver, 100).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "._ak1o ._ajv6"))
                        )
                        parent_element.click()
                        elementos = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i64zmx') and contains(@class, 'x1emribx')]")
                        if len(elementos) >= 2:
                            #este es el elemento de imagenes y videos
                            elementos[2].click()
                            keyboard.write(carpeta)
                            keyboard.send("enter")  
                            ruta_archivo = rutas_imagenes[0]  # Cambia esto con la ruta de tu archivo
                            keyboard.write(ruta_archivo)
                            keyboard.send("enter")
                            time.sleep(2)
                            keyboard.send("enter")















                    if len(rutas_adjuntos) > 0:
                    #boton de imagen 
                        parent_element = WebDriverWait(driver, 100).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "._ak1o ._ajv6"))
                        )
                        parent_element.click()
                        elementos = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i64zmx') and contains(@class, 'x1emribx')]")
                        if len(elementos) >= 2:
                            #este es el elemento de imagenes y videos
                            elementos[2].click()
                            keyboard.write(carpeta)
                            keyboard.send("enter")  
                            ruta_archivo = rutas_imagenes[0]  # Cambia esto con la ruta de tu archivo
                            keyboard.write(ruta_archivo)
                            keyboard.send("enter")
                            time.sleep(2)
                            keyboard.send("enter")

                   
                       


                
                
                
                   
                
                
                













                
                
                

        # Aquí puedes realizar las acciones específicas para el primer controlador
                elif index == 2:
                    print("controlador2")
                    
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                    )
                    print("Este es el primer controlador")
                    time.sleep(1)
                    elemento.click()
                    time.sleep(5)
                    campo_texto = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                    )
                    texto_a_ingresar = sublistas[1[i]]
                    campo_texto.send_keys(texto_a_ingresar)
                    print(923984)
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._21S-L > .cw3vfol9"))
                    )
                    elemento.click()

                
                
                
                    print("porfin")
                
                
                
                    mensaje_a_enviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3Uu1_"))
                    )
                    texto = lista_de_mensajes[i+2]
                    print("polisha")
                    mensaje_a_enviar.send_keys(texto)
                    botonenviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3XKXx"))
                    )
                    botonenviar.click()
        # Aquí puedes realizar las acciones específicas para el segundo controlador
                elif index == 3:
                    
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                    )
                    print("Este es el primer controlador")
                    time.sleep(1)
                    elemento.click()
                    time.sleep(5)
                    campo_texto = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                    )
                    texto_a_ingresar = sublistas[2[i]]
                    campo_texto.send_keys(texto_a_ingresar)
                    print(923984)
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._21S-L > .cw3vfol9"))
                    )
                    elemento.click()

                
                
                
                    print("porfin")
                
                
                
                    mensaje_a_enviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3Uu1_"))
                    )
                    texto = lista_de_mensajes[i+3]
                    print("polisha")
                    mensaje_a_enviar.send_keys(texto)
                    botonenviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3XKXx"))
                    )
                    botonenviar.click()
                elif index ==4:
                    
                    
                    
                    
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                    )
                    print("Este es el primer controlador")
                    time.sleep(1)
                    elemento.click()
                    time.sleep(5)
                    campo_texto = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                    )
                    texto_a_ingresar = sublistas[3[i]]
                    campo_texto.send_keys(texto_a_ingresar)
                    print(923984)
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._21S-L > .cw3vfol9"))
                    )
                    elemento.click()

                
                
                
                    print("porfin")
                
                
                
                    mensaje_a_enviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3Uu1_"))
                    )
                    texto = lista_de_mensajes[i+4]
                    print("polisha")
                    mensaje_a_enviar.send_keys(texto)
                    botonenviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3XKXx"))
                    )
                    botonenviar.click()
                    
                    
                    
                    
                elif index ==5:
                    
                    
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                    )
                    print("Este es el primer controlador")
                    time.sleep(1)
                    elemento.click()
                    time.sleep(5)
                    campo_texto = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                    )
                    texto_a_ingresar = sublistas[4[i]]
                    campo_texto.send_keys(texto_a_ingresar)
                    print(923984)
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._21S-L > .cw3vfol9"))
                    )
                    elemento.click()

                
                
                
                    print("porfin")
                
                
                
                    mensaje_a_enviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3Uu1_"))
                    )
                    texto = "Hola"
                    print("polisha")
                    mensaje_a_enviar.send_keys(texto)
                    botonenviar = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._3XKXx"))
                    )
                    botonenviar.click()

                
                
                
                print("porfin")
                
                
                
                mensaje_a_enviar = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3Uu1_"))
                )
                texto = lista_de_mensajes[i+5]
                print("polisha")
                mensaje_a_enviar.send_keys(texto)
                botonenviar = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3XKXx"))
                )
                botonenviar.click()
        # Aquí puedes realizar las acciones específicas para el tercer controlador

# Recuerda cerrar los controladores cuando hayas terminado con ellos
    for driver in drivers:
        driver.quit()


























        
        
        
       
















def numeroscalienta(request):
    return render(request, 'numeroscalienta.html')
@csrf_exempt
def numeroscalientaenvio(request):
    if request.method == 'POST':
        print(1)
        resultados = 1
        return render(request, 'results2.html', {'resultados': resultados})










from django.shortcuts import render
from django.http import HttpResponse
import os
from twilio.rest import Client
from decouple import config
from django.http import JsonResponse
from django.conf import settings
from .models import Usuario
from django.db import IntegrityError
from django.contrib import messages
from registro.models import Usuario
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def registroa(request):
    return render(request, 'registro.html')


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags




import hashlib

def generar_token_verificacion(correo):
    # Clave secreta para mayor seguridad
    secreto = "cliled"
    correo =str(correo)

    # Concatenar el correo electrónico y la clave secreta
    mensaje = correo + secreto

    # Calcular el hash MD5 del mensaje concatenado
    hash_md5 = hashlib.md5(mensaje.encode()).hexdigest()

    # Retornar el token de verificación
    objeto =str(hash_md5[:5])
    return objeto

# Ejemplo de uso




def generar_token_verificacionmes(correo):
    # Clave secreta para mayor seguridad
    secreto = "cliled1mesxd"
    correo =str(correo)

    # Concatenar el correo electrónico y la clave secreta
    mensaje = correo + secreto

    # Calcular el hash MD5 del mensaje concatenado
    hash_md5 = hashlib.md5(mensaje.encode()).hexdigest()

    # Retornar el token de verificación
    objeto =str(hash_md5[:12])
    return objeto
def generar_token_verificacion3meses(correo):
    # Clave secreta para mayor seguridad
    secreto = "cliled2mesesxds"
    correo =str(correo)

    # Concatenar el correo electrónico y la clave secreta
    mensaje = correo + secreto

    # Calcular el hash MD5 del mensaje concatenado
    hash_md5 = hashlib.md5(mensaje.encode()).hexdigest()

    # Retornar el token de verificación
    objeto =str(hash_md5[:12])
    return objeto
def generar_token_verificacion6meses(correo):
    # Clave secreta para mayor seguridad
    secreto = "cliled8mesesji"
    correo =str(correo)

    # Concatenar el correo electrónico y la clave secreta
    mensaje = correo + secreto

    # Calcular el hash MD5 del mensaje concatenado
    hash_md5 = hashlib.md5(mensaje.encode()).hexdigest()

    # Retornar el token de verificación
    objeto =str(hash_md5[:12])
    return objeto
def generar_token_verificacion12meses(correo):
    # Clave secreta para mayor seguridad
    secreto = "cliled12meserracos"
    correo =str(correo)

    # Concatenar el correo electrónico y la clave secreta
    mensaje = correo + secreto

    # Calcular el hash MD5 del mensaje concatenado
    hash_md5 = hashlib.md5(mensaje.encode()).hexdigest()

    # Retornar el token de verificación
    objeto =str(hash_md5[:12])
    return objeto










@csrf_exempt
def enviar_correo_paypal(request):
    if request.method == 'POST':
        tiempodelicencia = request.POST.get('tiempodelicencia')
        mail = request.user.username

        if tiempodelicencia == "basico-mes":
            token = request.user.licencia_mes
        elif tiempodelicencia == "basico-3meses":
            token = request.user.licencia_3meses
        elif tiempodelicencia == "basico-6meses":
            token = request.user.licencia_6meses
        elif tiempodelicencia == "basico-12meses":
            token = request.user.licencia_12meses
        else:
            return HttpResponse('Licencia no valida')
     # Función para generar un token único
    
        subject = 'Tu licencia '
        html_message = render_to_string('correo_verificacion.html', {'usuario': mail, 'token': token})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER  # Utiliza el correo electrónico configurado en tu settings.py

    # Esto debería imprimir correctamente el correo electrónico
        send_mail(subject, plain_message, from_email, [mail], html_message=html_message)
    return redirect('licencia')
    



















def enviar_correo_verificacion(mail,token):
     # Función para generar un token único
    
    subject = 'Verificación de cuenta'
    html_message = render_to_string('correo_verificacion.html', {'usuario': mail, 'token': token})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER  # Utiliza el correo electrónico configurado en tu settings.py
    
    # Esto debería imprimir correctamente el correo electrónico
    send_mail(subject, plain_message, from_email, [mail], html_message=html_message)
    









def verificar_recaptcha(response, remote_ip):
    # Realiza la solicitud a la API de reCAPTCHA para verificar el token de respuesta
    import requests
    import json

    secret_key = '6LdKu10pAAAAADKjQnq155n2CTujI60FXLa_sAb8'  # Reemplaza con tu clave secreta de reCAPTCHA

    data = {
        'secret': secret_key,
        'response': response,
        'remoteip': remote_ip,
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = json.loads(response.text)

    return result['success'], result.get('error-codes', [])































def verification(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response', '')
        remote_ip = request.META.get('REMOTE_ADDR', '')

        success, error_codes = verificar_recaptcha(recaptcha_response, remote_ip)

        if success:
            try:
                correo = str(request.POST.get('mail'))
                contraseña = request.POST.get('password')
                token = generar_token_verificacion(correo)
                username = correo
                tokenmes = generar_token_verificacionmes(correo)
                token3meses = generar_token_verificacion3meses(correo)
                token6meses = generar_token_verificacion6meses(correo)
                token12meses = generar_token_verificacion12meses(correo)

        
            
                enviar_correo_verificacion(correo, token)
                usuario = Usuario.objects.create(username=username, email=correo, token_verificacion=token, licencia_mes=tokenmes, licencia_3meses=token3meses, licencia_6meses=token6meses, licencia_12meses=token12meses)
               
                usuario.set_password(contraseña)
                usuario.save()
            
                return render(request, 'prueba.html', {'mail': correo})
            
            except IntegrityError as e:
                error_message = "Ya existe un usuario con el mismo correo electrónico."
                return HttpResponse(error_message, status=400)
        else:
            return JsonResponse({'error': 'El reCAPTCHA ha fallado.', 'error_codes': error_codes}, status=400)

    # Manejar la lógica para otros métodos HTTP (GET, etc.) según sea necesario
    # ...



    # Manejar la lógica para otros métodos HTTP (GET, etc.) según sea necesario
from django.shortcuts import redirect    # ...
def verificar_codigo(request):
    if request.method == 'POST':
        codigo = request.POST.get('verificationCode')
        print("nuevo")
        print(codigo)
        try:
            usuario = Usuario.objects.get(token_verificacion=codigo)
        except Usuario.DoesNotExist:
            # No se encontró ningún usuario con ese código de verificación
            return HttpResponse('Código de verificación inválido')

        # Verificar si el código de verificación coincide con el del usuario
        if codigo == usuario.token_verificacion:
            # Si el código coincide, actualizar el estado 'activado' del usuario
            usuario.activado = True
            usuario.save()
            messages.add_message(request=request, level=messages.SUCCESS,message="Su registro se ha realizado con exito")
            return redirect("login")
        else:
            # Si el código no coincide con el del usuario
            return HttpResponse('Código de verificación inválido')
    else:
        return HttpResponse('Método no permitido')



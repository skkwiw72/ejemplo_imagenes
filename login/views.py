from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from registro.models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib
from django.conf import settings

# Create your views here.
@csrf_exempt
def login(request):
    return render(request, 'login.html')




@csrf_exempt
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

@csrf_exempt
def enviar_correo_verificacion(mail,token):
     # Función para generar un token único
    
    subject = 'Cambia tu contraseña'
    html_message = render_to_string('correo_cambiodecontraseña.html', { 'token': token})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER  # Utiliza el correo electrónico configurado en tu settings.py
    
    # Esto debería imprimir correctamente el correo electrónico
    send_mail(subject, plain_message, from_email, [mail], html_message=html_message)




















@csrf_exempt
def cambiar_contrasena(request):
    return render(request, 'cambiar_contrasena.html')
@csrf_exempt
def elegir_contra(request,usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    print(usuario)
    
    # Aquí puedes hacer cualquier cosa con el objeto usuario
    # Por ejemplo, pasarlo como contexto a la plantilla renderizada
    return render(request, 'elegircontra.html', {'usuario': usuario})




    







   
@csrf_exempt
def cambiar_contrasenasoli(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        print(email)
        try:
            username = Usuario.objects.get(email=email)
            print(username)
            print(username)
            print(username)
            
            print("si existe")
            token = generar_token_verificacion(email)
            
            
            enviar_correo_verificacion(email, token)
            return render(request, 'codigo_contraseña.html', {'mail': email})

        except Usuario.DoesNotExist:
            
            messages.add_message(request=request, level=messages.SUCCESS,message="Esta cuenta no existe")
            return redirect('/registro')
        

from django.shortcuts import redirect 
@csrf_exempt
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
        print("todo va bien")
        print(usuario.id)
        print(usuario.id)
        print(usuario.id)
        print(usuario.id)
        # Verificar si el código de verificación coincide con el del usuario
        if codigo == usuario.token_verificacion:
            return redirect("elegir_contra",usuario_id=usuario.id)
            # Si el código coincide, actualizar el estado 'activado' del usuario
            
            
        else:
            # Si el código no coincide con el del usuario
            return HttpResponse('Código de verificación inválido')
    else:
        return HttpResponse('Método no permitido')


@csrf_exempt
def cambiar_contraseñafinal(request,usuario_id):
    
    if request.method == 'POST':
    # Obtener el usuario utilizando el ID pasado en la redirección
        usuario = Usuario.objects.get(id=usuario_id)
        nueva_contraseña = str(request.POST.get('password'))
        usuario.set_password(nueva_contraseña)
    # Aquí puedes cambiar la contraseña del usuario
        
        usuario.save()
        messages.add_message(request=request, level=messages.SUCCESS,message="Su contraseña ha sido cambiada con éxito")
    
    # Puedes redirigir al usuario a una página de éxito o cualquier otra página después de cambiar la contraseña
        return redirect("login")










  
































            
@csrf_exempt        
def verificar_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        
        # Obtener el nombre de usuario asociado al correo electrónico
        try:
            username = Usuario.objects.get(email=email)
            print(username)
            print(username)
            print(username)
            
            print("si existe")
        except Usuario.DoesNotExist:
            
            messages.add_message(request=request, level=messages.SUCCESS,message="Esta cuenta no existe")
            return redirect('/registro')
        
        # Autenticar al usuario utilizando el nombre de usuario y la contraseña
        user = authenticate( username=username, password=password)
        if user is not None:
            print("Sesión iniciada")
            auth_login(request,user)
            print("Sesión iniciada")
        else:
            messages.add_message(request=request, level=messages.SUCCESS,message="Su contraseña es incorrecta")
            return redirect("login")
        
        return redirect('dashboard')
    else:
        return HttpResponse("Solicitud no válida")
# paginainicio/views.py
from django.shortcuts import render
from django.contrib import messages
from .models import Contacto

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


def landing_page(request):
     return render(request, 'landing_page.html')
def contacto(request):
     return render(request, 'contact-us.html')
def contacto_cliled(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('phone')

        Marketing = request.POST.get('Marketing', False)
        if Marketing:
            intereses = "Marketing"

        Automatizaciones = request.POST.get('Automatizaciones', False)
        if Automatizaciones:
            intereses = "Automatizaciones"

        Software = request.POST.get('Software', False)
        if Software:
            intereses = "Software"

        other = request.POST.get('other', False)
        if other:
            intereses = "Alguna otra"
        
        mensaje = request.POST.get('message')
        acepta_privacidad = request.POST.get('gdpr') == 'on'

        # Crear una instancia del modelo Contacto y guardarla en la base de datos
        contacto = Contacto(nombre=nombre, email=email, telefono=telefono, intereses=intereses, mensaje=mensaje, acepta_privacidad=acepta_privacidad)
        contacto.save()

        messages.success(request, '¡El formulario se ha enviado correctamente!')

    return render(request, 'contact-us.html')
        
        
        
        
        
        
def privacidad(request):
     return render(request, 'privacy-policies.html')       
def serviciosweb(request):
     return render(request, 'paginaweb.html')
def automatizacion(request):
     return render(request, 'automatizacion.html')
def automatizaciondedatos(request):
     return render(request, 'automatizaciondedatos.html')
def marketing(request):
     return render(request, 'marketing.html')
def software(request):
     return render(request, 'software.html')
def seo(request):
     return render(request, 'seo.html')
def novartis(request):
     return render(request, 'novartis.html')
def missionbrand(request):
     return render(request, 'missionbrand.html')
def Tec(request):
     return render(request, 'tec.html')
def Menuderia(request):
     return render(request, 'menuderia.html')
def privacidad(request):
     return render(request, 'privacy-policies.html')
def ganaconnosotros(request):
     return render(request, 'gana-con-nosotros.html')
def precio(request):
     return render(request, 'precio.html')
def quienes(request):
     return render(request, 'quienessomos.html')
def comofunciona(request):
     return render(request, 'COMOFUNCIONA.html')
def licencia(request):
     return render(request, 'licensias.html')
def Office(request):
     return render(request, 'Oficce.html')
def Soporte(request):
     return render(request, 'Soporte.html')
def preciogrupos(request):
     return render(request, 'precio-grupos.html')
def ingresalicencia(request):
     return render(request, 'ingresalicencia.html')
@csrf_exempt
def procesarlicencia(request):
     if request.method == 'POST':
          licencia = request.POST.get('licencia')
          tipo_de_licencia_mes = request.user.licencia_mes
          tipo_de_licencia_3meses = request.user.licencia_3meses
          tipo_de_licencia_6meses = request.user.licencia_6meses
          tipo_de_licencia_12meses = request.user.licencia_12meses
          if licencia == tipo_de_licencia_mes:
               request.user.plan = 'b'
               request.user.tokens_contactos = 100000
               request.user.tokens_mensajes = 100000
               request.user.save()
               messages.success(request, '¡Licencia activada correctamente!')
          elif licencia == tipo_de_licencia_3meses:
               request.user.plan = 'c'
               request.user.tokens_contactos = 100000
               request.user.tokens_mensajes = 100000
               request.user.save()
               messages.success(request, '¡Licencia activada correctamente!')
          elif licencia == tipo_de_licencia_6meses:
               request.user.plan = 'd'
               request.user.tokens_contactos = 100000
               request.user.tokens_mensajes = 100000
               request.user.save()
               messages.success(request, '¡Licencia activada correctamente!')
          elif licencia == tipo_de_licencia_12meses:
               request.user.plan = 'e'
               request.user.tokens_contactos = 100000
               request.user.tokens_mensajes = 100000
               request.user.save()
               messages.success(request, '¡Licencia activada correctamente!')
          else:
               messages.error(request, '¡Licencia incorrecta!')
     return redirect('dashboard')
          


def usocontactos(request):
     return render(request, 'uso-contactos.html')
def usomensajes(request):
     return render(request, 'uso-mensajes.html')





     


    

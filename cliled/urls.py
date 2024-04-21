"""
URL configuration for cliled project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landingpage import views as landing_views
from login import views as login_views
from registro import views as register_views
from cliledcontactos import views as contactos_views
from cliledmensajes import views as mensajes_views
from extras import views as extras_views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', landing_views.landing_page, name='landing_page'),
    path('contacto', landing_views.contacto, name='contacto_page'),
    path('contacto/envio', landing_views.contacto_cliled, name='contacto_cliled'),
    path('servicios-web', landing_views.serviciosweb, name='serviciosweb'),
    path('automatizacion', landing_views.automatizacion, name='automatizacion'),
    path('automatizacion-de-datos', landing_views.automatizaciondedatos, name='automatizaciondedatos'),
    path('marketing', landing_views.marketing, name='marketing'),
    path('software', landing_views.software, name='software'),
    path('seo', landing_views.seo, name='seo'),
    path('politica-privacidad', landing_views.privacidad, name='privacidad'),
    path('gana-con-nosotros', landing_views.ganaconnosotros, name='gana-con-nosotros'),
    path('precio', landing_views.precio, name='precio'),
    path('terminos-condiciones', landing_views.privacidad, name='privacidad'),

    path('quienes-somos', landing_views.quienes, name='quienes'),
    path('uso-mensajes/', landing_views.usomensajes, name='uso-mensajes'),
    path('uso-contactos/', landing_views.usocontactos, name='uso-contactos'),
    path('como-funciona', landing_views.comofunciona, name='comofunciona'),
    path('licencia/', landing_views.licencia, name='licencia'),
    path('licencia/procesando', landing_views.procesarlicencia, name='procesarlicencia'),
    path('verificarspam/search', extras_views.searchspam, name='verificador_mail'),
    path('Soporte/',landing_views.Soporte, name='Soporte'),
    path('ingresalicencia/',landing_views.ingresalicencia, name='ingresalicencia'),



    #path('uso-mensajes/', landing_views.uso-mensajes, name='licencia'),
    #path('uso-contactos/', landing_views.uso-contactos, name='licencia'),
    path('Office/', landing_views.Office, name='Office'),
    path('precio-grupos/', landing_views.preciogrupos, name='preciogrupos'),
    
    
    
    
    
    
    
    
    
    
    path('Cliled-novartis', landing_views.novartis, name='novartis'),
    path('Cliled-missionbrand', landing_views.missionbrand, name='missionbrand'),
    path('Cliled-Tec', landing_views.Tec, name='Tec'),
    path('Cliled-Menuderia-La-Familia', landing_views.Menuderia, name='Menuderia'),
    
    
    
    
    
    
    path('login/', login_views.login, name='login'),
    path('login/verificar_usuario', login_views.verificar_usuario, name='verificar_usuario'),

    path('registro/', register_views.registroa, name='registroa'),
    path('registro/verification/', register_views.verification, name='verification'),
    path('registro/verification/confirmar/', register_views.verificar_codigo, name='verificar_codigo'),


    path('cambiar-contrasena/', login_views.cambiar_contrasena, name='cambiar_contrasena'),
    path('cambiar-contrasena/cambiar_contrasenasoli', login_views.cambiar_contrasenasoli, name='cambiar_contrasenasoli'),
    path('cambiar-contraseña/cambiar_contraseñasoli/verificar_codigo', login_views.verificar_codigo, name='verificar_codigo'),
    path('cambiar-contraseña/cambiar_contraseñasoli/verificar_codigo/cambiodecontraseña/<int:usuario_id>/', login_views.elegir_contra, name='elegir_contra'),
    path('cambiar-contraseña/cambiar_contraseñasoli/verificar_codigo/cambiodecontraseña/<int:usuario_id>/confirm', login_views.cambiar_contraseñafinal, name='cambiar_contraseñafinal'),
    

    
    path('dashboard/', contactos_views.dashboard, name='dashboard'),
    path('contactoscliled/', contactos_views.cliledcontactos, name='cliledcontactos'),
    path('contactoscliled/search', contactos_views.search, name='search'),
    path('contactosPersonas/', contactos_views.cliledpersonas, name='personas'),
    path('contactosPersonas/search', contactos_views.searchPersonas, name='searchinsta'),
    path('contactosInstagram/', contactos_views.cliledInstagram, name='Instagram'),
    path('contactosInstagram/search', contactos_views.searchinsta, name='searchinsta'),
    path('enviarcorreopaypal/', register_views.enviar_correo_paypal, name='enviar_correo_paypal'),



    
    
    
    
    
    path('Numeros-calentamiento/', mensajes_views.numeroscalienta, name='numeroscalienta'),
    path('Numeros-calentamiento/envio/', mensajes_views.numeroscalientaenvio, name='numeroscalientaenvio'),




    path('cliledmensajes/', mensajes_views.mailsender, name='mail_sender'),
    path('CliledMensajes/resultado', mensajes_views.enviomail, name='enviomail'),
    path('CliledWhatsapp/', mensajes_views.whatsapp, name='whatsapp'),
    path('CliledWhatsapp/resultado', mensajes_views.envio_whatsapp, name='envio_whatsapp'),
    
    path('MailVerifier/', extras_views.MailVerifier, name='MailVerifier'),
    path('MailVerifier/search', extras_views.search_mail_verifier, name='search_mail_verifier'),
    path('cliledplantillas/', extras_views.creador_plantillas, name='creador_plantillas'),
    path('cliledplantillas/templates/default.html', extras_views.default, name='default'),
    path('verificarspam/', extras_views.verificadorspam, name='verificador'),
    path('verificarspam/search', extras_views.searchspam, name='verificador_mail'),
    
    
    
    
    
    
]




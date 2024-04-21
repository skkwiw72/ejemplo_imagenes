
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .maps import main
from .instascraper import main
from django.contrib.auth.decorators import login_required
import re
import smtplib
import dns.resolver
import pandas as pd


import os
import csv
import time
import requests

# Create your views here.
def cliledpersonas(request):
    return render(request, 'cliledpersonas.html')
def searchPersonas(request):
    return render(request, 'cliledpersonas.html')

@login_required
def dashboard(request):
    username = request.user.username
    tokens_contactos = request.user.tokens_contactos
    tokens_mensajes = request.user.tokens_mensajes
    mensajes_enviados = request.user.mensajes_enviados
    contacos_enviado = request.user.contacos_enviado
    return render(request, 'dashboard.html', {'username': username, 'tokens_contactos': tokens_contactos, 'tokens_mensajes': tokens_mensajes, 'mensajes_enviados': mensajes_enviados, 'contacos_enviado': contacos_enviado})

def cliledcontactos(request):
    username = request.user.username
    tokens_contactos = request.user.tokens_contactos
    tokens_mensajes = request.user.tokens_mensajes
    mensajes_enviados = request.user.mensajes_enviados
    contacos_enviado = request.user.contacos_enviado
    return render(request, 'cliledcontactos.html', {'username': username, 'tokens_contactos': tokens_contactos, 'tokens_mensajes': tokens_mensajes, 'mensajes_enviados': mensajes_enviados, 'contacos_enviado': contacos_enviado})






def cliledpersonas(request):
    return render(request, 'cliledpersonas.html')
def cliledInstagram(request):
    username = request.user.username
    tokens_contactos = request.user.tokens_contactos
    tokens_mensajes = request.user.tokens_mensajes
    mensajes_enviados = request.user.mensajes_enviados
    contacos_enviado = request.user.contacos_enviado
    return render(request, 'cliledinstagram.html', {'username': username, 'tokens_contactos': tokens_contactos, 'tokens_mensajes': tokens_mensajes, 'mensajes_enviados': mensajes_enviados, 'contacos_enviado': contacos_enviado})















@csrf_exempt
def searchinsta(request):
    if request.method == 'POST':
        cuenta = str(request.POST.get('cuenta'))
       
        total = int(request.POST.get('total'))
        
        
        BASE_URL = "https://instagram-scraper-2022.p.rapidapi.com/ig"
        headers = {
	    "X-RapidAPI-Key": "eae1b73cb9mshc5dece8c05b7c84p172949jsned39caa145b8",
	    "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
        }

        followers_list = []
        

        data = main(cuenta)
        lista_names = []
        lista_username = []
        lista_biblio = []
        lista_url = []
        listanumero = []
        listamails = []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        for item in data:
            if isinstance(item, dict):  # Verifica si el elemento es un diccionario
                full_name = item.get('full_name', '')
                lista_names.append(full_name)
        
                username = item.get('username', '')
                lista_username.append(username)
                biography = item.get('biography', '')
                lista_biblio.append(biography)
                external_url = item.get('external_url', '')
                lista_url.append(external_url)
                contact_phone_number = item.get('contact_phone_number', '')
                listanumero.append(contact_phone_number)
                email = item.get('public_email', '')
                listamails.append(email)
            else:
        # Si el elemento no es un diccionario, se agrega una cadena vacía a cada lista
                lista_names.append('')
                lista_username.append('')
                lista_biblio.append('')
                lista_url.append('')
                listanumero.append('')
                listamails.append('')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        df = pd.DataFrame(list(zip(lista_names, lista_username,lista_biblio,lista_url,listanumero,listamails)), columns =['Nombres','Usernames','Bibliografia','Urls','Numerosdetelefono','Emails'])
        for column in df.columns:
            if df[column].nunique() == 1:
                df.drop(column, axis=1, inplace=True)
        df.to_csv(r'efwewfws.csv', index = False)
        
        
   
        
        
        # Pasa los resultados directamente a la plantilla
        return render(request, 'results3.html', {'resultados': df})

    return render(request, 'cliledcontactos.html')


































@csrf_exempt
def search(request):
    if request.method == 'POST':
        tipo_de_negocio = str(request.POST.get('tipo_de_negocio'))
        pais = str(request.POST.get('pais'))
        estado_ciudad = str(request.POST.get('estado_ciudad'))
        total = int(request.POST.get('total'))

        search_for = tipo_de_negocio + " en  "+estado_ciudad +" "+pais 

        # Aquí puedes llamar a tu función main
        resultados = main(search_for, total)
        print(resultados)
        # Pasa los resultados directamente a la plantilla
        return render(request, 'results.html', {'resultados': resultados})

    return render(request, 'cliledcontactos.html')

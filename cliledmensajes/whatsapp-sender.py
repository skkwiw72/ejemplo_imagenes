from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


drivers = []
cuentaswts = 1
for cuenta in range(cuentaswts):
        
        # Definir opciones del navegador
            options = webdriver.ChromeOptions()
            chromedriver_path = "C:/Users/Cliled/Desktop/chromedriver.exe"


            service = Service(executable_path=chromedriver_path)
        
        # Inicializar el controlador de Chrome
            driver = webdriver.Chrome(service = service, options=options)
        
        # Acceder a una URL (ejemplo)
            driver.get("https://web.whatsapp.com/")
        
        # Agregar el controlador a la lista
            drivers.append(driver)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def main(cuentas, mensajes, archivos_adjuntos, intervalos,numeros_amandar):
    numeros_amandar = numeros_amandar / cuentas
    # Lista para almacenar las instancias de los controladores
    drivers = []
    elementos_necesarios = []
    
    # Abrir el navegador tres veces
    for cuenta in range(cuentas):
        
        # Definir opciones del navegador
        options = webdriver.ChromeOptions()
        chromedriver_path = "C:/Users/rober/Pictures/chromedriver-win64/chromedriver.exe"
        
        # Inicializar el controlador de Chrome
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        
        # Acceder a una URL (ejemplo)
        driver.get("https://web.whatsapp.com/")
        
        # Agregar el controlador a la lista
        drivers.append(driver)
    
    for index, driver in enumerate(drivers, start=1):
        print(f"Interactuando con el controlador {index}")
    # Aquí puedes realizar operaciones específicas para cada controlador
    # Por ejemplo, puedes realizar acciones diferentes dependiendo del índice del controlador
        if index == 1:
                elemento = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                )
                print("Este es el primer controlador")
                elemento.click()
                campo_texto = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                )
                texto_a_ingresar = "+52 3334405611"
                campo_texto.send_keys(texto_a_ingresar)
                contacto = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_8nE1Y"))
                )
                contacto.click()
                mensaje_a_enviar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                )
                texto = "Hola"
                mensaje_a_enviar.send_keys(texto)

        # Aquí puedes realizar las acciones específicas para el primer controlador
        elif index == 2:
                elemento = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                )
                print("Este es el segundo controlador")
                elemento.click()
                campo_texto = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                )
                texto_a_ingresar = "+52 3334405611"
                campo_texto.send_keys(texto_a_ingresar)
                contacto = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_8nE1Y"))
                )
                contacto.click()
                mensaje_a_enviar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                )
                texto = "Hola2"
                mensaje_a_enviar.send_keys(texto)
        # Aquí puedes realizar las acciones específicas para el segundo controlador
        elif index == 3:
                elemento = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3ndVb.fbgy3m38.ft2m32mm.oq31bsqd.nu34rnf1[title='Nuevo chat']"))
                )
                print("Este es el segundo controlador")
                elemento.click()
                campo_texto = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                )
                texto_a_ingresar = "+52 3334405611"
                campo_texto.send_keys(texto_a_ingresar)
                contacto = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_8nE1Y"))
                )
                contacto.click()
                mensaje_a_enviar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".selectable-text.copyable-text.iq0m558w.g0rxnol2"))
                )
                texto = "Hola3"
                mensaje_a_enviar.send_keys(texto)
        # Aquí puedes realizar las acciones específicas para el tercer controlador

# Recuerda cerrar los controladores cuando hayas terminado con ellos
    for driver in drivers:
        driver.quit()

            
            
   
        
        
        

    

# Llamar a la función principal con argumentos de ejemplo
main(cuentas=3, mensajes=None, archivos_adjuntos=None, intervalos=None , numeros_amandar=None)    
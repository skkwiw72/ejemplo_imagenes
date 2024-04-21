from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
import keyboard

sublistas = []

def main(cuentas, mensajes, archivos_adjuntos, intervalos,numeros_amandar):

    

    
    
    
    
    numeros_amandar = len(numeros_amandar)
    numeros_amandar = numeros_amandar / cuentas
    # Lista para almacenar las instancias de los controladores
    drivers = []
    elementos_necesarios = []
    
    # Abrir el navegador tres veces
    for cuenta in range(cuentas):
        
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
                try:








                    
                    
                   
















































                    print("esperaning")
                    time.sleep(60)
                    print("funciona")
                    time.sleep(10)
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,  "._ak8l"))
                    )
             
                    elemento.click()
                    print("se dio el ckick")
                
                    time.sleep(10)
                    
                    parent_element = WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._ak1o ._ajv6"))
                    )
                    parent_element.click()
                    time.sleep(10)
                    print("se dio el ckic2222k")

                    print(22222222222222222222222)
                    elementos = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i64zmx') and contains(@class, 'x1emribx')]")


# Verifica si hay al menos dos elementos que coincidan
                    if len(elementos) >= 2:
                        print(3)
    # Haz clic en el segundo elemento
                        elementos[2].click()
                        time.sleep(5)
                        print("wow")
                    keyboard.write("Imágenes")
                    keyboard.send("enter")  
                    ruta_archivo = "as.jpg"  # Cambia esto con la ruta de tu archivo
                    keyboard.write(ruta_archivo)
                    print("wow")

# Presiona la tecla Enter para confirmar la selección
                    keyboard.send("enter")
                    time.sleep(5)
                    
# Hacer que la entrada sea visible usando JavaScript
                    print("wowclaudia")
                    time.sleep(5)
                    keyboard.send("enter")
                    print("wowclaudiaewfwefwe")
                   
 

# Envía la ruta del archivo al elemento file input
                  
                except StaleElementReferenceException: 
                    print("funcion2a")
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,  "._ak8l"))
                    )
             
                    elemento.click()
                
                    time.sleep(5)
                    ruta_del_archivo = "C:\\Users\\rober\\Pictures\\as.jpg"
                    parent_element = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1i64zmx.x1emribx input[type='file']"))
                    )
                    print(111111111122222222222222222)

# Hacer que la entrada sea visible usando JavaScript
                    driver.execute_script("arguments[0].style.display = 'block';", parent_element.find_element(By.TAG_NAME, "input"))
                    print("reinicio")
                    elemento = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,  "._ak8l"))
                    )
             
                    elemento.click()

# Ahora busque y envíe las teclas al elemento de entrada
                    input_file = parent_element.find_element(By.TAG_NAME, "input")
                    input_file.send_keys(ruta_del_archivo)

 

# Envía la ruta del archivo al elemento file input
                    ruta_del_archivo = "C:\\Users\\rober\\Pictures\\as.jpg"
                
                    print("wiiii")
                    
                
                
                
                

        # Aquí puedes realizar las acciones específicas para el primer controlador
            elif index == 2:
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
                texto_a_ingresar = "+52 3331305575"
                campo_texto.send_keys(texto_a_ingresar)
                print(923984)
                elemento = WebDriverWait(driver, 10000).until(
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
                texto_a_ingresar = "+52 3334405611"
                campo_texto.send_keys(texto_a_ingresar)
                print(923984)
                elemento = WebDriverWait(driver, 1000).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._21S-L > .cw3vfol9"))
                )
                elemento.click()
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
                texto_a_ingresar = "+52 3334405611"
                campo_texto.send_keys(texto_a_ingresar)
                print(923984)
                elemento = WebDriverWait(driver, 1000).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._21S-L > .cw3vfol9"))
                )
                elemento.click()
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
                texto_a_ingresar = "+52 3334405611"
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
        # Aquí puedes realizar las acciones específicas para el tercer controlador

# Recuerda cerrar los controladores cuando hayas terminado con ellos
    for driver in drivers:
        driver.quit()

            
            
   
        
        
        

    

# Llamar a la función principal con argumentos de ejemplo
main(cuentas=2, mensajes=None, archivos_adjuntos=None, intervalos=None ,numeros_amandar=[523337867650,523211053233,525550585771,524424391837,523331305575,526331090131,523325996906])    
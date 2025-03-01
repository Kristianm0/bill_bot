#@Kristian Martinez Colina | Programacion Python
"----"
"""Bill Bot: Mini-Proyecto  
Un bot en Python que manda mensajes de WhatsApp automáticamente, como si Bill hackeara la realidad.  

🟢 Guía en la descripción 🟢  
"""
"""Parte 5: ¿Como leer números en WhatsApp?
 Vamos a limpiar números en Python para que sean válidos en WhatsApp Web, asegurando que tengan el prefijo correcto. 
"""

## -> Parte 2: Automatización de WhatsApp con Selenium ##->
from selenium import webdriver
# 🟢 Sub modulos
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 🟢 Configuramos el ChromeDriver (el hechizo para controlarlo)
from webdriver_manager.chrome import ChromeDriverManager

# 🟢 Herramientas clave para interactuar con la web
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  

# 🟢 Jugamos con el tiempo y la realidad
import time  # Pausas entre acciones
import urllib.parse  # Modifica URLs sin errores

## -> Parte 3: Que es Github, comandos básicos de github (Hechos en consola)

# -> 3.1 Subir a un proyecto a Github (Hechos en consola)

# -> 4: Configuracion Navegador 
#Funcion 
# Ritual para invocar el navegador
def portal_dimensional():
    """Abre un portal interdimensional (Navegador)"""
    opciones = Options()  # 🔮 Preparamos el conjuro para configurar el navegador antes de invocarlo
    opciones.add_argument("--window-size=1100,700")  # 📏 Definimos el tamaño del portal (ventana del navegador)
    opciones.add_argument("--disable-notifications")  # 🚫 Bloqueamos interferencias (notificaciones de WhatsApp)

    # 🛠️ Invocamos al sirviente ChromeDriver para que maneje el navegador
    servicio = Service(ChromeDriverManager().install())  

    # 🔥 Finalmente, abrimos el portal (el navegador) con las configuraciones establecidas
    return webdriver.Chrome(service=servicio, options=opciones)  
  
#4.1 Fusionar Dimensiones (Merge a main)

#Rama de 
# 📌 5: Leer numeros whatsApp
#Funcion - Formato compatible con WA Web
def corregir_numero(numero):
    numero = "".join(filter(str.isdigit, numero))
    if len(numero) == 10 and not numero.startswith("57"):
        numero = "57" + numero
    if not numero.startswith("+"):
        numero = "+" + numero
    return numero
 
# 📌 6: Envio de Mensajes a WhatsApp
def invocar_mensaje(driver, numero, mensaje):
    try: 
        # Codificamos el mensaje para que WhatsApp lo entienda
        mensaje_codificado = urllib.parse.quote(mensaje)
        url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje_codificado}"
        print(f"Abriendo conexión con: {numero}")
        driver.get(url)

        # Esperamos hasta 60 segundos para que cargue el botón de enviar
        espera = WebDriverWait(driver, 60)
        boton_svg = espera.until(EC.presence_of_element_located((By.XPATH, "//span[@data-icon='send']")))
        boton_enviar = boton_svg.find_element(By.XPATH, ".//..")  # Obtenemos el botón real

        print("Usando magia oscura...")
        time.sleep(3)  # Esperamos un poco para que todo se cargue bien

        print("Lanzando mensaje al vacío...")
        driver.execute_script("arguments[0].click();", boton_enviar)  # Hacemos clic en el botón de enviar

        print("Esperando confirmación del más allá...")
        time.sleep(3)  # Damos tiempo para que el mensaje se envíe correctamente

        return True, "🟢 Mensaje enviado a otra dimensión"
    except Exception as e: 
        print(f"🔥 ¡Algo salió mal en el ritual! {str(e)}")
        return False, f"❌ Error dimensional: {str(e)}"



#@Kristian Martinez Colina | Programacion Python
"----"
"""Bill Bot: Mini-Proyecto  
Un bot en Python que manda mensajes de WhatsApp automáticamente, como si Bill hackeara la realidad.  

🟢 Guía en la descripción 🟢  
"""
"""Parte 4.1: ¿Como  Fusionar Dimensiones o ramas (Git Merge a main)?

# git status:  Verifica en qué dimensión (rama) estás
(Verificando que ya estas en la rama de cambios)
# git add . = Guarda los cambios de la dimensión (rama) alternativa

# git commit -m = "Descripción de cambios realizados"  

# Git checkout main = Viaja de vuelta a la dimensión (rama) principal (`main`)

# Git merge "nombre_rama" = Fusiona la dimensión alternativa con la línea principal (rama)

# git merge "nombre_rama" -d = (Opcional) Destruir la dimensión alternativa

#git push origin main = Sube todo a la dimension (rama) original


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

#📌
# -> 4: Configuracion Navegador 🍕
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


#Archivo main sin funcion


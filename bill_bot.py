#@Kristian Martinez Colina | Programacion Python
"----"
"""Bill Bot: Mini-Proyecto  
Un bot en Python que manda mensajes de WhatsApp automáticamente, como si Bill hackeara la realidad.  

🟢 Guía en la descripción 🟢  
"""
"""Parte 3.1: ¿Como Subir un proyecto a Github?
Bill subirá a su GitHub (o libro mágico) las modificaciones del Bill Bot o el hechizo para enviar mensajes por WhatsApp.

"""
"""Pasos: 
1. Crear repositorio (libro mágico) en GitHub.
2. Configurar Git (datos del hechicero o Bill).
3. Subir proyecto (hechizos).
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

# -> 3.1 Subir a un proyecto a Github

git_init = "Crea un nuevo libro/repositorio"
git_add = "Marca los hechizos/páginas que quieres guardar"
git_commit = "Guarda cambios de hechizos/código"
git_remote_add_origin = "Conecta tu grimorio a una biblioteca remota"
git_push = "Envía tu grimorio a la biblioteca para que otros magos lo vean"








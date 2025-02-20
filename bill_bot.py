#@Kristian Martinez Colina | Programacion Python
"----"
"""Bill Bot: Mini-Proyecto  
Un bot en Python que manda mensajes de WhatsApp automáticamente, como si Bill hackeara la realidad.  

🟢 Guía en la descripción 🟢  
"""
"""Parte 4.1: ¿Como Fusionar Dimensiones o ramas (Git Merge a main)?
- git status → Muestra en qué rama (dimension) estás y qué cambios hay.
- git add . -> Añde cambios de dimension de modificaciones 
- git commit -m "Descripcion" -> de cambios
- git checkout main → Cambia a la rama principal, dimension original
- git merge "Nombre_de_rama" → Fusiona los cambios de "Nombre_de_rama" en main, une dimension de modificaciones a dimension original
- git branch -d "Nombre_de_rama" → Borra la rama que hicistes (nombre_de_rama) si ya fue fusionada. (opcional)

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


#4.1 Fusionar Dimensiones (Merge a main)

#Nuevo
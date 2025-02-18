#@Kristian Martinez Colina | Programacion Python
"----"
"""Bill Bot: Mini-Proyecto  
Un bot en Python que manda mensajes de WhatsApp automáticamente, como si Bill hackeara la realidad.  

🟢 Guía en la descripción 🟢  
"""
"""Parte 3.2: ¿Como crear Ramas en Github para modificaciones?
Vamos a crear una nueva rama en GitHub usando VS Code, como si estuvieras dividiendo la realidad en dimensiones alternativas, para no romper la realidad donde estamos o el codigo original.
"""
"""Pasos: 
1. git status -> Muestra en qué realidad o codigo estás, chequeando el estado de tus cambios.

2. git checkout -b "nombre_rama" -> Abre un portal a una nueva rama o version del codigo, es como crear una nueva dimensión.

3. (Realiza cambios y guarda los archivos)
Bill edita la realidad (código) y guarda sus hechizos.

4. git add . -> Recolecta los ingredientes mágicos para el hechizo o los cambios del codigo.

5. git commit -m "Descripción de los cambios realizados" -> Guarda el hechizo o codigo en el libro de github con una nota descriptiva.

6. git push origin "nombre_rama" -> Envía el hechizo al repositorio mágico (GitHub) para que otros lo vean.
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

#📌
# -> 4: Configuracion Navegador 🍕





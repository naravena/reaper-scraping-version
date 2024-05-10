import requests
from bs4 import BeautifulSoup
import os

# Variables globales
URL = "https://www.reaper.fm/download.php"
CSS_SELECTOR = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.downloadinfo"
STATE_FILE = "previous_state.txt"
NO_STATE_MESSAGE = "No hay estado anterior registrado."
NO_ELEMENT_MESSAGE = "No se encontró ningún elemento con el selector CSS especificado."
CHANGE_MESSAGE = "¡La versión se ha actualizado!"


# Función para obtener el contenido de la página web
def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Error al obtener la página:", response.status_code)
        return None


# Función para extraer el texto del elemento con el selector CSS especificado
def extract_text(html_content, css_selector):
    soup = BeautifulSoup(html_content, 'html.parser')
    element = soup.select_one(css_selector)
    if element:
        return element.get_text(strip=True)
    else:
        print("No se encontró ningún elemento con el selector CSS especificado.")
        return None


# Función para cargar o crear el archivo de estado anterior y leer su contenido
def load_previous_state(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    else:
        return None


# Función para guardar el estado actual en el archivo
def save_current_state(filename, state):
    with open(filename, 'w') as file:
        file.write(state)

import requests
from bs4 import BeautifulSoup
import os

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


# URL de la página web a scrapear
url = "https://www.reaper.fm/download.php"

# Selector CSS del elemento a monitorear
css_selector = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.downloadinfo"

# Nombre del archivo para almacenar el estado anterior
state_file = "previous_state.txt"

# Obtener el contenido de la página web
html_content = get_page_content(url)

if html_content:
    # Extraer el texto del elemento
    current_state = extract_text(html_content, css_selector)
    if current_state:
        # Cargar el estado anterior
        previous_state = load_previous_state(state_file)

        if previous_state:
            # Comparar el estado actual con el estado anterior
            if current_state != previous_state:
                print("¡El texto ha cambiado!")
                # Guardar el estado actual para futuras comparaciones
                save_current_state(state_file, current_state)
            else:
                print("El texto sigue siendo el mismo.")
        else:
            # Si no hay estado anterior, guardar el estado actual para futuras comparaciones
            print("No hay estado anterior registrado.")
            save_current_state(state_file, current_state)

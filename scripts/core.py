import os

import requests
from bs4 import BeautifulSoup

URL = "https://www.reaper.fm/download.php"
CSS_SELECTOR = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.downloadinfo"
PREVIOUS_STATUS = os.environ['PREVIOUS_STATUS']  # Obtén el estado anterior de una variable


def get_current_status():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    status_element = soup.select_one(CSS_SELECTOR)
    if status_element:
        return status_element.get_text(strip=True)
    return None


def notify_status_change(previous_status, current_status):
    if previous_status != current_status:
        return True
    return False


def main():
    try:
        current_status = get_current_status()
        is_change_in_version = notify_status_change(PREVIOUS_STATUS, current_status)
        if current_status is not None and is_change_in_version:
            status_message = f'''
            ¡¡¡ Nueva Versión !!!
            *Estado anterior*: {PREVIOUS_STATUS}
            *Estado actual*: {current_status}
            '''
            return is_change_in_version, status_message
        else:
            return False, "No se encontró un cambio en la versión"
    except Exception as e:
        print("Se produjo un error durante la ejecución de main():", e)
        return False, "Error durante la ejecución del script"


if __name__ == "__main__":
    os.environ['IS_CHANGE_VERSION'] = str(main()[0])
    os.environ['STATUS_MESSAGE_TEXT'] = main()[1]

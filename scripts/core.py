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
        # Aquí puedes implementar la lógica para notificar el cambio de estado
        print("El estado ha cambiado. Se notificará el cambio.")
        return True
    return False


def main():
    current_status = get_current_status()
    is_change_in_version = notify_status_change(PREVIOUS_STATUS, current_status)

    try:
        if current_status is not None and is_change_in_version:
            status_message = f'''
            ¡¡¡ Nueva Versión !!!
            *Estado anterior*: {PREVIOUS_STATUS}
            *Estado actual*: {current_status}
            '''
            return is_change_in_version, status_message
    except Exception as e:
        print("Se produjo un error durante la ejecución de main():", e)
        return False


if __name__ == "__main__":
    is_change_version, status_message_text = main()
    os.environ['IS_CHANGE_VERSION'] = str(is_change_version)
    os.environ['STATUS_MESSAGE_TEXT'] = status_message_text


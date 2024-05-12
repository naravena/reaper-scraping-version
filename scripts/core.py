import requests
from bs4 import BeautifulSoup

from send_whatsapp_message import WhatsAppMessageSender
from utils import get_environment_variable, CSS_SELECTOR, URL


def get_current_status():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    status_element = soup.select_one(CSS_SELECTOR)
    if status_element:
        return status_element.get_text(strip=True)
    return None


def status_message(previous_status, current_status):
    return f'''
            ¡¡¡ Nueva Versión !!!
            *Estado anterior*: {previous_status}
            *Estado actual*: {current_status}
            '''


def main():
    try:
        current_status = get_current_status()
        is_change_in_version = get_environment_variable('PREVIOUS_STATUS') != current_status
        if current_status is not None and is_change_in_version:
            print(status_message(get_environment_variable('PREVIOUS_STATUS'), current_status))
            # Crear una instancia de WhatsAppMessageSender
            # Crear una instancia de WhatsAppMessageSender
            whatsapp_sender = WhatsAppMessageSender(get_environment_variable('TWILIO_ACCOUNT_SID'),
                                                    get_environment_variable('TWILIO_AUTH_TOKEN'),
                                                    get_environment_variable('TWILIO_PHONE_NUMBER'),
                                                    get_environment_variable('WHATSAPP_PHONE_NUMBER'))
            whatsapp_sender.send_message(status_message(get_environment_variable('PREVIOUS_STATUS'), current_status))
        else:
            print("NO HAY NUEVA VERSION")
    except Exception as e:
        print("Se produjo un error durante la ejecución de main():", e)


if __name__ == "__main__":
    main()

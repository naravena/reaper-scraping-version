import requests
from bs4 import BeautifulSoup

from scripts.send_whatsapp_message import WhatsAppMessageSender
from scripts.utils import URL, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, WHATSAPP_PHONE_NUMBER, \
    PREVIOUS_STATUS, CSS_SELECTOR


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
        is_change_in_version = PREVIOUS_STATUS != current_status
        if current_status is not None and is_change_in_version:
            print(status_message(PREVIOUS_STATUS, current_status))
            # Crear una instancia de WhatsAppMessageSender
            whatsapp_sender = WhatsAppMessageSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER,
                                                    WHATSAPP_PHONE_NUMBER)
            whatsapp_sender.send_message(status_message(PREVIOUS_STATUS, current_status))
        else:
            print("NO HAY NUEVA VERSION")
    except Exception as e:
        print("Se produjo un error durante la ejecución de main():", e)


if __name__ == "__main__":
    main()

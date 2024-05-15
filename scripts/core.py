import requests
from bs4 import BeautifulSoup

from whatsapp_app_message_sender import WhatsAppMessageSender
from utils import get_environment_variable, webs_to_scraping, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, \
    TWILIO_PHONE_NUMBER, WHATSAPP_PHONE_NUMBER


def get_current_status(selector):
    response = requests.get(selector)
    soup = BeautifulSoup(response.content, 'html.parser')
    status_element = soup.select_one(selector)
    if status_element:
        return status_element.get_text(strip=True)
    return None


def status_message(previous_status, current_status):
    return f'''
            ¡¡¡ Nueva Versión !!!
            *Estado anterior*: {previous_status}
            *Estado actual*: {current_status}
            '''


def send_message_by_whatsapp(pre_status, post_status):
    whatsapp_sender = WhatsAppMessageSender(get_environment_variable(TWILIO_ACCOUNT_SID),
                                            get_environment_variable(TWILIO_AUTH_TOKEN),
                                            get_environment_variable(TWILIO_PHONE_NUMBER),
                                            get_environment_variable(WHATSAPP_PHONE_NUMBER))
    print(status_message(pre_status, post_status))
    whatsapp_sender.send_message(status_message(pre_status, post_status))


def main():
    try:
        for page, (url, status) in webs_to_scraping.items():
            current_status = get_current_status(url)
            is_change_in_version = status != current_status
            if current_status is not None and is_change_in_version:
                send_message_by_whatsapp(status, current_status)
            else:
                print(f"NO HAY NUEVA VERSION PARA {page}")
    except Exception as e:
        print("Se produjo un error durante la ejecución de main():", e)


if __name__ == "__main__":
    main()

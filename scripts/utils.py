import os


def get_environment_variable(var_name, default=""):
    try:
        return os.environ[var_name]
    except KeyError:
        print(f"La variable de entorno '{var_name}' no está definida. Usando valor por defecto.")
        return default


# Variables globales
REAPER_URL = "https://www.reaper.fm/download.php"
OBS_URL = "https://obsproject.com/es/download"
REAPER_CSS_SELECTOR = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.downloadinfo"
OBS_CSS_SELECTOR = "#win_blurb > div.dl_box > span.dl_ver"

REAPER_PREVIOUS_STATUS = 'REAPER_PREVIOUS_STATUS'
OBS_PREVIOUS_STATUS = 'OBS_PREVIOUS_STATUS'
TWILIO_ACCOUNT_SID = 'TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'TWILIO_PHONE_NUMBER'
WHATSAPP_PHONE_NUMBER = 'WHATSAPP_PHONE_NUMBER'
MESSAGE = 'MESSAGE'

webs_to_scraping = {
    'REAPER': [REAPER_URL, get_environment_variable(REAPER_PREVIOUS_STATUS), REAPER_CSS_SELECTOR],
    'OBS': [OBS_URL, get_environment_variable(OBS_PREVIOUS_STATUS), OBS_CSS_SELECTOR]
}

params_to_send_whatsapp_message = [get_environment_variable(TWILIO_ACCOUNT_SID),
                                   get_environment_variable(TWILIO_AUTH_TOKEN),
                                   get_environment_variable(TWILIO_PHONE_NUMBER),
                                   get_environment_variable(WHATSAPP_PHONE_NUMBER)]

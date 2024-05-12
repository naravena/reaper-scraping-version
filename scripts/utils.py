import os


def get_environment_variable(var_name, default=""):
    try:
        return os.environ[var_name]
    except KeyError:
        print(f"La variable de entorno '{var_name}' no está definida. Usando valor por defecto.")
        return default


# Variables globales
URL = "https://www.reaper.fm/download.php"
CSS_SELECTOR = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.downloadinfo"
NO_STATE_MESSAGE = "No hay estado anterior registrado."
NO_ELEMENT_MESSAGE = "No se encontró ningún elemento con el selector CSS especificado."
CHANGE_MESSAGE = "¡La versión se ha actualizado!"
PREVIOUS_STATUS = get_environment_variable('PREVIOUS_STATUS')
TWILIO_ACCOUNT_SID = get_environment_variable('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = get_environment_variable('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = get_environment_variable('TWILIO_PHONE_NUMBER')
WHATSAPP_PHONE_NUMBER = get_environment_variable('WHATSAPP_PHONE_NUMBER')
MESSAGE = get_environment_variable('MESSAGE')

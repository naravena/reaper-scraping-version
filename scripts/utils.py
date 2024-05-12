import os

# Variables globales
URL = "https://www.reaper.fm/download.php"
CSS_SELECTOR = "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div.downloadinfo"
NO_STATE_MESSAGE = "No hay estado anterior registrado."
NO_ELEMENT_MESSAGE = "No se encontró ningún elemento con el selector CSS especificado."
CHANGE_MESSAGE = "¡La versión se ha actualizado!"
PREVIOUS_STATUS = os.environ['PREVIOUS_STATUS']  # Obtén el estado anterior de una variable
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
WHATSAPP_PHONE_NUMBER = os.environ['WHATSAPP_PHONE_NUMBER']
MESSAGE = os.environ['MESSAGE'] or ""

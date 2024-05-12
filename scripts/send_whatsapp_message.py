from whatsapp_app_message_sender import (WhatsAppMessageSender)
from utils import get_environment_variable

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de WhatsAppMessageSender
    whatsapp_sender = WhatsAppMessageSender(get_environment_variable('TWILIO_ACCOUNT_SID'),
                                            get_environment_variable('TWILIO_AUTH_TOKEN'),
                                            get_environment_variable('TWILIO_PHONE_NUMBER'),
                                            get_environment_variable('WHATSAPP_PHONE_NUMBER'))

    # Enviar el mensaje
    whatsapp_sender.send_message(get_environment_variable('MESSAGE'))

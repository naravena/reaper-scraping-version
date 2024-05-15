from whatsapp_app_message_sender import (WhatsAppMessageSender)
from utils import get_environment_variable, params_to_send_whatsapp_message

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de WhatsAppMessageSender
    whatsapp_sender = WhatsAppMessageSender(params_to_send_whatsapp_message)

    # Enviar el mensaje
    whatsapp_sender.send_message(get_environment_variable('MESSAGE'))

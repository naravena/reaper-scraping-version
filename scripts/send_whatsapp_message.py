from twilio.rest import Client

from utils import get_environment_variable


class WhatsAppMessageSender:
    def __init__(self, twilio_account_sid, twilio_auth_token, twilio_phone_number, whatsapp_phone_number):
        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_phone_number = twilio_phone_number
        self.whatsapp_phone_number = whatsapp_phone_number

        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_message(self, message):
        try:
            message = self.client.messages.create(
                from_=self.twilio_phone_number,
                body=message,
                to=self.whatsapp_phone_number
            )
            print("Mensaje enviado correctamente a:", message.to)
        except Exception as e:
            print("Se produjo un error al enviar el mensaje:", str(e))


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de WhatsAppMessageSender
    whatsapp_sender = WhatsAppMessageSender(get_environment_variable('TWILIO_ACCOUNT_SID'),
                                            get_environment_variable('TWILIO_AUTH_TOKEN'),
                                            get_environment_variable('TWILIO_PHONE_NUMBER'),
                                            get_environment_variable('WHATSAPP_PHONE_NUMBER'))

    # Enviar el mensaje
    whatsapp_sender.send_message(get_environment_variable('MESSAGE'))

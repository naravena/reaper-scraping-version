from twilio.rest import Client


class WhatsAppMessageSender:
    def __init__(self, params):
        self.twilio_account_sid, self.twilio_auth_token, self.twilio_phone_number, self.whatsapp_phone_number = params

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

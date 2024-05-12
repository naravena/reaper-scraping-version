from twilio.rest import Client


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

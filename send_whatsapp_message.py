import os

from twilio.rest import Client


# Configuración de la cuenta de Twilio
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']

# Configuración del número de teléfono de destino
WHATSAPP_PHONE_NUMBER = os.environ['WHATSAPP_PHONE_NUMBER']

# Mensaje que quieres enviar
mensaje = os.environ['MESSAGE']

# Crear el cliente de Twilio
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

try:
    # Enviar el mensaje de WhatsApp
    message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        body=mensaje,
        to=WHATSAPP_PHONE_NUMBER
    )

    print("Mensaje enviado correctamente a:", message.to)
except Exception as e:
    print("Se produjo un error al enviar el mensaje:", str(e))

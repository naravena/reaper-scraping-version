import os
from twilio.rest import Client

# Configuración de la cuenta de Twilio
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = 'tu_numero_de_telefono_twilio'

# Configuración del número de teléfono de destino
whatsapp_phone_number = os.environ['WHATSAPP_PHONE_NUMBER']

# Mensaje que quieres enviar
mensaje = os.environ['MESSAGE']

# Crear el cliente de Twilio
client = Client(account_sid, auth_token)

try:
    # Enviar el mensaje de WhatsApp
    message = client.messages.create(
        body=mensaje,
        from_=twilio_phone_number,
        to=whatsapp_phone_number
    )

    print("Mensaje enviado correctamente a:", message.to)
except Exception as e:
    print("Se produjo un error al enviar el mensaje:", str(e))

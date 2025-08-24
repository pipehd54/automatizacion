import os
import ssl
import smtplib
from email.message import EmailMessage
from getpass import getpass

def enviar_email(destinatario, asunto, cuerpo, remitente=None, password=None):
    # Usar variables de entorno seguras
    remitente = remitente or os.getenv('EMAIL_REMITENTE') or input("Ingrese el email del remitente: ")
    if password:
        pass
    elif os.getenv('EMAIL_PASSWORD'):
        password = os.getenv('EMAIL_PASSWORD')
    else:
        try:
            password = getpass("Ingrese la contraseña del email del remitente: ")
        except Exception:
            password = input("Ingrese la contraseña del email del remitente (visible): ")

    # Limpiar posibles saltos de línea y espacios
    remitente = remitente.strip()
    password = password.strip()

    if not remitente or not password:
        raise ValueError("El email y la contraseña son obligatorios.")

    em = EmailMessage()
    em['From'] = remitente
    em['To'] = destinatario
    em['Subject'] = asunto
    em.set_content(cuerpo)

    contexto = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(remitente, password)
            smtp.sendmail(remitente, destinatario, em.as_string())
            print("Email enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el email: {e}")

if __name__ == "__main__":
    # Puedes definir aquí el remitente y password o usar variables de entorno
    remitente = "email_aqui"  # Cambia por tu correo real
    password = "contrasena_aqui"  # Cambia por tu contraseña de aplicación real
    destinatario = 'pipetimoty@gmail.com'
    asunto = 'Esto es un mensaje automatizado.'
    cuerpo = '''
    Si ves este mensaje es porque funciono mi mensaje automatizado con Python mi papu
    '''

    enviar_email(destinatario, asunto, cuerpo, remitente, password)

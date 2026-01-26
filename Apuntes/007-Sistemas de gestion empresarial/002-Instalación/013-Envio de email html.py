'''
Script para el envío de correos asíncrono utilizando hilos.
Versión: 1.2
Autor: Valentin Antonio De Gennaro
'''

import smtplib
import threading
from email.message import EmailMessage

## CONFIGURACION DEL SERVIDOR SMTP ##
SMTP_SERVER = "mail.gmx.es"
SMTP_PORT = 587
SMTP_USER = "benito-camela@gmx.es"
SMTP_PASS = "chupameunhuevo25"

## DEFINIMOS LA FUNCION DE ENVIO ##
def enviarCorreoAsync(remitente, destinatario, asunto, contenido_html):
    # creamos el objeto mensaje #
    msg = EmailMessage()
    msg['From'] = remitente
    msg["To"] = destinatario
    msg["Subject"] = asunto

    msg.set_content("Este correo requiere un cliente compatible con HTML.")
    msg.add_alternative(contenido_html, subtype="html")

    try:
        # iniciamos la conexion smtp dentro del hilo #
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)
        
        print("\n--------------------")
        print(f"--> [EXITO] Correo enviado a: {destinatario}")
        print("--------------------")
            
    except Exception as error:
        print("\n--------------------")
        print(f"--> [ERROR] Fallo en el envío: {error}")
        print("--------------------")

## LOGICA PRINCIPAL DEL PROGRAMA ##
# definimos el contenido html #
html_content = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      td,th{padding:5px;}
    </style>
  </head>
  <body>
    <table border="0" style="font-family:sans-serif;text-align:justify;">
      <tr>
        <td style="width:10%"></td>
        <td style="width:80%">
          <table border="0" width="100%">
            <tr>
              <td>
                <h1 style="text-align:center;">Informe de notas</h1>
                <p>
                  Este no es el boletín trimestral de notas
                  del centro de formación.<br>
                  Este es un informe de notas de profesor.<br>
                  Incluye las notas de las asignaturas:
                </p>
                <ul>
                  <li>Programación</li>
                  <li>Lenguajes de marcas</li>
                  <li>Bases de datos</li>
                  <li>Proyecto intermodular I</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td>
                <table border="0" width="100%">
                  <tr style="background:indigo;color:white;">
                    <th>Módulo profesional</th>
                    <th>ACT</th>
                    <th>CONTROL</th>
                    <th>EVAL</th>
                    <th>COMP</th>
                    <th>TOT</th>
                  </tr>
                  <tr>
                    <td>Programación</td>
                    <td>8</td><td>8</td><td>8</td><td>8</td><td>8</td>
                  </tr>
                  <tr>
                    <td>Lenguajes de marcas</td>
                    <td>8</td><td>8</td><td>8</td><td>8</td><td>8</td>
                  </tr>
                  <tr>
                    <td>Bases de datos</td>
                    <td>8</td><td>8</td><td>8</td><td>8</td><td>8</td>
                  </tr>
                  <tr>
                    <td>Proyecto Intermodular</td>
                    <td>8</td><td>8</td><td>8</td><td>8</td><td>8</td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td>
                <h3 style="text-align:center;">Revisión de notas</h3>
                <p>
                  Quien quiera revisar calificaciones, mañana martes
                  27 de enero a las 11:15 (en el descanso)
                </p>
              </td>
            </tr>
          </table>
        </td>
        <td style="width:10%"></td>
      </tr>
    </table>
  </body>
</html>

"""

# preparamos los datos de envio #
remitente_data = "Benito Dev <benito-camela@gmx.es>"
destinatario_data = "danieloliveiravidal12@gmail.com"
asunto_data = "Informe de notas"

print("--------------------")
print("Preparando envío de correo...")

# creamos el hilo para no bloquear el programa #
hilo_correo = threading.Thread(
    target=enviarCorreoAsync, 
    args=(remitente_data, destinatario_data, asunto_data, html_content)
)

# iniciamos la ejecucion paralela #
hilo_correo.start()

print("El sistema sigue libre mientras se envía el correo.")
print("--------------------")

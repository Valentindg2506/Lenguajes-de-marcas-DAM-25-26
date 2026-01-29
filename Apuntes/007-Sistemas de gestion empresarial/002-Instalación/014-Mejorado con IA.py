import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# =========================
# CONFIGURACIÓN
# =========================

SMTP_SERVER = "smtp.resend.com"
SMTP_PORT = 587
SMTP_USER = "resend"
SMTP_PASSWORD = "re_ARFc9hM3_GGnxJA951gSz161fSWCLCoot"

while True:
	EMAIL_ORIGEN = "CEAC@tinoprop.com"
	EMAIL_DESTINO = "danieloliveiravidal12@gmail.com"

	ASUNTO = "Informe de notas"

	# =========================
	# CUERPO HTML
	# =========================

	HTML_CONTENT = """
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

	# =========================
	# ENVÍO DEL CORREO
	# =========================

	def enviar_correo():
		msg = MIMEMultipart("alternative")
		msg["From"] = EMAIL_ORIGEN
		msg["To"] = EMAIL_DESTINO
		msg["Subject"] = ASUNTO

		html_part = MIMEText(HTML_CONTENT, "html")
		msg.attach(html_part)

		with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
		    server.starttls()
		    server.login(SMTP_USER, SMTP_PASSWORD)
		    server.send_message(msg)

		print("✅ Correo enviado correctamente")

	if __name__ == "__main__":
		enviar_correo()


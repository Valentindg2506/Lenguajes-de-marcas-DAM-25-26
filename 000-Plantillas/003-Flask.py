## IMPORTO LA LIBRERIA FLASK PARA CREAR WEBS ##
from flask import Flask, render_template ## CARGO ARCHIVOS HTML ##

## CREO UNA NUEVA APP ##
app = Flask(__name__)

## ESCUCHO LA RUTA RAIZ ##
@app.route("/")
def inicio():
	## Y RENDERIZO UNA PLANTILLA LAMADA index.html ##	
	return render_template("index.html")

## SI ESTE ARCHIVO NO ES UNA LIBRERIA Y ES EL ARCHIVO PRINCIPAL
if __name__ == "__main__":
## PON EN MARCHA LA APLICACIÓN ##
	app.run(debug = True)

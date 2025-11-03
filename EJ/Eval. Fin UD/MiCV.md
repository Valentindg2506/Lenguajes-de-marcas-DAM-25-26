En este ejercicio vamos a realizar nuestro curriculum vitae pero en lenguaje HTML, vamos a realizar una pagina web completa y funcional y con su posicionamiento adecuado.

---

Para realizar este ejercicio primero debemos definir el tipo de documento y el idioma de la pagina de la siguiente manera:
```
	<!DOCTYPE html>
	<html lang="es">
```
Luego usando las etiquetas `<head>` vamos a indicar el lenguaje de codigo a utilizar y el titulo:
```
	title>Valentin Antonio De Gennaro</title>
	<meta charset="utf-8">
```
Luego dentro de ese mismo `<head>` debemos introducir las etiquetas de posicionamiento:
```
	<meta name= "Curriculum Vitae" content= "Curriculum Vitae de Valentin De Gennaro">
	<meta name= "viewport" content= "width=device-width, initial-scale=1.0">
	<meta name= "keywords" content= "Curriculum, CV, Valentin de gennaro">
	<meta name= "author" content= "Valentin Antonio De Gennaro">
	<link rel= "icon" href="imagen" type= "image/png">
	<meta property= "og:title" content= "Valentin De Gennaro">
	<meta property= "og:description" content= "Curriculum Vitae de Valentin De Gennaro">
	<meta property= "og:image" content= "imagen">
	<meta property= "og:url" content= "https://valentindegennarocv.com">
	<meta property= "og:type" content= "website">
```
Luego le añadimos el estilo:
```
	html{
		background:grey;
		font-family: sans-serif;
		font-size: 12px;
	}
```
Luego de definir todo lo anterior empezamos con el `<body>` que como el nombre lo indica es el cuerpo de la pagina, debemos dividir la pagina por secciones, para realizar el CV es util:
```
	<body>
        <section id="izquierda">
        <section id="derecha">
	</body>
```
Y luego le añadimos información dentro de esas secciones, en este caso dentro de la seccion izquierda encontras una imagen y datos puntuales de la persona:
```
	<img src="valentin.jpg">
	<h1>Valentín De Gennaro</h1>
	<h5>Estudiante de DAM</h5>
	<article>
		<h3>PERFIL</h3>
		<p>Me caracterizo por ser una persona dinámica, organizada y expeditiva. Altamente comprometido en trabajar en empresas que me impulsen a mi desarrollo personal y profesional.</p>
	</ul>
```
Y en la seccion derecha la experiencia profesional, los idiomas y la educación:
```
<div id="experiencia">
    <h3>Experiencia profesional</h3>
    <article>
        <div class="texto">
            <h4>MooveCars | 2025 - 2025</h4>
            <h5>Conductor VTC, Valencia</h5>
            <h5>Tareas:</h5>
            <p>Transporte de pasajeros mediante la aplicación de Uber.</p>
        </div>
	</article>
```

---

A continuación la pagina completa:
```
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Curriculum</title>
        <meta charset="utf-8">
        <meta name= "Curriculum Vitae" content= "Curriculum Vitae de Valentin De Gennaro">
        <meta name= "viewport" content= "width=device-width, initial-scale=1.0">
        <meta name= "keywords" content= "Curriculum, CV, Valentin de gennaro">
        <meta name= "author" content= "Valentin Antonio De Gennaro">
        <link rel= "icon" href="imagen" type= "image/png">
        <meta property= "og:title" content= "Valentin De Gennaro">
        <meta property= "og:description" content= "Curriculum Vitae de Valentin De Gennaro">
        <meta property= "og:image" content= "imagen">
        <meta property= "og:url" content= "https://valentindegennarocv.com">
        <meta property= "og:type" content= "website">
        <style>
            html{
                background:grey;
                font-family: sans-serif;
                font-size: 13px;
            }
            body{
                width:600px;
                background:white;
                margin:auto;
                display:flex;
            }
            #izquierda article{
                padding: 3%;
                height: auto;
            }
            #izquierda img{
                margin:auto;
                width:100%;
            }
            #izquierda{
                flex:2;
                font-size: 11px;
                background:steelblue;
                padding: 20px;
            }
            #derecha {
                flex:4;
                padding: 30px;
            }
            #derecha h3{
                text-transform: uppercase;
                text-decoration: none;
                color: inherit;
                color:dodgerblue;
                background: ghostwhite;
                padding: 5px;
            }
            #derecha article{
                display: flex;
                align-items: center;
                align-content: space-around;
                gap: 20px;
            }
            #derecha article *{
                padding: 0px;
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <section id="izquierda">
            <img src="valentin.jpg">
            <h1>Valentín De Gennaro</h1>
            <h5>Estudiante de DAM</h5>
            <article>
                <h3>PERFIL</h3>
                <p>Me caracterizo por ser una persona dinámica, organizada y expeditiva. Altamente comprometido en trabajar en empresas que me impulsen a mi desarrollo personal y profesional.</p>
                </ul>
            </article>
            <article>
                <h3>HABILIDADES</h3>
                <ul>
                    <li>Trabajo en equipo</li>
                    <li>Comunicación</li>
                    <li>Valencia, España</li>
                </ul>
            </article>
            <article>
                <h3>CONTACTO</h3>
                <ul>
                    <li>+34 641025668</li>
                    <li>valentin@jocarsa.com</li>
                    <li>Valencia, España</li>
                </ul>
            </article>
        </section>
        <section id="derecha">
            <div id="experiencia">
                <h3>Experiencia profesional</h3>
                <article>
                    <div class="texto">
                        <h4>MooveCars | 2025 - 2025</h4>
                        <h5>Conductor VTC, Valencia</h5>
                        <h5>Tareas:</h5>
                        <p>Transporte de pasajeros mediante la aplicación de Uber.</p>
                    </div>
                </article>
                <article>
                    <div class="texto">
                        <h4>4Play | 2024 - 2025</h4>
                        <h5>Administrativo, Buenos Aires</h5>
                        <h5>Tareas:</h5>
                        <p>Subir las ventas realizadas en la plataforma de la empresa y copiarlas a un excel.</p>
                    </div>
                </article>
                <article>
                    <div class="texto">
                        <h4>Burguer King | 2023 - 2023</h4>
                        <h5>Delivery, Valencia</h5>
                        <h5>Tareas:</h5>
                        <p>Delivery de alimentos en ciclomotor y venta de comida en el local.</p>
                    </div>
                </article>
                <article>
                    <div class="texto">
                        <h4>SuValencia | 2022 - 2023</h4>
                        <h5>Administrativo, Valencia</h5>
                        <h5>Tareas:</h5>
                        <p>Captación de clientes mediante redes sociales, manejo de redes sociales.</p>
                    </div>
                </article>
            </div>
            <div id="Idiomas">
                <h3>Idiomas</h3>
                <article>
                    <div class="texto">
                        <ul>Español: Nativo</ul>
                        <ul>Ingles: Intermedio</ul>
                    </div>
                </article>
            </div>
            <div id="Educacion">
                <h3>Educación</h3>
                <article>
                    <div class="texto">
                        <h5>2025 - Actualmente | España</h5>
                        <h4>Desarrollo de Aplicaciones Multiplataforma</h4>
                        <p>CEACFP</p>
                    </div>
                </article>
                <article>
                    <div class="texto">
                        <h5>2017 - 2022 | Argentina</h5>
                        <h4>Bachillerato - Ciencias sociales y humanidades</h4>
                        <p>IADES</p>
                    </div>
                </article>
            </div>
        </section>
    </body>
</html>
```

---

**NOTAS:**
- Es muy importante recordar cerrar todas las etiquetas que se abren, ya que de lo contrario esa etiqueta no va a funcionar.
- En este caso el CSS se introdujo dentro del documento HTML, pero no es 100% necesario ya que se puede guardar en un documento aparte que sea `.css` y se conecta con el HTML.

---

**CONCLUSION:**
- Hacer el curriculum en la web para un programador es util ya que es la manera de demostrar lo que hiciste y que sabes hacerlo.

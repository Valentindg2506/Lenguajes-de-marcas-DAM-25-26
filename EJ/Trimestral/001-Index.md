En este ejercicio vamos a crear una maqueta de una pagina web a partir de la base de datos creada anteriormante. Tiene varios articulos con la informacion del portafolio.

---

Para realizar este ejercicicio primero debemos indicar el tipo de documento y el idioma:
```
<!doctype html>
<html lang="es">
```
Luego abrimos la etiqueta `<head>` y indicamos el titulo y el lenguaje de codigo usado:
```
  <head>
    <title>Portafolio</title>
    <meta charset="utf-8">
```
Y comenzamos con la etiqueta `<style>` para definir el estilo de la web:
```
    <style>
      html,body{background:grey;font-family:sans-serif;}
      header,main,footer{
        background:orangered;
        padding:20px;
        width:800px;
        margin:auto;
        text-align:center;
      }
      main{
        background: white;
        display:grid;
        grid-template-columns:auto auto auto;
        gap:20px;
      }
    </style>
```
Y luego comenzamos con el `<body>`:
```
    <header>
      <h1>Valentín Antonio De Gennaro</h1>
      <h2>valentin@gmail.com</h2>
    </header>
```
Y creamos muchos articulos con la información de la base de datos:
```
    <main>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <p>fecha</p>
        <img src="valentin.jpg">
      </article>
```
Al final de eso hacemos el <footer>:
```
    <footer>
      (c) 2025 Valentin Antonio De Gennaro
    </footer>
```
Y cerramos las etiquetas:
```
  </body>
</html>
```

---

A continuación la web completa:
```
    <!doctype html>
    <html lang="es">
    <head>
        <title>Portafolio</title>
        <meta charset="utf-8">
        <style>
        html,body{background:grey;font-family:sans-serif;}
        header,main,footer{
            background:orangered;
            padding:20px;
            width:800px;
            margin:auto;
            text-align:center;
        }
        main{
            background: white;
            display:grid;
            grid-template-columns:auto auto auto;
            gap:20px;
        }
        </style>
    </head>
    <body>
        <header>
        <h1>Valentín Antonio De Gennaro</h1>
        <h2>valentin@gmail.com</h2>
        </header>
        <main>
        <article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
            <p>Categoria</p>
            <h3>Titulo</h3>
            <p>Descripcion</p>
            <p>fecha</p>
            <img src="valentin.jpg">
        </article>
        <footer>
        (c) 2025 Valentin Antonio De Gennaro
        </footer>
    </body>
    </html>
```

----

**NOTAS:**
- Es importante revisar el tabulado y cerrar las etiquetas.

---

**Conclusiòn:**
Esta pagina es importante para mostrar todo la informaciòn que metemos en la base de datos, a travez de python o del mismo MySql. Es la forma de mostrarle al usuario de una forma bonita la información.
En el ejercicio a continuacion vamos a crear un formulario en el cual el usuario debera introducir sus intereses personales y marcar sus hobbies, y enviarlo.
Para realizar este ejercicio primero hay que poner los elementos basicos para una estructura HTML:
```
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Intereses Personales</title>
        <meta charset="utf-8">
    </head>
    <body>
```
Luego de eso hay que crear el formulario para lo cual vamos a hacer uso de varias etiquetas `<form>` para definir que es un formulario, `<fieldset>` para agrupar los campos y separar uno de otro, `<legend>` para proporcionar una descripcion, `<label>` para asociar una descripcion con el campo de entrada de texto y `<input>` para introducir los datos. A continuacion un ejemplo:
```
    <fieldset>
        <legend> Intereses personales </legend>
        <label for="nombre">Introduce tu nombre</label>
        <input type="text" id="nombre">
        <label for="email">Introduce tu email</label>
        <input type="email" id="email">
        <label for="intereses personales">Introduce tus intereses personales</label>
        <textarea id="intereses personales"></textarea>
    </fieldset>
```
Luego ponemos el boton de enviar:
```
    <input type="submit">
```
A continuacion el codigo completo: 
```
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Intereses Personales</title>
        <meta charset="utf-8">
    </head>
    <body>
        <form>
            <fieldset>
                <legend> Intereses personales </legend>
                <label for="nombre">Introduce tu nombre</label>
                <input type="text" id="nombre">
                <label for="email">Introduce tu email</label>
                <input type="email" id="email">
                <label for="intereses personales">Introduce tus intereses personales</label>
                <textarea id="intereses personales"></textarea>
            </fieldset>
            <fieldset>
                <legend> Hobbies </legend>
                <label for="Hobbies">Jugar al rugby</label>
                <input type="checkbox" id="hobbies">
                <label for="Hobbies">Jugar con el movil</label>
                <input type="checkbox" id="hobbies">
                <label for="Hobbies">Andar en bicicleta</label>
                <input type="checkbox" id="hobbies">
                <label for="Hobbies">Jugar a Gta5</label>
                <input type="checkbox" id="hobbies">
                <label for="Hobbies">Jugar a ARK</label>
                <input type="checkbox" id="hobbies">
            </fieldset>
            <input type="submit">
        </form>
    </body>
</html>
```
**NOTAS:**
- Siempre hay que recordar cerrar las etiquetas ya que de lo contrario la pagina no va a funcionar como se espera.
- El uso del formulario es util para recopilar informacion, en este caso para recopilar intereses personales y hobbies.
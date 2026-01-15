En este proyecto realizamos un tracker de series y peliculas, es una aplicación web diseñada para llevar un control personal de las peliculas y series que consumes. Permite a los usuarios registrarse y organizar series y películas en listas personalizadas según su estado (viendo, vistas, pendientes).
Vamos a centrarnos en las vistas y el lenguaje de marcas en este documento.

---

## Estructura del proyecto

```
Proyecto-Entornos
├── README.md
├── admin
│   ├── BBDD
│   │   ├── AdminViews.png
│   │   ├── AdminViews.svg
│   │   ├── Base de datos.sql
│   │   └── diagrama.svg
│   ├── controladores
│   ├── css
│   │   └── estilo.css
│   ├── img
│   │   ├── adminviews.png
│   │   ├── adminviews_favicon.png
│   │   ├── flechaderecha.png
│   │   ├── iconologout.png
│   │   ├── iconopelicula.png
│   │   ├── iconoseries.png
│   │   └── iconovuelta.png
│   ├── inc
│   │   ├── cabecera.php
│   │   ├── conexion.php
│   │   ├── db.php
│   │   ├── piedepagina.php
│   │   └── sidebar.php
│   ├── index.php
│   ├── peliculas.php
│   ├── series.php
│   └── usuarios.php
├── front
│   ├── controladores
│   │   ├── guardar_contenido.php
│   │   ├── login_procesa.php
│   │   └── registro_procesa.php
│   ├── css
│   │   └── estilo.css
│   ├── exito.php
│   ├── formulario_pelicula.php
│   ├── formulario_serie.php
│   ├── img
│   │   ├── adminviews.png
│   │   ├── adminviews_favicon.png
│   │   ├── flechaderecha.png
│   │   ├── iconologout.png
│   │   ├── iconopelicula.png
│   │   ├── iconoseries.png
│   │   └── iconovuelta.png
│   ├── inc
│   │   ├── cabecera.php
│   │   ├── db.php
│   │   └── piedepagina.php
│   ├── index.php
│   ├── intruso.php
│   ├── peliculas.php
│   ├── series.php
│   └── style
│       └── style.css
├── informe.md
└── screenshots
    ├── adminindex.png
    ├── contenidocontenido.png
    ├── contenidousuarios.png
    ├── inicio.png
    ├── login.png
    ├── peliculas.png
    ├── registro.png
    ├── series.png
    ├── tablacontenido.png
    └── tablausuarios.png
```

---

## Vistas, flujo de información y como se desarrolla la aplicación

El proyecto se divide en dos partes, el `front` que es lo que ve el usuario y el `admin` que es lo que ve el administrador. La parte del front esta pensada para que al usuario le sea lo mas facil posible el uso de la aplicación, que le sea simple entenderlo. Y la parte del admin esta hecha para que el administrador pueda tener un pequeño informe sobre como va la aplicación.

La primera pantalla que se ve al abrir la aplicación es `front/index.php` que contiene el login y el registro para poder entrar a la aplicación, luego tenes dos caminos posibles:

	- El primero en el caso de ser un usuario es registrarse -> login y pasar a la pantalla principal de la app.
	- La segunda ser el admin y usar el usuario de administrador y que te lleve al `AdminPanel`.

Luego en el primero caso entrarias a `front/exito.php` donde veras un header con el logo de la app, un boton arriba a la izquierda para volver atras (cerrar sesion), y en el medio dos opciones:

	- La primera ir a peliculas `front/peliculas.php` donde tendras dos tablas una que pondra `Por ver` y otra que pondra `Vistas` ahi es donde veras las peliculas que agregues dependiendo de cual tabla indiques, te preguntaras como añado las peliculas, para hacer eso hay un boton arriba a la izquierda que pone `+ Agregar pelicula` y al darle te aparecera una pantalla emergente de un formulario `front/formulario_pelicula.php` donde ingresaras el nombre de la pelicula, un comentario y a cual tabla corresponde.
	
	- La segunda ir a series `front/series.php` donde en este caso tendras tres tablas `Por ver, Viendo y Vistas` es donde veras las series que vallas agregando. En este caso tambien tienes un boton arriba a la izquierda para agregar las series y en este caso te sale un formulario que es `front/formulario_series.php` el cual te va a dar una tabla mas para elegir donde corresponde poner esa serie.
	
	
Tanto series como peliculas tienen el mismo header `front/inc/cabecera.php` el cual contiene el logo, el boton para volver hacia atras y una barra de navegacion para ir a: `Inicio, Series o Peliculas`.

Y en el caso de el footer todas las pantallas menos el login lo tienen `front/inc/piedepagina.php`.

En el segundo caso el `Admin` al iniciar sesion con las credenciales del admin te llevara a `admin/index.php` donde veras mucha informacion en graficos, primero tienes un cuadrado en el cual ves el total de usuario que hay registrados, el total de series y peliuculas que hay almacenadas en la base de datos. Y debajo veras un grafico bastante grande en el cual indica la cantidad de series y/o peliculas que hay en estdo `por_ver, viendo y vistas` y debajo un top 10 de series mas vistas y otro top 10 de peliculas mas vistas. Luego a la izquierda hay un menu que tiene 3 opciones mas:
	
	- Usuarios: Una lista del total de usuario registrados con su nombre y correo correspondiente.
	- Peliculas: Una lista de todas las peliculas que hay en la base de datos con su respectiva informacion y imagen.
	- Series: Una lista de todas las series que hay en la base de datos con su respectiva informacion y imagen.
	
A continuación una imagen de lo explicado pero en un diagrama de flujo:


---

## Explicación del HTML, CSS y JS utilizado

**HTML:**

Un ejemplo de la estructura html que utilizamos en este proyecto:
```
	<header>
		<nav>
			<a href="index.php">Inicio</a>
			<a href="pelicula.php">Peliculas</a>
			<a href="serie.php">Series</a>
		</nav>
	</header>

	<main>
		<section>
			<h1>Panel principal</h1>
			<p>Contenido principal de la aplicación</p>
		</section>
	</main>
```
Las etiquetas principales que utilizamos en este proyecto son:

- `<header>` Para la cabecera.

- `<nav>` Para la barra de navegación.

- `<main>` Para poner todo el contenido principal.

- `<section>` Para dividir los contenidos en secciones.

- `<table>` Para mostrar los datos en la tabla.

- `<form>, <label>, <input>` Para los formularios.

**CSS:**

Ejemplo de uso de Flexbox:
```
	nav {
		display: flex;
		gap: 20px;
	}
```
Flexbox se utilizó para:

- Colocar el menú de navegación.

- Alinear los elementos horizontal y verticalmente.

- Organizar los formularis y los botones.

Ejemplo de uso de Grid:
```
	.dashboard {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 20px;
	}

```
Grid se utilizó para:

- Distribuir las tarjetas.

- Organizar los bloques de la información.

- Ademas de esas etiquetas, tambien utilizamos estas:

- `margin` y `padding` para separación de elementos

- `:hover` para mejorar la interacción visual

- `@media` para adaptar la aplicación a distintos tamaños de pantalla

**JavaScript:**

JavaScript se uso poco en este proyecto, se utilizó principalmente para:

- Gestionar eventos de clic.

- Mostrar u ocultar elementos.

- Confirmar acciones del usuario.

- API de peliculas y series.

Ejemplo:
```
	boton.addEventListener("click", function () {
		alert("Acción realizada");
	});
```

---

**Conclusión:**

En este proyecto utilizamos html, css y un poco de js, documentando todo el codigo de forma clara, con buenas practicas. Todo el interfaz que ve el usuario `front` esta pensado para que sea de un uso facil que no lleve tiempo aprender su uso, con colores claros, un diseño bonito y bien estructurado `css`, utilizamos `JS` para el script de la `API` que es una ayuda para el usuario que le autocompleta el nombre de la serie o pelicula cuando la va escribiendo y le muestra la imagen de portada.

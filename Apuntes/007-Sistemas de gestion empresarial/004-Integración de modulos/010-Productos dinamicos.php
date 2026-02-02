<Doctype html>
<html lang="es">
	<head>
		<title>Tienda</title>
		<meta charset="UTF-8">
		<meta name="viewport"
			content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
	/* Reset básico para inputs y botones en móvil */
	* {
		box-sizing: border-box;
	}

	body {
		background-color: #f4f4f4;
	}

	/* Mejora del contenedor principal para scroll */
	main {
		flex: 1;
		overflow-y: auto;
		padding: 20px;
		width: 100%;
	}

	/* Estilo de las secciones (tarjetas visuales) */
	section {
		background: white;
		padding: 15px;
		border-radius: 10px;
		margin-bottom: 20px;
		box-shadow: 0 2px 5px rgba(0,0,0,0.1);
	}

	h3 {
		margin-top: 0;
		color: #333;
		border-bottom: 2px solid #eee;
		padding-bottom: 10px;
	}

	/* GRD DE PRODUCTOS: Adaptable a pantallas pequeñas */
	#productos > div {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
		gap: 15px;
	}

	article {
		border: 1px solid #eee;
		border-radius: 8px;
		padding: 15px;
		text-align: center;
		background: #fff;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	article h4 {
		margin: 10px 0;
		font-size: 1.1em;
	}

	/* BOTONES TÁCTILES: Área de toque grande (min 44px) */
	button {
		background: MediumBlue;
		color: white;
		border: none;
		padding: 12px;
		width: 100%;
		border-radius: 5px;
		font-size: 16px;
		font-weight: bold;
		cursor: pointer;
		touch-action: manipulation; /* Mejora respuesta táctil */
	}

	button:active {
		background: #0000cd; /* Feedback visual al tocar */
		transform: scale(0.98);
	}

	/* FORMULARIOS: Inputs grandes y legibles */
	input[type="text"] {
		width: 100%;
		padding: 15px;
		margin-bottom: 15px;
		border: 1px solid #ccc;
		border-radius: 5px;
		font-size: 16px; /* Evita zoom automático en iOS */
		background: #f9f9f9;
	}

	/* BOTÓN DE ENVIAR (que es un DIV en tu HTML) */
	#enviar {
		background: #28a745;
		color: white;
		padding: 18px;
		text-align: center;
		border-radius: 8px;
		font-size: 18px;
		font-weight: bold;
		text-transform: uppercase;
		cursor: pointer;
		box-shadow: 0 4px 6px rgba(0,0,0,0.1);
		margin-top: 10px;
	}

	#enviar:active {
		background: #218838;
		transform: translateY(2px);
	}
    </style>
	</head>
	<body>
		<header>
			<h1>Microtiendas</h1>
		</header>
		<main>
			<section id="productos">
				<h3>Productos</h3>
				<div>
					<?php
						$host = "localhost";
						$user = "microtienda";
						$pass = "Microtienda123$";
						$db   = "microtienda";
						$conexion = new mysqli($host, $user, $pass, $db);
						$sql = "SELECT * FROM productos;";
						$resultado = $conexion->query($sql);
						while ($fila = $resultado->fetch_assoc()) {
					?>
					<article>
						<h4><?= $fila['nombre'] ?></h4>
						<button nombre="<?= $fila['nombre'] ?>"><?= $fila['precio'] ?>€</button>
					</article>
				<?php }?>
				</div>
			</section>
			<section>
				<h3>Datos de cliente</h3>
				<div>
					<input type="text" id="nombre" placeholder="Nombre">
					<input type="text" id="apellidos" placeholder="Apellidos">
					<input type="text" id="email" placeholder="Email">
					<div id="enviar">Enviar pedido</div>
				</div>
			</section>
		</main>
		<footer>
			(c) 2026 Valentín De Gennaro
		</footer>
	</body>
	<script>
		var fecha = new Date();
		var pedido = {
			cliente:{},
			productos:[],
			pedido:{
				"numero":Date.now(),
				"fecha":fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate()
			}
		};
		///////// ATRAPA PRODUCTOS Y LOS METE EN CARRITO ////////
		let botones = document.querySelectorAll("button");
		botones.forEach(function(boton){
			boton.onclick = function(){
				pedido.productos.push({
					"nombre":this.getAttribute("nombre"),
					"precio":this.textContent
				})
				console.log(pedido)
			}
		})
		//////////// ATRAPA LOS DATOS DEL CLIENTE //////////////
		let boton_enviar = document.querySelector("#enviar");
		boton_enviar.onclick = function(){
			let nombre_cliente = document.querySelector("#nombre").value;
			let apellidos_cliente = document.querySelector("#apellidos").value;
			let email_cliente = document.querySelector("#email").value;
			pedido.cliente = {
				"nombre":nombre_cliente,
				"apellidos":apellidos_cliente,
				"email":email_cliente
			}
			console.log(pedido)
		}
	</script>
</html>












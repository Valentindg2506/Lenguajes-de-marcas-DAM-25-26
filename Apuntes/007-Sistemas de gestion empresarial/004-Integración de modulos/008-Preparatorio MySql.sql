sudo mysql -u root -p
CREATE DATABASE microtienda;
USE microtienda;

CREATE TABLE productos(
	nombre VARCHAR(255),
  descripcion TEXT,
  precio INT(255)
);

INSERT INTO productos VALUES(
	'Zapatillas',
  'Zapatillas chulas de deporte',
  30
);

INSERT INTO productos VALUES
('Camiseta deportiva', 'Camiseta transpirable para entrenamiento', 15),
('Pantalón corto', 'Pantalón corto cómodo para deporte', 18),
('Sudadera', 'Sudadera con capucha de algodón', 35),
('Calcetines deportivos', 'Pack de calcetines para running', 8),
('Mochila', 'Mochila resistente para uso diario', 40),
('Gorra', 'Gorra ajustable para actividades al aire libre', 12),
('Botella de agua', 'Botella reutilizable de 1 litro', 10),
('Chaqueta cortavientos', 'Chaqueta ligera resistente al viento', 45),
('Zapatillas casual', 'Zapatillas cómodas para uso diario', 32),
('Bolsa de deporte', 'Bolsa amplia para gimnasio o viajes cortos', 28);

SELECT * FROM productos;

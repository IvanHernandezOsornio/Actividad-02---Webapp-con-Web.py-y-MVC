CREATE DATABASE ria_iniciales;

USE ria;

CREATE TABLE personas(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    email varchar(50) NOT NULL,
    turno char(1) NOT NULL,
    direccion varchar(50) NOT NULL,
    genero varchar(50) NOT NULL);


INSERT INTO personas (nombre, email, turno, direccion, genero)
VALUES ('Jose','Jose@gmail.com','1','av trabajo','hombre'),
('leri','Leri@gmail.com','2','2 de enero','mujer'),
('luis','Luis@gmail.com','3','agropecuaria','hombre'),
('Nancy','Nancy@gmail.com','4','Rojo jomez','mujer'),
('Anel','Anel@gmail.com','5','la joya','mujer');


SHOW TABLES;

SELECT * FROM personas;

DESCRIBE personas;


CREATE TABLE productos(
    nombre_prod varchar(50) NOT NULL,
    marca varchar(50) NOT NULL,
    existencias char(50) NOT NULL,
    descripcion varchar(50) NOT NULL,
    costo char(50) NOT NULL);


INSERT INTO productos (nombre_prod, marca, existencias, descripcion, costo)
VALUES ('telefono','sony','3','color negro','3000'),
('labadora','mave','8','mediana','8000'),
('tarjeta de video','nvidia','1','pequeña','2300'),
('sombrero','calvin clain','3','color cafe','200'),
('juego de mesa','matel','20','empaquetado','150');


SHOW TABLES;

SELECT * FROM productos;

DESCRIBE productos;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;

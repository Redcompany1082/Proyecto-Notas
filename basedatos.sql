CREATE DATABASE IF NOT EXISTS master_python; --crear una base de datos 

use master_python; --para entrar en la base datos


--crear una tabla y los diferentes campos
CREATE TABLE IF NOT EXISTS usuarios(
id          int(25) auto_increment not null, --Este id se incrementa cada vez que se crea y no se puede dejar vacío y el int(25) se refiere a que puede tener hasta 25 caracteres
nombre      varchar(100),
apellido    varchar(255),
email       varchar(200)not null,
password    varchar(255) not null,
fecha       date not null,

CONSTRAINT  pk_usuarios PRIMARY KEY(id),--constraint una regla, donde el id debe ser único y no debe estar vacío y con esta clave se puede relacionar con otras tablas
CONSTRAINT  uq_email UNIQUE(email), --el valor de este campo no se puede repetir

)ENGINE = InnoDb;

CREATE TABLE IF NOT EXISTS notas(
id          int(25) auto_increment not null,
usuario_id  int(25) not null, --para poder relacionar con la tabla usuarios
titulo      varchar(255) not null,
descripcion MEDIUMTEXT,
fecha       date not null,
CONSTRAINT  pk_notas PRIMARY KEY(id),
CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)--con foreign key se le dice relacioname usuario_id con la base usarios y el campo id 


)ENGINE = InnoDb;
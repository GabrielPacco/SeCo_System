CREATE DATABASE BBDDSECOSISTEM;
USE  BBDDSECOSISTEM;

CREATE TABLE  usuario
(
    id_user INT PRIMARY KEY ,
    nombre VARCHAR(50),
    contrasenia VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE invitado
(
	id_inv INT,
    id_user INT,
    universidad  VARCHAR(50),
    carrera  VARCHAR(50),
    grado  VARCHAR(20),
    PRIMARY KEY (id_user,id_inv),
    FOREIGN KEY (id_user) REFERENCES usuario (id_user)
);
CREATE TABLE administrador
(
	id_adm INT,
    id_user INT,
    PRIMARY KEY (id_user,id_adm),
    FOREIGN KEY (id_user) REFERENCES usuario (id_user)
);
CREATE TABLE contribuidor
(
	id_cont INT PRIMARY KEY,
    nombre VARCHAR(50),
    universidad  VARCHAR(50),
    especialidad VARCHAR(50),
    descripcion TEXT,
    facebool VARCHAR(50),
    email VARCHAR(50),
    linkedin VARCHAR(50),
    rol VARCHAR(20)
);
CREATE TABLE actividad
(
    id_act INT PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion TEXT,
    fecha DATE,
    hora_inicio TIME,
    hora_fin TIME,
    estado VARCHAR(30),
    enlace_reu TEXT
);
CREATE TABLE edicion 
(
	id_edi INT,
    id_act INT,
    anho INT,
    nombre VARCHAR(30),
    PRIMARY KEY (id_edi,id_act),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE concurso 
(	
	id_conc INT,
    id_act INT,
    participante VARCHAR(40),
    base TEXT,
    premio VARCHAR(30),
	PRIMARY KEY (id_conc,id_act),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE ponencia 
(
	id_pon INT,
    id_act INT,
    topico VARCHAR(30),
	PRIMARY KEY (id_pon,id_act),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE protocolar 
(
	id_prot INT,
    id_act INT,
    regla TEXT,
	PRIMARY KEY (id_prot,id_act),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE panel 
(
	id_pan INT,
    id_act INT,
    topico VARCHAR(30),
	PRIMARY KEY (id_pan,id_act),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);

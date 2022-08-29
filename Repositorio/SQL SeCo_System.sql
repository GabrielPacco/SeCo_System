CREATE DATABASE BBDDSECOSYSTEM;
USE  BBDDSECOSYSTEM;
                                                       
CREATE TABLE  usuario
(
    id_user INT,
    nombre VARCHAR(50),
    contrasenia VARCHAR(50),
    email VARCHAR(50),
    PRIMARY KEY (id_user),
);

CREATE TABLE invitado
(
    id_inv INT NOT NULL AUTO_INCREMENT,
    id_user INT,
    universidad  VARCHAR(50),
    carrera  VARCHAR(50),
    grado  VARCHAR(20),
    PRIMARY KEY (id_inv),
    FOREIGN KEY (id_user) REFERENCES usuario (id_user)
);
CREATE TABLE administrador
(
    id_adm INT NOT NULL AUTO_INCREMENT,
    id_user INT,
    rol VARCHAR(100),
    PRIMARY KEY (id_adm),
    FOREIGN KEY (id_user) REFERENCES usuario (id_user)
);
CREATE TABLE contribuidor
(
    id_cont INT NOT NULL AUTO_INCREMENT ,
    nombre VARCHAR(50),
    universidad  VARCHAR(50),
    especialidad VARCHAR(50),
    descripcion TEXT,
    facebool VARCHAR(50),
    email VARCHAR(50),
    linkedin VARCHAR(50),
    rol VARCHAR(20),
    PRIMARY KEY (id_cont)
);
CREATE TABLE actividad
(
    id_act INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30),
    descripcion TEXT,
    fecha DATE,
    hora_inicio VARCHAR(20),
    hora_fin VARCHAR(20),
    estado VARCHAR(30),
    enlace_reu TEXT,
    PRIMARY KEY (id_act)
);
CREATE TABLE edicion 
(
    id_edi INT NOT NULL AUTO_INCREMENT,
    id_act INT,
    anho INT,
    nombre VARCHAR(30),
    PRIMARY KEY (id_edi),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE concurso 
(	
    id_conc INT NOT NULL AUTO_INCREMENT,
    id_act INT,
    participante VARCHAR(40),
    base TEXT,
    premio VARCHAR(30),
    PRIMARY KEY (id_conc),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE ponencia 
(
    id_pon INT NOT NULL AUTO_INCREMENT,
    id_act INT,
    topico VARCHAR(30),
    PRIMARY KEY (id_pon),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE protocolar 
(
    id_prot INT NOT NULL AUTO_INCREMENT,
    id_act INT,
    regla TEXT,
    PRIMARY KEY (id_prot),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);
CREATE TABLE panel 
(
    id_pan INT NOT NULL AUTO_INCREMENT,
    id_act INT,
    topico VARCHAR(30),
    PRIMARY KEY (id_pan),
    FOREIGN KEY (id_act) REFERENCES actividad (id_act)
);

#  INGENIERÍA DE SOFTWARE I -PROYECTO SeCo_System :desktop_computer: 
## :label: Propósito del Proyecto
El  proyecto desarrollado es referido a "La semana de computación " en la escuela profesional de Ciencia de la Computación, la cual tiene como proposito proporcionar información a los usuarios que quieren saber mas de la escuela, asi como de poder participar ya sea como invitados, ponentes, o simplemente en los concursos que ofrece la escuela.
## :red_circle: Desarrollo
### Diagrama de Casos de Uso
![image](https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Main.png) 
### Diseño de Modelo de Datos 
![image](https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/modelo.png)
### Diseño de Arquitectura
![image](https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Arquitectura.png)
## Estilos de Programación <br>
### **CookBook**: <br>
:crossed_swords: Problema más grande descompuesto en abstracciones de procedimiento.<br>
:crossed_swords: Problema más grande resuelto como una secuencia de comandos, cada uno correspondiente a un procedimiento.<br>
:crossed_swords: Al terminar un registoro correcto, el redireccionamiento no necesita de entradas ni salidas,por lo que una simple secuencia de procedimientos para notificar al usuario y redireccionarlo a una pagina en cuestion<br>
<br>
```
################# Usuario ################################
@task_blueprint.route('/usuario/add_usuario', methods=['POST'])
@cross_origin()
def create_user():
    content = model.add_usuario(request.json['nombre'], request.json['apellido'], request.json['contrasenia'], request.json['email']) 
    return jsonify(content)
################# Invitado ################################
@task_blueprint.route('/invitado/delete_invitado', methods=['POST'])
@cross_origin()
def delete_invitado():
    return jsonify(model.delete_invitado(int(request.json['id_invitado'])))
```
### **Resful**: <br>
REST es un estilo para aplicaciones interactivas basadas en red que subyace en la Web. El ejemplo aquí no pasa por la red, pero conserva las principales restricciones de REST, que son:<br>
:crossed_swords: Interactivo: extremo a extremo entre un agente activo (por ejemplo, una persona) y un backend.<br>
:crossed_swords: Separación entre Cliente (interfaz de usuario) y Servidor (almacenamiento de datos).<br>
:crossed_swords: Sin estado, como en cliente--servidor sin estado: cada solicitud del cliente al servidor debe contener toda la información necesaria para que el servidor atienda la solicitud. El servidor no puede almacenar el contexto de la interacción. El estado de la sesión está en el cliente.<br>
:crossed_swords: Interfaz uniforme: recursos que se crean y recuperan, identificadores de recursos y representación hipermedia que es el motor del estado de la aplicación<br>
<br>
```
################# Carpetas separadas del Cliente y Servidor ################################

Donde el controlador del proyecto se encuentra en la carpe Backend SeCo System
Parte de las vistas en secosystem/srs/views

```
###  **Thinks**: <br>
:crossed_swords: El problema más grande se descompone en 'cosas' que tienen sentido para el dominio del problema.<br>
:crossed_swords: Cada 'cosa' es una cápsula de datos que expone los procedimientos al resto del mundo.<br>
:crossed_swords:Nunca se accede a los datos directamente, solo a través de estos procedimientos.<br>
```
##Estilo de programacion orientado a Objetos para el uso de atributos y funciones.<br>
##Clase Usuario
class Usuario:
    #Atributos
    def __init__(self):
        self.id = None
        self.nombre = None
        self.usuario = None
        self.contrasenha = None
        self.email = None
        self.telefono = None
##Clase Invitado
class Invitado:
    #Atributos
    def __init__(self):
        self.universidad = None
        self.carreraProfesional = None
        self.gradodeestudio = None
```
## :red_circle: Practicas de Codigo Legible
### :newspaper_roll: **Comentar y Documentar**: <br>
Se documentara cada funcion y metodo que se use en el codigo, para poder ser entendido por cualquiera que revise el codigo. <br>
```
//Clase invitado
class Invitado:
    //Atributos de la clase invitado
    def __init__(self):
        self.universidad = None
        self.carreraProfesional = None
        self.gradodeestudio = None

    // funciones que tendra el invitado
    def inscribirParticipacion(self, ):
        pass

    def confirmarParticipacion(self, ):
        pass

    def contactarOrganizacion(self, ):
        pass

    def buscarActividad(self, ):
        pass

    def visualizarEvento(self, ):
        pass
```
### :newspaper_roll: **Organizar las carpetas del proyecto**: <br>
Separar lo que es el dominio, los controladores y repositorio.

![image](https://live.staticflickr.com/65535/52300101188_80a37989c3_n.jpg)

### :newspaper_roll: **Identacion correspondiente**: <br>
Identar cada linea de codigo, o darle la sangria correspondiente, para tener un codigo mas ordenado y facil de comprender.<br>
```
// clase usuario
class Usuario:
    //Atributos de la clase usuario
    def __init__(self):
        self.id = None
        self.nombre = None
        self.usuario = None
        self.contrasenha = None
        self.email = None
        self.telefono = None
    //funcion inicial 
    def iniciarSesion(self, ):
        pass
```
### :newspaper_roll: **Evitar codigo redundante**: <br>
No declarar variables o comentarios que son obvios o que pueda sobrecargar el codigo. <br>
```

```
### :newspaper_roll: **Usar un mismo lenguaje**: <br>
Si vamos a programar con sentencias en español, para ser entendidas por cualquiera que revise el codigo, procurar hacerlo solo en ese idioma, excepto por palabras reservadas del lenguaje de programacion usado.<br>
```
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
```
### :newspaper_roll: **Una funcion, una tarea**: <br>
Al momento de declarar las funciones, estas solo deben de realizar una tarea en especifico, para no tener problemas si es que esque se modifica la funcion y pueda afectar a las demas.
```
# Funcion para obtener todas las actividades
def get_actividads(self):  
    ...
return data

# Funcion para agregar una actividad
def add_actividad(self, nombre, descripcion,
    fechaInicio, fechaFin, enlaceReunion, isProtocolar,
    isPonencia, isPanel, isConcurso, bases):
    ...    
return data
```

## :red_circle: Principios SOLID

### :gem: **_1_**: <br> 
### :gem: **_2_***: <br>
### :gem: **_3_***: <br>


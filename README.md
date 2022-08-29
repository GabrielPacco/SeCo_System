
#  INGENIERÍA DE SOFTWARE I -PROYECTO SeCo_System :desktop_computer: 

## :label: Propósito del Proyecto
El  proyecto desarrollado es referido a "La semana de computación " en la escuela profesional de Ciencia de la Computación, la cual tiene como proposito proporcionar información a los usuarios que quieren saber mas de la escuela, asi como de poder participar ya sea como invitados, ponentes, o simplemente en los concursos que ofrece la escuela.<br>
## :label: Tecnologias Usadas <br>
- **a)** *Vue* 
- **b)** *Vuetify* 
- **c)** *Lenguaje de Programación Python* 
- **d)** *JavaScript* 
- **e)** *Framework Flask*
 
## :label: Interfaz del Proyecto <br>
	
<center><img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Interfaz.gif" width="800" height="545"></center>

## :red_circle: Desarrollo

### Funcionalidades
:scroll:  Registrar cuenta: El usuario debe registrar una cuenta. Registra sus datos personales y de acceso. <br>
:scroll: Iniciar sesión: El actor debe ingresar con los datos de inicio de sesión de su cuenta para poder acceder. <br>
:scroll: Inscribir participación: El usuario debe inscribirse a un evento. Registra el evento al que quiere participar. <br>
:scroll: Confirmar actividad: El usuario debe elegir una actividad programada en el cronograma. <br>
:scroll: Visualizar menú de eventos: El usuario debe visualizar el menú de eventos. Abre una página con el menú de los eventos. <br>
:scroll: Visualizar edición: El usuario debe visualizar los eventos programados. <br>
:scroll: Visualizar programa: El usuario debe visualizar el calendario de actividades. Se muestra el cronograma de actividades, cada actividad tendrá un nombre, su expositor y la hora. <br>
:scroll: Visualizar actividad (track): El usuario debe visualizar las actividades programadas. Se muestra el cronograma e información de las actividades.
:scroll: Buscar actividad: El usuario podrá realizar búsquedas a través de filtros. <br>
:scroll: Contactar organización: El usuario podrá visualizar información de contacto y podrá enviar mensaje a los organizadores. <br>
:scroll: Gestionar cuenta: El administrador podrá dirigir las cuentas de los usuarios. <br>
:scroll: Gestionar actividad (track): El administrador puede gestionar una actividad, esto incluye programar una nueva actividad, modificarla o finalizarla. <br>
:scroll: Añadir actividad: El administrador debe ser capaz de añadir actividades a un evento en la página. <br>
:scroll: Eliminar actividad: El administrador puede eliminar una actividad de un evento. El evento seleccionado se desecha del calendario. <br>
:scroll: Modificar Actividad: El administrador puede modificar una actividad, pudiendo editar sus datos y actualizarlos en el calendario. <br>

### Diagrama de Casos de Uso

<center><img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/diagrama_casos.png" width="550" height="550"></center>

### Diseño de Modelo de Datos 

<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/modelo.png" width="550" height="550">

### Diseño de Arquitectura

<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Arquitectura.png" width="550" height="550">



# **Estilos de Programación**

## 1. Declared-Intentions.

### Restricciones 
- **a)** *Existencia de un verificador de tipos en tiempo de ejecución.* 
- **b)** *Los procedimientos y funciones declaran qué tipos de argumentos esperan.* 
- **c)** *Si las personas que llaman envían argumentos de tipos que no se esperan, los procedimientos/funciones no se ejecutan.*


    El problema de la verificación de tipos es un problema resuelto en los lenguajes tipificados estáticamente, por lo que al programar en F# no hay casi nada que debamos hacer realmente para este estilo.

    Usando la misma solución del estilo Pipeline (también conocido como funcional), agregué algunas declaraciones de tipo explícitas para cumplir mejor con las restricciones.

    ```  
    ################### Concurso ################################

    # Funcion para obtener un concurso por su ID
    def get_concurso(self, id_conc):
        params = {'id_conc' : id_conc}      
        rv = self.mysql_pool.execute("SELECT * from concurso where id_conc=%(id_conc)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_conc': result[0], 'id_act': result[1], 'participante': result[2], 'base': result[3], 'premio': result[4]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los concursos
    def get_concursos(self):
        rv = self.mysql_pool.execute("SELECT * from concurso")  
        data = []
        content = {}
        for result in rv:
            content = {'id_conc': result[0], 'id_act': result[1], 'participante': result[2], 'base': result[3], 'premio': result[4]}
            data.append(content)
            content = {}
        return data

    ```

## 2. Plugins.

### *Restricciones* 

- **a)** *El problema se descompone utilizando alguna forma de abstracción (procedimientos, funciones, objetos, etc.)*
- **b)** *Todas o algunas de esas abstracciones se encapsulan físicamente en sus propios paquetes, generalmente precompilados. El programa principal y cada uno de los paquetes se compilan de forma independiente. Estos paquetes son cargados dinámicamente por el programa principal, generalmente al principio (pero no necesariamente).*
- **c)** *El programa principal usa funciones/objetos de los paquetes cargados dinámicamente, sin saber qué implementaciones exactas se usarán. Se pueden usar nuevas implementaciones sin tener que adaptar o recompilar el programa principal.*
- **d)** *Especificación externa de qué paquetes cargar. Esto se puede hacer mediante un archivo de configuración, convenciones de ruta, entrada de usuario u otros mecanismos para que la especificación externa del código se vincule en tiempo de ejecución.*

    ``` 
    import '@fortawesome/fontawesome-free/css/all.css'
    import 'material-design-icons-iconfont/dist/material-design-icons.css'

    import Vue from 'vue';
    import Vuetify from 'vuetify/lib';

    import colors from 'vuetify/lib/util/colors'
    Vue.use(Vuetify);

    export default new Vuetify({
        icons: {
            iconfont: 'md' || 'fa' 
          },
          theme: {
            themes: {
                light: {
                    background: colors.grey.lighten2, // Not automatically applied
                  },
              dark: {
                background: colors.shades.white, // If not using lighten/darken, use base to return hex
              },
            },
          },
    });
    ```
## 3. Dataspaces.

### *Restricciones*
- **a)** *Existencia de una o más unidades que ejecutan concurrentemente.* 
- **b)** *Existencia de uno o más espacios de datos donde las unidades concurrentes almacenan y recuperan datos.* 
- **c)** *No hay intercambios de datos directos entre las unidades concurrentes, excepto a través de los espacios de datos.*


 ## 4. Resful.
REST es un estilo para aplicaciones interactivas basadas en red que subyace en la Web. El ejemplo aquí no pasa por la red, pero conserva las principales restricciones de REST, que son:
### *Restricciones*
- **a)** *Interactivo: extremo a extremo entre un agente activo (por ejemplo, una persona) y un backend.* 
- **b)** *Separación entre Cliente (interfaz de usuario) y Servidor (almacenamiento de datos).* 
- **c)** *Sin estado, como en cliente--servidor sin estado: cada solicitud del cliente al servidor debe contener toda la información necesaria para que el servidor atienda la solicitud. El servidor no puede almacenar el contexto de la interacción. El estado de la sesión está en el cliente.*
- **d)** Interfaz uniforme: recursos que se crean y recuperan, identificadores de recursos y representación hipermedia que es el motor del estado de la aplicación*

```
    ################# Carpetas separadas del Cliente y Servidor ################################
    Donde el controlador del proyecto se encuentra en la carpe Backend SeCo System
    Parte de las vistas en secosystem/srs/views

```
## 5. Pipeline.
Este estilo con programacion orientado a objetos es usado en las clases de backend/models ya que estas clases contienen funciones que retornan datos que no son compartidos entre otras funciones de la misma clase.
```
    ################### Actividad ################################
    # Funcion para obtener una actividad por su ID
    def get_actividad(self, id_act):
        params = {'id_act' : id_act}      
        rv = self.mysql_pool.execute("SELECT * from actividad where id_act=%(id_act)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_act': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3], 'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para obtener todas las actividades
    def get_actividades(self):
        rv = self.mysql_pool.execute("SELECT * from actividad")  
        data = []
        content = {}
        for result in rv:
            content = {'id_act': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3], 'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

```
# **Concepto CRUD aplicado**
CRUD hace referencia a un acrónimo en el que se reúnen las primeras letras de las cuatro operaciones fundamentales de aplicaciones persistentes en sistemas de bases de datos:
### Create (Crear registros)
### Read bzw. Retrieve (Leer registros)
### Update (Actualizar registros)
### Delete bzw. Destroy (Borrar registros)
En pocas palabras, CRUD resume las funciones requeridas por un usuario para crear y gestionar datos. Varios procesos de gestión de datos están basados en CRUD, en los que dichas operaciones están específicamente adaptadas a los requisitos del sistema y de usuario, ya sea para la gestión de bases de datos o para el uso de aplicaciones.
# **Prácticas de Código Legible**

## *1. Agrupación de código.*
    La mayoría de las veces, ciertas tareas requieren unas pocas líneas de código. Es una buena idea mantener estas tareas dentro de bloques de código separados, con algunos espacios entre ellos.
    ```{js}
    ################### Actividad ################################
    # Funcion para obtener una actividad por su ID
    def get_actividad(self, ID_Actividad):    
        params = {'ID_Actividad' : ID_Actividad}      
        rv = self.mysql_pool.execute("SELECT * from actividad where ID_Actividad=%(ID_Actividad)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID_Actividad': result[0], 'nombre': result[1], 'descripcion': result[2], 'fechaInicio': result[3], 'fechaFin': result[4], 'enlaceReunion': result[5], 'isProtocolar': result[6], 'isPonencia': result[7], 'isPanel': result[8], 'isConcurso': result[9], 'bases': result[10]}
            data.append(content)
            content = {}
        return data


    ################### Contribuidor ################################
    # Funcion para obtener un contribuidor por su ID
    def get_contribuidor(self, ID_Contribuidor):
        params = {'ID_Contribuidor' : ID_Contribuidor}      
        rv = self.mysql_pool.execute("SELECT * from contribuidor where ID_Contribuidor=%(ID_Contribuidor)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID_Contribuidor': result[0], 'nombre': result[1], 'apellido': result[2], 'email': result[3], 'telefono': result[4], 'isOrganizador': result[5], 'isAsistente': result[6], 'isInvitado': result[7]}
            data.append(content)
            content = {}
        return data
    ```
## *2. Se Utilizo el mismo vocabulario para el mismo tipo de variable*
    ``` {js}
    get_Actividad();
    get_Adminstrador();
    get_Concurso();
    get_Edicion();

    add_Actividad();
    add_Adminstrador();
    add_Concurso();
    add_Edicion();
    ```
## *3. Identacion correspondiente* <br>
Identar cada linea de codigo, o darle la sangria correspondiente, para tener un codigo mas ordenado y facil de comprender.
```
<template>
  <v-app id="inspire">
    <v-content>

      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12" fab color="#ccffff" outline>
              <v-window v-model="step" >
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="8">
                      <!--<img src="src/assets/logo.png" height="50px" width="550px"/> -->
                      <v-card-text class="mt-12">
                        <h1
                          class="text-center display-5 teal--blue text--blue" 
                        >Iniciar sesión en SeCo_System</h1>
```
## *4. Poner en mayúscula las palabras especiales de SQL*
    ```{js}
    CREATE TABLE  usuario
    (
        id_user INT PRIMARY KEY ,
        nombre VARCHAR(50),
        usuario VARCHAR(50),
        contrasenia VARCHAR(50),
        email VARCHAR(50),
        telefono INT
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
    ```
## *5. Cada función realiza solo realiza una tarea*
    ```{js}
    # Funcion para obtener una actividad por su ID
    def get_actividad(self, ID_Actividad):    
        ...
    return data

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

    # Funcion para eliminar una actividad
    def delete_actividad(self, ID_Actividad):    
        ...
    return data
    ```
## *6. Los nombres de las funciones realizan lo mencionado*
    ``` {js}
        # Funcion para agregar un usuario
    def add_usuario(self, nombre, contrasenia, email):
        params = {
            'nombre' : nombre,
            'constrasenia' : contrasenia,
            'email' : email
        }  
        query = """insert into usuario (nombre, contrasenia, email)
            values (%(nombre)s, %(constrasenia)s, %(email)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_user': cursor.lastrowid, 'nombre': nombre, 'constrasenia': contrasenia, 'email': email}
        return data
    
    # Funcion para eliminar un usuario
    def delete_usuario(self, id_user):
        params = {'id_user' : id_user}      
        query = """delete from usuario where id_user = %(id_user)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
    ```
## *7. Organización de Archivos y Carpetas.*

<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/imagen4.PNG">

## *8. Evitar codigo redundante.* <br>

No declarar variables o comentarios que son obvios o que pueda sobrecargar el codigo.
# **Principios SOLID**
## *1) El principio de responsabilidad única (SRP)*

### *“Una clase debe tener una, y sólo una, razón para cambiar”*

En otras palabras, cada componente de su código (en general una clase, pero también una función) debe tener una y solo una responsabilidad . Como consecuencia de eso, solo debería haber una razón para cambiarlo.

Con demasiada frecuencia, ve una pieza de código que se encarga de todo un proceso a la vez. Es decir, una función que carga datos, los modifica y los grafica, todo antes de devolver su resultado.

Tomemos un ejemplo más simple, donde tenemos una lista de números L = [n1, n2, …, nx] y calculamos algunas funciones matemáticas para esta lista. Por ejemplo, calcule la media, la mediana, etc. En nuestro caso, tenemos a nuestro conector de la base de datos que nos ayuda con la conexión MYSQL, ha sufrido cambios pero solo con una razón en cada uno de ellos, mejorar la interacción con MySQL.


``` 
class MySQLPool(object):
    
    def __init__(self):             
        self.pool = self.create_pool(pool_name='task_pool', pool_size=3)

    def create_pool(self, pool_name, pool_size):
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **dbconfig)
        return pool

    def close(self, conn, cursor):

        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            self.close(conn, cursor)
            return cursor
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res
```


## *2) El principio abierto-cerrado (OCP)*

### *“Las entidades de software… deben estar abiertas a la extensión pero cerradas a la modificación”*

En otras palabras:No debería necesitar modificar el código que ya ha escrito para acomodar la nueva funcionalidad, simplemente agregue lo que necesita ahora.

Esto no significa que no pueda cambiar su código cuando las premisas del código necesiten ser modificadas, sino que si necesita agregar nuevas funciones similares a la presente, no debería necesitar cambiar otras partes del código.

Para aclarar este punto vamos a referirnos al ejemplo que vimos anteriormente. Si quisiéramos agregar una nueva funcionalidad, por ejemplo, calcular la mediana, deberíamos haber creado una nueva función de método y agregar su invocación a "principal". Eso habría agregado una extensión pero también modificado el principal. 

En nuestro caso hemos agregado muchas extensiones, por ejemplo en Home.vue primero fue agregado el inicio de sesión, lo que nos permitia pasar al siguiente endpoint, pero luego añadimos la extensión de registrarse, sin eliminar ningún elemento anterior hecho.


``` 
                        <h1>Iniciar sesión en SeCo_System</h1>
                        <h4 class="text-center mt-4">Ingresa tu correo y contraseña</h4>
                        <v-form>
                          <v-text-field
                            label="Correo"
                            name="Email"
                            prepend-icon="email"
                            type="text"
                            color="#ff0000"
                          />

                          <v-text-field
                            id="password"
                            label="Contraseña"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="#ff0000"
                          />
                        </v-form>
                        <h3 class="text-center mt-4">¿Ovidaste tu contraseña?</h3>
                      </v-card-text>
                      <div class="text-center mt-3">
                        <v-btn
                          color="blue darken-4"
                          v-bind="attrs"
                          v-on="on"
                          dark
                          rounded
                          link @click="$router.push({ path: '/admin' })"
                        >
                          INGRESAR
                        </v-btn>
                      </div>
                    </v-col>
                    <v-col cols="12" md="4" class="blue darken-4" height="40">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola Amigo!</h1>
                        <h5
                          class="text-center"
                        >Bienvenido a la semana de la computación, ingresa tus datos para resgistrarte</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded color="white" @click="step++">CREAR CUENTA</v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="blue darken-4">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">¡Hola! de nuevo</h1>
                        <h5
                          class="text-center"
                        >Para ingresa al apartado principal, ingresar tus datos</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded  color="white" @click="step--">INGRESAR</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12">
                        <h1 class="text-center display-2 teal--blue text--accent-3">Crear Cuenta</h1>

                        <h4 class="text-center mt-4">Ingresa tu correo y contraseña</h4>
                        <v-form>
                          <v-text-field
                            label="Nombre"
                            name="Name"
                            prepend-icon="person"
                            type="text"
                            color="#ff0000"
                          />
                          <v-text-field
                            label="Correo"
                            name="Email"
                            prepend-icon="email"
                            type="text"
                            color="#ff0000"
                          />

                          <v-text-field
                            id="password"
                            label="Contraseña"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="#ff0000"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-n5">
                        <v-btn
                          color="blue darken-4"
                          v-bind="attrs"
                          v-on="on"
                          dark
                          rounded
                          link @click="$router.push({ path: '/admin' })"
                        >
                          CREAR CUENTA
                        </v-btn>
```

## *3) El Principio de Inversión de Dependencias (DIP)*

### *“Depende de abstracciones, no de concreciones”*

Los componentes individuales no deben de ser una dependencia para operaciones generales, esto es de lo que se trata el principio de inversión de dependencias, ambos deben depender de abstracciones, logrando un bajo acoplamiento entre las clases.

Dicho esto, tenemos como abstracciones en nuestros archivos .vue tales como el registro o inicio de sesión de un usuario, su inscripción en algún concurso, la creación de varios concursos con respecto al administrador, etc.<br>
<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/imagen2.PNG" width="550" height="550"><br>
# **Conceptos DDD**
## Arquitectura en capas: 
Consta en dividir la aplicación en capas, con la intención de que cada capa tenga un rol muy definido, como podría ser, una capa de presentación (UI), una capa de reglas de negocio (servicios) y una capa de acceso a datos (DAO), sin embargo, este estilo arquitectónico no define cuantas capas debe de tener la aplicación, sino más bien, se centra en la separación de la aplicación en capas (Aplica el principio Separación de preocupaciones (SoC)).<br>
### Separación de responsabilidades: 
Permite la separación de preocupaciones (SoC), ya que cada capa tiene una sola responsabilidad.
### Fácil de desarrollar: 
Este estilo arquitectónico es especialmente fácil de implementar, además de que es muy conocido y una gran mayoría de las aplicaciones la utilizan.<br>
### Fácil de probar: 
Debido a que la aplicación construida por capas, es posible ir probando de forma individual cada capa, lo que permite probar por separada cada capa.<br>
### Fácil de mantener: 
Debido a que cada capa hace una tarea muy específica, es fácil detectar el origen de un bug para corregirlo, o simplemente se puede identificar donde se debe aplicar un cambio.<br>
### Seguridad:
La separación de capas permite el aislamiento de los servidores en subredes diferentes, lo que hace más difícil realizar ataques.<br>
## Lenguaje Ubiquo: 
El lenguaje ubicuo es el concepto de definir un lenguaje (hablado y escrito) que se usa por igual entre los desarrolladores y los expertos en dominios para evitar incoherencias y falta de comunicación debido a problemas de traducción y malentendidos. Verá la misma terminología en el código, las conversaciones entre cualquier miembro del equipo, las especificaciones funcionales, etc.
	´´´

	def add_concurso(self, participante, base, premio):
		params = {
		    'participante' : participante,
		    'base' : base,
		    'premio' : premio
		}  
		query = """insert into concurso (participante, base, premio)
		    values (%(participante)s, %(base)s, %(premio)s)"""    
		cursor = self.mysql_pool.execute(query, params, commit=True)   

		data = {'id_conc': cursor.lastrowid, 'participante': participante, 'base': base, 'premio': premio}
		return data
	´´´
### 🔩Planificación de tareas de implementación en la herramienta TRELLO 🔩
https://trello.com/b/FxYv1sZo/seco

### 🔩COLABORADORES🔩

- [x] Erick Jesús Perez Chipa: Base de Datos, Arquitectura de Software y Frontend(About us) 
- [x] Gabriel Pacco Huaraca: Backend y Hosting
- [x] Ronald Gutierrez Arratia: Frontend (Home), Arquitectura de Software y Base de datos 
- [x] Uberto Garcia Caceres: Readme , Trello
- [x] Fabrizio Miguel Mattos Cahui:  Readme, Requisitos de Software y Base de Datos
- [x] Albert Daniel Llica Alvarez: Frontend (Ponencia Panel),  Requisitos de Software, Base de Datos e Imagenes
- [x] Diego Josue Aquino Quispe: Frontend 

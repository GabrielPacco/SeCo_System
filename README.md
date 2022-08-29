
#  INGENIERÍA DE SOFTWARE I -PROYECTO SeCo_System :desktop_computer: 

## :label: Propósito del Proyecto
El  proyecto desarrollado es referido a "La semana de computación " en la escuela profesional de Ciencia de la Computación, la cual tiene como proposito proporcionar información a los usuarios que quieren saber mas de la escuela, asi como de poder participar ya sea como invitados, ponentes, o simplemente en los concursos que ofrece la escuela.
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

<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/diagrama_casos.png" width="550" height="550">

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
    @task_blueprint.route('/actividad/add_actividad', methods=['POST'])
    @cross_origin()
    def create_task():
        content = model.add_actividad(request.json['nombre'], request.json['descripcion'], request.json['fecha'], request.json['hora_inicio'], request.json['hora_fin'], request.json['estado'], request.json['enlace_reu']) 
        return jsonify(content)

    @task_blueprint.route('/actividad/delete_actividad', methods=['POST'])
    @cross_origin()
    def delete_task():
        return jsonify(model.delete_actividad(int(request.json['id_act'])))

    @task_blueprint.route('/actividad/get_actividad', methods=['POST'])
    @cross_origin()
    def actividad():
        return jsonify(model.get_actividad(int(request.json['id_act'])))

    @task_blueprint.route('/actividad/get_actividads', methods=['POST'])
    @cross_origin()
    def actividads():
        return jsonify(model.get_actividads())

    ```

## 2. Plugins.

### *Restricciones* 

- **a)** *El problema se descompone utilizando alguna forma de abstracción (procedimientos, funciones, objetos, etc.)*
- **b)** *Todas o algunas de esas abstracciones se encapsulan físicamente en sus propios paquetes, generalmente precompilados. El programa principal y cada uno de los paquetes se compilan de forma independiente. Estos paquetes son cargados dinámicamente por el programa principal, generalmente al principio (pero no necesariamente).*
- **c)** *El programa principal usa funciones/objetos de los paquetes cargados dinámicamente, sin saber qué implementaciones exactas se usarán. Se pueden usar nuevas implementaciones sin tener que adaptar o recompilar el programa principal.*
- **d)** *Especificación externa de qué paquetes cargar. Esto se puede hacer mediante un archivo de configuración, convenciones de ruta, entrada de usuario u otros mecanismos para que la especificación externa del código se vincule en tiempo de ejecución.*


    ``` 


    ```
## 3. Dataspaces.

### *Restricciones*
- **a)** *Existencia de una o más unidades que ejecutan concurrentemente.* 
- **b)** *Existencia de uno o más espacios de datos donde las unidades concurrentes almacenan y recuperan datos.* 
- **c)** *No hay intercambios de datos directos entre las unidades concurrentes, excepto a través de los espacios de datos.*

    ```
    ```
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
  

# **Prácticas de Código Legible**

## *1. Agrupación de código.*
    La mayoría de las veces, ciertas tareas requieren unas pocas líneas de código. Es una buena idea mantener estas tareas dentro de bloques de código separados, con algunos espacios entre ellos.
    ``` 
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
    @task_blueprint.route('/actividad/add_actividad', methods=['POST'])
    @cross_origin()
    def create_task():
        ...
        return jsonify(content)

    @task_blueprint.route('/actividad/delete_actividad', methods=['POST'])
    @cross_origin()
    def delete_task():
        return jsonify(model.delete_actividad(int(request.json['ID_Actividad'])))

    @task_blueprint.route('/actividad/get_actividad', methods=['POST'])
    @cross_origin()
    def actividad():
        return jsonify(model.get_actividad(int(request.json['ID_Actividad'])))

    @task_blueprint.route('/actividad/get_actividads', methods=['POST'])
    @cross_origin()
    def tasks():
        return jsonify(model.get_actividads())
    ```
## *7. Organización de Archivos y Carpetas.*

![image](https://live.staticflickr.com/65535/52300101188_80a37989c3_n.jpg)

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

## *3) El Principio de Segregación de Interfaz (ISP)*

### *“Muchas interfaces específicas del cliente son mejores que una interfaz de propósito general”*

En el concurso de clases se considera una interfaz, todos los métodos y propiedades “ expuestos ”, es decir, todo aquello con lo que un usuario puede interactuar que pertenece a esa clase.

En este sentido, los principios de IS nos dicen que una clase solo debe tener la interfaz necesaria (SRP) y evitar métodos que no funcionarán o que no tienen por qué ser parte de esa clase.

Este problema surge, principalmente, cuando una subclase hereda métodos de una clase base que no necesita. En nuestro trabajo, encontramos diversidad de interfaces para poder interactuar con el usuario, tales como Admin.vue y User.vue. tanto User.uve es diferente a Admin.vue a pesar de que ambos son usuarios, O tro ejemplo que tenemos es como tanto el inicio como el registro de usuario es muy diferente.

<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/imagen1.jpg" width="550" height="550">

## *4) El Principio de Substitución de Liskov (LSP)*

### *“Las subclases pueden ser sustiuidas por la superclase”*

Las clases menores pueden ser sustituidas por superclases, siguiendo la substitución de Liskov


## *5) El Principio de Inversión de Dependencias (DIP)*

### *“Los módulos de alto nivel no deben tener dependencia de los de bajo nivel”*

En el concurso de clases se considera una interfaz, todos los métodos y propiedades “ expuestos ”, es decir, todo aquello con lo que un usuario puede interactuar que pertenece a esa clase.

En este sentido, los principios de IS nos dicen que una clase solo debe tener la interfaz necesaria (SRP) y evitar métodos que no funcionarán o que no tienen por qué ser parte de esa clase.

### 🔩Planificación de tareas de implementación en la herramienta TRELLO 🔩
https://trello.com/b/FxYv1sZo/seco

### 🔩COLABORADORES 🔩

- [x] Erick Jesús Perez Chipa
- [x] Gabriel Pacco Huaraca
- [x] Ronald Gutierrez Arratia
- [x] Uberto Garcia Caceres
- [x] Fabrizio Miguel Mattos Cahui
- [x] Albert Daniel Llica Alvarez
- [x] Diego Josue Aquino Quispe


#  INGENIERÍA DE SOFTWARE I -PROYECTO SeCo_System :desktop_computer: 
## :label: Propósito del Proyecto
El  proyecto desarrollado es referido a "La semana de computación " en la escuela profesional de Ciencia de la Computación, la cual tiene como proposito proporcionar información a los usuarios que quieren saber mas de la escuela, asi como de poder participar ya sea como invitados, ponentes, o simplemente en los concursos que ofrece la escuela.
## :red_circle: Desarrollo
### Diagrama de Casos de Uso
![image](https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Main.png) 
<img src="https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Main.png" width="450" height="450">
### Diseño de Modelo de Datos 
![image](https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/modelo.png)
### Diseño de Arquitectura
![image](https://github.com/GabrielPacco/SeCo_System/blob/main/Recursos/Arquitectura.png)

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
        content = model.add_actividad(request.json['nombre'], request.json['descripcion'], request.json['fechaInicio'], request.json['fechaFin'], request.json['enlaceReunion'], request.json['isProtocolar'], request.json['isPonencia'], request.json['isPanel'], request.json['isConcurso'], request.json['bases']) 
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
## *3. Poner en mayúscula las palabras especiales de SQL*
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
## *4. Cada función realiza solo realiza una tarea*
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
## *5. Los nombres de las funciones realizan lo mencionado*
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
## *6. Organización de Archivos y Carpetas.*

![image](https://live.staticflickr.com/65535/52300101188_80a37989c3_n.jpg)

# **Principios SOLID**
## *1) El principio de responsabilidad única (SRP)*

### *“Una clase debe tener una, y sólo una, razón para cambiar”*

En otras palabras, cada componente de su código (en general una clase, pero también una función) debe tener una y solo una responsabilidad . Como consecuencia de eso, solo debería haber una razón para cambiarlo.

Con demasiada frecuencia, ve una pieza de código que se encarga de todo un proceso a la vez. Es decir, una función que carga datos, los modifica y los grafica, todo antes de devolver su resultado.

Tomemos un ejemplo más simple, donde tenemos una lista de números L = [n1, n2, …, nx] y calculamos algunas funciones matemáticas para esta lista. Por ejemplo, calcule la media, la mediana, etc.


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

``` 

```

## *3) El Principio de Segregación de Interfaz (ISP)*

### *“Muchas interfaces específicas del cliente son mejores que una interfaz de propósito general”*

En el concurso de clases se considera una interfaz, todos los métodos y propiedades “ expuestos ”, es decir, todo aquello con lo que un usuario puede interactuar que pertenece a esa clase.

En este sentido, los principios de IS nos dicen que una clase solo debe tener la interfaz necesaria (SRP) y evitar métodos que no funcionarán o que no tienen por qué ser parte de esa clase.

Este problema surge, principalmente, cuando una subclase hereda métodos de una clase base que no necesita.

``` 

```
### 🔩COLABORADORES 🔩

- [x] Erick Jesús Perez Chipa
- [x] Gabriel Pacco Huaraca
- [x] Ronald Gutierrez Arratia
- [x] Uberto Garcia Caceres
- [x] Fabrizio Miguel Mattos Cahui
- [x] Albert Daniel Llica Alvarez
- [x] Diego Josue Aquino Quispe

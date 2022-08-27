from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

################### Actividad ################################
    # Funcion para obtener una actividad por su ID
    def get_actividad(self, ID_Actividad):    
        params = {'ID_Actividad' : ID_Actividad}      
        rv = self.mysql_pool.execute("SELECT * from actividad where ID_Actividad=%(ID_Actividad)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID_Actividad': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3], 'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todas las actividades
    def get_actividads(self):  
        rv = self.mysql_pool.execute("SELECT * from actividad")  
        data = []
        content = {}
        for result in rv:
            content = {'ID_Actividad': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3], 'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar una actividad
    def add_actividad(self, nombre, descripcion, fecha, hora_inicio, hora_fin, estado, enlace_reu):
        params = {
            'nombre' : nombre,
            'descripcion' : descripcion,
            'fecha' : fecha,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
            'estado' : estado,
            'enlace_reu' : enlace_reu
        }  
        query = """insert into actividad (nombre, descripcion, fechaInicio, fechaFin, enlaceReunion, isProtocolar, isPonencia, isPanel, isConcurso, bases)
            values (%(nombre)s, %(descripcion)s, %(fechaInicio)s, %(fechaFin)s, %(enlaceReunion)s, %(isProtocolar)s, %(isPonencia)s, %(isPanel)s, %(isConcurso)s, %(bases)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'ID_Actividad': cursor.lastrowid, 'nombre': nombre, 'descripcion': descripcion, 
        'fecha': fecha, 'hora_inicio': hora_inicio, 'hora_fin': hora_fin,
         'estado': estado, 'enlace_reu': enlace_reu}
        return data

    # Funcion para eliminar una actividad
    def delete_actividad(self, ID_Actividad):    
        params = {'ID_Actividad' : ID_Actividad}      
        query = """delete from actividad where ID_Actividad = %(ID_Actividad)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

################### Usuario ################################

    # Funcion para obtener un usuario por su ID
    def get_usuario(self, id_user):
        params = {'id_user' : id_user}      
        rv = self.mysql_pool.execute("SELECT * from usuario where id_user=%(id_user)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_user': result[0], 'nombre': result[1], 'constrasenia': result[2], 'email': result[3]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los usuarios
    def get_usuarios(self):
        rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_user': result[0], 'nombre': result[1], 'constrasenia': result[2], 'email': result[3]}
            data.append(content)
            content = {}
        return data
    
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
        

################### Invitado ################################

    # Funcion para obtener un invitado por su ID
    def get_invitado(self, id_inv):
        params = {'id_inv' : id_inv}      
        rv = self.mysql_pool.execute("SELECT * from invitado where id_inv=%(id_inv)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_inv': result[0], 'universidad': result[1], 'carrera': result[2], 'grado': result[3]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para obtener todos los invitados
    def get_invitados(self):
        rv = self.mysql_pool.execute("SELECT * from invitado")  
        data = []
        content = {}
        for result in rv:
            content = {'id_inv': result[0], 'universidad': result[1], 'carrera': result[2], 'grado': result[3]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar un invitado
    def add_invitado(self, universidad, carrera, grado):
        params = {
            'universidad' : universidad,
            'carrera' : carrera,
            'grado' : grado
        }  
        query = """insert into invitado (universidad, carrera, grado)
            values (%(universidad)s, %(carrera)s, %(grado)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_inv': cursor.lastrowid, 'universidad': universidad, 'carrera': carrera, 'grado': grado}
        return data

    # Funcion para eliminar un invitado
    def delete_invitado(self, id_inv):
        params = {'id_inv' : id_inv}      
        query = """delete from invitado where id_inv = %(id_inv)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_actividad(1))
    #print(tm.get_actividads())
    print(tm.delete_actividad(67))
    print(tm.get_actividads())
    #print(tm.create_actividad('prueba 10', 'desde python'))
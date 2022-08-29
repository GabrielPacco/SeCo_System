from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

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
        query = """insert into actividad (nombre, descripcion, fecha, hora_inicio, hora_fin, estado, enlace_reu)
            values (%(nombre)s, %(descripcion)s, %(fecha)s, %(hora_inicio)s, %(hora_fin)s, %(estado)s, %(enlace_reu)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_act': cursor.lastrowid, 'nombre': nombre, 'descripcion': descripcion, 'fecha': fecha, 'hora_inicio': hora_inicio, 'hora_fin': hora_fin, 'estado': estado, 'enlace_reu': enlace_reu}
        return data

    # Funcion para eliminar una actividad
    def delete_actividad(self, id_act):
        params = {'id_act' : id_act}      
        query = """delete from actividad where id_act = %(id_act)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


################### Administrador ################################

    # Funcion para obtener un administrador por su ID
    def get_administrador(self, id_adm):
        params = {'id_adm' : id_adm}      
        rv = self.mysql_pool.execute("SELECT * from administrador where id_adm=%(id_adm)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_adm': result[0], 'rol': result[1]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para obtener todos los administradores
    def get_administradors(self):
        rv = self.mysql_pool.execute("SELECT * from administrador")  
        data = []
        content = {}
        for result in rv:
            content = {'id_adm': result[0], 'rol': result[1]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para agregar un administrador
    def add_administrador(self, rol):
        params = {
            'rol' : rol
        }  
        query = """insert into administrador (rol)
            values (%(rol)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_adm': cursor.lastrowid, 'rol': rol}
        return data
    
    # Funcion para eliminar un administrador
    def delete_administrador(self, id_adm):
        params = {'id_adm' : id_adm}      
        query = """delete from administrador where id_adm = %(id_adm)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
    

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
    
    # Funcion para agregar un concurso
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

    # Funcion para eliminar un concurso
    def delete_concurso(self, id_conc):
        params = {'id_conc' : id_conc}      
        query = """delete from concurso where id_conc = %(id_conc)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


################### Contribuidor ################################

    # Funcion para obtener un contribuidor por su ID
    def get_contribuidor(self, id_cont):
        params = {'id_cont' : id_cont}      
        rv = self.mysql_pool.execute("SELECT * from contribuidor where id_cont=%(id_cont)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_cont': result[0], 'nombre': result[1], 'universidad': result[2], 'especialidad': result[3], 'decsripcion': result[4], 'facebool': result[5], 'email': result[6], 'linkedin': result[7], 'rol': result[8]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los contribuidores
    def get_contribuidors(self):
        rv = self.mysql_pool.execute("SELECT * from contribuidor")  
        data = []
        content = {}
        for result in rv:
            content = {'id_cont': result[0], 'nombre': result[1], 'universidad': result[2], 'especialidad': result[3], 'decsripcion': result[4], 'facebool': result[5], 'email': result[6], 'linkedin': result[7], 'rol': result[8]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar un contribuidor
    def add_contribuidor(self, nombre, universidad, especialidad, decsripcion, facebool, email, linkedin, rol):
        params = {
            'nombre' : nombre,
            'universidad' : universidad,
            'especialidad' : especialidad,
            'decsripcion' : decsripcion,
            'facebool' : facebool,
            'email' : email,
            'linkedin' : linkedin,
            'rol' : rol
        }  
        query = """insert into contribuidor (nombre, universidad, especialidad, decsripcion, facebool, email, linkedin, rol)
            values (%(nombre)s, %(universidad)s, %(especialidad)s, %(decsripcion)s, %(facebool)s, %(email)s, %(linkedin)s, %(rol)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_cont': cursor.lastrowid, 'nombre': nombre, 'universidad': universidad, 'especialidad': especialidad, 'decsripcion': decsripcion, 'facebool': facebool, 'email': email, 'linkedin': linkedin, 'rol': rol}
        return data
    
    # Funcion para eliminar un contribuidor
    def delete_contribuidor(self, id_cont):
        params = {'id_cont' : id_cont}      
        query = """delete from contribuidor where id_cont = %(id_cont)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


################### Edición ################################

    # Funcion para obtener una edición por su ID
    def get_edicion(self, id_edi):
        params = {'id_edi' : id_edi}      
        rv = self.mysql_pool.execute("SELECT * from edicion where id_edi=%(id_edi)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_edi': result[0], 'id_act': result[1], 'anho': result[2], 'nombre': result[3]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para obtener todas las ediciones
    def get_edicions(self):
        rv = self.mysql_pool.execute("SELECT * from edicion")  
        data = []
        content = {}
        for result in rv:
            content = {'id_edi': result[0], 'id_act': result[1], 'anho': result[2], 'nombre': result[3]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para agregar una edición
    def add_edicion(self, anho, nombre):
        params = {
            'anho' : anho,
            'nombre' : nombre
        }  
        query = """insert into edicion (anho, nombre)
            values (%(anho)s, %(nombre)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_edi': cursor.lastrowid, 'anho': anho, 'nombre': nombre}
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



################### Panel #################################

    # Funcion para obtener un panel por su ID
    def get_panel(self, id_pan):
        params = {'id_pan' : id_pan}      
        rv = self.mysql_pool.execute("SELECT * from panel where id_pan=%(id_pan)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_pon': result[0], 'id_act': result[1], 'topico': result[2]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los paneles
    def get_panels(self):
        rv = self.mysql_pool.execute("SELECT * from panel")  
        data = []
        content = {}
        for result in rv:
            content = {'id_pon': result[0], 'id_act': result[1], 'topico': result[2]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para agregar un panel
    def add_panel(self, topico):
        params = {
            'topico' : topico
        }  
        query = """insert into panel (topico)
            values (%(topico)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_pan': cursor.lastrowid, 'topico': topico}
        return data
    
    # Funcion para eliminar un panel
    def delete_panel(self, id_pan):
        params = {'id_pan' : id_pan}      
        query = """delete from panel where id_pan = %(id_pan)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



################### Ponencia ################################

    # Funcion para obtener una ponencia por su ID
    def get_ponencia(self, id_pon):
        params = {'id_pon' : id_pon}      
        rv = self.mysql_pool.execute("SELECT * from ponencia where id_pon=%(id_pon)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_pon': result[0], 'id_act': result[1], 'topico': result[2]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todas las ponencias
    def get_ponencias(self):
        rv = self.mysql_pool.execute("SELECT * from ponencia")  
        data = []
        content = {}
        for result in rv:
            content = {'id_pon': result[0], 'id_act': result[1], 'topico': result[2]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para agregar una ponencia
    def add_ponencia(self, topico):
        params = {
            'topico' : topico
        }  
        query = """insert into ponencia (topico)
            values (%(topico)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_pon': cursor.lastrowid, 'topico': topico}
        return data
    
    # Funcion para eliminar una ponencia
    def delete_ponencia(self, id_pon):
        params = {'id_pon' : id_pon}      
        query = """delete from ponencia where id_pon = %(id_pon)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
    

################### Protocolar #################################

    # Funcion para obtener un protocolar por su ID
    def get_protocolar(self, id_prot):
        params = {'id_prot' : id_prot}      
        rv = self.mysql_pool.execute("SELECT * from protocolar where id_prot=%(id_prot)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_prot': result[0], 'regla': result[1]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los protocolares
    def get_protocolars(self):
        rv = self.mysql_pool.execute("SELECT * from protocolar")  
        data = []
        content = {}
        for result in rv:
            content = {'id_prot': result[0], 'regla': result[1]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar un protocolar
    def add_protocolar(self, regla):
        params = {
            'regla' : regla
        }  
        query = """insert into protocolar (regla)
            values (%(regla)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_prot': cursor.lastrowid, 'regla': regla}
        return data
    
    # Funcion para eliminar un protocolar
    def delete_protocolar(self, id_prot):
        params = {'id_prot' : id_prot}      
        query = """delete from protocolar where id_prot = %(id_prot)s"""    
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
        

if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_actividad(1))
    #print(tm.get_actividads())
    print(tm.delete_usuario(67))
    print(tm.get_usuarios())
    #print(tm.create_actividad('prueba 10', 'desde python'))
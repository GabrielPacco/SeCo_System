from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

################# Actividad ################################

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


################# Administrador ################################

@task_blueprint.route('/administrador/add_administrador', methods=['POST'])
@cross_origin()
def create_administrador():
    content = model.add_administrador(request.json['rol']) 
    return jsonify(content)    

@task_blueprint.route('/administrador/delete_administrador', methods=['POST'])
@cross_origin()
def delete_administrador():
    return jsonify(model.delete_administrador(int(request.json['ID_Administrador'])))

@task_blueprint.route('/administrador/get_administrador', methods=['POST'])
@cross_origin()
def administrador():
    return jsonify(model.get_administrador(int(request.json['ID_Administrador'])))

@task_blueprint.route('/administrador/get_administradors', methods=['POST'])
@cross_origin()
def administradors():
    return jsonify(model.get_administradors())


################# Concurso ################################

@task_blueprint.route('/concurso/add_concurso', methods=['POST'])
@cross_origin()
def create_concurso():
    content = model.add_concurso(request.json['participante'], request.json['base'], request.json['premio']) 
    return jsonify(content)

@task_blueprint.route('/concurso/delete_concurso', methods=['POST'])
@cross_origin()
def delete_concurso():
    return jsonify(model.delete_concurso(int(request.json['ID_Concurso'])))

@task_blueprint.route('/concurso/get_concurso', methods=['POST'])
@cross_origin()
def concurso():
    return jsonify(model.get_concurso(int(request.json['ID_Concurso'])))

@task_blueprint.route('/concurso/get_concursos', methods=['POST'])
@cross_origin()
def concursos():
    return jsonify(model.get_concursos())


################# Contribuidor ################################

@task_blueprint.route('/contribuidor/add_contribuidor', methods=['POST'])
@cross_origin()
def create_contribuidor():
    content = model.add_contribuidor(request.json['nombre'], request.json['universidad'], request.json['especialidad'], request.json['descripcion'], request.json['facebool'], request.json['email'], request.json['linkedin'], request.json['rol']) 
    return jsonify(content)

@task_blueprint.route('/contribuidor/delete_contribuidor', methods=['POST'])
@cross_origin()
def delete_contribuidor():
    return jsonify(model.delete_contribuidor(int(request.json['ID_Contribuidor'])))

@task_blueprint.route('/contribuidor/get_contribuidor', methods=['POST'])
@cross_origin()
def contribuidor():
    return jsonify(model.get_contribuidor(int(request.json['ID_Contribuidor'])))

@task_blueprint.route('/contribuidor/get_contribuidors', methods=['POST'])
@cross_origin()
def contribuidors():
    return jsonify(model.get_contribuidors())


################# Edición ################################

@task_blueprint.route('/edicion/add_edicion', methods=['POST'])
@cross_origin()
def create_edicion():
    content = model.add_edicion(request.json['anho'], request.json['nombre']) 
    return jsonify(content)

@task_blueprint.route('/edicion/delete_edicion', methods=['POST'])
@cross_origin()
def delete_edicion():
    return jsonify(model.delete_edicion(int(request.json['ID_Edicion'])))

@task_blueprint.route('/edicion/get_edicion', methods=['POST'])
@cross_origin()
def edicion():
    return jsonify(model.get_edicion(int(request.json['ID_Edicion'])))

@task_blueprint.route('/edicion/get_edicions', methods=['POST'])
@cross_origin()
def edicions():
    return jsonify(model.get_edicions())


################# Invitado ################################

@task_blueprint.route('/invitado/add_invitado', methods=['POST'])
@cross_origin()
def create_invitado():
    content = model.add_invitado(request.json['universidad'], request.json['carrera'], request.json['grado']) 
    return jsonify(content)

@task_blueprint.route('/invitado/delete_invitado', methods=['POST'])
@cross_origin()
def delete_invitado():
    return jsonify(model.delete_invitado(int(request.json['id_invitado'])))

@task_blueprint.route('/invitado/get_invitado', methods=['POST'])
@cross_origin()
def invitado():
    return jsonify(model.get_invitado(int(request.json['id_invitado'])))

@task_blueprint.route('/invitado/get_invitados', methods=['POST'])
@cross_origin()
def invitados():
    return jsonify(model.get_invitados())


################# Panel ################################

@task_blueprint.route('/panel/add_panel', methods=['POST'])
@cross_origin()
def create_panel():
    content = model.add_panel(request.json['topico']) 
    return jsonify(content)

@task_blueprint.route('/panel/delete_panel', methods=['POST'])
@cross_origin()
def delete_panel():
    return jsonify(model.delete_panel(int(request.json['ID_Panel'])))

@task_blueprint.route('/panel/get_panel', methods=['POST'])
@cross_origin()
def panel():
    return jsonify(model.get_panel(int(request.json['ID_Panel'])))

@task_blueprint.route('/panel/get_panels', methods=['POST'])
@cross_origin()
def panels():
    return jsonify(model.get_panels())



################# Ponencia ################################

@task_blueprint.route('/ponencia/add_ponencia', methods=['POST'])
@cross_origin()
def create_ponencia():
    content = model.add_ponencia(request.json['topico']) 
    return jsonify(content)

@task_blueprint.route('/ponencia/delete_ponencia', methods=['POST'])
@cross_origin()
def delete_ponencia():
    return jsonify(model.delete_ponencia(int(request.json['ID_Ponencia'])))

@task_blueprint.route('/ponencia/get_ponencia', methods=['POST'])
@cross_origin()
def ponencia():
    return jsonify(model.get_ponencia(int(request.json['ID_Ponencia'])))

@task_blueprint.route('/ponencia/get_ponencias', methods=['POST'])
@cross_origin()
def ponencias():
    return jsonify(model.get_ponencias())


################# Protocolar ################################

@task_blueprint.route('/protocolar/add_protocolar', methods=['POST'])
@cross_origin()
def create_protocolar():
    content = model.add_protocolar(request.json['regla']) 
    return jsonify(content)

@task_blueprint.route('/protocolar/delete_protocolar', methods=['POST'])
@cross_origin()
def delete_protocolar():
    return jsonify(model.delete_protocolar(int(request.json['ID_Protocolar'])))

@task_blueprint.route('/protocolar/get_protocolar', methods=['POST'])
@cross_origin()
def protocolar():
    return jsonify(model.get_protocolar(int(request.json['ID_Protocolar'])))

@task_blueprint.route('/protocolar/get_protocolars', methods=['POST'])
@cross_origin()
def protocolars():
    return jsonify(model.get_protocolars())


################# Usuario ################################
@task_blueprint.route('/usuario/add_usuario', methods=['POST'])
@cross_origin()
def create_user():
    content = model.add_usuario(request.json['nombre'], request.json['contrasenia'], request.json['email']) 
    return jsonify(content)

@task_blueprint.route('/usuario/delete_usuario', methods=['POST'])
@cross_origin()
def delete_user():
    return jsonify(model.delete_usuario(int(request.json['id_user'])))

@task_blueprint.route('/usuario/get_usuario', methods=['POST'])
@cross_origin()
def user():
    return jsonify(model.get_usuario(int(request.json['id_user'])))

@task_blueprint.route('/usuario/get_usuarios', methods=['POST'])
@cross_origin()
def users():
    return jsonify(model.get_usuarios())



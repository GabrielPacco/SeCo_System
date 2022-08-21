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

################# Usuario ################################
@task_blueprint.route('/usuario/add_usuario', methods=['POST'])
@cross_origin()
def create_user():
    content = model.add_usuario(request.json['nombre'], request.json['apellido'], request.json['contrasenia'], request.json['email']) 
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

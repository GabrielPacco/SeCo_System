#!/usr/bin/python
#-*- coding: utf-8 -*-

import Invitado, Edicion, Contribuidor
class Administrador():
    def __init__(self,inv_1):
        self.usuario=inv_1[0]
        pass
    def agregarActividad(self, actividad, list_act):
        list_act.append(actividad[0])
        pass
    def modificarActividad(self, pos_1, actividad_cambios, lista_act):
        lista_act[pos_1].id = actividad_cambios[0]
        lista_act[pos_1].nombreActividad = actividad_cambios[1]
        lista_act[pos_1].fecha = actividad_cambios[2]        
        lista_act[pos_1].horainicio = actividad_cambios[3]     
        lista_act[pos_1].horafin = actividad_cambios[4]
        lista_act[pos_1].estado = actividad_cambios[5]
        lista_act[pos_1].enlacereunion = actividad_cambios[6]
        lista_act[pos_1].ponencia.topico = actividad_cambios[7]
        lista_act[pos_1].panel.topico = actividad_cambios[8]
        lista_act[pos_1].concurso.base = actividad_cambios[9]
        lista_act[pos_1].concurso.premio = actividad_cambios[10]
        pass

    def eliminarActividad(self, pos_1, lista_act):
        del lista_act[pos_1]
        pass

    def agregarContribuidor(self, contribuidor, lista_con):
        lista_con.append(contribuidor[0])
        pass

    def modificarContribuidor(self,pos_1,contribuidor_cambios, lista_con):
        lista_con[pos_1].id = contribuidor_cambios[0]
        lista_con[pos_1].nombre = contribuidor_cambios[1]
        lista_con[pos_1].universidad = contribuidor_cambios[2]
        lista_con[pos_1].especialidad = contribuidor_cambios[3]
        lista_con[pos_1].descripcion = contribuidor_cambios[4]
        lista_con[pos_1].email = contribuidor_cambios[5]
        lista_con[pos_1].facebook = contribuidor_cambios[6]
        lista_con[pos_1].linkedin = contribuidor_cambios[7]
        lista_con[pos_1].rol = contribuidor_cambios[8]
        pass

    def eliminarContribuidor(self, pos_1,lista_con):
        del lista_con[pos_1]
        pass

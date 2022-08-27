#!/usr/bin/python
#-*- coding: utf-8 -*-

import Usuario, Actividad
class Invitado:
    def __init__(self,usu_1,uni_1,car_1,gra_1):
        self.usuario=usu_1[0]
        self.universidad = uni_1
        self.carreraProfesional = car_1
        self.gradodeestudio = gra_1

    def inscribirParticipacion(self, lista_par):
        lista_par(self.usuario.id)
        pass

    def confirmarParticipacion(self, res_1):
        if(res_1==0):
            return False
        return True

    def contactarOrganizacion(self, tel_1):
        if(len(tel_1)==9):
            return True
        return False

    def buscarActividad(self, lista_act, actividad):
        actividades=[]
        if(actividad.id!=None):
            for i in lista_act:
                if(actividad.id==i.id)
                    actividades.append(i)
                    return actividades
        for i in lista_act:
            if((i.nombre.find(actividad.nombre))!=-1 && (i.fecha.find(actividad.fecha)!=-1))
                actividades.append(i)
        return actividades

    def visualizarEvento(self, eve_1 , list_act):
        return  list_act[eve_1]

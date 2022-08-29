#!/usr/bin/python
#-*- coding: utf-8 -*-
#conero de M
import Ponencia, Panel, Concurso, Protocolar
class Actividad:
    def __init__(self,id_1,nom_1,fec_1,hoI_1,hoF_1,est_1,enl_1,pon_1,pan_top,con_bas,con_pre):
        self.id = id_1
        self.nombreActividad = nom_1
        self.fecha = fec_1
        self.horainicio = hoI_1
        self.horafin = hoF_1
        self.estado = est_1
        self.enlacereunion = enl_1
        self.ponencia = Ponencia(pon_1)
        self.panel = Panel(pan_top)
        self.concurso = Concurso(con_bas,con_pre)
        self.protocolar = Protocolar()

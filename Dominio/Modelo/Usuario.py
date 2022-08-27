#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario:
    def __init__(self,id_1,nom_1,usu_1,con_1,ema_1,tel_1):
        self.id = id_1
        self.nombre = nom_1
        self.usuario = usu_1
        self.contrasenha = con_1
        self.email = ema_1
        self.telefono = tel_1

    def iniciarSesion(self, lista_usu,lista_con):
        x=-1
        it=len(lista_usu)
        for i in range(it):
            if(lista_usu[i]==self.usuario):
                x=i
                break
        if(x!=-1):
            if(lista_con[x]==self.contrasenha):
                return true;
        return false

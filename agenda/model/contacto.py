#!/usr/bin/python
# -*- coding: utf-8 -*-

class Contacto(object):
    """Modelo de un Contacto de la agenda
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, telefono, email, tweeter, skype):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tweeter = tweeter
        self.skype = skype

    def descripcion(self):
    	return "%s %s" %(self.nombre, self.apellido)

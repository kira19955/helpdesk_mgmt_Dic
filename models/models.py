# -*- coding: utf-8 -*-
from odoo import fields,models,api

class TipoDeMantenimiento (models.Model):
    _name = 'tipo_de_mantenimiento'
    _description = 'Catalogo de los tipos de mantenimientos que hay en el departamento'

    name = fields.Char(String="Descripción")

class TipoDeEquipo(models.Model):
    _name = 'tipo_de_equipo'
    _description = 'Catalogo de los diferentes tipos de equipos que hay'

    name = fields.Char(string="Descripción")

class Situacion(models.Model):
    _name = 'situacion'
    _description = 'Catalogo de los diferentes tipos de situacion'

    name = fields.Char(string="Descripción")

class CentroDeServicios(models.Model):
    _name = 'centro_de_servicios'
    _description = 'Catalogo de centro de servicios'

    name = fields.Char(string="Descripción")
    tel = fields.Char(string="Teléfono")
    direccion = fields.Char(string="Dirección")


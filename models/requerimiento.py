from odoo import fields, models, api

class Solicitud(models.Model):
    _name = 'solicitud'
    _description = 'Modelo que almacena los datos de la solicitud' \
                   'y lo que solicita el usuario'

    name = fields.Char()
    tipo_solicitud = fields.Selection([('computo', 'Computo'),
                                       ('telefonia', 'Telefonia'),
                                       ('redes', 'Redes'),
                                       ('sistemas', 'Sistemas'),
                                       ('diseño', 'Diseño'),
                                       ('prestamos', 'Prestamos'),
                                       ('administracion', 'Administracion')],
                                      string="Tipo de Solicitud")
    equipo2 = fields.Many2one(comodel_name="tipo_de_equipo")
    serie = fields.Char(string="Serie")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    inventario = fields.Char(string="Inventario")
    descripcion = fields.Char(string="Descripción")
    ubicacion = fields.Char(string="Ubicación")
    situacion2 = fields.Many2one(comodel_name="situacion", string="Situacion")
    requerimiento2 = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='requerimiento')
    cal_serv = fields.Selection(
        string='Como Califica el Servicio',
        selection=[('sin calificaion', 'S/calif'),
                   ('malo', 'Malo'),
                   ('regular', 'Regular'),
                   ('bueno', 'Bueno')])
    reporte = fields.Boolean(
        string='Reporte',
        required=False)
    tipo_daño = fields.Selection(
        string='Tipo',
        selection=[('daño', 'Daño'),
                   ('recomendaciones', 'Recomendaciones')])
    fec_daño = fields.Date(string="Fecha")
    fch_evento = fields.Date(string="Fecha Evento")
    hora_evento = fields.Float(string="Hora del Evento")
    hora_entrega = fields.Float(string="Hora de Entrega")
    accion_realizada = fields.Char(
        string='Descripción de la Accion realizada')
    observaciones = fields.Char(
        string='Observaciones')
    estado_equipo = fields.Char(String="Estado")
    observaciones_reporte = fields.Char(string="Observaciones")
    num_reporte = fields.Char(string="Reporte # ", copy="false")

    def secuencia(self):
        sequence_obj = self.env['ir.sequence']
        correlativo = sequence_obj.next_by_code('secuencia.reportes.tecnicos')
        return self.num_reporte == self.correlativo

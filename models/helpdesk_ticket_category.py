from odoo import fields, models


class HelpdeskCategory(models.Model):

    _name = 'helpdesk.ticket.category'
    _description = 'Helpdesk Ticket Category'

    active = fields.Boolean(string='Activo', default=True,)
    name = fields.Char(string='Nombre', required=True)
    tipo_mantenimiento = fields.Many2one(comodel_name="tipo_de_mantenimiento")
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        default=lambda self: self.env['res.company']._company_default_get(
            'helpdesk.ticket')
    )

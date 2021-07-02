from odoo import models, fields


class HelpdeskTicketChannel(models.Model):

    _name = 'helpdesk.ticket.channel'
    _description = 'Helpdesk Ticket Channel'

    name = fields.Char(required=True, string="Nombre")
    active = fields.Boolean(default=True, string="Activo")
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        default=lambda self: self.env['res.company']._company_default_get(
            'helpdesk.ticket')
    )

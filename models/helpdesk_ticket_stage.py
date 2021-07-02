from odoo import fields, models


class HelpdeskTicketStage(models.Model):
    _name = 'helpdesk.ticket.stage'
    _description = 'Helpdesk Ticket Stage'
    _order = 'sequence, id'

    name = fields.Char(string='Nombre Del Estado', required=True, translate=True)

    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True)
    unattended = fields.Boolean(
        string='Unattended')
    closed = fields.Boolean(
        string='Closed')

    fold = fields.Boolean(
        string='Folded in Kanban',
        help="This stage is folded in the kanban view "
             "when there are no records in that stage "
             "to display.")
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        default=lambda self: self.env['res.company']._company_default_get(
            'helpdesk.ticket')
    )

from odoo import _, api, fields, models, tools


class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'
    _rec_name = 'name'
    _order = 'name desc'
    departamento = fields.Many2one('hr.department', compute="get_department",track_visibility=True)

    @api.one
    def get_department(self):
        user = self.env['res.users'].search([('id', '=', self._uid)])
        employee = self.env['hr.employee'].search([('partner_id', '=', user.partner_id.id)])
        if employee.department_id:
            self.departamento = employee.department_id

    def _get_default_stage_id(self):
        return self.env['helpdesk.ticket.stage'].search([], limit=1).id

    name = fields.Char(string='Nombre Del Solicitante', required=True, readonly=False)

    user_id = fields.Many2one(
        'res.users',
        string='Asignado',)

    user_ids = fields.Many2many(
        comodel_name='res.users',
        related='team_id.user_ids',
        string='Users')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['helpdesk.ticket.stage'].search([])
        return stage_ids

    stage_id = fields.Many2one(
        'helpdesk.ticket.stage',
        string='Estado Del Requerimiento',
        group_expand='_read_group_stage_ids',
        default=_get_default_stage_id,
        track_visibility='onchange',
    )
    partner_id = fields.Many2one('res.partner')
    partner_name = fields.Char()
    partner_email = fields.Char()

    closed = fields.Boolean(related='stage_id.closed')
    unattended = fields.Boolean(related='stage_id.unattended')
    tag_ids = fields.Many2many('helpdesk.ticket.tag', string="Posible Falla")
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        default=lambda self: self.env['res.company']._company_default_get(
            'helpdesk.ticket')
    )
    channel_id = fields.Many2one(
        'helpdesk.ticket.channel',
        string='Tipo De Solicitud')

    category_id = fields.Many2one('helpdesk.ticket.category',
                                  string='Categoria')
    team_id = fields.Many2one('helpdesk.ticket.team', string="Equipo")

    attachment_ids = fields.One2many(
        'ir.attachment', 'res_id',
        domain=[('res_model', '=', 'helpdesk.ticket')],
        string="Media Attachments")
    color = fields.Integer(string='Color Index')
    kanban_state = fields.Selection([
        ('normal', 'Default'),
        ('done', 'Ready for next stage'),
        ('blocked', 'Blocked')], string='Kanban State')

    dep_padre = fields.Many2one(comodel_name="hr.department")
    solicitud2 = fields.One2many(
        comodel_name='solicitud',
        inverse_name='requerimiento2',
        string='Solicitud2',
        required=False)


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.partner_name = self.partner_id.name
            self.partner_email = self.partner_id.email

    @api.multi
    @api.onchange('team_id', 'user_id')
    def _onchange_dominion_user_id(self):
        if self.user_id:
            if self.user_id and self.user_ids and \
                    self.user_id not in self.user_ids:
                self.update({
                    'user_id': False
                })
                return {'domain': {'user_id': []}}
        if self.team_id:
            return {'domain': {'user_id': [('id', 'in', self.user_ids.ids)]}}
        else:
            return {'domain': {'user_id': []}}

    # ---------------------------------------------------
    # CRUD
    # ---------------------------------------------------

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if not vals.get('create_date'):
            res['create_date'] = fields.Datetime.now()
        return res

class print_report_vale_salida_view(models.AbstractModel):
    _name = 'report.helpdesk_mgmt.report_vale_salida_view'

    @api.model
    def get_report_values(self,docids, data=None):
        docs = self.env['helpdesk.ticket'].browse(docids[0])

        jefe_departamento = self.env['hr.department'].search([('name','=','Departamento de Infraestructura y Comunicaciones')])

        if jefe_departamento.manager_id.partner_id.title.display_name != False and jefe_departamento.manager_id.partner_id.title.display_name != "False" and jefe_departamento.manager_id.partner_id.title.display_name != "":
            titulo_contralor = str(jefe_departamento.manager_id.partner_id.title.display_name) + " "    
        else:
            titulo_contralor = ""

        jefe_departamento = titulo_contralor +str(jefe_departamento.manager_id.name)
        
        return {
            'doc_model': 'helpdesk',
            'docs': docs,
            'jefe_departamento': jefe_departamento,
        }
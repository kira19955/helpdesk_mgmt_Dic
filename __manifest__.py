# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'DIC',
    'summary': """
        Modulo para la recepcion de Requerimitos 
        del departamento DIC Fase 1
        """,
    'version': '11.0.1.11.0',
    'license': 'AGPL-3',
    'category': '',
    'author': 'Luis Antonio Cruz Gutierrez',
    'website': '',
    'depends': ['base', 'hr', 'contacts', 'directions_utils', 'mail'],
    'data': [
        'data/helpdesk_data.xml',
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/helpdesk_ticket_view.xml',
        'views/helpdesk_ticket_menu.xml',
        'views/helpdesk_ticket_team_view.xml',
        'views/helpdesk_ticket_stage_view.xml',
        'views/helpdesk_ticket_category_view.xml',
        'views/helpdesk_ticket_channel_view.xml',
        'views/helpdesk_ticket_tag_view.xml',
        'views/menu.xml',
        'views/requerimiento.xml',
        'views/views.xml',
        'report/report.xml',
        'report/report2.xml',
        'report/report3.xml',
    ],
    'demo': [

    ],
    'application': True,
    'installable': True,
}

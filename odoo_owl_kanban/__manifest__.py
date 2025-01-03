# -*- coding: utf-8 -*-
{
    'name': "Odoo OWL JS (Kanban)",
    'summary': "Odoo OWL JS",
    'description': "Odoo OWL JS",
    'author': "Adil Akbar",
    'version': '0.1',
    'sequence': 1,
    'depends': ['web', 'crm'],
    'data': [
        'ir.model.access.csv',
        'crm_lead_confirm_wiz.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_owl_kanban/static/src/js/kanban_controller.js',
            'odoo_owl_kanban/static/src/xml/kanban_controller.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}

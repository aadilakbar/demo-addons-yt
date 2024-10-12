# -*- coding: utf-8 -*-
{
    'name': "Odoo OWL JS",
    'summary': "Odoo OWL JS",
    'description': "Odoo OWL JS",
    'author': "Adil Akbar",
    'version': '0.1',
    'sequence': 1,
    'depends': ['web', 'sale_management'],
    'data': [
        'sale.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_owl_list/static/src/js/list_controller.js',
            'odoo_owl_list/static/src/xml/list_controller.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}

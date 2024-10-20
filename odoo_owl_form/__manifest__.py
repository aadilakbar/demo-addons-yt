# -*- coding: utf-8 -*-
{
    'name': "Odoo OWL JS Demo",
    'summary': "Odoo OWL JS",
    'description': "Odoo OWL JS",
    'author': "Adil Akbar",
    'version': '0.1',
    'sequence': 1,
    'depends': ['web'],
    'data': [
        'ir.model.access.csv',
        'odoo_owl_demo.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_owl_form/static/src/xml/form_controller.xml',
            'odoo_owl_form/static/src/js/form_controller.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}

# -*- coding: utf-8 -*-
{
    'name': "Multi-Company Demo",

    'summary': """ Multi-Company Demo Module """,

    'description': """
        Multi-Company Demo Module
    """,

    'author': "Adil Akbar",
    'website': "",
    'category': 'Tools',
    'version': '16.0',
    'depends': ['web', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}

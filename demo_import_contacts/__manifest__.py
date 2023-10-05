# -*- coding: utf-8 -*-
{
    'name': "Import Contacts XLSX",

    'summary': """ Import Contacts XLSX """,

    'description': """
        Import Contacts XLSX
    """,

    'author': "Adil Akbar",
    'website': "",
    'category': 'Tools',
    'version': '16.0',
    'depends': ['base', 'web', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/contact_import_wiz.xml',
        'views/server_action.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}

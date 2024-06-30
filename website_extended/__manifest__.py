# __manifest__.py
{
    'name': 'Website Custom Page',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Add a Custom page in Website',
    'summary': 'Add a Custom page in Website',
    'author': 'Adil Akbar',
    'depends': ['website'],
    'data': [
        'views/custom_page_template.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': False,
}

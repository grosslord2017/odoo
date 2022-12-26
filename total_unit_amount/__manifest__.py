{
    'name': 'Total Unit Amount',
    'description': '''add new field in account.analytic.line''',
    'version': '15.0.1.0.0',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/account_analytic_views.xml',
        'views/project_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
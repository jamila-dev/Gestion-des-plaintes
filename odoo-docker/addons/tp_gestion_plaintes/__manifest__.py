{
    'name': 'Gestion des Plaintes Internes',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Gestion des plaintes internes pour le TP',
    'author': 'User',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/plainte_views.xml',
        'report/plainte_report.xml',
        'report/plainte_report_templates.xml',
    ],
    'installable': True,
    'application': True,
}

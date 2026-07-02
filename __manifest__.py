{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Manage Patients and Doctors',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
    ],
    'installable': True,
    'application': True,
}
{
    'name': 'SSNIT & Digital Address Fields',
    'version': '1.0',
    'category': 'Contacts',
    'summary': 'Field for accepting ssnit and digital address numbers',
    'description': "Field for accepting ssnit and digital address numbers",
    'depends': ['base'],
     'data': [
        'views/social_security.xml',
        'views/digital_address.xml'
        
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False
} 
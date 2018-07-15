# -*- coding: utf-8 -*-
{
    'name': "alquiler",

    'summary': """
        Modulo de alquiler según instructivo 2018-06-26 Contratación Desarrollador Odoo - Prueba práctica
        """,
    'description': """
        Modulo de alquiler de locales
    """,
    'author': "Daniel Arrieta Alfaro",
    'website': "https://github.com/Darrieta05",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    'license': 'AGPL-3',
    'data': [
        'views/alquiler.xml',
        'views/local.xml',
        'views/building.xml',
        'views/floor.xml',
        'views/actions.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    "application": True
}

# -*- coding: utf-8 -*-
{
    'name': 'Test Odoo Cajas - Erick Cruz',
    'version': '1.0',
    'summary': 'control completo cajas',
    'description': 'Control y gestion de cajas de la empresa',
    'author': 'Erick Cruz Cedeño',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'application': True,
    'depends': ['base', 'contacts', 'stock', 'product'],
    'data': [
        'views/contacts/view_age.xml',
        'views/box/view_box.xml',
        'security/ir.model.access.csv',
        # 'views/stock/view_inh.xml',
        # 'security/security.xml'
    ],
    'images': ['./static/description/icon.png']
}

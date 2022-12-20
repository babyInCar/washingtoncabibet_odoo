
# -*- coding: utf-8 -*-
{
    'name': 'delivery manage',
    'version': '0.1',
    'summary': '发货模块添加新功能',
    'description': '',
    'category': 'Uncategorized',
    'author': 'gaoshuang916@126.com',
    'depends': ['base', 'sale', 'web', 'account', 'stock'],
    'data': [
        #  'security/ir.model.access.csv',
        'views/stock_pick_views.xml',
    ],
    'installable': True,
    'application': True,
}

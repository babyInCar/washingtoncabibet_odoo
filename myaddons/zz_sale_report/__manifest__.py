# -*- coding: utf-8 -*-
{
    'name': "zz_sale_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "zz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'web', 'account', 'stock'],

    # always loaded
    'data': [
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'report/report_sale_order.xml',
        'report/report_invoice.xml',
        'report/report_stockpicking_operations.xml',
        'report/report_deliveryslip.xml',
    ],
    # only loaded in demonstration mode
}

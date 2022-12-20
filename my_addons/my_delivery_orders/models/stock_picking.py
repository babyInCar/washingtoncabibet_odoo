# -*- coding: utf-8 -*-

from odoo import fields, models

class MyStockPicking(models.Model):
    _inherit = "stock.picking"
    _description = "rewrite stock picking"

    def action_verify(self):
    """通知仓库可以进行发货了 """
        raise UserError(_("I get your request!"))
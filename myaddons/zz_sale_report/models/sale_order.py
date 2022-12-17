# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    assembly = fields.Boolean(string='Assembly')
    delivery = fields.Boolean(string='Delivery')
    pick_up = fields.Boolean(string='Pick up')
    install = fields.Boolean(string=' Install')

    designer = fields.Many2one('res.partner', string='Designer')
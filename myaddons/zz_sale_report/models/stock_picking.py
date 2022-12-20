# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    assembly = fields.Boolean(string='Assembly', related='sale_id.assembly')
    delivery = fields.Boolean(string='Delivery', related='sale_id.delivery')
    pick_up = fields.Boolean(string='Pick up', related='sale_id.pick_up')
    install = fields.Boolean(string=' Install', related='sale_id.pick_up')

    assembly_pro = fields.Boolean(string='Assembly')
    delivery_pro = fields.Boolean(string='Delivery')
    pick_up_pro = fields.Boolean(string='Pick up')
    install_pro = fields.Boolean(string=' Install')

    payment_state = fields.Selection(selection=[
        ('not_paid', 'Not Paid'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
        ('partial', 'Partially Paid'),
        ('reversed', 'Reversed'),
        ('invoicing_legacy', 'Invoicing App Legacy')],
        string="Payment Status", related='sale_id.payment_state')

    total_pieces = fields.Integer(string='Total Pieces', compute="compute_pieces_cabinets")
    total_cabinets = fields.Integer(string='Total Cabinets', compute="compute_pieces_cabinets")
    is_sale_show = fields.Boolean(string='is_sale', compute='compute_is_show')

    @api.depends('move_ids_without_package')
    def compute_pieces_cabinets(self):
        for line in self:
            line.total_pieces = sum(line.move_ids_without_package.mapped('product_uom_qty'))
            line.total_cabinets = sum(line.move_ids_without_package.mapped('product_uom_qty'))

    @api.depends('sale_id', 'picking_type_id')
    def compute_is_show(self):
        for line in self:
            if line.sale_id and line.picking_type_id.sequence_code == 'OUT':
                line.is_sale_show = False
            else:
                line.is_sale_show = True

    @api.depends('sale_id','sale_id.invoice_ids')
    def compute_payment_state(self):
        for line in self:
            payment_state = False
            if line.sale_id:
                account = self.env['account.move'].search([('id', 'in', line.sale_id.invoice_ids.ids)],
                                                          order='write_date desc', limit=1)
                if account:
                    payment_state = account.payment_state

            line.payment_state = payment_state

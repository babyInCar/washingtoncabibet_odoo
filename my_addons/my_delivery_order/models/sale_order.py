# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MySaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_state = fields.Selection(selection=[
        ('not_paid', 'Not Paid'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
        ('partial', 'Partially Paid'),
        ('reversed', 'Reversed'),
        ('invoicing_legacy', 'Invoicing App Legacy')],
        string="Payment Status", compute='compute_payment_state')

    @api.depends('invoice_ids')
    def compute_payment_state(self):
        for line in self:
            payment_state = False
            if line.invoice_ids:
                account = self.env['account.move'].search([('id', 'in', line.invoice_ids.ids)],
                                                          order='write_date desc', limit=1)
                if account:
                    payment_state = account.payment_state

            line.payment_state = payment_state

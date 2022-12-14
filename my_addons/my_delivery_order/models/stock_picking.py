# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError

class MyStockPicking(models.Model):
    _inherit = "stock.picking"
    _description = "rewrite stock picking"

    payment_state = fields.Selection(selection=[
        ('not_paid', 'Not Paid'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
        ('partial', 'Partially Paid'),
        ('reversed', 'Reversed'),
        ('invoicing_legacy', 'Invoicing App Legacy')],
        string="Payment Status", related='sale_id.payment_state')

    # @api.depends('sale_id','sale_id.invoice_ids')
    # def _compute_payment_state(self):
    #     for line in self:
    #         payment_state = False
    #         if line.sale_id:
    #             account = self.env['account.move'].search([('id', 'in', line.sale_id.invoice_ids.ids)],
    #                                                       order='write_date desc', limit=1)
    #             if account:
    #                 payment_state = account.payment_state
    #         line.payment_state = payment_state    

    def action_verify(self):
        """通知仓库可以进行发货了 """
        try:
            category_obj = self.env['ir.module.category'].search([('name','=','Inventory')],limit=1)
            category_id = category_obj.id
            group_obj = self.env['res.groups'].search([("category_id", "=", category_id),('name','=','User')], limit=1)
            print(group_obj.users.user_ids)
            # for inventory_user_id in group_obj.users.user_ids:
            #     self._send_sys_message(inventory_user_id, "请及时准备发货！")
            partner_ids = [user.partner_id.id for user in group_obj.users.user_ids]
            print(partner_ids)
            self.message_notify(
                body="<p>You have received a notification</p>",      # f"Hello，please prepare to delivery goods of {self.name}",
                subject=_('Message are pending moderation'),
                partner_ids=partner_ids,
                subtype_xmlid='mail.mt_comment',
                email_layout_xmlid='mail.mail_notification_light',
            )
        except Exception as e:
            print(f"消息发送失败，失败原因为：{e}")

    def button_validate(self):
        """重写验证方法 gaos add this 2022.12.20 """
        for line in self:
            if line.payment_state not in ["paid","partial"]:
                raise UserError("The source document is not paid. This order cannot be delivered. ")
        return super(MyStockPicking, self).button_validate()

    def _send_sys_message(self, user, message):
        """通过OdooBot给指定用户发送消息

        :param user: 'res.users' 对象
        :param message: str, 消息内容
        """
        # 获取OdooBot的partner_id
        odoobot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
        # 获取OdooBot和用户的聊天频道
        channel = self.env['mail.channel'].with_user(user.id).search(
            [('channel_type', '=', 'chat'), ('channel_partner_ids', 'in', [odoobot_id])], limit=1)
        # 不存在则初始化聊天频道
        if not channel:
            user.odoobot_state = 'not_initialized'
            channel = self.env['mail.channel'].init_odoobot()

        # 发送消息
        channel.with_context(mail_create_nosubscribe=True).message_post(
            subject="Delivery reminder",
            body=message, 
            message_type='notification', 
            subtype_xmlid='mail.mt_comment')
        
        
# -*- coding: utf-8 -*-
# from odoo import http


# class MyDeliveryOrder(http.Controller):
#     @http.route('/my_delivery_order/my_delivery_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_delivery_order/my_delivery_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_delivery_order.listing', {
#             'root': '/my_delivery_order/my_delivery_order',
#             'objects': http.request.env['my_delivery_order.my_delivery_order'].search([]),
#         })

#     @http.route('/my_delivery_order/my_delivery_order/objects/<model("my_delivery_order.my_delivery_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_delivery_order.object', {
#             'object': obj
#         })

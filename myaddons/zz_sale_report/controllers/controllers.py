# -*- coding: utf-8 -*-
# from odoo import http


# class ZzSaleReport(http.Controller):
#     @http.route('/zz_sale_report/zz_sale_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zz_sale_report/zz_sale_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zz_sale_report.listing', {
#             'root': '/zz_sale_report/zz_sale_report',
#             'objects': http.request.env['zz_sale_report.zz_sale_report'].search([]),
#         })

#     @http.route('/zz_sale_report/zz_sale_report/objects/<model("zz_sale_report.zz_sale_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zz_sale_report.object', {
#             'object': obj
#         })

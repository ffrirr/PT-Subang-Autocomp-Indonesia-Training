# -*- coding: utf-8 -*-
# from odoo import http


# class RealEstateUser(http.Controller):
#     @http.route('/real_estate_user/real_estate_user', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_user/real_estate_user/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_user.listing', {
#             'root': '/real_estate_user/real_estate_user',
#             'objects': http.request.env['real_estate_user.real_estate_user'].search([]),
#         })

#     @http.route('/real_estate_user/real_estate_user/objects/<model("real_estate_user.real_estate_user"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_user.object', {
#             'object': obj
#         })

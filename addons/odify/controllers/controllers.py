# -*- coding: utf-8 -*-
from odoo import http

class Odify(http.Controller):
     @http.route('/odify', auth="user",type='http', website=True)
     def index(self, **kw):
        test = http.request.env['product.template'].search([], order = 'create_date desc')
        test2 = http.request.env['product.template'].search_read([], ['name'])
        print(test)
        print(test2)
        return http.request.render(
                     'odify.odify', {'products': test[0:3]}
                         )


#     @http.route('/odify/odify/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odify.listing', {
#             'root': '/odify/odify',
#             'objects': http.request.env['odify.odify'].search([]),
#         })

#     @http.route('/odify/odify/objects/<model("odify.odify"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odify.object', {
#             'object': obj
#         })
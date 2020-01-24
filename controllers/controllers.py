# -*- coding: utf-8 -*-
from odoo import http

# class OdooCursos(http.Controller):
#     @http.route('/odoo_formacion/odoo_formacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_formacion/odoo_formacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_formacion.listing', {
#             'root': '/odoo_formacion/odoo_formacion',
#             'objects': http.request.env['odoo_formacion.odoo_formacion'].search([]),
#         })

#     @http.route('/odoo_formacion/odoo_formacion/objects/<model("odoo_formacion.odoo_formacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_formacion.object', {
#             'object': obj
#         })
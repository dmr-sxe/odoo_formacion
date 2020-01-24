# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError


class sesion(models.Model):
    _name = 'odoo_formacion.sesion' #IMPORTANTE é o nome da táboa
    _description = "Sesións dos cursos"

    name = fields.Char(required=True, string="Nome da Sesión")  # IMPORTANTE o campo ten que chamarse name
    data_sesion = fields.Datetime(string="Data da Sesión", default=lambda self: fields.Datetime.now())
    duracion = fields.Float(digits=(6, 2), string="Duración en horas", default=2)
    asentos = fields.Integer(string="Número de asentos")
    curso_id = fields.Many2one('odoo_formacion.curso', ondelete='cascade', required=True, string="Título do Curso")
    asistentes_ids = fields.Many2many('res.partner', relation='odoo_formacion_relacion_sesion_res_partner',
                                      column1='sesion_id', column2='asistente_id',
                                      ondelete='set null')  # Para definir nos a táboa relación, senón podería ser
    pais = fields.Many2one('res.country', string="País",
                           default=lambda self: self.env['res.country'].search([('code', '=', 'ES')], limit=1))
    enderezo = fields.Text(string="Enderezo")
    localidade = fields.Char(string="Localidade", size=40)
    codigo_postal = fields.Char(size=5, string="Código Postal")
    provincia = fields.Many2one('res.country.state', string="Provincia", domain="[('country_id','=',pais)]",
                                default=lambda self: self.env['res.country.state'].search(
                                    [('name', '=', 'A Coruña (La Coruña)')], limit=1))

    @api.constrains('duracion')
    def _constrain_duracion_sesion(self):
        for rexistro in self:
            if rexistro.duracion < 1 or rexistro.duracion > 4:
                raise ValidationError(
                    'A duración da %s ten que ser entre 1 e 4 horas' % rexistro.name)

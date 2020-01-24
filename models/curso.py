# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class curso (models.Model):
    _name="odoo_formacion.curso" # Será o nome da táboa
    _description = "Xestión de cursos"
    _sql_constraints = [('nome unico', 'unique(name)', 'Non se pode repetir o nome'),('relatores_distintos', 'CHECK(relator1_id != relator2_id)', 'Non se pode repetir o relator')]

    name = fields.Char(compute="_data_e_titulo", store=True)
    titulo = fields.Char(required=True,size=20,string="Titulo do curso",default="noname")
    descripcion = fields.Text(string="Descripción do curso") # string é a etiqueta do campo
    cartel = fields.Binary(string='Cartel')
    moeda_euro_id = fields.Many2one('res.currency',default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],limit=1))
    material_en_euros = fields.Monetary("Gasto en material", 'moeda_euro_id',default=0)
    docencia_en_euros = fields.Monetary("Gasto en docencia", 'moeda_euro_id',default=0)
    orzamento_total = fields.Monetary("Gasto total", 'moeda_euro_id', compute="_orzamento", store=True)
    autorizado = fields.Boolean(string="¿Curso Autorizado?", default=True)
    data_inicio = fields.Date(string="Data Inicio", required=True, default=lambda self: fields.Date.today())
    data_fin = fields.Date(string="Data Fin", required=True, default=lambda self: fields.Date.today())
    relator1_id = fields.Many2one('res.partner', ondelete='set null', index=True, string="Relator 1")
    relator2_id = fields.Many2one('res.partner', ondelete='set null', index=True, string="Relator 2")

    sesion_ids = fields.One2many('odoo_formacion.sesion', 'curso_id', 'sesion')  # Os campos One2many Non se almacena na BD

    @api.depends('titulo', 'data_inicio')
    def _data_e_titulo(self):
        for rexistro in self:
            if rexistro.titulo and rexistro.data_inicio:
                rexistro.name = rexistro.data_inicio.strftime("%d%m%Y") + "-" +str(rexistro.titulo)

    @api.depends('docencia_en_euros','material_en_euros')
    def _orzamento(self):
        for rexistro in self:
            rexistro.orzamento_total = float(rexistro.material_en_euros) + float(rexistro.docencia_en_euros)


    @api.constrains('data_inicio', 'data_fin')  # Ao usar constrains temos que importar a libreria ValidationError
    def _constrain_data(self):
       for rexistro in self:
           if rexistro.data_inicio < fields.Date.today() or rexistro.data_fin < fields.Date.today():
               raise ValidationError(
                  'As datas teñen que ser maiores a %s ' % fields.Date.today().strftime("%d do %m do %Y"))
           if rexistro.data_inicio > rexistro.data_fin:
                raise ValidationError('A data fin ten que ser maior que a data inicio ')
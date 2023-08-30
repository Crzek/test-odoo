from odoo import models, fields


class Contact_irh(models.Model):  # Corrección en el nombre del modelo
    _inherit = 'res.partner'

    age = fields.Integer(string="Edad")
    product_ids = fields.One2many(
        comodel_name='product.product',
        inverse_name='contact_id',
        string="Productos"
    )

class Stock_irh(models.Model):  # Corrección en el nombre del modelo
    _inherit = 'product.product'

    contact_id = fields.Many2one(
        comodel_name='res.partner',
        inverse_name='product_ids',
        string="Contacto"
    )
    box_ids = fields.Many2many(
        comodel_name='to.box',
        relation='box_product_rel',  # Cambiado para evitar conflictos de nombres
        column1='product_id',
        column2='box_id',
        string='Cajas Asociadas'
    )


from odoo import models, fields


class Contact_irh(models.Model):
    # hereda de contacto y productos (stock)
    _inherit = ['res.partner']

    # campos
    age = fields.Integer(string="Edad")
    products = fields.One2many(
        comodel_name='stock.picking',  # tabla a la que se relaciona
        inverse_name='contact_id',  # campo de la tabla relacionada
        string="Productos"  # nombre del campo
    )


class Stock_irh(models.Model):
    _inherit = ['stock.picking']

    contact_id = fields.Many2one(
        comodel_name='res.partner',  # tabla a la que se relaciona
        string="Contacto"  # nombre del campo
    )

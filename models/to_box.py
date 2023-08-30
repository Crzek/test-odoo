from odoo import models, fields, api


class Box(models.Model):
    _name = 'to.box'
    _description = 'Cajas de la empresa'

    name = fields.Selection(
        string="Nombre",
        selection=[
            ('standard', 'Standard'),
            ('marcas', 'Marcas'),
            ('decorada', 'Decorada')
        ],
        default='standard'  # Debes coincidir con el valor del primer elemento en la selección
    )
    type_id = fields.Selection(
        string="Tipo de caja",
        selection=[
            ('fina', 'Capa fina'),
            ('normal', 'Capa normal'),
            ('doble', 'Capa doble')
        ],
        default='normal'  # Debes coincidir con el valor del primer elemento en la selección
    )
    provider_id = fields.Many2one(
        comodel_name='res.partner',
        string="Proveedor"
    )
    product_ids = fields.Many2many(
        comodel_name='product.product',
        relation='box_product_rel',  # Cambiado para evitar conflictos de nombres
        column1='box_id',
        column2='product_id',
        string='Productos Asociados'
    )

    # def _compute_display_name(self):
    #     for box in self:
    #         box.display_name = box.name + '_' + str(box.id)
    #
    # display_name = fields.Char(compute='_compute_display_name')

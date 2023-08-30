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
        default='Standard'

    )
    type_id = fields.Selection(
        string="Tipo de caja",
        selection=[
            ('fina', 'Capa fina'),
            ('normal', 'Capa normal'),
            ('doble', 'Capa doble')
        ],
        default='Capa normal'
    )
    provider_id = fields.Many2one(
        comodel_name='res.partner',
        string="Proveedor"
    )
    product_ids = fields.Many2one(
        comodel_name='product.product',
        string="Producto"
    )

    # def _compute_display_name(self):
    #     for box in self:
    #         box.display_name = box.name + '_' + str(box.id)
    #
    # display_name = fields.Char(compute='_compute_display_name')

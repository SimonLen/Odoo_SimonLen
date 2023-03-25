import random

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(
        string='Test',
        default=lambda self: random.randint(1, 999),
        readonly=True,
        states={'draft': [('readonly', False)]}
    )

    @api.onchange('order_line', 'date_order')
    def _onchange_quotation(self):
        if self.test:
            self.test = f'{self.amount_total} - {self.date_order}'

    @api.onchange('test')
    def _onchange_test(self):
        if self.test and len(self.test) > 50:
            raise models.ValidationError(
                'Длина текста должна быть меньше 50 символов!'
            )

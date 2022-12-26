from odoo import models, fields


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    total_unit_amount = fields.Float(default=0.0)

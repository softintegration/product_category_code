# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductCategory(models.Model):
    _inherit = "product.category"

    code = fields.Char('Code',required=True)

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The code of the category must be unique !')
    ]
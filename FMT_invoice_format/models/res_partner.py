# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char()


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    arabic_name = fields.Char()

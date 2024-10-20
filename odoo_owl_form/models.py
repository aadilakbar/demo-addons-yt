# -*- coding: utf-8 -*-

from odoo import fields, models


class OdooOwlDemo(models.Model):
    _name = 'odoo.owl.demo'

    name = fields.Char(string='Name')

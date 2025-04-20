# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    custom_app_favicon = fields.Binary(
        string="App Favicon",
        help="Favicon used in backend",
    )

    def write(self, vals):
        res = super(ResCompany, self).write(vals)
        if 'custom_app_favicon' in vals:
            self.env['ir.attachment'].search([
                ('res_model', '=', 'res.company'),
                ('res_field', '=', 'custom_app_favicon'),
                ('res_id', '=', 0)
            ]).unlink()

            self.env['ir.attachment'].create({
                'name': 'Favicon',
                'res_model': 'res.company',
                'res_field': 'custom_app_favicon',
                'res_id': 0,
                'mimetype': 'image/x-icon',
                'datas': self.custom_app_favicon
            })
        return res

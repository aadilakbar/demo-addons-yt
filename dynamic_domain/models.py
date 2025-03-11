# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SalesTeam(models.Model):
    _inherit = 'crm.team'

    sale_partner_ids = fields.Many2many('res.partner', 'crm_team_sale_partners_rel', 'team_id', 'partner_id', 'Allowed Customers')


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    additional_team_id = fields.Many2one('crm.team', 'Sales Team')
    sales_team_domain = fields.Binary(string='sales team domain', compute='_compute_additional_sales_team_domain')

    @api.depends('partner_id')
    def _compute_additional_sales_team_domain(self):
        for order in self:
            if order.partner_id:
                order.sales_team_domain = [('sale_partner_ids', 'in', [order.partner_id.id])]
            else:
                order.sales_team_domain = [('id', '=', -1)]

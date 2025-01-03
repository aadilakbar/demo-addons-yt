from odoo import fields, models


class CrmLeadConfirmWiz(models.TransientModel):
    _name = 'crm.lead.confirm.wiz'

    lead_ids = fields.Many2many('crm.lead', string='Select Opportunity')

    def button_confirm(self):
        for lead in self.lead_ids:
            lead.action_set_won_rainbowman()

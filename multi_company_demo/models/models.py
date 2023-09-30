from odoo import fields, models


class CompanyDependentData(models.Model):
    _name = 'company.dependent.data'
    _description = 'Company Dependent Data'
    _rec_name = 'product_id'
    _check_company_auto = True

    # domain -> [('company_id', '=', False), ('company_id', 'in', 'company_ids')]
    # company_ids = user selected active company ids

    product_id = fields.Many2one('product.product', 'Product')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    product_status = fields.Char('Product Status', company_dependent=True)

    product_status_2 = fields.Char('Product Status')
    company_id_2 = fields.Many2one('res.company', 'Company')

    def get_product_status(self):
        self.product_status_2 = self.with_company(self.company_id_2).product_status

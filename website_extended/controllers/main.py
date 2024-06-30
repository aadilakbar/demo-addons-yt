from odoo import http
from odoo.http import request


class WebsiteCustomController(http.Controller):

    @http.route('/custom_page', type='http', auth='public', website=True)
    def custom_page(self, **kwargs):
        return request.render('website_extended.custom_page_template')

    @http.route('/custom_page/button_action', type='http', auth='public', website=True)
    def button_action(self, **kwargs):
        return request.redirect('/contactus')



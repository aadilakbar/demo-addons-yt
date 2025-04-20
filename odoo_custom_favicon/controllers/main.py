import base64
from odoo import http
from odoo.http import request, Response


class CustomFaviconController(http.Controller):

    @http.route('/web/static/img/app_favicon.ico', type='http', auth='public')
    def favicon(self, **kwargs):
        attachment = request.env['ir.attachment'].search([
            ('res_model', '=', 'res.company'),
            ('res_field', '=', 'custom_app_favicon'),
            ('res_id', '=', 0)
        ], limit=1)

        if attachment and attachment.datas:
            img_date = base64.b64decode(attachment.datas)
            return Response(
                img_date,
                content_type='image/x-icon',
                headers={'Cache-Control': f'public, max-age={http.STATIC_CACHE}'}
            )
        return request.redirect('/web/static/img/favicon.ico', code=301)

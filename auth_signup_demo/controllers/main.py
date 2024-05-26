from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class AuthSignupHomeInherit(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        qcontext = super(AuthSignupHomeInherit, self).get_auth_signup_qcontext()
        qcontext.update({k: v for (k, v) in request.params.items() if k in ['mobile', 'phone']})
        return qcontext

    def _prepare_signup_values(self, qcontext):
        values = super(AuthSignupHomeInherit, self)._prepare_signup_values(qcontext)
        values.update({key: qcontext.get(key) for key in ('mobile', 'phone')})
        return values

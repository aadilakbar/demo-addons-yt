from odoo import fields, models
from odoo.exceptions import UserError

import xlrd
import tempfile
import binascii


class ContactImportWiz(models.TransientModel):
    _name = 'contact.import.wiz'

    import_file = fields.Binary('Import File')
    filename = fields.Char('File Name')

    def button_import_xlsx_contacts(self):
        try:
            fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
            fp.write(binascii.a2b_base64(self.import_file))
            fp.seek(0)
            fp.close
        except:
            raise UserError("Invalid File!")

        workbook = xlrd.open_workbook(fp.name, on_demand=True)
        sheet = workbook.sheet_by_index(0)

        if sheet.ncols == 0:
            return

        first_row = []
        for col in range(sheet.ncols):
            first_row.append(sheet.cell_value(0, col))

        import_lines = []
        for row in range(1, sheet.nrows):
            line = {}
            for col in range(sheet.ncols):
                line[first_row[col]] = sheet.cell_value(row, col)
            import_lines.append(line)

        print(import_lines)

        partner_ids = []
        for import_line in import_lines:
            partner_ids.append(self.env['res.partner'].create({
                'name': import_line.get('Name'),
                'function': import_line.get('Job Position'),
                'phone': import_line.get('Phone'),
                'mobile': import_line.get('Mobile'),
                'email': import_line.get('Email'),
                'vat': import_line.get('Tax ID'),
                'website': import_line.get('Website'),
                'street': import_line.get('Street'),
            }).id)

        action = self.env['ir.actions.actions']._for_xml_id('contacts.action_contacts')
        action['domain'] = [('id', 'in', partner_ids)]
        return action

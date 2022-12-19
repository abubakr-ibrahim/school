from odoo import model

class(models.Model):
    _name="subject.subject"

    name = fields.Char('Name')
    parent_name = fields.Char("subject Name")

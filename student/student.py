from odoo import model

class(models.Model):
    _name="student.student"
    
    name = fields.Char('Name')
    parent_name = fields.Char("Parent Name")

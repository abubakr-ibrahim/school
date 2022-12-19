from odoo import model

class(models.Model):
    _name="student.student"
    
    name = fields.Char('Name')
    email = fields.Char("Email")
    phone = fields.Char("Phone Number")

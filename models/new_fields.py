from odoo import fields , models

class New_Fields(models.Model):
    _inherit = "res.partner"
   
    # create and assign fields 
    social_security = fields.Char(string = "SSNIT")
    digital_address = fields.Char(string = "Digital Address")
    

    
    
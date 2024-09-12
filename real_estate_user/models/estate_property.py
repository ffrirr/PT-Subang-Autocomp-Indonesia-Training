from odoo import _, api, fields, models

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    buyer_id = fields.Many2one(comodel_name='res.partner', string='Buyer')
    seller_id = fields.Many2one(comodel_name='res.users', string='Seller', 
                                default=lambda self: self.env.user)
    
    

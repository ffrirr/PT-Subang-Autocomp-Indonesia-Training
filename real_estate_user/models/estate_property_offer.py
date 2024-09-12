from odoo import _, api, fields, models
from odoo.exceptions import UserError



class EstatePropertyOffer(models.Model):
    _inherit = 'estate.property.offer'

    def action_accepted(self):
        self.write({'state':'accepted'})
        return self.mapped('property_id').write({'state':'offer_accepted',
                                       'selling_price':self.price,
                                       'buyer_id':self.partner_id})
    
    def write(self, vals):
        if 'accepted' in self.mapped('poperty_id.offer_ids.state'):
            raise UserError('Anda tidak dapat mengaccept offer lagi, karena sudah ada offer yang diterima')
        return super().write(vals)

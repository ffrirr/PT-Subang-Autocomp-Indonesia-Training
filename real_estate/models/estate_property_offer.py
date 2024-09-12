from odoo import _, api, fields, models
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(string='Price')
    validity = fields.Integer(string='Validity(days)')
    date_deadline = fields.Date(string='Deadline', compute="_compute_date_deadline")
    partner_id= fields.Many2one(comodel_name='res.partner', string='Partner')
    property_id = fields.Many2one(comodel_name='estate.property', string='Property')
    state = fields.Selection(string='Status', selection=[('accepted', 'Accepted'), ('refused', 'Refused'),])
    

    @api.depends('validity')
    def _compute_date_deadline(self):
        for offer in self:
            date= offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)
    
    @api.model
    def create(self, vals):
        if vals.get('price') and vals.get('property_id'):
            property=self.env['estate.property'].browse(vals['property_id'])
            property.write({'state':'offer_received'})
        return super().create(vals)
    
    def action_accepted(self):
        self.write({'state':'accepted'})
        return self.mapped('property_id').write({'state':'offer_accepted',
                                       'selling_price':self.price})
    
    def action_refused(self):
        return self.write({'state':'refused'})
    

    
    
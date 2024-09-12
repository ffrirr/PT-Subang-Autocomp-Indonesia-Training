from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.modules.module import get_module_resource
import base64



class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    # @api.model
    # def _default_image(self):
    #     image_path = get_module_resource('lunch', 'static/img', 'people.png')
    #     return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(string='Name', required=True )
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bed rooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation', 
                                          selection=[('n', 'N'),
                                                    ('s', 'S'),
                                                    ('e', 'E'),
                                                    ('w', 'W'),])
    estate_property_type_id = fields.Many2one(comodel_name='estate.property.type',
                                                string='Property Type')
    tag_ids = fields.Many2many(comodel_name='estate.property.tag', string='Tags')
    total_area = fields.Integer(string='Total Area', compute="_compute_total_area")
    state = fields.Selection(string='Status', selection=[('new', 'New'), 
                                                         ('offer_received', 'Offer Received'),
                                                         ('offer_accepted', 'Offer Accepted'),
                                                         ('sold', 'Sold'),
                                                         ('cancel', 'Cancel'),],
                                                         default='new')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offers')
    image_1920 = fields.Image()
    
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for prop in self:
            prop.total_area = prop.living_area + prop.garden_area
    
    @api.onchange('garage')
    def onchange_garage(self):
        for prop in self:
            if prop.garage:
                prop.garden=True
            else:
                prop.garden=False
    
    @api.constrains('garden','garden_area')
    def _check_garden(self):
        for prop in self:
            if prop.garden_area and not prop.garden:
                raise UserError('Anda tidak bisa mempunyai daerah kebun jika tidak punya kebun')
            
    def action_sold(self):
        for prop in self:
            prop.write({'state':'sold'})

    def action_cancelled(self):
        for prop in self:
            prop.write({'state':'cancelled'})
            
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


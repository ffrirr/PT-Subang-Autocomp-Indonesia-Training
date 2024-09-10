from odoo import _, api, fields, models



class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'


    name = fields.Char(string='Name')
    property_ids = fields.One2many(comodel_name='estate.property', 
                                   inverse_name='estate_property_type_id', 
                                   string='Estate Properties')
    
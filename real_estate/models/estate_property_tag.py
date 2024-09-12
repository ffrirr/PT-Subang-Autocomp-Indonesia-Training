from random import randint

from odoo import fields, models



class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'


    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string='Color Index', default=_get_default_color)
    

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
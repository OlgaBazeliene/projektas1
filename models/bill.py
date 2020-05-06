from odoo import models, fields, api


class Bill(models.Model):
    _name = 'projektas1.bill'
    _description = "Sąskaitos"

    number = fields.Char(string="Number", required=True)
    client_id = fields.Many2one('res.partner', string="Client")
    projektas_id = fields.Many2one('projektas1.project', string="Project")


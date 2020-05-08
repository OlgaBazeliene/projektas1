from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    manager = fields.Boolean(string="Manager")
    project_ids = fields.Many2many('projektas1.project', string="Projects", readonly=True)
from odoo import models, fields, api


class Work(models.Model):
    _name = 'projektas1.work'

    name = fields.Char(string="Work name", required=True)
    projektas_id = fields.Many2one('projektas1.project', string="Project")
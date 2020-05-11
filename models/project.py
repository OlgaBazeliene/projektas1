from odoo import models, fields, api


class Project(models.Model):
    _name = 'projektas1.project'

    name = fields.Char(string="Project name", required=True)
    start_date = fields.Date(string="Start date", default=fields.Date.today)
    end_date = fields.Date(string="End date")
    client_id = fields.Many2one('res.partner', string="Client")
    employees_ids = fields.Many2many('hr.employee', string="Empoyees")
    works_ids = fields.One2many('projektas1.work', 'projektas_id', string="Works")
    vadovas_id = fields.Many2one('hr.employee', string="Manager")

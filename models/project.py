from odoo import models, fields, api


class Project(models.Model):
    _name = 'projektas1.project'

    name = fields.Char(string="Project name", required=True)
    start_date = fields.Date(string="Start date", default=fields.Date.today)
    end_date = fields.Date(string="End date")

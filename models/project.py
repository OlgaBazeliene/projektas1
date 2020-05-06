from odoo import models, fields, api


class Project(models.Model):
    _name = 'projektas1.project'

    name = fields.Char(string="Projekto pavadinimas", required=True)
    start_date = fields.Date(string="Pradžios data", default=fields.Date.today)
    end_date = fields.Date(string="Pabaigos data")
    client_id = fields.Many2one('res.partner', string="Klientas")
    employees_ids = fields.Many2many('hr.employee', string="Darbuotojai")
    works_ids = fields.One2many('projektas1.work', 'projektas_id', string="Darbai")
    vadovas_id = fields.Many2one('hr.employee', string="Vadovas")

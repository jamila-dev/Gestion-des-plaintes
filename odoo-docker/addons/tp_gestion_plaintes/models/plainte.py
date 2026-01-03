from odoo import models, fields

class TpPlainte(models.Model):
    _name = 'tp.plainte'
    _description = 'Plainte Interne'

    name = fields.Char(string='Sujet', required=True)
    description = fields.Text(string='Description')
    employee_name = fields.Char(string='Employé')
    date_plainte = fields.Date(string='Date', default=fields.Date.context_today)
    state = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('traite', 'Traité'),
        ('rejete', 'Rejeté')
    ], string='Statut', default='nouveau')

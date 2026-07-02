from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    disease = fields.Char(string='Disease')
    doctor = fields.Char(string='Doctor Name')
    appointment_date = fields.Date(string='Appointment Date')
    is_available = fields.Boolean(string='Available', default=True)
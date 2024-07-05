from odoo import models, fields, api
from datetime import date

class Biodata(models.Model):
    _name = 'latihan.biodata'
    _description = 'Biodata'

    name = fields.Char(string='Nama')
    fullname = fields.Char(string='Nama Lengkap')
    birthdate = fields.Date(string='Tanggal Lahir')
    age = fields.Integer(string='Umur', compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('Laki-laki', 'Perempuan')], string='Jenis Kelamin')
    child_count = fields.Integer(string='Anak ke-')
    photo = fields.Binary(string='Photo')

    education_sd = fields.Boolean(string='SD')
    education_smp = fields.Boolean(string='SMP')
    education_sltp = fields.Boolean(string='SLTP')
    education_sma = fields.Boolean(string='SMA')
    education_smk = fields.Boolean(string='SMK')
    education_smu = fields.Boolean(string='SMU')
    education_slta = fields.Boolean(string='SLTA')
    education_college = fields.Boolean(string='Kuliah')

    @api.depends('birthdate')
    def _compute_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = date.today().year - rec.birthdate.year
            else:
                rec.age = 0

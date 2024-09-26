from odoo import models, fields

class Carrera(models.Model):
    _name = 'tutorias.carrera'
    _description = 'Carrera'

    nombre_carrera = fields.Char(string='Nombre Carrera', required=True)
    
    def __str__(self):
        return self.nombre_carrera

class Ciclo(models.Model):
    _name = 'tutorias.ciclo'
    _description = 'Ciclo'

    nombre_ciclo = fields.Char(string='Nombre Ciclo', required=True)
    
    def __str__(self):
        return self.nombre_ciclo

class Docente(models.Model):
    _name = 'tutorias.docente'
    _description = 'Docente'

    id_user = fields.Many2one('res.users', string='Usuario', required=True)
    
    def __str__(self):
        return f'{self.id_user.name}'

class Estudiante(models.Model):
    _name = 'tutorias.estudiante'
    _description = 'Estudiante'

    id_user = fields.Many2one('res.users', string='Usuario', required=True)
    
    def __str__(self):
        return f'{self.id_user.name}'

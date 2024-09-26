{
    'name': 'Tutorias',
    'version': '1.0',
    'summary': 'Gestión de carreras, ciclos, docentes y estudiantes en tutorías',
    'author': 'Juan Jose Benites Coronel',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/tutorias_security.xml',
        # Incluir archivos de vistas y otros datos si los añades más adelante
    ],
    'installable': True,
}
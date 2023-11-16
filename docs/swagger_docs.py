# swagger_docs.py

bulk_create_doc = {
    'tags': ['Bulk'],
    'description': 'Crear un bulk.',
    'parameters': [
        {
            'name': 'data',
            'description': 'Datos del bulk',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'int',
                        'description': 'Estado del bulk'
                    },
                    'name': {
                        'type': 'str',
                        'description': 'Nombre del bulk'
                    }
                },
                'required': ['status', 'name']
            }
        }
    ],
    'responses': {
        '204': {
            'description': 'Sin contenido'
        },
        '409': {
            'description': 'Error - ID del bulk ya existe',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Mensaje de error'
                    }
                }
            }
        },
        '500': {
            'description': 'Error interno del servidor',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Mensaje de error'
                    }
                }
            }
        }
    }
}

get_bulk_status_doc = {
    'tags': ['Bulk'],
    'description': 'Obtener bulks por estado.',
    'parameters': [
        {
            'name': 'status',
            'description': 'Estado del bulk',
            'in': 'path',
            'type': 'string'
        }
    ],
    'responses': {
        '200': {
            'description': 'Éxito',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object'
                    # Especifica aquí la estructura del objeto de respuesta si es necesario
                }
            }
        },
        '404': {
            'description': 'No encontrado - Bulks no encontrados',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Mensaje de error'
                    }
                }
            }
        },
        '500': {
            'description': 'Error interno del servidor',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Mensaje de error'
                    }
                }
            }
        }
    }
}

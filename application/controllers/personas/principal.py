import web
import config as config


class Principal:
    def __init__(self):
        pass

    def GET(self):  
        personas = config.model_personas.select_personas().list() # Selecciona todos los registros de personas
        return config.render.principal(personas) # Envia todos los registros y renderiza index.html

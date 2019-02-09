import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre):  
        persona = config.model_personas.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.view(persona) # Envia el registro y renderiza view.html

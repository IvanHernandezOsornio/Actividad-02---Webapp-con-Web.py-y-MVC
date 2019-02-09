import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre): 
        personas = config.model_personas.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.delete(personas) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre = formulario['nombre'] # Obtine el nombre almacenado en el formulario
        config.model_personas.delete_persona(nombre) # Borra el registro del nombre seleccionado
        raise web.seeother('/principal') # Redirecciona a raiz
        
        
 
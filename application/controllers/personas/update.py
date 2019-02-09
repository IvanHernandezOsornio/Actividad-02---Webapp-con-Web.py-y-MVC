import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        persona = config.model_personas.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(persona) # Envia el registro y renderiza update.html
    
       
    
    
    def POST(self, email):
        formulario = web.input() # almacena los datos del formulario web
        nombre = formulario['nombre'] # almacena el nombre del input email
        email = formulario['email']
        direccion = formulario['direccion']
        genero = formulario['genero']        # almacena el email del input password
        config.model_personas.update_persona(nombre, email, direccion, genero) # actuliza los valores
        raise web.seeother('/principal') # redirecciona al index

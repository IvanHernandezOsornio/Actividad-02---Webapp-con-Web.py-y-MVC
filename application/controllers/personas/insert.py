import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # alamcena el nombre escrito en el input
        email = formulario['email']
        turno = formulario['turno']
        direccion = formulario['direccion']
        genero = formulario['genero']# almacena el email escrito en el input
        config.model_personas.insert_persona(nombre, email, turno, direccion, genero) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/principal') # redirecciona al index.html

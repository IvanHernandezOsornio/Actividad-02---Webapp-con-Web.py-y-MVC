import web
import config as config


class Insertp:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insertp() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre_prod = formulario['nombre_prod'] # alamcena el nombre escrito en el input
        marca = formulario['marca']
        existencias = formulario['existencias']
        descripcion = formulario['descripcion']
        costo = formulario['costo']# almacena el email escrito en el input
        config.model_productos.insert_productos(nombre_prod, marca, existencias, descripcion, costo) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/prod') # redirecciona al index.html

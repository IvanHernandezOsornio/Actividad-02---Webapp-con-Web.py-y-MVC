import web
import config as config


class Deletep:
    def __init__(self):
        pass

    def GET(self, nombre_prod): 
        productos = config.model_productos.select_nombre_prod(nombre_prod) # Selecciona el registro que coincida con nombre
        return config.render.deletep(productos) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre_prod):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre_prod = formulario['nombre_prod'] # Obtine el nombre almacenado en el formulario
        config.model_productos.delete_productos(nombre_prod) # Borra el registro del nombre seleccionado
        raise web.seeother('/prod') # Redirecciona a raiz
        
        
 
import web
import config as config


class Updatep:
    def __init__(self):
        pass
    
    def GET(self, nombre_prod): 
        productos = config.model_productos.select_nombre_prod(nombre_prod) # Selecciona el registro que coincida con nombre
        return config.render.updatep(productos) # Envia el registro y renderiza delete.html
    
    
    
    def POST(self, marca):
        formulario = web.input() # almacena los datos del formulario web
        nombre_prod = formulario['nombre_prod'] # almacena el nombre del input email
        marca = formulario['marca']
        existencias = formulario['existencias']        
        descripcion = formulario['descripcion']
        costo = formulario['costo']        # almacena el email del input password
        config.model_productos.update_productos(nombre_prod, marca, existencias, descripcion, costo) # actuliza los valores
        raise web.seeother('/prod') # redirecciona al index

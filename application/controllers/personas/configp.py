import web # importa la libreria web.py
import application.models.model_productos as model_personas # importa el modelo_personas 


render = web.template.render('application/views/personas/', base='master') # configura la ubicacion de las vistas

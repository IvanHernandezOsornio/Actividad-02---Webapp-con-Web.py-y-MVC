import web # importa la libreria web.py
import application.models.model_personas as model_personas # importa el modelo_personas 
import application.models.model_productos as model_productos # importa el modelo_personas 


render = web.template.render('application/views/personas/', base='master') # configura la ubicacion de las vistas

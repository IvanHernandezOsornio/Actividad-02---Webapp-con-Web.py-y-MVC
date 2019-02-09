import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla persornas
'''
def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_personas Error {}".format(e.args)
        print "Model select_personas Message {}".format(e.message)
        return None


'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre_prod(nombre_prod):
    try:
        return db.select('productos',where='nombre_prod=$nombre_prod', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre_prod Error {}".format(e.args)
        print "Model select_nombre_prod Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando nombre y email
'''
def insert_productos(nombre_prod, marca, existencias,descripcion, costo):
    try:
        return db.insert('productos', nombre_prod=nombre_prod,marca=marca,existencias=existencias,descripcion=descripcion,costo=costo) # inserta un registro en personas
    except Exception as e:
        print "Model insert_productos Error {}".format(e.args)
        print "Model insert_productos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_productos(nombre_prod):
    try:
        return db.delete('productos', where='nombre_prod=$nombre_prod',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_productos Error {}".format(e.args)
        print "Model delete_productos Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email, del nombre recibido
'''
def update_productos(nombre_prod, marca, existencias, descripcion, costo): # actualiza el email de personas que coincidan con el nombre
    try:
        return db.update('productos', 
            marca=marca,
            existencias=existencias,
            descripcion=descripcion,
            costo=costo, 
            where='nombre_prod=$nombre_prod',
            vars=locals())
    except Exception as e:
        print "Model update_productos Error {}".format(e.args)
        print "Model update_productos Message {}".format(e.message)
        return None
'''
Metodo para ver un registro que coincida con el nombre recibido
'''
def ver_productos(nombre_prod):
    try:
        return db.ver('productos', where='nombre_prod=$nombre_prod',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_productos Error {}".format(e.args)
        print "Model delete_productos Message {}".format(e.message)
        return None


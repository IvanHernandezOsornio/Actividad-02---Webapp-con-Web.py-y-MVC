import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla persornas
'''
def select_personas():
    try:
        return db.select('personas') # Selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_personas Error {}".format(e.args)
        print "Model select_personas Message {}".format(e.message)
        return None


'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre(nombre):
    try:
        return db.select('personas',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando nombre y email
'''
def insert_persona(nombre, email, turno, direccion, genero):
    try:
        return db.insert('personas', nombre=nombre,email=email,turno=turno,direccion=direccion,genero=genero) # inserta un registro en personas
    except Exception as e:
        print "Model insert_personas Error {}".format(e.args)
        print "Model insert_personas Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_persona(nombre):
    try:
        return db.delete('personas', where='nombre=$nombre',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_persona Error {}".format(e.args)
        print "Model delete_persona Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email, del nombre recibido
'''
def update_persona(nombre, email, direccion, genero): # actualiza el email de personas que coincidan con el nombre
    try:
        return db.update('personas', 
            email=email,            
            direccion=direccion,
            genero=genero, 
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_persona Error {}".format(e.args)
        print "Model update_persona Message {}".format(e.message)
        return None

'''
Metodo para ver un registro
'''
def ver_persona(nombre):
    try:
        return db.ver('personas', where='nombre=$nombre',vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_persona Error {}".format(e.args)
        print "Model delete_persona Message {}".format(e.message)
        return None

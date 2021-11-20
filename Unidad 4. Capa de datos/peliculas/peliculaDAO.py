from conexion import connect_mongo

# listar
def select_all(database, collection):
    con = connect_mongo()
    db = con[database]
    col = db[collection]
    docs = col.find()
    return docs

def select_by(database, collection, criteria):
    con = connect_mongo()
    db = con[database]
    col = db[collection]
    docs = col.find(criteria)
    return docs

# insertar
    def insert():
        pass
# actualizar
    def update():
        pass
# eliminar
    def delete():
        pass




from conexion import connect_mongo


# listar
def select_all(database, collection):
    con = connect_mongo()
    db = con[database]
    col = db[collection]

# insertar
# actualizar
# eliminar




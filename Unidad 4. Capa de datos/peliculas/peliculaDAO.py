from conexion import get_database
import pelicula
from bson.objectid import ObjectId

collection = 'pelicula'
# listar
def select_all():
    db = get_database()
    col = db[collection]
    docs = col.find()
    return docs

# insertar
def insert(pelicula):
    db = get_database()
    col = db[collection]
    id = col.insert_one(
        {
            "name": pelicula.name,
            "director": pelicula.director
        }
    ).inserted_id
    return print('Insertada la pelicula ' + str(id))

# actualizar
def update(id, pelicula):
    db = get_database()
    col = db[collection]
    # actualizar
    res = col.update_one(
        {
            '_id': ObjectId(id)
        },
        {
            '$set': {
                "name": pelicula.name,
                "director": pelicula.director
            }
        }
    )
    up = res.modified_count
    return print('Fue modificado '+str(up)+' documento')

def update_by_object(pelicula1, pelicula2):
    db = get_database()
    col = db[collection]
    # actualizar
    res = col.update_one(
        {
            'name': pelicula1.name,
            'director': pelicula1.director
        },
        {
            '$set': {
                "name": pelicula2.name,
                "director": pelicula2.director
            }
        }
    )
    up = res.modified_count
    return print('Fue modificado '+str(up)+' documento')

# eliminar
def delete(id):
    db = get_database()
    col = db[collection]
    res = col.delete_one(
        {
            '_id': ObjectId(id)
        }
    )
    cont = res.deleted_count
    return print("Eliminado "+str(cont)+ " Documento")




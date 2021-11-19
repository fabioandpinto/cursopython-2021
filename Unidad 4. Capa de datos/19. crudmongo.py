from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)

mydb = client['testStore']
collection = mydb['products']

# Agregar dato
# collection.insert_one({'name': 'keyboard', 'price': 34})

#Agregar varios datos
"""
producto1 = {'name': 'mouse', 'price': 78}
producto2 = {'name': 'desktop', 'price': 300}

collection.insert_many([producto1, producto2])
"""

# leer productos
"""
resultados = collection.find()
for r in resultados:
    print(r)

resultados = collection.find_one()
print(resultados)
"""

# eliminar productos
"""
collection.delete_one({'name':'keyboard'})
resultados = collection.find()
for r in resultados:
    print(r)
"""

# actualizar dato
"""
collection.update_one({'name': 'mouse'}, {"$set": {'name': 'vertical Mouse', 'model': 'g67p'}} )
collection.update_one({'name': 'vertical Mouse'}, {"$inc": {'price':30}} )
resultados = collection.find()
for r in resultados:
    print(r)
"""

#contar
print(collection.count_documents({}))
print(collection.find().count())
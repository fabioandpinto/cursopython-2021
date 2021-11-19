## Diccionarios
# coleccion de pares, formados por una clave y por un valor
"""
    {
        clave1 : valor
        ....
        ....

    }

No tiene orden
Puede contener elementos de distinto tipo
Son mutables - se pueden alterar
Las claves son únicas y no pueden repetirse en el mismo diccionario

"""
print(type({}))

dict1 = {'nombre': 'Cristobal', 'apellido': 'garcia', 'email': 'cgarcia@agrosavia.co'}
print(dict1)

dict2 = {'nombre_completo': {'primer_nombre': 'Cristobal', 'segundo_nombre': 'José'},
         'apellido': 'garcia',
         'email': 'cgarcia@agrosavia.co'}

print(dict2)

print(dict2.get('nombre_completo'))


## operaciones con diccionarios
# no modifican

print(len(dict1))
print('email' in dict1)
print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

## operaciones que modifican el diccionario
dict1['nombre'] = 'Fabio'
print(dict1)

dict_otro = { 'edad': 35 }
dict1.update(dict_otro)
print(dict1)

#pop
dict1.pop('edad')
print(dict1)

#popitem
dict1.popitem()
print(dict1)

#clear
dict2.clear()
print(dict2)



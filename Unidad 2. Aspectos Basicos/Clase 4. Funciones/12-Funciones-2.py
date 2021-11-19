## Segunda parte clase de funciones
# ambito para los argumentos - scope
# argumentos locales y argumentos globales

# funcion
lenguaje = "Python"
def bienvenida(nombre):
     #variable local - scope : funcion
    print('Bienvenido(a) a ' + lenguaje + ', ' + nombre)

bienvenida("Eliana")
print(lenguaje)

## Paso de argumentos por referencia
edades_colombia = [34 ,45 ,30 ,40 ]
edades_argentina = [6 ,45 ,30]

def añadir_edades(pais, edad):
    pais.append(edad)
    return 'añadida'

print(edades_argentina)
añadir_edades(edades_argentina, 78)
print(edades_argentina)

# Documentar funciones
# help

def añadir_edades(pais, edad):
    """
    Esta funcion añade elementos a una lista determinada
    Parametros
    pais: lista de paises
    edad: edad que deseo agregar
    return: mensaje de EXITO
    """
    pais.append(edad)
    return 'añadida'

help(añadir_edades)

## funciones como argumentos
def operacion( oper, a , b):
    return oper(a,b)
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
print(operacion(suma,2,3))





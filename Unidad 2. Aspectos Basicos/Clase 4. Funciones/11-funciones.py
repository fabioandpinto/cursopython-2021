# bloque con un nombre y de invocación recurrente
"""
def nombrefuncion(parametros):
    bloque código
    return objeto
"""
## Basico
def saludo():
    textoSaludo = '¡Hola!'
    return textoSaludo

print(type(saludo())) #Acceso al producto de la funcion
print(type(saludo)) ##Acceso a la definicion de la funcion
print(saludo()) #Imprimo el producto de la función

# Argumentos
def saludo(nombre):
    textoSaludo = '¡Hola ' + nombre + '!'
    return textoSaludo

print(saludo("Ana"))

# Tipos de argumentos
# argumentos posicionales -- se determinan por el orden en el que se cargan en la funcion
# argumentos nominales -- se determinan por el nombre que lleven en la funcion

# pitagoras ------- a = cateto abyacente , b = cateto opuesto
def pitagoras(aby,op):
    hipo = (aby**2+op**2)**(1/2)
    return hipo

print(pitagoras(2,3)) # posicional
print(pitagoras(op=3, aby=2)) #nominal

# Argumentos por defecto
def saludoCompleto(nombre, lenguaje = "Python"):
    textoSaludo = '¡Hola ' + nombre + '! Bienvenida al curso de ' + lenguaje
    return textoSaludo

print(saludoCompleto('Ana', 'Javascript'))

# Argumentos de lista
argumentos = ['Ana', 'Fortran']
print(saludoCompleto(*argumentos)) # desempaquetando la lista dentro de la función de manera posicional
print(saludoCompleto(lenguaje=argumentos[0], nombre=argumentos[1])) # desempaquetando la lista dentro de la función de manera posicional

# Argumento llave valor
argumentos = {
    'lenguaje': 'CSS',
    'nombre': 'Ana',
}
print(saludoCompleto(**argumentos))
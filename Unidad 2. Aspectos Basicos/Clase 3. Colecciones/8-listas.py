## Listas 
# coleccion ordenada de datos 
# listas son de tamaño dinámico - mutables
# Susceptibles de indexacion 

## Creacion de listas 
lista1 = [] # lista vacia variable inicializada en 0 
lista2 = [123, 'abc', 1.23, True, {}, lista1] ## Elementos de diverso tipo 

for i in lista2:
    print(i)

## Lista dentro de lista 
lista3 = ["Fabio", 30, ['abc', 'def']] # El primer elemento de una lista tiene index 0 
print(lista3[2][0])

## Lista de string 
strings = list('murcielago')
print(strings)

## Lista con un rango 
rango = list(range(-4,10))
print(rango)

# Slice Lista[i] o puedo indexar una lista embebida con Lista[i][j] (Matriz)
# Slice con rango L[i:j]
# El numero de elementos de una lista se halla con len(lista)

nuevalista = lista3 + strings
print(nuevalista)
print(strings*2) 

## ciclo ternario for in 
for x in range(-4,10): print(x)
print('u' in strings)

entrada = input("Ingrese la palabra: ")
if 'a' in entrada:
    print("La palabra tiene una a")






# Secuencia ordenada  []
# list ()
# como acceder a los elementos
# sublistas
#
# Operaciones con listas (Que no modifican la lista)
lista1 = [1,2,5,0,67,30]
# tamaño de la lista
print( len(lista1) )

# min y el maximo
print(min(lista1))
print(max(lista1 ))

#suma
suma = sum(lista1)
print(suma)

#validacion
print( 3 in lista1 )

#index
# devuelve la posición que ocupa el dato en la lista
print( lista1.index(0) )

#count
# devuelve las veces que el valor aparece en la lista
p = "pajaro"
lp = list(p)
print(lp)
print(lp.count('a'))

# all y any
# all es true si todos los elementos de la lista son true
# any nos devolverá true si algún elemento de la lista es true
print(all(lp))

### Operaciones con listas (que modifican la lista)
# concatenacion
l1 = list("pajaro")
l2 = list("carpintero")
l3 = []

l3 = l1 + l2
print(l3)

# append -> para añadir datos al final de la lista
l1.append('s')
print(l1)

# insert -> insertar un dato en la posición indice que le indique y va a desplazar todos los elementos
l1.insert(3, 'w')
print(l1)

# remove(dato) -> eliminar el primer elemento con el valor que le indique y desplaza todos los elementos sobrantes
print(l1)
l1.remove('w')
print(l1)

# pop(indice o los indices) -> elimina un elemento dado su indice
l2.pop(3)
print(l2)

l2.pop()
print(l2)

# sort -> ordenar la lista
lista1.sort()
l1.sort()
print(l1)

l1.reverse()
print(l1)



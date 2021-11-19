"""
Crear archivos
Escribir datos en un archivo
Leer un archivo
Borrar un archivo
"""

"""
## Crear y escribir
l = 'Eliana, Dimitri, Ana'

# - open(ruta, 'w') para escribir o 'r' para leer - fichero o archivo
# f = open(ruta, 'w')

# escribir --> f.write(texto)
f = open('nombre.txt', 'a')
f.write(l)
f.write("\nCristobal, Juan, Fabio ")



## leer
f = open('nombre.txt', 'r')
# read
r = f.read()
print(r)
"""

f = open('nombre.txt', 'r')
lineas = f.readlines()
f.close()
print(lineas)

import os
os.remove('nombre.txt')




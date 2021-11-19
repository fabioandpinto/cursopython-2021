## Tuplas
# coleccion ordenada
# puede contener elementos de distintos tipos
# no se pueden modificar - no pueden alterarse

# para representar colecciones con una estructura determinada
# vectores y matrices
"""


tupla1 = (1 , "dos", True)
print(type(tupla1))
print(tupla1)

vector1 = (1,2,3)
print(vector1)
"""

# Indexación
"""
matriz = ((1,2,3),(4,5,6))
print(matriz[0][0])
"""
A = [[1,2,3],[4,5,6]]
B = [[-1,0],[0,1],[1,1]]
# 2x3 3x2 ------- 2x2 (resultado)
C = [ [0,0] , [0,0] ]

for i in range(len(A)): # 0-1
  for j in range(len(B[0])): # 0-1
    for k in range(len(B)): # 0 - 2
      C[i][j] += A[i][k] * B[k][j]

print(C)






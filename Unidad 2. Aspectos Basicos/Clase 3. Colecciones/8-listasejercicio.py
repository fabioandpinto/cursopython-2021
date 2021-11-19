alfabeto1 = "abcdefghijklmnopqrstuvwxyz"
alfabeto = list(alfabeto1)

indexes = []
nuevoalfabeto = []
for i in range(len(alfabeto),1,-1):
  if i%3 == 0:
    alfabeto.pop(i-1)
print(alfabeto)


## for para iteracion 
# range: me crea un vector con una secuencia 

print(range(4))

for i in range(4):
    print(str(i))

for i in [1,2,3,4]:
    print(i)

for i in "murcielago":
    print(i)

#------------------------ ejercicio 
# tomar una palabra y desplegar el numero de letras que tiene por conteo 
palabra = "otorrino"

for i in range(len(palabra)):
    print(str(i) + " - " + palabra[i])

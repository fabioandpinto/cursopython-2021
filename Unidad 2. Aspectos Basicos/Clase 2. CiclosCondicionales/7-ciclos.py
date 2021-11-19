## While  
# while prueba:
#   pasos
# else 

#while True: 
    #print("¡Oprime ctrl-c para detenerme!")

x = "Murcielago"
while x: #Mientras que x no sea igual a "" 
    print(x, end = '\n')
    x = x[:-1]
print("Finalizacion del ciclo")

### 
x = float(input("Ingresa el numero hasta el que quieres contar"))
i = 0
while i <= x:
    print(str(i))
    i+=1

### 
opcion = 0 
while opcion != 5:
    print(" Menu:")
    print(" 1. Menu:")
    print(" 2. Menu:")
    print(" Oprime 5 para salir")
    opcion = int(input("Ingrese la opcion en el menu: "))
print("Has oprimido 5, adios")



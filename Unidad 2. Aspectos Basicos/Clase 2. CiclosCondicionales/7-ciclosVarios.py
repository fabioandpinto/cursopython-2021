"""
## instrucciones de control 
## break, continue y pass 

## Break - cerrar el bucle cuando se activa una condicion externa 

numero = 0 
for numero in range(10):
    if numero == 5:
        print("Llegaste al 5")
        break 
    print("El numero es " + str(numero))

# -------- 
cantidad = int(input("¿Cuantos televisores vas a comprar en el día sin iva?"))

for i in range(1,cantidad): 
    if i == 4:
        print("No se pueden llevar más de 3 artículos por referencia")
        break
    print("Televisor numero " + str(i) + " empacado")

# --------
## Continue - cuando se activa la condicion externa, permite omitir una parte del bucle
## Pero continuar 

## subiendo el elevador 



for piso in range(1,pisos): 
    if piso == 13:
        print("Mala suerte")
        continue
    print("Estamos en piso " + str(piso))
print("Llegamos a la cima")
"""
pisos = 18 
## pass - permite manejar una condicion sinque el bucle se vea afectado 
for piso in range(1,pisos): 
    if piso == 13:
        print("Mala suerte")
    if piso == 14:
        print("Piso 14 ya ")
    print("Estamos en piso " + str(piso))
print("Llegamos a la cima")

## Switch case 




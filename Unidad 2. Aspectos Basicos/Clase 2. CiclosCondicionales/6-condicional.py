## If, if else, if elif, operador ternario 

## formato general de if 
# If prueba: 
#   pasos

if False:
    print("Estamos en el if")
print("No entré al if")

# If - else
edad = 18
if edad >= 18:
   print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# if - elif - else 
edad = 18
if edad > 18:
   print("Eres mayor de edad")
elif edad == 18:
    print("tienes 18 años")
else:
    print("Eres menor de edad")

## Operador ternario 
# if en una sola linea  -> ?
## Forma clásica
a = 6
if a>5:
    print("es > 5")

#Operador ternario 
a=6
print("Es > 5 ternario" if a > 5 else "Es < 5")








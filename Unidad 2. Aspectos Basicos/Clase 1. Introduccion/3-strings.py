## Trabajo con cadenas de texto 
s = "INGLATERRA"

print(len(s)) #para hallar el tamaño del string 
print(s[5]) #indexamos el caracter 5
print(s[-1])

print(s[len(s)-1])

#slice de string 
print(s[3:7])
print(s[:4])
print(s[5:])
print(s[:])

## concatenacion 
nombre = "ISABEL DE "
print(nombre+s+ " II")

## repeticion 
verso = "lamama"
coro = verso*10
print(coro)

## otras funciones 
s = "ABBA"
lista = list(s)
print(lista)

m = "murciegalo"
print(m.find("c")) #substring 

m = m.replace("gal","lag")
print(m)

line = "fabio,PINTO,oviedo" 
palabras = line.split(",")
print(palabras)
nombre = palabras[0]
apellido1 = palabras[1]
apellido2 = palabras[2]
print("Mi nombre es " + nombre.upper() + " y mi apellido es " + apellido1.lower())


help(str.capitalize)

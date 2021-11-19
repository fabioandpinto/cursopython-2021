#seno
#coseno
#tangente
#exponencial
#logaritmo neperiano - ln
import math

def seno(numero):
    return math.sin(numero)

def coseno(numero):
    return math.cos(numero)

def tangente(numero):
    return math.tan(numero)

def exponencial(numero):
    return math.exp(numero)

def ln(numero):
    return math.log(numero)

def calcula(numero, funcion):
    datos = {}
    for i in range(1,numero):
        datos[i] = funcion(i)
    return datos

table = calcula(15, ln)
print(table)

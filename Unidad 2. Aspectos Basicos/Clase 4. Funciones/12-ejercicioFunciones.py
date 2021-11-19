def descuento(precio, tasa = 0.25):
  descuento = precio*(1-tasa)
  return descuento

def aplica_iva(precio, tasa = 0.19):
  precio_iva = precio*(1+tasa)
  return precio_iva

productos = {
    'televisor':{
        "precio": 195000,
        "porcentaje": 0.20
    },
    'computador':{
        "precio" : 300,
        "porcentaje": 0.20
    }
}

def aplica(productos, operacion):
    total = 0
    for i in productos.values():
        print(i)
        lista = list(i.values())
        print(lista)
        total += operacion(lista[0], lista[1])
    return print(total)

aplica(productos, aplica_iva)

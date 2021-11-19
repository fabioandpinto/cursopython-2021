"""
    paradigma de programacion.
    Almacenar los datos y las operaciones.
    Bancaria -> tarjetas, usuarios, cuentas, sucursales etc
    caracteristicas: atributos -> estática
    operaciones: métodos -> dinámica
    POO simplificar la logica de negocio, dividir una logica grande en pequeñas unidades

    Tarjeta de crédito --> objeto
    Atributos:
    Numero de la tarjeta
    Franquicia
    Nombre del titular
    Fecha de vencimiento
    codigo de seguridad
    Chip

    Métodos:
    Pagar
    Adelantos
    Activar
    Cancelar
    AcumularBeneficios


    Objetos -------------------------
    - dir(objeto) - lista de atributos y métodos de un objeto
    - objeto.atributo ---> acceder atributo del objeto
    - objeto.metodo(atributo) ---> ejecutar el metodo del objeto con los atributos que carguemos

    Existen unos tipos de datos en python que son objetos primitivos

    (cliente, proveedor, vendedor, trabajador) ---> persona (clase)
    class nombre_clase:
        atributos
        metodos
"""
"""
# String
p = "ana lucia"
print(type(p))
print(p.split(" "))

# listas
l = [1 , 2 , 3 ]
l.append(4)
print(l)
"""

# instanciación de clases
class Saludo:
    pass

s = Saludo()
print(s)

# definicion de metodos
class Saludo:
    mensaje = '¡Hola!'
    def saludar(self, nombre):
        print(self.mensaje + ", " + nombre)

s = Saludo()
s.saludar('Dimitri')

# método inicializador: llama cada vez que se hace la instanciacion de una clase, y sirve para inicializar
# atributos iniciales que tiene que tener la clase
class Tarjeta:
    def __init__(self, numero_tarjeta, franquicia, nombre, fecha_vencimiento, codigo):
        self.numero_tarjeta = numero_tarjeta
        self.franquicia = franquicia
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo = codigo
        print("Creaste una tarjeta,  " + nombre )

    def muestraFecha(self):
        print("La fecha de vencimiento es " + self.fecha_vencimiento)

    def __str__(self):
        return 'Tarjeta con nombre ' + self.nombre + ' y fecha de vencimiento ' + self.fecha_vencimiento

t = Tarjeta("34242334234", "Visa", "Eliana Guerrero", '12/25', 789)
t.muestraFecha()





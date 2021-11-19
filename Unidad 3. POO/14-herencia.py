# (cliente, proveedor, vendedor, trabajador) ---> persona (clase)
# herencia --> clases especializadas a partir de una clase padre
# hereda los atributos y metodos de la clase original (padre) y va a poder tener atributos propios y metodos propios

# clase tarjeta
class Tarjeta:
    def __init__(self, numero_tarjeta, franquicia, nombre, fecha_vencimiento, codigo):
        self.numero_tarjeta = numero_tarjeta
        self.franquicia = franquicia
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo = codigo
        print("Creaste una tarjeta,  " + nombre)

    def muestraFecha(self):
        print("La fecha de vencimiento es " + self.fecha_vencimiento)

    def __str__(self):
        return 'Tarjeta con nombre ' + self.nombre + ' y fecha de vencimiento ' + self.fecha_vencimiento

# Clase tarjeta -----> tarjeta credito, tarjeta debito, tarjeta compras
class TarjetaCredito(Tarjeta):
    def __init__(self, numero_tarjeta, franquicia, nombre, fecha_vencimiento, codigo, cupo):
        # referencia al padre con super
        super().__init__(numero_tarjeta, franquicia, nombre, fecha_vencimiento, codigo)
        self.cupo = cupo
    def __str__(self):
        return 'Tarjeta de credito con nombre ' + self.nombre + ' y cupo ' + str(self.cupo)

class TarjetaDebito(Tarjeta):
    def __init__(self, numero_tarjeta, franquicia, nombre, fecha_vencimiento, codigo, saldo):
        # referencia al padre con super
        super().__init__(numero_tarjeta, franquicia, nombre, fecha_vencimiento, codigo)
        self.saldo = saldo
    def __str__(self):
        return 'Tarjeta de debito con nombre ' + self.nombre + ' y saldo ' + str(self.saldo)


credito = TarjetaCredito(23423432234, 'Visa', 'Fabio', '06/27', 456, 456000)
debito = TarjetaDebito(23423432234, 'Visa', 'Fabio', '06/27', 456, 456000)
print(credito)
print(debito)





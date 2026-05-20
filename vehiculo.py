# ------------------------------------------------------------
# CLASE: Plantilla para crear objetos. Define atributos y métodos.
# ------------------------------------------------------------
class Vehiculo:
    # METODO CONSTRUCTOR: Se ejecuta al crear un objeto.
    def __init__(self, marca, modelo):
        # ENCAPSULAMIENTO: Atributos privados (__) no accesibles directamente desde fuera.
        self.__marca = marca
        self.__modelo = modelo

    # METODO PUBLICO: Permite acceder a los atributos privados de forma controlada.
    def mostrar_info(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")

    # METODO: Comportamiento genérico que será sobrescrito por las clases hijas.
    def arrancar(self):
        print("El vehículo está arrancando...")

# ------------------------------------------------------------
# HERENCIA: La clase Carro hereda de Vehiculo.
# ------------------------------------------------------------
class Carro(Vehiculo):
    # POLIMORFISMO: Sobrescribe el método arrancar con su propia implementación.
    def arrancar(self):
        print("El carro enciende con la llave")

# ------------------------------------------------------------
# HERENCIA: La clase Moto hereda de Vehiculo.
# ------------------------------------------------------------
class Moto(Vehiculo):
    # POLIMORFISMO: Otra implementación distinta del método arrancar.
    def arrancar(self):
        print("La moto enciende con botón")

# ------------------------------------------------------------
# OBJETOS: Instancias concretas de las clases.
# ------------------------------------------------------------
carro1 = Carro("HONDA", "CRV")   # Objeto de tipo Carro
moto1 = Moto("BAJAJ", "Pulsar200") # Objeto de tipo Moto

# Uso de los objetos:
carro1.mostrar_info()   # Usa el método heredado de Vehiculo
carro1.arrancar()       # Polimorfismo: ejecuta la versión de Carro

print("----------------")

moto1.mostrar_info()    # Método heredado
moto1.arrancar()        # Polimorfismo: ejecuta la versión de Moto
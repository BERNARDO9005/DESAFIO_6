class Producto:
    def __init__(self, nombre, stock_inicial):
        self.nombre = nombre
        self.stock = stock_inicial

    def agregar_stock(self, cantidad):
        self.stock = self.stock + cantidad

    def vender(self, cantidad):
        if cantidad > self.stock:
            print("Error: No hay suficiente stock.")
        else:
            self.stock = self.stock - cantidad
            print(f"Venta exitosa de {cantidad} unidades.")

# --- Prueba de ejecución ---
laptop = Producto("Laptop", 5)
laptop.vender(10)          # Error, stock sigue siendo 5
moto = Producto("Motocicleta", 10)
moto.vender(15)            # Error, stock sigue siendo 10
print(f"Stock final de {laptop.nombre}: {laptop.stock}")  # 5
print(f"Stock final de {moto.nombre}: {moto.stock}")      # 10
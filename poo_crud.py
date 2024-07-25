# Desafío 1: Sistema de Gestión de Productos
# Objetivo: Desarrollar un sistema para manejar productos en un inventario.

# Requisitos:

# Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
# Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
# Implementar operaciones CRUD para gestionar productos del inventario.
# Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
# Persistir los datos en archivo JSON.

class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.__nombre = self.validar_nombre(nombre)
        self.__precio = self.validar_precio(precio)
        self.__cantidad_en_stock = self.validar_cantidad(cantidad_en_stock)
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def cantidad(self):
        return self.__cantidad_en_stock
    
    @nombre.setter
    def nombre(self, validar_nombre):
        self.nombre = self.validar_nombre(validar_nombre)

    @precio.setter
    def precio(self, validar_precio):
        self.precio = self.validar_precio(validar_precio)
        
    @cantidad.setter
    def cantidad (self, validar_cantidad):
        self.cantidad = self.validar_cantidad(validar_cantidad)
        
    
    def validar_nombre(self, nombre):
        try:
            nuevo_nombre = str(nombre)
            if not nombre:
                 raise ValueError("El nombre del producto no puede estar vacío")
            if nombre != str(nombre) and nombre == int(nombre):
                 raise ValueError("No se aceptan valores numéricos")
            return nuevo_nombre
        except ValueError:
           raise ValueError("Ingrese un nombre con letras, sin números, y en minúscula")

    def validar_precio(self, precio):
        try:
            precio_producto = float(precio)
            if not precio:
                raise ValueError("Solo se aceptan valores numericos")
            if precio <= 0:
                raise ValueError("Monto menor a 0 no disponible")
            return precio_producto
        except ValueError:
            raise ValueError("El precio debe oscilar de 1 a 999 únicamente")
      
    
    def validar_cantidad(self, cantidad):
        try:
            stock = int(cantidad)
            if not cantidad:
                raise ValueError("Solo se aceptan valores numericos")
            if cantidad <= 0:
                raise ValueError("Monto menor a 0 no disponible")
            return stock
        except ValueError:
            raise ValueError("Ingrese una cantidad admitida")

p1 = Producto("Mate", 25.50, 10)
#print(f"Producto 1: {p1.nombre} - Precio: ${p1.precio:.2f} - Stock: {p1.cantidad}")

p1 = p1.validar_precio(5)
print (p1)

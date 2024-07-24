#crear una aplicación sencilla para gestionar productos en una tienda

# Ejercicio CRUD con POO en Python
# Descripción:

# Este ejercicio te propone crear una aplicación sencilla para gestionar productos en una tienda. Implementarás las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) utilizando Programación Orientada a Objetos (POO) en Python.



# 1. Define las clases:

# Crea dos clases: Producto y Tienda.

# La clase Producto debe tener atributos como nombre, precio, cantidad y métodos para:

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = self.nombre
        self.__precio = self.validar_precio(precio)
        self.__cantidad = self.validar_cantidad(cantidad)
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def cantidad(self):
        return self.__cantidad
    
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = self.__nombre(nombre)

    @precio.setter
    def precio(self, validar_precio):
        self.nombre = self.__validar_precio(validar_precio)
        
    @cantidad.setter
    def cantidad (self, validar_cantidad):
        self.nombre = self.__validar_nombre(validar_cantidad)
    
    def validar_precio(self, precio):
        try:
            precio_producto = float(precio)
            if len(str(precio)) not in [1, 999]:
                raise ValueError("Monto no disponible")
            if precio_producto <= 0:
                raise ValueError("Monto menor a 0 no disponible")
            return precio_producto
        except ValueError:
            raise ValueError("El precio de ser oscilar de 1 a 999 únicamente")
    
    def validar_cantidad(self, cantidad):
        try:
            cantidad_producto = int(cantidad)
            if len(str(cantidad)) not in [1, 999]:
                raise ValueError("Monto no disponible")
            if cantidad_producto <= 0:
                raise ValueError("Monto menor a 0 no disponible")
            return cantidad_producto
        except ValueError:
            raise ValueError("El precio de ser oscilar de 1 a 999 únicamente")


    

# Mostrar información: Imprimir los detalles del producto.
# Actualizar stock: Modificar la cantidad disponible.
# La clase Tienda debe tener un atributo productos (una lista) para almacenar objetos Producto. Además, debe tener métodos para:

# Agregar producto: Crear un validar objeto Producto y agregarlo a la lista.
# Mostrar productos: Imprimir una lista de todos los productos disponibles.
# Buscar producto: Buscar un producto por nombre y devolverlo.
# Actualizar producto: Modificar los atributos de un producto existente.
# Eliminar producto: Eliminar un producto de la lista.
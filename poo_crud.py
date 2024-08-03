# Desafío 1: Sistema de Gestión de Productos
# Objetivo: Desarrollar un sistema para manejar productos en un inventario.

# Requisitos:

# Crear una clase base Producto con atributos como nombre, precio, stock en stock, etc.
# Definir al menos 2 clases derivadas para diferentes categorías de productos
# (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
# Implementar operaciones CRUD para gestionar productos del inventario.
# Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
# Persistir los datos en archivo JSON.

import json

class Producto:
    def __init__(self, nombre, precio, stock, color, memoria_ram, categoria, marca, modelo):
        self.__nombre = self.validar_nombre(nombre)
        self.__precio = self.validar_precio(precio)
        self.__stock = self.validar_stock(stock)
        self.__color = self.validar_color(color)    
        self.__memoria_ram = self.validar_memoria_ram(memoria_ram)  
        self.__categoria = self.validar_categoria(categoria)
        self.__marca = self.validar_marca(marca)
        self.__modelo = self.validar_modelo(modelo)
    @property
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock

    @property
    def color(self):
        return self.__color.capitalize()

    @property
    def memoria_ram(self):
        return self.__memoria_ram

    @property
    def categoria(self):
        return self.__categoria.capitalize()

    @property
    def marca(self):
        return self.__marca.capitalize()

    @property
    def modelo(self):
        return self.__modelo.capitalize()
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.nombre = self.validar_nombre(nuevo_nombre)

    @precio.setter
    def precio(self, nuevo_precio):
        self.precio = self.validar_precio(nuevo_precio)
        
    @stock.setter
    def stock (self, nuevo_stock):
        self.stock = self.validar_stock(nuevo_stock)

    @color.setter
    def color (self, nuevo_color):
        self.color = self.validar_color(nuevo_color)

    @memoria_ram.setter
    def memoria_ram (self, nueva_memoria_ram):
        self.memoria_ram = self.validar_memoria_ram(nueva_memoria_ram)

    @categoria.setter
    def categoria (self, nueva_categoria):
        self.categoria = self.validar_categoria(nueva_categoria)

    @marca.setter
    def marca (self, nueva_marca):
        self.marca = self.validar_marca(nueva_marca)

    @modelo.setter
    def modelo (self, nuevo_modelo):
        self.modelo = self.validar_modelo(nuevo_modelo)
        
    
    def validar_nombre(self, nombre):
        try:
            nuevo_nombre = str(nombre).strip() 
            if not nuevo_nombre.isalpha():
              raise ValueError("El nombre debe contener solo letras")
            return nuevo_nombre
        except ValueError as e:
            raise ValueError("Error al validar el nombre: " + str(e))


    def validar_precio(self, precio):
        try:
            nuevo_precio = float(precio)
            if nuevo_precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")
            return nuevo_precio
        except ValueError:
            raise ValueError("El precio ingresado no es válido. Debe ser un número positivo.")

      
    
    def validar_stock(self, stock):
        try:
            nuevo_stock = int(stock)
            if nuevo_stock <= 0:
                raise ValueError("El stock debe ser un número entero positivo")
            return nuevo_stock
        except ValueError:
            raise ValueError("El valor ingresado no es válido para el stock. Debe ser un número entero positivo.")



    def validar_color(self, color):
        try:
            nuevo_color = str(color).strip() 
            if not nuevo_color:
                raise ValueError("El campo de color no puede estar vacío")
            if not nuevo_color.isalpha():
                raise ValueError("El color debe contener solo letras")
            return nuevo_color
        except ValueError as e:
            raise ValueError(f"Error al validar el color: {str(e)}")


    def validar_memoria_ram(self, memoria_ram):
        try:
            nueva_memoria_ram = int(memoria_ram)  
            if nueva_memoria_ram <= 0:
                raise ValueError("La memoria RAM debe ser un número entero positivo")
            return nueva_memoria_ram
        except ValueError:
            raise ValueError("El valor ingresado para la memoria RAM no es válido. Debe ser un número entero positivo.")

    def validar_categoria(self, categoria):
        try:
            nueva_categoria = str(categoria).strip() 
            if not nueva_categoria:
                raise ValueError("El nombre de la categoría no puede estar vacío")
            if not nueva_categoria.isalpha():
                raise ValueError("El nombre de la categoría debe contener solo letras")
            return nueva_categoria.lower()
        except ValueError as e:
            raise ValueError(f"Error al validar la categoría: {str(e)}")


    def validar_marca(self, marca):
        try:
            nueva_marca = str(marca).strip()  # Eliminamos espacios en blanco
            if not nueva_marca:
                raise ValueError("El nombre de la marca no puede estar vacío")
            if not nueva_marca.isalpha():
                raise ValueError("El nombre de la marca debe contener solo letras")
            return nueva_marca
        except ValueError as e:
            raise ValueError(f"Error al validar la marca: {str(e)}")


    def validar_modelo(self, modelo):
        try:
            nuevo_modelo = str(modelo).strip()  # Eliminamos espacios en blanco
            if not nuevo_modelo:
                raise ValueError("El nombre del modelo no puede estar vacío")
            if not nuevo_modelo.isalnum():
                raise ValueError("El nombre del modelo debe contener solo letras y números")
            return nuevo_modelo
        except ValueError as e:
            raise ValueError(f"Error al validar el modelo: {str(e)}")

     
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "color": self.color,
            "memoria ram": self.memoria_ram,
            "categoria": self.categoria,
            "marca": self.marca,
            "modelo": self.modelo
        }

    def __str__(self):
        return f"{self.nombre} {self.color} {self.memoria_ram} {self.categoria} {self.marca} {self.modelo}"
       

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, stock, color, memoria_ram, categoria, marca, modelo, plataforma, tamanio):
        super().__init__(nombre, precio, stock, color, memoria_ram, categoria, marca, modelo)
        self.__plataforma = self.validar_plataforma(plataforma)
        self.__tamanio = self.validar_tamanio(tamanio)
        
    @property
    def plataforma(self):
        return self.__plataforma.capitalize()

    @property
    def tamanio(self):
        return self.__tamanio.capitalize()

    @plataforma.setter
    def plataforma (self, nueva_plataforma):
        self.plataforma = self.validar_plataforma(nueva_plataforma)

    @tamanio.setter
    def tamanio (self, nuevo_tamanio):
        self.tamanio = self.validar_tamanio(nuevo_tamanio)

    def validar_plataforma(self, plataforma):
        try:
            nueva_plataforma = str(plataforma).strip()
            if not nueva_plataforma:
                raise ValueError("El nombre de la plataforma no puede estar vacío")
            if not nueva_plataforma.isalnum():
                raise ValueError("El nombre de la plataforma debe contener solo letras y números")
            return nueva_plataforma
        except ValueError as e:
            raise ValueError(f"Error al validar la plataforma: {str(e)}")


    def validar_tamanio(self, tamanio):
        try:
            nuevo_tamanio = str(tamanio).strip()  
            if not nuevo_tamanio:
                raise ValueError("El campo de tamaño no puede estar vacío")
            return nuevo_tamanio
        except ValueError as e:
            raise ValueError(f"Error al validar el tamaño: {str(e)}")



    def to_dict(self):
        data = super().to_dict()
        data["plataforma"] = self.plataforma
        data["tamanio"] = self.tamanio
        return data

    def __str__(self):
        return f"{super().__str__()} - Plataforma: {self.plataforma} - tamanio: {self.tamanio}"

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, color, memoria_ram, categoria, marca, modelo, sistema_operativo, condicion, accesorios):
        super().__init__(nombre, precio, stock, color, memoria_ram, categoria, marca, modelo)
        self.__sistema_operativo = self.validar_sistema_operativo(sistema_operativo)
        self.__condicion = self.validar_condicion(condicion)
        self.__accesorios = self.validar_accesorios(accesorios)
    
    @property
    def sistema_operativo(self):
        return self.__sistema_operativo  
    
    @property
    def condicion(self):
        return self.__condicion.capitalize()

    @property
    def accesorios(self):
        return self.__accesorios.capitalize()

    @sistema_operativo.setter
    def sistema_operativo (self, nuevo_sistema_operativo):
        self.sistema_operativo = self.validar_sistema_operativo(nuevo_sistema_operativo)

    @condicion.setter
    def condicion (self, nueva_condicion):
        self.condicion = self.validar_condicion(nueva_condicion)

        
    @accesorios.setter
    def accesorios (self, nuevos_accesorios):
        self.accesorios = self.validar_accesorios(nuevos_accesorios)
        
    def validar_sistema_operativo(self, sistema_operativo):
        try:
            nuevo_sistema_operativo = str(sistema_operativo).strip()  
            if not nuevo_sistema_operativo:
                raise ValueError("El nombre del sistema operativo no puede estar vacío")
            if not nuevo_sistema_operativo.isalnum():
                raise ValueError("El nombre del sistema operativo debe contener solo letras y números")
            return nuevo_sistema_operativo
        except ValueError as e:
            raise ValueError(f"Error al validar el sistema operativo: {str(e)}")

       

    def validar_condicion(self, condicion):
        try:
            nueva_condicion = str(condicion).strip()  
            if not nueva_condicion:
                raise ValueError("El campo de condición no puede estar vacío")
            return nueva_condicion
        except ValueError as e:
            raise ValueError(f"Error al validar la condición del producto: {str(e)}")


    def validar_accesorios(self, accesorios):
        try:
            nuevos_accesorios = str(accesorios).strip() 
            if not nuevos_accesorios:
                raise ValueError("El campo de accesorios no puede estar vacío")
            return nuevos_accesorios
        except ValueError as e:
            raise ValueError(f"Error al validar los accesorios: {str(e)}")


    def to_dict(self):
        data = super().to_dict()
        data["sistema_operativo"] = self.sistema_operativo
        data["condicion"] = self.condicion
        data["accesorios"] = self.accesorios
        return data

    def __str__(self):
        return f"{super().__str__()} - sistema_operativo: {self.sistema_operativo} - Condición: {self.condicion} - Accesorios: {self.accesorios}"

class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_producto(self, producto):
        try:
            datos = self.leer_datos()
            nombre = producto.nombre
            if not str(nombre) in datos.keys():
                datos[nombre] = producto.to_dict()
                self.guardar_datos(datos)
                print(f'Guardado exitoso')
            else:
                print(f'El producto con el nombre {nombre} ya existe')
        except Exception as error:
            print(f'Error inesperado al ingresar un nuevo producto: {error}')

    def leer_producto(self, nombre):
        try:
            datos = self.leer_datos()
            if nombre in datos:
                producto_data = datos[nombre]
                if 'nombre' in producto_data:
                    producto = ProductoDigital(**producto_data)
                else:
                    producto = ProductoFisico(**producto_data)
                print(f'Producto encontrado en stock por su nombre: {nombre}')
            else:
                print(f'No se encontró el producto en stock por su nombre: {nombre}')

        except Exception as e:
            print('Error al leer producto: {e}')

    def actualizar_producto(self, nombre, nuevo_stock):
        try:
            datos = self.leer_datos()
            if str(nombre) in datos.keys():
                 datos[nombre]['stock'] = nuevo_stock
                 self.guardar_datos(datos)
                 print(f'Se ha actualizado el stock del producto: {nombre}')
            else:
                print(f'No se ha encontrado en stock el producto: {nombre}')
        except Exception as e:
            print(f'Error al actualizar el producto: {e}')

    def eliminar_producto(self, nombre):
        try:
            datos = self.leer_datos()
            if str(nombre) in datos.keys():
                 del datos[nombre]
                 self.guardar_datos(datos)
                 print(f'Se ha eliminado el producto: {nombre} correctamente')
            else:
                print(f'No se encontró el producto con nombre:{nombre}')
        except Exception as e:
            print(f'Error al eliminar el producto: {e}')

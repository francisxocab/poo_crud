import os, platform
from poo_crud import (ProductoDigital, ProductoFisico, GestionProductos)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Gestión de Productos ==========")
    print('1. Agregar producto digital')
    print('2. Agregar producto físico')
    print('3. Buscar producto por nombre')
    print('4. Actualizar producto')
    print('5. Eliminar producto por nombre')
    print('6. Mostrar todos los productos')
    print('7. Salir')
    print('======================================================')

def agregar_producto(gestion, tipo_producto):
    try:
        nombre = (input('Ingrese el nombre del producto: '))
        precio = float(input('Ingrese el precio del producto: '))
        stock = int(input('Ingrese el stock actual del producto: '))
        color = (input('Ingrese el color del producto: '))
        memoria_ram = input('Ingrese la memoria RAM del producto: ')
        categoria = (input('Ingrese la categoría a la que corresponde el producto: '))
        marca = (input('Ingrese la marca del producto: '))
        modelo = (input('Ingrese el modelo del producto: '))
        if tipo_producto == '1':
            plataforma = (input('Ingrese la plataforma compatabible para uso del producto: '))
            tamanio = float(input('Ingrese el tamaño de memoria del producto: '))
            producto = ProductoDigital(nombre, precio, stock, color, memoria_ram, categoria, marca, modelo, plataforma, tamanio)
        elif tipo_producto == '2':
            sistema_operativo = (input('Ingrese el sistema operativo del producto: '))
            condicion = (input('Ingrese el estado (usado/nuevo) en que se encuentra el producto: '))
            accesorios = (input('Ingrese los accesorios que trae el producto: '))
            producto = ProductoFisico(nombre, precio, stock, color, memoria_ram, categoria, marca, modelo, sistema_operativo, condicion, accesorios)
        else:
            print('Opción inválida')
            return

        gestion.crear_producto(producto)
        input('Presione enter para continuar...')

    except ValueError as exc:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {exc}')

def buscar_producto_por_nombre(gestion):
    nombre = input('Ingrese el nombre del producto a buscar: ')
    gestion.leer_producto(nombre)
    input('Presione enter para continuar...')

def actualizar_producto(gestion):
    nombre = input('Ingrese el nombre del producto para actualizar stock: ')
    stock = int(input('Ingrese el stock actual del producto: '))
    gestion.actualizar_producto(nombre, stock)
    input('Presione enter para continuar...')

def eliminar_producto_por_nombre(gestion):
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    gestion.eliminar_producto(nombre)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(gestion):
    print('=============== Listado completo de los producto ==============')
    for producto in gestion.leer_datos().values():
        if 'nombre' in producto:
            print(f" - Producto: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['stock']} - Categoria: {producto['categoria']} - Marca: {producto['marca']} - Modelo: {producto['modelo']}")
        else:
            print(f"- Producto: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['stock']} - Categoria: {producto['categoria']} - Marca: {producto['marca']} - Modelo: {producto['modelo']}")
    print('=====================================================================')
    input('Presione enter para continuar...')

if __name__ == "__main__":
    archivo_productos = 'productos_stock.json'
    gestion = GestionProductos(archivo_productos)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        
        elif opcion == '3':
            buscar_producto_por_nombre(gestion)

        elif opcion == '4':
            actualizar_producto(gestion)

        elif opcion == '5':
            eliminar_producto_por_nombre(gestion)

        elif opcion == '6':
            mostrar_todos_los_productos(gestion)

        elif opcion == '7':
            print('Programa finalizado...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
        

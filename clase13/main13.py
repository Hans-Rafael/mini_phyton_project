import os
import sqlite3
# Esta linea es para ubicar python en el directorio actual
os.chdir(os.path.dirname(__file__))

#Funcion para limpiar la pantalla Recordar va con import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    return None

try:
    conection = sqlite3.connect("productos.db")
    print("Conexión establecida exitosamente.")
    cursor = conection.cursor()
    # Crear la tabla productos
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS productos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       precio REAL NOT NULL
                   )
                   """)
    
    # solucito productos
    while True:
        continuar = input("¿Desea continuar con la carga de productos? (s/n): ").lower().strip()
        if continuar != 's':
            break
        nombre_producto = input(
            "Ingrese el nombre del producto: ").lower().strip()
        precio_producto = float(input("Ingrese el precio del producto: "))
        if len(nombre_producto) != 0 and precio_producto >= 0:
            # Insertar el producto en la base de datos
            cursor.execute("""INSERT INTO productos (nombre,precio) VALUES (?,?)""",
                           (nombre_producto, precio_producto)
                           )
            info = input("quiere agregar otro producto s/n?")
            if info == "s":
                continue
            else:
                break

    # guardo cambios
    conection.commit()
    print("valores agregados a la database")
    #menu de lectura de valores
    while True:
        limpiar_pantalla() # limpia la pantalla y genera efecto visual siempre abierto
        print("\nSeleccione una opción:")
        print("====================================")
        print("1. Ver todos los productos")
        print("2. Buscar un producto por nombre")
        print("3. Buscar un producto por precio")
        print("4. Salir")
        valor = input()
        if valor == "1":
            #me traigo toda la info de la db
            cursor.execute('SELECT * FROM productos')
            productos = cursor.fetchall()
            print(f"{'======= Lista de Productos =======':^40}")
            for producto in productos:
                print(f"ID: {producto[0]}, nombre: {producto[1]}, Precio {producto[2]:.2f}")
            pregunta = input("desea salir s/n?")
            if pregunta == "s":
                break
        if valor == "2":
            name = input("ingrese el nombre del producto que busca: ").lower().strip()
            cursor.execute('SELECT nombre FROM productos WHERE nombre LIKE ?', (name + '%',))
            productos = cursor.fetchall()
            if len(productos) == 0:
                print("No se encontraron productos con ese nombre.")
            for producto in productos:
                print(f"nombre: {producto[0]}, Precio {producto[1]:.2f}")
                
            # Pregunta si desea salir
            pregunta = input("desea salir s/n?")
            if pregunta == "s":
                break
        if valor == "3":
            cantidad = float(input("Valor del precio de los productosdesea buscar:").strip())
            cursor.execute('SELECT * FROM productos WHERE precio = ?', (cantidad,))
            productos = cursor.fetchall()
            if len(productos) == 0:
                print("No se encontraron productos con ese nombre.")
            for producto in productos:
                print(f"ID: {producto[0]}, Precio {producto[2]:.2f}, nombre: {producto[1]}")
            pregunta = input("desea salir s/n?")
            if pregunta == "s":
                break
        if valor == "4":
            break
    # cerrar conexion
    conection.close()
    print("Feliz jornada!")#📦
except (NameError, sqlite3.Error, Exception) as e:
    print(f"Ocurrió un error: {e}")

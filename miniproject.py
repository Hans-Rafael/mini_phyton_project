# funcion para validar el nombre de la categoria y del producto


def validation_name(entrada, campo="el Texto", min=3, max=30):
    """
    Valida que la entrada sea un texto no vacío, con una longitud mínima y máxima.
    Args:
         entrada(str): la entrada es el string se quiere validar
         campo(str,optional): El nombre del texto a desplegar in el error.defaults es "el Texto"
         min(str,optional): El numero minimo de caracteres permitidos de la entrada de texto. Defoults es 3
         max(str,optional): El numero maximo de caracteres permitidos de la entrada de texto. Defaults es 30
    Returns:
        bool: True si la entrada es valida sino False. print error mensaje si es invalido
    """
    entrada = entrada.strip()
    if not entrada:
        print(f"{campo} no puede estar vacío.")
        return False
    elif len(entrada) < min:
        print(f"{campo} Debe tener al menos {min} caracteres.")
        return False
    elif len(entrada) > max:
        print(f"{campo} Debe tener como máximo {max} caracteres.")
        return False
    else:
        return True

# funcion para validar el precio

def validation_price(precio, min=0, max=10000000000):
    """
    Valida que el precio sea un número entero positivo y dentro de un rango específico.
    Args:
        precio(str): El precio a validar como un string.
        min(int,optional): El valor mínimo permitido para el precio. Defaults es 0.
        max(int,optional): El valor máximo permitido para el precio. Defaults es 10000000000.
    Returns:
        bool: True si el precio es válido, False en caso contrario. Imprime un mensaje de error si es inválido.
    """
    if not isinstance(precio, str) or not precio.isdigit():
        print("Debe ser un número entero.")
        return False
    precio = int(precio)
    if precio < min:
        print("No puede ser negativo.")
        return False
    elif precio > max:
        print(f"Debe ser menor a {max}.")
        return False
    return True
# funcion para agregar productos

def agregar_producto(lista_productos):
    """
    Agrega un producto a la lista de productos.
    Solicita al usuario la categoría, nombre y precio del producto.
    La categoría y el nombre deben ser validados para que no estén vacíos y cumplan con las longitudes mínimas y máximas.
    El precio debe ser un número entero positivo dentro de un rango específico.
    Args:
        lista_productos (list): La lista donde se almacenarán los productos.
    Returns:
        None: La función no retorna nada, pero agrega un producto al diccionario de productos.
    Raises:
        None: No se esperan excepciones específicas, pero se imprimen mensajes de error si las validaciones fallan.
    Ejemplo de uso:
        agregar_producto(productos)
    Esta función solicita al usuario que ingrese la categoría, nombre y precio de un producto,
    valida cada entrada y, si son correctas, agrega el producto a la lista de productos.
    La función imprime un mensaje de éxito al agregar el producto.
    """
    producto = {}  # CORRECTO: se declara un diccionario para el producto
    # Validación categoría
    while True:
        categoria = input(
            "Por favor, ingresa la categoría del producto: ").strip()
        if validation_name(categoria, "La categoría"):
            break
    producto["categoria"] = categoria
    # Validación nombre
    while True:
        nombre = input(
            "Por favor, ingresa el nombre del producto: ").strip()
        if validation_name(nombre, "El nombre"):
            break
    producto["nombre"] = nombre
    # Validación precio
    while True:
        precio_str = input(
            "Por favor, ingresa el precio como un entero(sin centavos): $").strip()
        if validation_price(precio_str):
            break
    producto["precio"] = int(precio_str)

    # Agregar producto a lista de productos
    lista_productos.append(producto)
    print(
        f"Producto '{nombre}' de categoría '{categoria}' al precio de ${precio_str} agregado exitosamente.\n")
# funcion para ver todos los productos


def ver_productos(lista_productos):
    """
    Muestra todos los productos registrados.
    """
    if not lista_productos:
        print("No se han registrado productos.")
    else:
        cont = 0
        for i in lista_productos:
            cont += 1
            print(
                f"{cont}. Nombre: {i['nombre']}, Categoria: {i['categoria']}, Precio : ${i['precio']}")
    print("---------------------------------------------")
# funcion busqueda de productos


def buscar_productos(lista_productos, abuscar):
    """
    Busca productos en la lista por nombre o categoría.
    abuscar: Término de búsqueda ingresado por el usuario.
    La lista de productos se pasa como parámetro.
    """
    if not lista_productos:
        print("No hay productos registrados aun.")
        return
    else:
        if not validation_name(abuscar, "término de búsqueda", 1, 15):
            return  # Si la validación falla, salimos de la función
        # Búsqueda de productos
        encontrados = []
        for producto in lista_productos:
            if abuscar.lower() in producto["nombre"].lower() or abuscar.lower() in producto["categoria"].lower():
                encontrados.append(producto)
        if encontrados:
            print(f"\n--- Resultados para '{abuscar}' ---")
            for id, producto in enumerate(encontrados, start=1):
                print(
                    f"{id}. Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Precio: ${producto['precio']}")
                print("----------------------------------------\n")
        else:
            print(f"No se encontraron productos para: '{abuscar}'")
# funcion para eliminar productos por numero en lista


def eliminar_producto(lista_productos, item_borrar):
    """
    Elimina un producto de la lista por su número de posición.
    item_borrar: debe ser un string numerico.
    La lista de productos se pasa como parámetro.
    """
    if not lista_productos:
        print("No hay productos para borrar.")
        return False
    # vailod que el numero ingresado sea un entero y este dentro del rango de la lista
    if not validation_price(str(item_borrar), 1, len(lista_productos)):
        print("Número de producto inválido. Debe ser un número entero dentro del rango de productos.")
        return False
    # Si la validación es correcta, procedo a eliminar
    numero = int(item_borrar)
    lista_productos.pop(numero - 1)
    print(f"Producto número {numero} eliminado exitosamente.")
    return True  # Retorno True para indicar que se eliminó un producto correctamente


def impresion_respuesta(respuesta):
    """
    Imprime la respuesta en una estructura más visible.
    """
    if not respuesta:
        print("Operación fallida.")
        return

    ancho_total = 100  # ancho total del marco
    marco = "!" * ancho_total
    contenidoz = f"| {' '*(ancho_total - 4)} |"
    # centrado, restamos 4 por los bordes y espacios
    contenido = f"| {respuesta.center(ancho_total - 4)} |"

    print(marco)
    print(contenidoz)
    print(contenido)
    print(contenidoz)
    print(marco)

productos = []  # la lista de productos

# Mensaje de bienvenida
impresion_respuesta(
    "¡Bienvenidos a ***** SiGePro *****, tu aplicación de gestión de productos!")


# Aquí comienza el menú principal
while True:  # Menú Principal
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Buscar productos")
    print("4. Eliminar producto")
    print("5. Salir")
    print("----------------------")

    opcion = input("Selecciona una opción: ").strip()

    # agrego productos
    if opcion == "1":
        while True:
            # Validación de entrada para agregar un producto
            agregar_producto(productos)
            # Continuar agregando productos
            continuar = input("¿Deseas agregar otro producto? (s/n): ").lower()
            if continuar != 's':
                break

    # aqui muestro los productos registrados
    elif opcion == "2":
        print("\n--- Productos Registrados ---")
        ver_productos(productos)
        input("precione una tecla para continuar")

# Búsqueda del producto
    elif opcion == "3":
        while True:
            # validacion
            busqueda = input(
                "Ingresa el nombre o categoría a buscar: ").strip().lower()
            buscar_productos(productos, busqueda)
            # desea volver a buscar
            continuar = input(
                "¿Deseas buscar otro producto? (s/n): ").strip().lower()
            if continuar != 's':
                print("Saliendo de la búsqueda de productos.")
                break

    # Borrado de productos
    elif opcion == "4":
        print("\n--- Borrado del PRODUCTO por NÚMERO DE POSICIÓN ---")
        while True:
            ver_productos(productos)
            item_borrar = input(
                "Ingresa el número de la posición del producto a borrar (o '-x' para volver al menú):").strip().lower()
            if item_borrar == "-x":
                print("Saliendo de la eliminación de producto.")
                break
            elif eliminar_producto(productos, item_borrar):
                continuar = input(
                    "¿Deseas eliminar otro producto? (s/n): ").strip().lower()
                if continuar != 's':
                    print("Saliendo de la eliminación de producto.")
                    break
        # Mensaje de despedida
    elif opcion == "5":
        impresion_respuesta("¡Gracias por usar SiGePro!")
        break
    else:
        impresion_respuesta("Opción inválida. Por favor, elige entre 1 y 5.")
        # Mensaje de error para opción inválida
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print("|                                                 |")
        # print("| Opción inválida. Por favor, elegí entre 1 y 5.  |")
        # print("|                                                 |")
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

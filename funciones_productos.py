# Importamos tipos para listas, diccionarios y para indicar que un valor puede ser de varios tipos
from typing import List, Dict, Union 

# funcion para validar el nombre de la categoria y del producto
def validation_name(entrada:str, campo:str="el Texto", min:str=2, max:str=30)->bool:
    """
    Valida que la entrada sea un texto no vacío, con una longitud mínima y máxima.
    Args:
         entrada(str): la entrada es el string se quiere validar
         campo(str,optional): El nombre del texto a desplegar in el error.defaults es "el Texto"
         min(str,optional): El numero minimo de caracteres permitidos de la entrada de texto. Defaults es 2
         max(str,optional): El numero maximo de caracteres permitidos de la entrada de texto. Defaults es 30
    Returns:
        bool: True si la entrada es valida sino False. print error mensaje si es invalido
    Raises:
        ValueError: Si la entrada es un string vacio o no cumple con las longitudes minima y maxima.
        TypeError: Si la entrada no es un string.
    Ejemplo de uso:
        validation_name("camisa", "Nombre del producto", 2, 30)
    Esta función valida que la entrada sea un texto no vacío, con una longitud mínima y máxima.
    Si la entrada no cumple con las condiciones, imprime un mensaje de error y lanza una excepción.
    Si la entrada es válida, retorna True.
    """
    entrada = entrada.strip()
    if not isinstance(entrada, str):
        raise TypeError(f"{campo} Debe ser un valor de tipo string.")
    elif not entrada:
        raise ValueError(f"{campo} Debe tener entre {min} y {max} caracteres.")
    elif len(entrada) < min:
        raise ValueError(f"{campo} Debe tener entre {min} y {max} caracteres.")
    elif len(entrada) > max:
        raise ValueError(f"{campo} Debe tener entre {min} y {max} caracteres.")
    else:
        return True

# funcion para validar el precio o numero de la entrada

def validation_numero(precio:str, min:Union[int,float]=0, max:Union[int,float]=10000000000)->bool:
    """
    Valida que el precio sea un número decimal positivo y dentro de un rango específico.
    Args:
        precio(str): El precio a validar como un string.
        min(int,optional): El valor mínimo permitido para el precio. Defaults es 0.
        max(int,optional): El valor máximo permitido para el precio. Defaults es 10000000000.
    Returns:
        bool: True si el precio es válido, False en caso contrario. Imprime un mensaje de error si es inválido.
    Raises:
        ValueError: Si el precio no es un número decimal, es negativo o está fuera del rango especificado.
        TypeError: Si el precio no es un string.
    Ejemplo de uso:
        validation_numero("1500", 0, 10000)
    Esta función valida que el precio sea un número decimal positivo y dentro de un rango específico.
    Si el precio no es un número decimal, es negativo o está fuera del rango, imprime un mensaje de error y retorna False.
    Si el precio es válido, retorna True.
    """
    if not isinstance(precio, str):
        # print("Debe ser un número decimal positivo.")
        # return False
        raise TypeError("No es un valor de tipo string")
    if precio.count('.') > 1 or precio.startswith('.') or precio.endswith('.'):
        # print("Debe ser un número decimal positivo.")
        # return False
        raise ValueError(
            "El valor debe ser un numero positivo con un '.' para indicar decimal")
    partes = precio.split('.')
    if not all(parte.isdigit() for parte in partes):
        raise ValueError(
            "El valor debe ser un numero positivo con un '.' para indicar decimal")
    precio_float = float(precio)
    if precio_float < min:
        raise ValueError(
            f"El valor debe ser un numero positivo con un '.' para indicar decimal entre {min}-{max}")
    elif precio_float > max:
        raise ValueError(
            f"El valor debe ser un numero positivo con un '.' para indicar decimal entre {min}-{max}")
    return True

# funcion para agregar productos

def agregar_producto(lista_productos:List[Dict])-> None:
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
            "Por favor, ingresa la categoría del producto: ").lower().strip()
        try:
            validation_name(categoria, "La categoría")
            producto["categoria"] = categoria
            break  # Si la validación es exitosa, se sale del bucle
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")
            continue  # Vuelve a pedir la categoría
        except TypeError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")
            continue
    # Validación nombre
    while True:
        nombre = input(
            "Por favor, ingresa el nombre del producto: ").strip().lower()
        try:
            validation_name(nombre, "El nombre")
            producto["nombre"] = nombre
            break
        except (TypeError, ValueError) as e:
            print(f"Error: {e} Por favor, inténtalo de nuevo.")
            continue
    # Validación precio
    while True:
        precio_str = input(
            "Por favor, ingresa el precio como un numero positivo (sin centavos): $").strip()
        try:
            validation_numero(precio_str)
            producto["precio"] = float(precio_str)
            break
        except (TypeError, ValueError) as e:
            print(f"Error: {e} Por favor, inténtalo de nuevo.")
            continue

    # Agregar producto a lista de productos
    lista_productos.append(producto)
    print(
        f"Producto '{nombre}' de categoría '{categoria}' al precio de ${precio_str} agregado exitosamente.\n")

# funcion para ver todos los productos


def ver_productos(lista_productos:List[Dict])-> None:
    """
    Muestra todos los productos registrados.
    Args:
        lista_productos (list): La lista de diccionarios de productos.
    Returns:
        None: La función no retorna nada, pero imprime los productos en la consola.
    Raises:
        None: No se esperan excepciones específicas, pero se imprime un mensaje si no hay productos registrados.
    Ejemplo de uso:
        ver_productos(productos)
    Esta función recorre la lista de productos y muestra cada uno con su nombre, categoría y precio.
    Si no hay productos registrados, imprime un mensaje indicando que no se han registrado productos.
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
# **criterios_busqueda: Dict[str, Union[str, float]] significa
# un diccionario con claves string y valores que pueden ser string o float

def buscar_productos(lista_productos:List[Dict], **criterios_abuscar:Dict[str, Union[str, float]])->List[Dict]:
    """
    Busca productos en la lista basándose en una cantidad variable de criterios nombrados.
   Args:
        lista_productos (list): La lista de diccionarios de productos.
        **criterios_abuscar (str): Criterios de búsqueda como nombre o categoría.
    Returns:
        encontrados: lista de productos encontrados que coinciden con los criterios de búsqueda.

    Raises:
        None: No se esperan excepciones específicas, pero se imprime un mensaje si no hay productos registrados.
    Prints:
        - Los productos encontrados que coinciden con los criterios de búsqueda.
        - Un mensaje si no se encontraron productos que coincidan con los criterios.
    Ejemplo de uso:
        buscar_productos(productos, nombre='camisa', categoria='ropa')
    Esta función permite buscar productos en la lista de productos utilizando uno o más criterios de búsqueda.
    Si se proporciona un término de búsqueda general, buscará en los campos 'nombre' y 'categoría'.
    Si se proporcionan criterios específicos como 'precio_maximo' o 'precio_minimo', los aplicará a los productos.
    Si no se encuentran productos que coincidan con los criterios, se imprimirá un mensaje indicando que no se encontraron resultados.  

    """
    encontrados: List[Dict] = []  # Lista para almacenar productos encontrados
    # Validación de entrada
    if not lista_productos:
        print("No hay productos registrados aun.")
        return []  # sin productos retorno una lista vacia
    # Búsqueda de productos donde producto es un diccionario
    for producto in lista_productos:
        coincide_criterio = True
        # recorre la lista de tuplas ejemplo: ('nombre', 'camisa'), ('categoria', 'ropa')
        for criterio, valor in criterios_abuscar.items():
            # Manejo especial para un término de búsqueda general
            if criterio == 'termino':
                if not (valor.lower() in producto.get('nombre', '').lower() or
                        valor.lower() in producto.get('categoria', '').lower()):
                    coincide_criterio = False
                    break  # Si no coincide, salimos del bucle y pasa al siguiente producto
            # manejo de criterios de precios(ej. precio_maximo, precio_minimo)
            elif criterio == 'precio_maximo':
                if producto.get('precio', float('inf')) > valor:
                    coincide_criterio = False
                    break
            elif criterio == 'precio_minimo':
                if producto.get('precio', 0) < valor:
                    coincide_criterio = False
                    break
            # Manejo de otros criterios específicos como nombre y categoría si no son el termino general
            else:
                # Compruebo si el atributo existe en el producto y si coincide con el valor buscado
                if criterio in producto:
                    if isinstance(producto[criterio], str):
                        if valor.lower() not in producto[criterio].lower():
                            coincide_criterio = False
                            break
                    else:  # para otros tipos de datos, comparacion exacta
                        if producto[criterio] != valor:
                            coincide_criterio = False
                            break
                else:  # el criterio de busqueda no existe en el producto
                    coincide_criterio = False
                    break
        if coincide_criterio:
            encontrados.append(producto)
    # Imprimir resultados
    if encontrados:
        print(f"\n--- Resultados de búsqueda ---")
        for id, producto in enumerate(encontrados, start=1):
            print(
                f"{id} . Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Precio: ${producto['precio']}")
        print("----------------------------------------\n")
    else:
        print(
            f"\nNo se encontraron productos para los criterios: {criterios_abuscar}.\n")

# funcion para eliminar productos por numero en lista
# Función para eliminar productos por número en lista


def eliminar_producto(lista_productos:List[Dict], *items_a_borrar:Union[int,str])->bool:
    """
    Elimina uno o más productos de la lista de productos por su número de posición en dicha lista.
    Args:
        lista_productos (list): La lista de productos de la que se eliminará un producto.
        *items_a_borrar (int or str): Uno o más números de productos a eliminar. Puede ser un número entero o un string con números separados por comas.
    Returns:
        bool: True si se eliminó al menos un producto, False si no se eliminaron productos o si hubo un error.
    """
    entrada_procesada_str: List[str] = []  # Lista para almacenar entradas procesadas
    productos_eliminados_detalles: List[Dict] = []  # Lista para almacenar detalles de productos eliminados
    cantidad_eliminados: int = 0

    if not lista_productos:
        print("\nNo hay productos para borrar.\n")
        return False

    if not items_a_borrar:
        print("\nNo se especificó ningún producto para eliminar.\n")
        return False

    # --- SET para evitar duplicados y para el método .add() ---
    numeros_a_eliminar = set()

    rango_max_lista = len(lista_productos)

    # Paso 1: Normalizar la entrada a una lista de strings de números individuales
    if len(items_a_borrar) == 1 and isinstance(items_a_borrar[0], str) and ',' in items_a_borrar[0]:
        entrada_procesada_str = [parte.strip()
                                 for parte in items_a_borrar[0].split(',')]
    else:
        entrada_procesada_str = [str(item) for item in items_a_borrar]

    # Paso 2: Validar y convertir cada string individual a entero
    hay_errores_validacion = False
    for item_str in entrada_procesada_str:
        # Aquí, validation_numero se usa para un SOLO STRING NUMÉRICO y valida el rango
        try:
            if validation_numero(item_str, 1, rango_max_lista):
                # --- Uso .add() para el set ---
                numeros_a_eliminar.add(int(item_str))
        except (TypeError, ValueError) as e:
            print(
                f"Error al procesar '{item_str}': {e}. Debe ser un número entero entre 1 y {rango_max_lista}.")
            hay_errores_validacion = True  # Si hay un error de validación, lo marcamos
            continue  # Continuamos con el siguiente elemento
    if hay_errores_validacion:
        print("\nNo se pudo completar la eliminación debido a entradas inválidas.\n")
        return False  # Si algo no es válido, salimos de la función sin eliminar

    if not numeros_a_eliminar:  # Si después de la validación no quedaron números válidos
        print("\nNo se especificaron números de producto válidos para eliminar.\n")
        return False

    # Paso 3: Ordenar los números de mayor a menor para eliminar sin afectar índices
    numeros_a_eliminar_sorted = sorted(list(numeros_a_eliminar), reverse=True)

    for numero_idx in numeros_a_eliminar_sorted:
        try:
            producto_eliminado = lista_productos.pop(numero_idx - 1)
            productos_eliminados_detalles.append(producto_eliminado)
            cantidad_eliminados += 1
        except IndexError:
            print(
                f"Advertencia: No se pudo eliminar el producto número {numero_idx}. (Índice fuera de rango inesperado).")

    if cantidad_eliminados > 0:
        print(f"{cantidad_eliminados} producto(s) eliminado(s) con éxito.")
        for prod_det in productos_eliminados_detalles:
            print(
                f"  - Eliminado: {prod_det['nombre']} ({prod_det['categoria']}, ${prod_det['precio']:.2f})")
        return True
    else:
        print("\nNo se eliminó ningún producto válido.\n")
        return False


def impresion_respuesta(respuesta:str)-> None:
    """
    Imprime la respuesta en una estructura más visible.
    Args:
        respuesta (str): La respuesta a imprimir.
    Returns:
        None: La función no retorna nada, pero imprime la respuesta en un formato estructurado.
    Raises:
        None: No se esperan excepciones específicas, pero se imprime un mensaje si la respuesta está vacía.
    Ejemplo de uso:
        impresion_respuesta("¡Producto agregado exitosamente!")
    Esta función imprime la respuesta en un marco visualmente atractivo, centrando el texto dentro de un marco de caracteres.   
    """
    if not respuesta:
        print("Operación fallida.")
        return

    ancho_total = 100  # ancho total del marco
    marco = "!" * ancho_total
    linea_espaciada = f"| {' '*(ancho_total - 4)} |"
    # centrado, restamos 4 por los bordes y espacios
    contenido = f"| {respuesta.center(ancho_total - 4)} |"

    print(marco)
    print(linea_espaciada)
    print(contenido)
    print(linea_espaciada)
    print(marco)

# funcion para validar el nombre de la categoria y del producto
def validation_name(entrada, campo="el Texto", min=2, max=30):  
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
        raise ValueError (f"{campo} Debe tener entre {min} y {max} caracteres.")
    elif len(entrada) > max:
        raise ValueError (f"{campo} Debe tener entre {min} y {max} caracteres.")
    else:
        return True

# funcion para validar el precio o numero de la entrada
def validation_numero(precio, min=0, max=10000000000):
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
        #print("Debe ser un número decimal positivo.")
        #return False
        raise TypeError("No es un valor de tipo string")
    if precio.count('.') > 1 or precio.startswith('.') or precio.endswith('.'):
        #print("Debe ser un número decimal positivo.")
        #return False
        raise ValueError ("El valor debe ser un numero positivo con un '.' para indicar decimal")
    partes = precio.split('.')
    if not all(parte.isdigit() for parte in partes):
        raise ValueError ("El valor debe ser un numero positivo con un '.' para indicar decimal")
    precio_float = float(precio)
    if precio_float < min:
        raise ValueError (f"El valor debe ser un numero positivo con un '.' para indicar decimal entre {min}-{max}")
    elif precio_float > max:
        raise ValueError (f"El valor debe ser un numero positivo con un '.' para indicar decimal entre {min}-{max}")
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
        categoria = input("Por favor, ingresa la categoría del producto: ").lower().strip()
        try:
            validation_name(categoria, "La categoría")
            producto["categoria"] = categoria
            break  # Si la validación es exitosa, se sale del bucle
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")
            continue ## Vuelve a pedir la categoría
        except TypeError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")
            continue
    # Validación nombre
    while True:
        nombre = input("Por favor, ingresa el nombre del producto: ").strip().lower()
        try:
            validation_name(nombre, "El nombre")
            producto["nombre"] = nombre
            break
        except (TypeError,ValueError) as e:
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
        except (TypeError,ValueError) as e:
            print(f"Error: {e} Por favor, inténtalo de nuevo.")
            continue

    # Agregar producto a lista de productos
    lista_productos.append(producto)
    print(
        f"Producto '{nombre}' de categoría '{categoria}' al precio de ${precio_str} agregado exitosamente.\n")

# funcion para ver todos los productos
def ver_productos(lista_productos):
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
def buscar_productos(lista_productos, **criterios_abuscar):
    """
    Busca productos en la lista basándose en una cantidad variable de criterios nombrados.
   Args:
        lista_productos (list): La lista de diccionarios de productos.
        **criterios_abuscar (str): Criterios de búsqueda como nombre o categoría.
    Returns:
        encontrados: lista de productos encontrados que coinciden con los criterios de búsqueda.
    Raises:
        None: No se esperan excepciones específicas, pero se imprimen mensajes de error si las validaciones fallan.
    Ejemplo de uso:
        buscar_productos(productos, nombre='camisa', categoria='ropa')
    Esta función permite buscar productos en la lista de productos utilizando uno o más criterios de búsqueda.
    Si se proporciona un término de búsqueda general, buscará en los campos 'nombre' y 'categoría'.
    Si se proporcionan criterios específicos como 'precio_maximo' o 'precio_minimo', los aplicará a los productos.
    Si no se encuentran productos que coincidan con los criterios, se imprimirá un mensaje indicando que no se encontraron resultados.  

    """
    encontrados = []
    # Validación de entrada
    if not lista_productos:
        print("No hay productos registrados aun.")
        return []# sin productos retorno una lista vacia
    # Búsqueda de productos donde producto es un diccionario
    for producto in lista_productos: 
        coincide_criterio = True
        for criterio, valor in criterios_abuscar.items(): #recorre la lista de tuplas ejemplo: ('nombre', 'camisa'), ('categoria', 'ropa')
            # Manejo especial para un término de búsqueda general 
            if criterio == 'termino':
                if not (valor.lower()in producto.get('nombre', '').lower() or
                        valor.lower() in producto.get('categoria', '').lower()):
                    coincide_criterio = False
                    break # Si no coincide, salimos del bucle y pasa al siguiente producto
            #manejo de criterios de precios(ej. precio_maximo, precio_minimo)
            elif criterio == 'precio_maximo':
                if producto.get('precio',float('inf')) > valor:
                    coincide_criterio = False
                    break
            elif criterio == 'precio_minimo':
                if producto.get('precio', 0) < valor:
                    coincide_criterio = False
                    break
            # Manejo de otros criterios específicos como nombre y categoría si no son el termino general
            else:
                #Compruebo si el atributo existe en el producto y si coincide con el valor buscado
                if criterio in producto:
                    if isinstance(producto[criterio], str):
                        if valor.lower() not in producto[criterio].lower():
                            coincide_criterio = False
                            break
                    else:#para otros tipos de datos, comparacion exacta
                        if producto[criterio] != valor:
                            coincide_criterio = False
                            break
                else: # el criterio de busqueda no existe en el producto
                    coincide_criterio = False
                    break
        if coincide_criterio:
            encontrados.append(producto)
    # Imprimir resultados
    if encontrados:
                print(f"\n--- Resultados de búsqueda ---")
                for id, producto in enumerate(encontrados, start=1):
                    print(f"{id} . Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Precio: ${producto['precio']}")
                print("----------------------------------------\n")
    else:
        print(f"\nNo se encontraron productos para los criterios: {criterios_abuscar}.\n")

# funcion para eliminar productos por numero en lista
# Función para eliminar productos por número en lista
def eliminar_producto(lista_productos, *items_a_borrar):
    """
    Elimina uno o más productos de la lista de productos por su número de posición en dicha lista.
    Args:
        lista_productos (list): La lista de productos de la que se eliminará un producto.
        *items_a_borrar (int or str): Uno o más números de productos a eliminar. Puede ser un número entero o un string con números separados por comas.
    Returns:
        bool: True si se eliminó al menos un producto, False si no se eliminaron productos o si hubo un error.
    """
    entrada_procesada_str = []
    productos_eliminados_detalles = [] 
    cantidad_eliminados = 0
    
    if not lista_productos:
        print("\nNo hay productos para borrar.\n")
        return False
    
    if not items_a_borrar:
        print("\nNo se especificó ningún producto para eliminar.\n")
        return False
    
    # --- CORRECCIÓN CLAVE AQUÍ: Usamos un SET para evitar duplicados y para el método .add() ---
    numeros_a_eliminar = set() 
    # --- FIN CORRECCIÓN CLAVE ---

    rango_max_lista = len(lista_productos)

    # Paso 1: Normalizar la entrada a una lista de strings de números individuales
    if len(items_a_borrar) == 1 and isinstance(items_a_borrar[0], str) and ',' in items_a_borrar[0]:
        entrada_procesada_str = [parte.strip() for parte in items_a_borrar[0].split(',')]
    else:
        entrada_procesada_str = [str(item) for item in items_a_borrar]
    
    # Paso 2: Validar y convertir cada string individual a entero
    hay_errores_validacion = False
    for item_str in entrada_procesada_str:
        # Aquí, validation_numero se usa para un SOLO STRING NUMÉRICO y valida el rango
        try:
            if validation_numero(item_str, 1, rango_max_lista):
                numeros_a_eliminar.add(int(item_str)) # --- Uso .add() para el set ---
        except (TypeError, ValueError) as e:
            print(f"Error al procesar '{item_str}': {e}. Debe ser un número entero entre 1 y {rango_max_lista}.")
            hay_errores_validacion = True # Si hay un error de validación, lo marcamos
            continue # Continuamos con el siguiente elemento
    if hay_errores_validacion:
        print("\nNo se pudo completar la eliminación debido a entradas inválidas.\n")
        return False # Si algo no es válido, salimos de la función sin eliminar
    
    if not numeros_a_eliminar: # Si después de la validación no quedaron números válidos
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
            print(f"Advertencia: No se pudo eliminar el producto número {numero_idx}. (Índice fuera de rango inesperado).")

    if cantidad_eliminados > 0:
        print(f"{cantidad_eliminados} producto(s) eliminado(s) con éxito.")
        for prod_det in productos_eliminados_detalles:
            print(f"  - Eliminado: {prod_det['nombre']} ({prod_det['categoria']}, ${prod_det['precio']:.2f})")
        return True
    else:
        print("\nNo se eliminó ningún producto válido.\n")
        return False

def impresion_respuesta(respuesta):
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

productos = []  # la lista de productos
criterios = {} # Diccionario para almacenar criterios de búsqueda
# Mensaje de bienvenida
impresion_respuesta("¡Bienvenidos a ***** SiGePro *****, tu aplicación de gestión de productos!")

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
        print("\n--- Registrando Productos ---")
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
        print("\n--- BÚSQUEDA DE PRODUCTOS ---")
        while True:
            busqueda = input(
                "Ingresa el nombre o categoría a buscar menor a 30 caracteres (dejar vacío para omitir): ").strip().lower()
            # Validación de entrada para la búsqueda
            if len(busqueda) > 30:
                print("El término de búsqueda debe tener menos de 30 caracteres.")
                continue
            if busqueda:
                # Si hay un término de búsqueda, lo agrego al diccionario de criterios
                criterios['termino'] = busqueda
            #cirterios de precio maximo y minimo
            precio_maximo = input(
                "Ingresa el precio máximo a buscar (dejar vacío para omitir): ").strip()
            #valido sea un numero entero
            try:
                if validation_numero(precio_maximo) and precio_maximo != "":
                    criterios['precio_maximo'] = float(precio_maximo)
            except (ValueError,TypeError)as e:
                print(f"Error: {e}. El precio máximo debe ser un número positivo, intentelo de nuevo")
           #criterio para precio minimo
            precio_minimo = input(
                "Ingresa el precio mínimo a buscar (dejar vacío para omitir): ").strip()
            #valido sea un numero decimal
            try:
                if validation_numero(precio_minimo) and precio_minimo != "":
                    criterios['precio_minimo'] = float(precio_minimo)
                    break
            except (TypeError,ValueError,Exception) as e:
                print(f"Error: {e}, El precio mínimo debe ser un número positivo, intentelo de nuevo")
                continue
            if not criterios:
                print("No se ingresaron criterios de búsqueda. Volviendo al menú.")
                continue # Volver al inicio del bucle del menú
            # Realizo la búsqueda de productos
            impresion_respuesta(f"Buscando productos con los criterios: {criterios}")
            # Llamo a la función de búsqueda con los criterios
            buscar_productos(productos, **criterios)
            # Limpio los criterios para la próxima búsqueda
            criterios.clear()
            # Pregunto al usuario si desea volver a buscar
            continuar = input(
                "¿Deseas buscar otro producto? (s/n): ").strip().lower()
            if continuar != 's':
                print("Saliendo de la búsqueda de productos.")
                break
        
    # Borrado de productos
    elif opcion == "4":
        print("\n--- Borrado del PRODUCTO por NÚMERO DE POSICIÓN ---")
        while True:
            ver_productos(productos)#ver los productos actuales
            item_borrar = input("Ingresa el número(s) de los productos a borrar (ej: 1 o 2,3,4). Usa comas para eliminar varios productos o '-x' para volver al menú: :").strip().lower()
            if item_borrar == "-x":
                print("Saliendo de la eliminación de producto.")
                break
            elif input(f"¿Seguro que deseas eliminar los productos número {item_borrar} ?  (s/n): ").strip().lower() != 's':
                print("Eliminación cancelada.")
                continue
            elif eliminar_producto(productos, item_borrar):
                continuar = input(
                    "¿Deseas eliminar otro producto? (s/n): ").strip().lower()
                if continuar != 's':
                    print("Saliendo de la eliminación de producto.")
                    break
    # Salir del programa
    elif opcion == "5":
        impresion_respuesta("¡Gracias por usar SiGePro!")
        break
    else:
        impresion_respuesta("Opción inválida. Por favor, elige entre 1 y 5.")
        continue
# Fin del programa

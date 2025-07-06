
import sqlite3

# validar es un numero real(Float) no nulo menor a 999.999.999


def validar_float_positivo(valor):
    """
    Valida que el valor recibido sea un número real (float), mayor que 0 y menor que 999.999.999.
    Retorna True si es válido, False en caso contrario.
    """
    try:
        dato = float(valor)
        return 0 < dato < 999_999_999
    except (ValueError, TypeError, Exception):
        return False

    # valida si es un string no nulo menor a 50 caracteres


def validar_string(txt) -> bool:
    if isinstance(txt, str) and txt.strip() and len(txt.strip()) < 50:
        return True
    else:
        print("El texto debe ser un string entre 1 y 50 caracteres.")
        return False

# valida si es un entero positivo no nulo menor a 999999999


def validar_entero_positivo(valor):
    try:
        dato = int(valor)
        return 0 < dato < 999_999_999
    except (ValueError, TypeError, Exception):
        return False

# funcion conecta a la database, si el data.db no existe lo crea.


def conexion_db(data_base: str = "data.db") -> sqlite3.Connection:
    """Si el archivo existe, se conecta Y si no existe, lo crea vacío en el mismo directorio del script, y se conecta"""
    try:
        conex = sqlite3.connect(data_base)
        print(f"Conectado correctamente a '{data_base}'")
        return conex
    except (Exception) as e:
        print(f"Ocurrió un error al conectarse a la db: {e}")
        return None
# Crear tabla en la base de datos si aun no existe!


def crear_tabla_db(nombre_db, nombre_tabla, col1, col2, col3, col4, col5, col6):
    """Crea una tabla en la base de datos si no existe."""
    columnas = [col1, col2, col3, col4, col5, col6]
    # paso los campos a mayusculas y gartantizo no espacios en blancos al final.
    for i in range(len(columnas)):
        columnas[i] = columnas[i].strip().upper()

    # reviso no este repetido un valor en el array
    if len(columnas) != len(set(columnas)):
        print("Error: Los nombres de las columnas no pueden estar repetidos.")
        return
    # reviso que los nombres de las columnas o campos no sean nulos y sean strings
    for nombre in columnas:
        if not validar_string(nombre):
            return
    # valido que el nombre de la tabla sea un string no nulo
    if not validar_string(nombre_tabla):
        return

    # Operación con conexión protegida
    try:
        # realizo conexion a la db
        conexion = conexion_db(nombre_db)
        if conexion is None:
            return
        cursor = conexion.cursor()
        # Ejecuto la consulta para crear la tabla si no existe
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {nombre_tabla} (
                {col1} INTEGER PRIMARY KEY AUTOINCREMENT,
                {col2} TEXT NOT NULL,
                {col3} TEXT,
                {col4} INTEGER NOT NULL,
                {col5} REAL NOT NULL,
                {col6} TEXT
            )
        """)
        # Confirma los cambios y los hace permanentes.
        conexion.commit()
        print(f"Tabla '{nombre_tabla}' creada o ya existente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()

# 1 Registrar nuevo producto en la db


def registrar_producto(nombre_db, nombre_tabla, campo1_str, campo2_str, cantidad, precio, campo3_str):
    array_string = [campo1_str, campo2_str, campo3_str]
    # valido entradas.
    if not validar_float_positivo(precio):
        print("Precio no válido")
        return
    if not validar_entero_positivo(cantidad):
        print("Cantidad no válida")
        return
    for name in array_string:
        if not validar_string(name):
            print(f"Valor inválido: {name}")
            return
    try:
        cantidad = int(cantidad)  # paso entrada a integer
        precio = float(precio)   # convierto entrada en float
        conexion = sqlite3.connect(nombre_db)
        cursor = conexion.cursor()
        # ejecuto comando de sql para inyectar o insertar de forma segura mediante tuplas.
        cursor.execute(f"""INSERT INTO {nombre_tabla} (nombre, descripcion, cantidad, precio, categoria)
         VALUES (?, ?, ?, ?, ?)
         """, (campo1_str, campo2_str, cantidad, precio, campo3_str))
        conexion.commit()  # guardo cambios en la db
        print(
            f"producto {campo1_str} de la categoria {campo3_str} agregado exitosamente")
    except (Exception) as e:
        print(f"ERROR al registrar producto:{e}")
        # conexion.rollback()  # ← DESHACE si falló antes del commit
    finally:
        conexion.close()  # libero recursos
# 2 ver todos los productos en db:


def ver_registro_db(nombre_db, tabla):
    try:
        conexion = sqlite3.connect(nombre_db)
        if not conexion:
            return []
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        productos = cursor.fetchall()  # MI LISTA DE TUPLAS
        # si no hay productos en la db imprimo una pantalla vacias para dar impresion de vista a la tabla
        if not productos:
            print("La base de datos está vacía.")
            print("=" * 90)
            print(
                f"ID: - | nombre: - | descripcion: - | cantidad: - | precio: - | categoria: - | \n")
            print("=" * 90)
            return
        # devuelvo lo encontrado:
        return productos
    except (Exception) as e:
        print(f"ERROR al intentar ver el registro: {e}")
        return []  # si no hay conexion retorno una lista vacia
    # manejo del error
    finally:
        if conexion:
            conexion.close()

# 3 Update datos del producto.


def actualizar_informacion(nombre_db, tabla, pk, campo, valor):
    # valido entradas
    if not validar_entero_positivo(pk):
        return
    if not validar_string(campo):
        return
    if not validar_string(valor):
        return
    # valido que la tabla es string no nulo (deberia ver si la tabla existe)
    if not validar_string(tabla):
        return
    try:
        conexion = sqlite3.connect(nombre_db)
        if not conexion:
            return
        cursor = conexion.cursor()
        # ejecuto comando de sql para actualizar el producto por su id
        # uso ? para evitar inyeccion sql
        cursor.execute(
            f"UPDATE {tabla} SET {campo} = ? WHERE id = ?", (valor, pk))
        conexion.commit()  # guardo cambios en la db
        print(f"se an guardado exitosamente {valor}")
    except (Exception) as e:
        # manejo del error
        print(f"ERROR al intentar ver el registro: {e}")
    finally:
        conexion.close()
# 4 Borrar producto por su ID


def borrar_producto(nombre_db, tabla, pk):
    # validar entradas.
    if not validar_string(nombre_db):
        return
    if not validar_string(tabla):
        return
    if not validar_entero_positivo(pk):
        return
    try:
        # realizo conexion a la db
        conexion = conexion_db(nombre_db)
        if not conexion:
            return
        cursor = conexion.cursor()
        # ejecuto comando de sql para eliminar el producto por su id
        # uso ? para evitar inyeccion sql
        cursor.execute(f"DELETE FROM {tabla} WHERE id= ?", (pk))
        conexion.commit()  # guardo cambios en la db
        print(f"Se elimino el produccto de id: #{pk}")
    except (Exception) as e:
        print(f"Al borrar el producto #{pk} se produjo un Error: {e} ")
    finally:
        conexion.close()
# 5 Busqueda del producto empiezan con valor y ordenado alfabeticamente a-z


def busqueda_producto(db, tabla, campo, valor):
    # valido entradas
    if not validar_string(db) or not validar_string(tabla) or not validar_string(campo):
        return
    try:
        conexion = conexion_db(db)
        if not conexion:
            return
        cursor = conexion.cursor()
        # busco por id primero
        if campo == "id":
            if not validar_entero_positivo(valor):
                print(f"El ID debe ser un numero entero positivo")
                return
            # ejecuto la consulta para buscar por id
            cursor.execute(f"SELECT * FROM {tabla} WHERE id= ?", (valor,))
        else:
            # ejecuto la consulta para strings
            cursor.execute(
                f"SELECT * FROM {tabla} WHERE {campo} LIKE ? ORDER BY {campo} ASC", (valor+'%',))
        # me traigo toda las filas
        productos = cursor.fetchall()

        if not productos:
            print(f"el producto {valor} No se encuentra en la base de datos")
            return False
        #
        # retorno los productos encontrados
        return productos
    except (Exception) as e:
        print(f"Error al busacar: {valor} : {e} ")
    finally:
        conexion.close()


# 6 reporte del producto <=cantidad: imprime los productos que cumplen con condicion
def reporte_bajo_stock(db, tabla, limite):
    # valido las entradas
    if not validar_entero_positivo(limite):
        return
    try:
        conexion = conexion_db(db)
        if not conexion:
            return
        cursor = conexion.cursor()
        # ejecuto la consulta para buscar productos con cantidad menor o igual al limite
        cursor.execute(f"SELECT * FROM {tabla} WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()
        if not productos:
            print(
                f"No se encontraron productos con stock igual o menor a {limite}.")
        else:
            # retorno la lista de tuplas de productos encontrados
            return productos
    except (Exception) as e:
        print(
            f" Error al buscar productos con cantidad menor o igual a #{limite} : {e} ")
    finally:
        conexion.close()

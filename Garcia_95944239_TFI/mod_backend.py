
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
# Función para validar si un nombre de los campos de la tabla es válido para este proyecto.
def validar_columnas_tabla(columnas_dict):
    """Valida que el diccionario de columnas tenga los campos necesarios para una tabla de productos."""
    campos_requeridos = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "nombre": "TEXT NOT NULL",
        "descripcion": "TEXT",
        "cantidad": "INTEGER NOT NULL",
        "precio": "REAL NOT NULL",
        "categoria": "TEXT"
    }
    # Valido que el argumento sea un diccionario
    if not isinstance(columnas_dict, dict):
        print("Error: Las columnas deben ser un diccionario.")
        return False

    # Valido que todas las claves requeridas estén presentes
    claves_faltantes = set(campos_requeridos.keys()) - set(columnas_dict.keys())
    if claves_faltantes:
        print(f"Error: Faltan campos requeridos: {claves_faltantes}")
        return False

    # Valido que los tipos de datos coincidan exactamente
    for campo, tipo in campos_requeridos.items():
        if columnas_dict[campo].strip().upper() != tipo:
            print(f"Error: El campo '{campo}' debe ser '{tipo}', pero se recibió '{columnas_dict[campo]}'")
            return False

    return True
# Crear tabla en la base de datos si aun no existe!
# converti entradas de crear_tabla_db(nombre_db, nombre_tabla, col1, col2, col3, col4, col5, col6):
# a diccionario mas escalable y reutilizable.
def crear_tabla_db(nombre_db, nombre_tabla, columnas_dict):
    """Crea una tabla en la base de datos si no existe."""
    #valido tipo de datos no reviso sea igual a 6 columnas para ser mas reutilizable hare funcion valide diccionario particular
    if not isinstance(columnas_dict, dict) or len(columnas_dict) == 0:
        print("Error: Debe proporcionar un diccionario con columnas.")
        return
    #valida nombre de tabla
    if not validar_string(nombre_tabla):
        return
    columnas_limpias={}
    # paso los campos a mayusculas y gartantizo no espacios en blancos al final.
    for nombre, tipo in columnas_dict.items():
        nombre_limpio = nombre.strip().upper()
        tipo_limpio = tipo.strip().upper()
        # valido que el nombre de la columna sea un string no nulo
        if not validar_string(nombre_limpio) or not validar_string(tipo_limpio):
            return
        columnas_limpias[nombre_limpio] = tipo_limpio
         # Verificar que no haya nombres de columnas repetidos
    if len(columnas_limpias) != len(set(columnas_limpias)):
        print("Error: Los nombres de columnas no pueden repetirse.")
        return
    # Armo la parte del SQL con columnas y tipos
    partes_columnas = []
    for nombre, tipo in columnas_limpias.items():
        partes_columnas.append(f"{nombre} {tipo}")
    
    columnas_sql = ", ".join(partes_columnas)
   
    try:
        # realizo conexion a la db
        conexion = conexion_db(nombre_db)
        if conexion is None:
            return
        cursor = conexion.cursor()
        # Ejecuto la consulta para crear la tabla si no existe
        cursor.execute(f""" CREATE TABLE IF NOT EXISTS {nombre_tabla} ( {columnas_sql} ) """)
        # Confirma los cambios y los hace permanentes.
        conexion.commit()
        print(f"Tabla '{nombre_tabla}' creada o ya existente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()

# 1 Registrar nuevo producto en la db ahora con diccionario de campos.
def registrar_producto(nombre_db, nombre_tabla, campos_dict):
    """Inserta un producto usando un diccionario {columna: valor}."""

    if not isinstance(campos_dict, dict) or not campos_dict:
        print("Error: campos_dict debe ser un diccionario no vacío.")
        return

    if not validar_string(nombre_db) or not validar_string(nombre_tabla):
        return

    columnas = list(campos_dict.keys())     # ["nombre", "descripcion", ...]
    valores = list(campos_dict.values())    # ["Lapicera", "Tinta azul", ...]
    
    #
    columnas_sql = ", ".join(columnas)# "nombre, descripcion, cantidad, precio, categoria"
    valores_sql = ", ".join(["?"] * len(columnas)) # "?, ?, ?, ?, ?"

    try:
        conexion = conexion_db(nombre_db)
        if not conexion:
            return
        cursor = conexion.cursor()
        #
        cursor.execute(
            f"INSERT INTO {nombre_tabla} ({columnas_sql}) VALUES ({valores_sql})",
            tuple(valores)
        )
        conexion.commit()
        print(f"Producto '{campos_dict.get('nombre', '')}' insertado con éxito.")
    except Exception as e:
        print(f"Error al registrar producto: {e}")
    finally:
        conexion.close()


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
        # realizo conexion a la db
        conexion = conexion_db(nombre_db)
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
        conexion = conexion_db(db)  ### 
        if not conexion:
            return
        cursor = conexion.cursor() #####
        # busco por id primero
        if campo == "id":
            if not validar_entero_positivo(valor):
                print(f"El ID debe ser un numero entero positivo")
                return
            # ejecuto la consulta para buscar por id
            cursor.execute(f"SELECT * FROM {tabla} WHERE {campo}= ?", (valor,))
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

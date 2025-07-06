import os

# funcion para limpiar la pantalla


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# función para pausar la ejecución del programa


def pausa():
    """Pausa la ejecución del programa y espera a que el usuario presione una tecla."""
    input("Presione Enter para continuar...")
# funcion imprime el menu Principal del sistema de gestion de productos
# y retorna la opcion elegida por el usuario


def menu():
    limpiar_pantalla()  # llamo a la funcion que limpia la pantalla de la terminal
    # imprimo el menu a mostrar
    print("=====-SiGePro - Menu del Sistema de Gestion de productos. =====")
    print("1. Registrar nuevo producto")
    print("2. Ver todos los registros en db")
    print("3. Actualizar datos del producto por su ID")
    print("4. Borrar un producto mediante su ID")
    print("5. Busqueda de producto por Id, nombre o categoria")
    print("6. Reporte de bajo stock")
    print("0. Para salir")
    print("======================================================")
    # tomo la opción del usuario y elimino espacios al inicio y final
    opcion = input("Seleccione una opción: ").strip()
    # verifico y notifco a usuario si la obsion es erronea
    if not opcion.isdigit() or int(opcion) not in range(0, 7):
        print("XXXXXXXX  Opción no válida. Debe ser un número entre 0 y 6. XXXXXXXX")
        pausa()
        return None  # retorno None si la opcion no es valida no es obligatorio pero es una buena practica
    return opcion

# función para imprimir la tabla de productos Estructurada


def imprime_tabla(productos):
    if not productos:
        print("No hay datos para mostrar.")
        return
    # Encabezado de la tabla
    print("\n Lista de Productos Registrados")
    print("=" * 85 + "=" * 25)
    print(f"{'ID':>1} {'Nombre':>10} {'Descripción':>30} {'Cant':>20} {'Precio':>15} {'Categoría':>20}")
    print("=" * 85 + "=" * 25)
    # resto de la tabla
    for producto in productos:
        print(
            f"{producto[0]:<5} {producto[1]:<25} {producto[2]:<30} {producto[3]:<12} ${producto[4]:<15.2f} {producto[5]:<10} \n")

# función para mostrar un submenú y retornar la opción elegida opciones como diccionario


def sub_menu(titulo, opciones: dict):
    """
    Muestra un submenú y retorna la clave elegida.
    recibe un titulo(str) y un diccionario de opciones.
    El diccionario debe tener claves como strings y descripciones como strings.
    Ejemplo:
    opciones = {
        "1": "Registrar nuevo producto",
        "2": "Ver todos los registros en db",
        "3": "Actualizar datos del producto por su ID",
        }

    """
    while True:
        print("=" * 54)
        print(f"⇩ {titulo.upper()} ⇩")
        print("=" * 54)
        for clave, descripcion in opciones.items():
            print(f"{clave}. {descripcion}")
        print("=" * 54)
        seleccion = input("Seleccion: ").strip()
        if seleccion in opciones:
            return seleccion
        else:
            print("Opción inválida. Intente nuevamente.\n")
            pausa()
            limpiar_pantalla()

import os

# funcion para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausa():
    """Pausa la ejecución del programa y espera a que el usuario presione una tecla."""
    input("Presione Enter para continuar...")
# funcion imprime el menu


def menu():
    limpiar_pantalla()
    print("===== Menu del Sistema de Gestion de productos. =====")
    print("1. Registrar nuevo producto")
    print("2. Ver todos los registros en db")
    print("3. Actualizar datos del producto por su ID")
    print("4. Borrar un producto mediante su ID")
    print("5. Busqueda de producto por Id, nombre o categoria")
    print("6. Reporte de bajo stock")
    print("0. Para salir")
    print("======================================================")
    opcion = input("Seleccione una opción: ").strip()
    return opcion


def imprime_tabla(productos):
    # Encabezado de la tabla
    print("\n📦 Lista de Productos Registrados")
    print("=" * 85 + "=" * 25)
    print(f"{'ID':>1} {'Nombre':>10} {'Descripción':>30} {'Cant':>20} {'Precio':>15} {'Categoría':>20}")
    print("=" * 85 + "=" * 25)
    # resto de la tabla
    for producto in productos:
        print(
            f"{producto[0]:<5} {producto[1]:<25} {producto[2]:<30} {producto[3]:<12} ${producto[4]:<15.2f} {producto[5]:<10} \n")

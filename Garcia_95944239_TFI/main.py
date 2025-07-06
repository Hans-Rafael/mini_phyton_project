
import os

from mod_backend import (
    validar_entero_positivo,
    validar_float_positivo,
    validar_string,
    crear_tabla_db,
    registrar_producto,
    ver_registro_db,
    actualizar_informacion,
    borrar_producto,
    busqueda_producto,
    reporte_bajo_stock,
)

from mod_frontend import menu, imprime_tabla, pausa, limpiar_pantalla, sub_menu


def main():
    # Esta linea es para ubicar python en el directorio actual
    # Configuración inicial para el funcionamiento de la aplicación.
    os.chdir(os.path.dirname(__file__))
    # declaro las variables
    db = 'data.db'
    tbl = 'productos'
    # creo la database (data.db) con una tabla (productos) y los campos requeridos
    crear_tabla_db(db, tbl, 'id', 'nombre', 'descripcion',
                   'cantidad', 'precio', 'categoria')
    menu_opcion = ""
    while menu_opcion != "0":
        menu_opcion = menu()
        # === OPCIÓN 1: Registrar nuevo producto ===
        if menu_opcion == "1":
            while True:
                while True:
                    nombre = input("Nombre del producto: ").strip()
                    if validar_string(nombre):
                        break
                    print("Nombre inválido. Intente de nuevo.")
                while True:
                    descripcion = input("Una pequeña descripcion: ").strip()
                    if validar_string(descripcion):
                        break
                    print(
                        "recuerda no debe estar vacio y ser menos a 50 caracteres, trata de nuevo")
                while True:
                    cantidad = input("Cantidad de Items: ")
                    if validar_entero_positivo(cantidad):
                        break
                    print(
                        "recuera debe ser un numero entero positivo menor a 999.999.999, intenta de nuevo")
                while True:
                    precio = input("El precio: $").strip()
                    if validar_float_positivo(precio):
                        break
                    print(
                        "recueda el campo no puede estar vacio y ser menor a 999.999.999")
                while True:
                    categoria = input("A que categoria pertenece: ").strip()
                    if validar_string(categoria):
                        break
                    print(
                        "recuerda no debe estar vacio y ser menos a 50 caracteres, trata de nuevo")
                registrar_producto(db, tbl, nombre, descripcion,
                                   cantidad, precio, categoria)
                print("Producto registrado correctamente.")
                respuesta = input(
                    "desea registrar otro producto (s/n): ").strip().lower()
                limpiar_pantalla()
                if respuesta != "s":
                    break

        # === OPCIÓN 2: Ver registros ===
        elif menu_opcion == "2":
            # guardo como productos de la base de datos
            productos = ver_registro_db(db, tbl)
            # Verifico si hay productos registrados
            if not productos:
                print("La base de datos está vacía. No hay productos registrados.")
            else:
                imprime_tabla(productos)
            pausa()

        # === OPCIÓN 3:  Actualizar datos del producto por su ID ===
        elif menu_opcion == "3":
            while True:
                pk = input("Ingrese el ID del producto a modificar: ").strip()
                if not validar_entero_positivo(pk):
                    print(
                        "El ID debe ser un número entero positivo. Intente nuevamente.")
                    pausa()
                    continue
                # Submenú para elegir qué campo modificar
                campos_opciones = {
                    "1": "nombre",
                    "2": "descripcion",
                    "3": "cantidad",
                    "4": "precio",
                    "5": "categoria"
                }
                campo_key = sub_menu(
                    "Seleccione el campo a modificar", campos_opciones)
                # Extraigo el nombre del campo real
                campo = campos_opciones[campo_key]

                while True:
                    if campo == "cantidad":
                        valor = input("Ingrese la nueva cantidad: ").strip()
                        if not validar_entero_positivo(valor):
                            print("La cantidad debe ser un número entero positivo.")
                            pausa()
                            continue

                    elif campo == "precio":
                        valor = input("Ingrese el nuevo precio: $").strip()
                        if not validar_float_positivo(valor):
                            print("El precio debe ser un número real positivo.")
                            pausa()
                            continue

                    else:  # campos string
                        valor = input(
                            f"Ingrese el nuevo valor para '{campo}': ").strip()
                        if not validar_string(valor):
                            print(
                                f"El valor ingresado para {campo} no es válido.")
                            pausa()
                            continue

                    # Si llegó aquí, es porque el valor es válido
                    actualizar_informacion(db, tbl, pk, campo, valor)
                    print(
                        f"El campo '{campo}' del producto #{pk} ha sido actualizado a: {valor}")
                    # pausa()
                    # Pregunto si desea modificar otro campo del mismo producto
                    otra_modificacion = input(
                        "¿Desea modificar otro campo de este producto? (s/n): ").strip().lower()
                    if otra_modificacion == "s":
                        # Si elige "s", vuelvo a pedir el campo a modificar
                        campo_key = sub_menu(
                            "Seleccione el campo a modificar", campos_opciones)
                        campo = campos_opciones[campo_key]
                    else:
                        # Si elige otra cosa, salgo del bucle de campos
                        print("Modificación del producto finalizada.")
                        pausa()
                        break
                # Pregunto si desea modificar otro producto
                otro_producto = input(
                    "¿Desea modificar otro producto? (s/n): ").strip().lower()
                if otro_producto != "s":
                    break  # salgo del while general

        # === OPCIÓN 4: Eliminar producto por ID ===
        elif menu_opcion == "4":
            elemento = input("Ingrese el ID del producto a eliminar: ").strip()
            print(
                f"\n==== A decidido eliminar el producto de ID {elemento} =====")
            productos = busqueda_producto(db, tbl, 'id', elemento)
            if productos:
                imprime_tabla(productos)
                # Confirmación para eliminar el producto
                print(f"===== Confirma desea eliminar el producto  (s/n )=====\n")
                confirmacion = input("Confirmar: ").strip().lower()
                if confirmacion == "s":
                    borrar_producto(db, tbl, elemento)
                    pausa()
            else:
                pausa()
                continue

        # === OPCIÓN 5: Busqueda de producto por Id, nombre o categoria ===
        elif menu_opcion == "5":
            while True:
                # campo = input(f"{'=='*25}\ningrese por que campo desea buscar: \n1. ID\n2. Categoria\n3. Nombre del producto\n{'=='*25}\nSeleccion:").strip()
                campos_busqueda = {
                    "1": "ID", "2": "Categoria", "3": "Nombre del producto"}
                campo = sub_menu("Buscar producto", campos_busqueda)
                if campo not in ("1", "2", "3"):
                    print("XXX--> Opción inválida. Intente nuevamente.<--XXX")
                    pausa()
                    limpiar_pantalla()
                    continue
                if campo == "1":
                    valor = input("Ingrese el ID del producto:  ").strip()
                    if not validar_entero_positivo(valor):
                        print(
                            "XXXXX--> El ID debe ser un número entero positivo. <--XXXXXX")
                        pausa()
                        limpiar_pantalla()
                        continue
                    # si el campo es id, busco por id
                    productos = busqueda_producto(db, tbl, "id", valor)
                if campo == "2":
                    valor = input("Ingrese la Categoria:  ").strip()
                    if not validar_string(valor):
                        print(
                            "XXXXX--> el tipo de categoria debe ser un texto no nulo. <--XXXXXX")
                        pausa()
                        limpiar_pantalla()
                        continue
                    # si el campo es categoria, busco por categoria
                    productos = busqueda_producto(db, tbl, "categoria", valor)
                if campo == "3":
                    valor = input("Ingrese Nombre del producto:  ").strip()
                    if not validar_string(valor):
                        print(
                            "XXXXX--> el nombre del producto debe ser un texto no nulo. <--XXXXXX")
                        pausa()
                        limpiar_pantalla()
                        continue
                    productos = busqueda_producto(db, tbl, "nombre", valor)
                # imprimo la tabla de productos encontrados
                imprime_tabla(productos)
                preferencia = input(
                    "Desea realizar una nueva busqueda (s/n)").strip().lower()
                print("preferencia:", preferencia)
                # limpiar_pantalla()  # No limpio la pantalla para mantener en ella busquedas anteriores.
                if preferencia != "s":
                    break
        # === OPCIÓN 6: Reporte de bajo stock ===
        elif menu_opcion == "6":
            while True:
                # Solicito el limite de stock para el reporte
                limite = input(
                    "Mostrar productos con stock menor o igual a: ").strip()
                # Valido que el limite sea un entero positivo
                if validar_entero_positivo(limite):
                    # recibo los productos con stock bajo
                    productos = reporte_bajo_stock(db, tbl, limite)
                    if productos:
                        # Si los tengo, imprimo la tabla de productos con stock bajo
                        imprime_tabla(productos)
                    else:
                        print(
                            f"No se encontraron productos con stock menor o igual a {limite}.")
                    pausa()  # pausa para que el usuario vea el reporte antes de limpiar pantalla
                    # una ultima Pregunta si desea realizar una nueva busqueda
                    preferencia = input(
                        "Desea realizar una nueva busqueda (s/n)").strip().lower()
                    print("preferencia:", preferencia)
                    if preferencia != "s":
                        break
        # === OPCIÓN 0: Salir del programa ===
        elif menu_opcion == "0":
            print("Gracias por usar SiGePro - Sistema de Gestión de Productos.")
            pausa()


if __name__ == '__main__':  # Punto de entrada de la aplicación.
    main()

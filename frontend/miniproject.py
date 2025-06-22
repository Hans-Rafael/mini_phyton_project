# Importamos tipos para listas, diccionarios y para indicar que un valor puede ser de varios tipos
from typing import List, Dict

from backend.funciones_productos import(
    validation_numero,
    agregar_producto,
    ver_productos,
    buscar_productos,
    eliminar_producto,
    impresion_respuesta,
    estructurar_error_mensaje
)
#Si quiero importar todas las funciones puedo hacerlo asi:
#  import funciones_productos as fp
## Luego, llamas a las funciones usando el prefijo:
## fp.agregar_producto(productos)

# ### Función Principal del Programa (`main()`)
def main()-> None:
    # Lista para almacenar los productos
    productos:List[Dict] = []

    # Mensaje de bienvenida
    impresion_respuesta(
        "¡Bienvenidos a ***** SiGePro *****, tu aplicación de gestión de productos!")
    # menu del programa(Bucle pirncipal)
    while True:
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
                continuar = input(
                    "¿Deseas agregar otro producto? (s/n): ").lower()
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
                criterios = {}  # Diccionario para almacenar criterios de búsqueda
                busqueda = input(
                    "Ingresa el nombre o categoría a buscar menor a 30 caracteres (dejar vacío para omitir): ").strip().lower()
                # Validación de entrada para la búsqueda
                if len(busqueda) > 30:
                    print("El término de búsqueda debe tener menos de 30 caracteres.")
                    continue
                if busqueda:
                    # Si hay un término de búsqueda, lo agrego al diccionario de criterios
                    criterios['termino'] = busqueda
                # cirterios de precio maximo y minimo
                precio_maximo = input(
                    "Ingresa el precio máximo a buscar (dejar vacío para omitir): ").strip()
                # valido sea un numero entero
                try:
                    if validation_numero(precio_maximo) and precio_maximo != "":
                        criterios['precio_maximo'] = float(precio_maximo)
                except (ValueError, TypeError)as e:
                    print(estructurar_error_mensaje(e))
                except Exception as e:
                  # Manejo genérico para cualquier otro error
                    print(f"Ocurrió un error inesperado: {e}")
            # criterio para precio minimo
                precio_minimo = input(
                    "Ingresa el precio mínimo a buscar (dejar vacío para omitir): ").strip()
                # valido sea un numero decimal
                try:
                    if validation_numero(precio_minimo) and precio_minimo != "":
                        criterios['precio_minimo'] = float(precio_minimo)
                        break
                except (TypeError, ValueError) as e:
                    print(estructurar_error_mensaje(e))
                    continue
                except Exception as e:
                  # Manejo genérico para cualquier otro error
                    print(f"Ocurrió un error inesperado: {e}")
                if not criterios:
                    print("No se ingresaron criterios de búsqueda. Volviendo al menú.")
                    continue  # Volver al inicio del bucle del menú
                # Realizo la búsqueda de productos
                impresion_respuesta(
                    f"Buscando productos con los criterios: {criterios}")
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
                ver_productos(productos)  # ver los productos actuales
                item_borrar = input(
                    "Ingresa el número(s) de los productos a borrar (ej: 1 o 2,3,4). Usa comas para eliminar varios productos o '-x' para volver al menú: :").strip().lower()
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
            impresion_respuesta(
                "Opción inválida. Por favor, elige entre 1 y 5.")
            continue

        # Fin del programa
     # print(">>> Intentando llamar a la función main() <<<") # Línea de depuración
      # mandatorio
if __name__ == "__main__":  # verifica si el script se está ejecutando directamente
    main()

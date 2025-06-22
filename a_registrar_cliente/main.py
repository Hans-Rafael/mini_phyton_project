# Importamos tipos para listas, diccionarios y para indicar que un valor puede ser de varios tipos
from typing import List, Dict, Union

from funciones import( validar_texto, validar_correo, registrar_nuevo_cliente, imprimir_registro_clientes)

# menú permite ingresar los datos de un cliente: nombre, apellido y correo electrónico

# Función Principal del Programa (`main()`)
def main() -> None:
    print("===== Bienvenido al sistema de registro de clientes. =====")
    while True:
        # Aquí va la lógica principal del programa
        # Solicitar datos del cliente
        
        while True:
            nombre = input("Ingrese el nombre del cliente: ").lower().strip()
            # Validar el nombre
            try:
                validar_texto(nombre)
                # registro nombre
                print("Nombre agregado es:", nombre)
                break
            except (TypeError, ValueError, Exception) as e:
                print(f"Error: {e} Por favor, inténtalo de nuevo.")
                continue
        while True:
            apellido = input("Ingrese el apellido del cliente: ").lower().strip()
            try:
                validar_texto(apellido)
                # registro apellido
                print("apellido agregado es:", apellido)
                break
            except (TypeError, ValueError, Exception) as e:
                print(f"Error: {e} Por favor, inténtalo de nuevo.")
                continue
        while True:
            try:
                correo = input("Ingrese el correo electrónico del cliente: ").strip()
                validar_correo(correo)
                print("Correo agregado es:", correo)
                break
            except (TypeError, ValueError, Exception) as e:
                print(f"Error: {e} Por favor, inténtalo de nuevo.")
                continue 
        #Registro del cliente
        registrar_nuevo_cliente(nombre, apellido, correo,"clientes.txt")
        continuar = input("¿Desea agregar otro usuario (s/n)?").lower().strip()
        if continuar != 's':
            #break
            mostrar = input("¿Desea ver como esta el registro o archivo (s/n) ?").lower().strip()
            if mostrar == "s":
                    imprimir_registro_clientes("clientes.txt")
            else:
                break
# verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()

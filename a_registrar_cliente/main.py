# Importamos tipos para listas, diccionarios y para indicar que un valor puede ser de varios tipos
from typing import List, Dict, Union


def validar_texto(n: str) -> bool:
    if not isinstance(n, str):
        raise TypeError(f"{n} debe ser un setring")
    elif not n or len(n) < 2 or len(n) > 50:
        raise ValueError(
            f"La entrada '{n}' debe tener entre 2 y 50 caracteres. Longitud actual: {len(n)}")
    else:
        return True
def validar_correo(e:str)-> bool:
    """
    Hola
    """
    e.lower().strip()
    correo = e.split("@") # para ver si hay caracteres antes del @
    if not isinstance(e,str):
        raise TypeError (f"la entrada {e} debe ser un string")
    elif not e or len(e) > 50 or "@" not in e or "." not in e or e.startswith('@') or e.endswith('@') :
        raise ValueError (f"el correo {e} no es valido, revisar e intentar de nuevo")
    elif len(correo) != 2 :
        raise ValueError (f"el correo {e} no es valido, revisar e intentar de nuevo")
    else:
        return True
# menu permite ingresar los datos de un cliente: nombre, apellido y correo electrónico

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
                print("Nombre es:", nombre)
                break
            except (TypeError, ValueError, Exception) as e:
                print(f"Error: {e} Por favor, inténtalo de nuevo.")
                continue
        while True:
            apellido = input("Ingrese el apellido del cliente: ").lower().strip()
            try:
                validar_texto(apellido)
                # registro nombre
                print("apellido es:", apellido)
                break
            except (TypeError, ValueError, Exception) as e:
                print(f"Error: {e} Por favor, inténtalo de nuevo.")
                continue
        while True:
            try:
                correo = input("Ingrese el correo electrónico del cliente: ").strip()
                validar_correo(correo)
                print("Correo electrónico es:", correo)
                break
            except (TypeError, ValueError, Exception) as e:
                print(f"Error: {e} Por favor, inténtalo de nuevo.")
                continue        # informar que se guardo
        continuar = input("¿Desea agregar otro usuario (s/n)?")
        if continuar != 's':
            break

        # preguntar si desea ver como quedo el registro total ahora:
# verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()

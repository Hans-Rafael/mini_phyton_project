# Importamos tipos para listas, diccionarios y para indicar que un valor puede ser de varios tipos
from typing import List, Dict, Union

#validar texto
def validar_texto(n: str) -> bool:
    """
    Args:
        n (str): La cadena de texto a validar.
    Returns:
        bool: True si la cadena es válida, False en caso contrario.
    Raises:
        TypeError: Si la entrada no es un string.
        ValueError: Si la cadena está vacía o no cumple con las restricciones de longitud.
    Descripción:
        Esta función valida que la entrada sea un string no vacío con una longitud entre 2 y 50 caracteres.
        Si la entrada no cumple con estas condiciones, se lanzan excepciones apropiadas.
    """
    if not isinstance(n, str):
        raise TypeError(f"{n} debe ser un setring")
    elif not n or len(n) < 2 or len(n) > 50:
        raise ValueError(
            f"La entrada '{n}' debe tener entre 2 y 50 caracteres. Longitud actual: {len(n)}")
    else:
        return True
#Validar correo
def validar_correo(e:str)-> bool:
    """
    Args:
        e (str): La dirección de correo electrónico a validar.
    Returns:
        bool: True si el correo es válido, False en caso contrario.
    Raises:
        TypeError: Si la entrada no es un string.
        ValueError: Si el correo no cumple con las restricciones de formato.
    Descripción:
        Esta función valida que la dirección de correo electrónico tenga un formato correcto.
    """
    e.lower().strip()
    correo = e.split("@") # para ver si hay caracteres antes del @
    if not isinstance(e,str):
        raise TypeError (f"la entrada {e} debe ser un string")
    elif not e or len(e) > 50 or "@" not in e or "." not in e or e.startswith('@') or e.endswith('@') :
        raise ValueError (f"el correo {e} no es valido")
    elif len(correo) != 2 :
        raise ValueError (f"el correo {e} no es valido")
    else:
        return True
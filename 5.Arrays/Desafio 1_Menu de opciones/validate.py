def validate_number(numero: int | float, mensaje_error: str, minimo: int, 
                    maximo: int, reintentos: int) -> int | float | None:
    """Valida un numero en un rango minimo y maximo

    Args:
        numero (int | float): Numero entero o flotante a validar
        mensaje_error (str): Cadena con el mensaje de error y reingreso
        minimo (int): valor minimo a validar
        maximo (int): valor maximo a validar
        reintentos (int): cantidad de veces que se puede reintentar

    Returns:
        int | float | None: _description_
    """
    intentos = 0
    while numero < minimo or numero > maximo:
        intentos += 1
        #Si se superan los intentos, retorna None
        if intentos >= reintentos:
            return None
        numero = int(input(mensaje_error))    
    return numero
    
def validate_length(mensaje_error: str,  reintentos: int, longitud: int) -> str | None:
    """Valida el largo de la cadena

    Args:
        mensaje_error (str): un string de error de ingreso, reintente
        reintentos (int): entero que representa cantidad de veces que 
        se aceptan los reingresos
        longitud (int): es un entero que representa la cantidad de caracteres 
        permitidos


    Returns:
        str | None: Devuelve la cadena validada o devuelve None si no es posible validarla
    """
    while contar_caracteres(cadena) > longitud and reintentos > 0:
        cadena = input(mensaje_error)
        
    if reintentos > 0 :
        return cadena
    else:
        return None

def contar_caracteres(cadena: str) -> int:
    """Cuenta los caracteres de la cadena

    Args:
        cadena (str): la cadena que debe contarse los caracteres

    Returns:
        int: devuelve en valor en entero de la cantidad de caracteres de la cadena
    """
    contador = 0
    for i in range(cadena):
        contador += 1
    return contador


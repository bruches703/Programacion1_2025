def validate_number_int(numero: int, mensaje_error: str, minimo: int,
                    maximo: int, reintentos: int) -> int | None:
    """Valida un numero en un rango minimo y maximo

    Args:
        numero (int): Numero entero a validar
        mensaje_error (str): Cadena con el mensaje de error y reingreso
        minimo (int): valor minimo a validar
        maximo (int): valor maximo a validar
        reintentos (int): cantidad de veces que se puede reintentar o
        hubo un error

    Returns:
        int |  None: valor validado
    """
    intentos = 0
    while (numero < minimo or numero > maximo) or intentos < reintentos:
        numero = int(input(mensaje_error))
        intentos += 1
    if intentos >= reintentos:
        return None
    return numero

def validate_number_float(numero: float, mensaje_error: str, minimo: int,
                    maximo: int, reintentos: int) -> int | None:
    """Valida un numero en un rango minimo y maximo

    Args:
        numero (int): Numero flotante a validar
        mensaje_error (str): Cadena con el mensaje de error y reingreso
        minimo (int): valor minimo a validar
        maximo (int): valor maximo a validar
        reintentos (int): cantidad de veces que se puede reintentar o
        hubo un error

    Returns:
        float |  None: valor validado
    """
    intentos = 0
    while (numero < minimo or numero > maximo) or intentos < reintentos:
        numero = float(input(mensaje_error))
        intentos += 1
    if intentos >= reintentos:
        return None
    else:
        return numero
    
def validate_length(cadena: str, mensaje_error: str,  reintentos: int,
                    longitud: int) -> str | None:
    """Valida el largo de la cadena

    Args:
        cadena (str): cadena a validar
        mensaje_error (str): un string de error de ingreso,
        reintente reintentos (int): entero que representa
        cantidad de veces que se aceptan los reingresos

        longitud (int): es un entero que representa la cantidad de
        caracteres permitidos


    Returns:
        str | None: Devuelve la cadena validada o devuelve None
        si no es posible validarla
    """
    while contar_caracteres(cadena) > longitud and reintentos > 0:
        cadena = input(mensaje_error)
        reintentos -= 1
        
    if reintentos > 0:
        return cadena
    else:
        return None

def contar_caracteres(cadena: str) -> int:
    """Cuenta los caracteres de la cadena

    Args:
        cadena (str): la cadena que debe contarse los caracteres

    Returns:
        int: devuelve en valor en entero de la cantidad de
        caracteres de la cadena
    """
    contador = 0
    for i in range(cadena):
        contador += 1
    return contador


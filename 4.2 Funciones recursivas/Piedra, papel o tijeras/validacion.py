def validate_number(numero: int | float, mensaje_error: str, minimo: int, 
                    maximo: int) -> int | float | None:
    """Valida un numero en un rango minimo y maximo

    Args:
        numero (int | float): Numero entero o flotante a validar
        mensaje_error (str): Cadena con el mensaje de error y reingreso
        minimo (int): valor minimo a validar
        maximo (int): valor maximo a validar

    Returns:
        int | float | None: Retorna el numero validado o None de no ser un numero
    """

    if isinstance(numero, float):
        while numero < minimo or numero > maximo:
            numero = float(input(mensaje_error))
    elif isinstance(numero, int):
        while numero < minimo or numero > maximo:
            numero = int(input(mensaje_error))
    else:
        return None
    return numero
    
def validate_length(mensaje_error: str, longitud: int) -> str:
    """Valida el largo de la cadena

    Args:
        mensaje_error (str): un string de error de ingreso, reintente
        longitud (int): es un entero que representa la cantidad de caracteres 
        permitidos


    Returns:
        str : Devuelve la cadena validada
    """
    while contar_caracteres(cadena) > longitud:
        cadena = input(mensaje_error)
        
    return cadena


def contar_caracteres(cadena: str) -> int:
    """Cuenta los caracteres de la cadena

    Args:
        cadena (str): la cadena que debe contarse los caracteres

    Returns:
        int: devuelve en valor en entero de la cantidad de caracteres de la cadena
    """
    contador = 0
    for i in range (cadena):
        contador += 1
    return contador
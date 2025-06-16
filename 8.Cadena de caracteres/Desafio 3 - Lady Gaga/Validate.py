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
    while (numero < minimo or numero > maximo) and intentos < reintentos or type(numero) is not int:
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
    
def validate_length(cadena: str, mensaje_error: str,  reintentos: int, longitud: int, longitud_min: int=0) -> str | None:
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
    while (len(cadena) < longitud_min or len(cadena) > longitud) and reintentos > 0 or not validar_caracteres(cadena):
        if not validar_caracteres(cadena):
            print("Error, la cadena no puede contener numeros o caracteres especiales.")
        cadena = input(mensaje_error)
        reintentos -= 1

    if reintentos > 0 :
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

def validar_caracteres(cadena: str) -> bool:
    """Valida una cadena de caracteres, corrabora que no
    contenga numeros
    Args:
        cadena (str): cadena a validar

    Returns:
        bool: True si la cadena es valida, False si no lo es
    """
    for caracter in cadena:
        # Comprueba si el caracter es una letra mayuscula, minuscula o un espacio
        if (ord(caracter) < 65 or ord(caracter) > 90) and (ord(caracter) < 97 or ord(caracter) > 122) and ord(caracter) != 32:
            return False
    return True

def comparar_cadenas_ignorando_case(cadena1: str, cadena2: str) -> bool:
    """Compara dos cadenas ignorando mayusculas y minusculas

    Args:
        cadena1 (str): primera cadena a comparar
        cadena2 (str): segunda cadena a comparar

    Returns:
        bool: True si las cadenas son iguales ignorando mayusculas y minusculas,
        False si no lo son
    """
    # Si las cadenas no tienen la misma cantidad de caracteres, no son iguales y
    # se termina la comparacion
    if len(cadena1) != len(cadena2):
        return False
    
    for i in range(len(cadena1)):
        # Comparo que el caracter acutal sea igual, luego compara que el caracter sea igual pero con mayuscula o minuscula
        # por ultimo compara que sean iguales pero en minuscual, por medio de codigo ascii
        if ord(cadena1[i]) != ord(cadena2[i]) and ord(cadena1[i]) != ord(cadena2[i]) + 32 and ord(cadena1[i]) != ord(cadena2[i]) - 32:
            return False
    return True

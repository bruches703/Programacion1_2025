from Validate import *
def get_int(mensaje: str, mensaje_error: str, minimo: int,
            maximo: int, reintentos: int) -> int | None:
    """Esta función pide un numero entero y lo valida, dando un mensaje de
    peticion, uno de error, el rango aceptable y la cantidad de intentos

    Args:
        mensaje (str): es un string de peticion de ingreso

        mensaje_error (str): un string de error de ingreso, reintente

        minimo (int): entero que representa valor minimo aceptable para a
        validar el numero ingresado

        maximo (int): entero que representa valor maximo aceptable para a
        validar el numero ingresado

        reintentos (int): entero que representa cantidad de veces que se
        aceptan los reingresos

    Returns:
        int | None: regresa un numero entero ya validado o None si no hay
        un valor valido
    """
    # Mientras haya reintentos, se repite el bucle para pedir un numero
    while reintentos > 0:
        entrada = input(mensaje)
        # Intenta convertir la entrada a un entero, si falla, muestra el mensaje de error
        try:
            numero = int(entrada)
        except ValueError:
            print(mensaje_error)
            reintentos -= 1
            continue
        # Valida el numero mediante la funcion
        resultado = validate_number_int(numero, mensaje_error, minimo, maximo, reintentos)
        if resultado is not None:
            return resultado
        reintentos -= 1
    return None

def get_string(mensaje: str, mensaje_error: str, longitud_min: int,
               longitud: int, reintentos: int) -> str | None:
    """Esta función pide el ingreso de una palabra, letra o frase y lo valida,
    dando un mensaje de peticion, uno de error, longitud aceptable y la
    cantidad de intentos

    Args:
        mensaje (str): es un string de peticion de ingreso

        mensaje_error (str): un string de error de ingreso, reintente

        longitud_min (int): entero que representa valor minimo aceptable

        longitud (int): entero que representa valor maximo aceptable para a
        validar la lingitud de la cadena

        reintentos (int): entero que representa cantidad de veces que se
        aceptan los reingresos

    Returns:
        str | None: regresa una cadena ya validada o None si no hay un
        valor valido
    """
    cadena = input(mensaje)
    return validate_length(cadena, mensaje_error, reintentos, longitud, longitud_min)

    

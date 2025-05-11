import validacion

def get_int(mensaje: str, mensaje_error: str, minimo: int, 
            maximo: int) -> int | None:
    """Esta función pide un numero entero y lo valida, dando un mensaje de peticion, uno de error, el rango aceptable 
    y la cantidad de intentos

    Args:
        mensaje (str): es un string de peticion de ingreso
        mensaje_error (str): un string de error de ingreso, reintente
        minimo (int): entero que representa valor minimo aceptable para a validar el numero ingresado
        maximo (int): entero que representa valor maximo aceptable para a validar el numero ingresado

    Returns:
        int | None: regresa un numero entero ya validado o None si hay un error
    """
    numero = validacion.validate_number(int(input(mensaje)),mensaje_error, minimo, maximo)
    return numero

def get_float(mensaje: str, mensaje_error: str, minimo: int, 
              maximo: int) -> float | None:
    """Esta función pide un numero flotante y lo valida, dando un mensaje de peticion, uno de error, el rango aceptable 
    y la cantidad de intentos

    Args:
        mensaje (str): es un string de peticion de ingreso
        mensaje_error (str): un string de error de ingreso, reintente
        
        minimo (int): entero que representa valor minimo aceptable para a 
        validar el numero ingresado

        maximo (int): entero que representa valor maximo aceptable para a 
        validar el numero ingresado

    Returns:
        float | None: regresa un numero flotante ya validado o None si no hay 
        un valor valido
    """
    numero = validacion.validate_number(float(input(mensaje)),mensaje_error, minimo, maximo)

def get_string(mensaje: str, mensaje_error: str,  reintentos: int, longitud: int) -> str | None:
    """Pide una cadena de caracteres y lo valida dependiendo la longitud deseada al ingresarlo

    Args:
        mensaje (str): es un string de peticion de ingreso
        mensaje_error (str): un string de error de ingreso, reintente
        reintentos (int): entero que representa cantidad de veces que 
        se aceptan los reingresos
        longitud (int): es un entero que representa la cantidad de caracteres 
        permitidos

    Returns:
        str | None: retorna un string que esta validado por su longitud, o None si no puede validarse
    """
    cadena = input(mensaje)
    contador = 0
    intentos = reintentos
    for i in cadena:
        contador =+ 1
    while contador > longitud and intentos > 0:
        cadena = input(mensaje_error)
        for i in cadena:
            contador =+ 1
    if intentos > 0 :
        return cadena
    else:
        return None


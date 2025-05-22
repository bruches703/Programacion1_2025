import validate
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
    numero = int(input(mensaje))
    return validate.validate_number_int(numero, mensaje_error,
                                        minimo, maximo, 10)

def get_float(mensaje: str, mensaje_error: str, minimo: int,
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
    numero = float(input(mensaje))
    return validate.validate_number_int(numero, mensaje_error,
                                      minimo, maximo, 10)

def get_float(mensaje: str, mensaje_error: str, minimo: int,
              maximo: int, reintentos: int) -> float | None:
    """Esta función pide un numero flotante y lo valida, dando un mensaje de
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
        float | None: regresa un numero flotante ya validado o None si no
        hay un valor valido
    """
    numero = float(input(mensaje))
    numero = validate.validate_number_float(numero, "Error de ingreso, reingrese: ",
                                      minimo, maximo, 10)
    return numero

def get_string(mensaje: str, mensaje_error: str, longitud: int,
               reintentos: int) -> str | None:
    """Esta función pide el ingreso de una palabra, letra o frase y lo valida,
    dando un mensaje de peticion, uno de error, longitud aceptable y la
    cantidad de intentos

    Args:
        mensaje (str): es un string de peticion de ingreso

        mensaje_error (str): un string de error de ingreso, reintente

        longitud (int): entero que representa valor maximo aceptable para a
        validar la lingitud de la cadena

        reintentos (int): entero que representa cantidad de veces que se
        aceptan los reingresos

    Returns:
        str | None: regresa un numero flotante ya validado o None si no hay un
        valor valido
    """
    cadena = input(mensaje)
    return validate.validate_length(cadena, mensaje_error, reintentos,
                                    longitud)

def menu() -> int:
    """Muestra un menu por pantalla para que el usuario elija una opcion

    Returns:
        int: opcion escogida por el usuario
    """
    pass
    print("0-Salir")
    return get_int("Ingrese opcion: ", "Opcion incorrecta, reingrese: ", 0, 2, 10)
    

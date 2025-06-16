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
        int | None: regresa un numero entero ya validado o None si no hay un valor valido
    """
    numero = int(input(mensaje))
    numero = validate.validate_number(numero, "Error de ingreso, reingrese: ", minimo, maximo, 10)
    return numero

def new_Array(cantidad_elementos: int) -> list:
    """Crea un arreglo inicializado con 0 con la cantidad de elementos indicada en parametro

    Args:
        cantidad_elementos (int): cantidad de elementos del arreglo

    Returns:
        list: array de enteros con cantidad de elementos ingresados por parametro
    """
    nuevo_array = [0] * cantidad_elementos

    return nuevo_array 

def crear_array(mensaje: str, mensaje_error: str, minimo: int, 
                maximo: int, reintentos: int, cantidad_elementos: int) -> list | None:
    """Crea un arreglo y permite el ingreso por consola de los elementos

    Args:
        mensaje (str): Cadena de caracteres que se muestra para el ingreso de elementos
        mensaje_error (str): Cadena de caracteres que muestra error si no se puede validar
        minimo (int): valor minimo a ingresar (-1000)
        maximo (int): valor maximo a ingresar (1000)
        reintentos (int): cantidad
        cantidad_elementos (int): cantidad de elementos que tendra el array

    Returns:
        list | None: Retorna la lista de enteros, o None si hay algun fallo
    """
    
    array_de_numeros = new_Array(cantidad_elementos)
    for i in range(cantidad_elementos):
        elemento = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
        if elemento == None:
            print("Error de ingreso, finaliza el programa")
            return None
        else:
            array_de_numeros[i] = elemento
    return array_de_numeros


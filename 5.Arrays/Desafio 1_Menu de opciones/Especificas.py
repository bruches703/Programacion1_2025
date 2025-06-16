def comprobar_opcion_menu(opcion: int, array: list) -> int:
    """Comprueba la eleccion y retorna la opcion validada

    Args:
        opcion (int): opcion escogida
        flag (bool): Esta en True cuando se ingresaron los valores en la opcion 1, 
                    en False si aun no se ingresaron

    Returns:
        int: Devuelve la opcion ya validada:
            1: si no se ingresaron los valores al vector
            9: si se excede los 10 intentes de ingreso
            opcion: del valor 2-7 si se ingreso todo de manera correcta
    """
    if len(array) == 0 and opcion != 1: 
    # Se dirige a la opcion 1 si es la opcion escogida o si no hay elemenmtos en el array
        print("No se ingresaron valores aun, se redirige al ingreso\n")
        input("Presione tecla enter para continuar...")
        return 1
    elif opcion is None:
    # Si superan los 10 intentos de reingreso, cierra el programa
        print("Error, cantidad de ingresos exedidos\n")
        input("Presione tecla enter para continuar...")
        return 8
    else:
    # Si hay elementos devuelve la opcion escogida
        return opcion
    
def contador_positivos_o_negativos(array: list, opcion: int) -> int | None:
    """Comprueba si necesita calcular los positivos o los negativos y devuelve la cantaidad de elementos de ese tipo

    Args:
        array (list): array de enteros a buscar los valores positivos o negativos
        opcion (int): opcion para contar los tipos de valores de los numeros del array
                0: cuenta los ceros
                1: cuenta los positivos
                2: cuenta los negativos

    Returns:
        int | None: retorna la cantidad de elementos positivos o negativos, o None si hubo algun error
    """
    if len(array) == 0: 
        return None
    else:
        return contador_iguales(array, opcion)

def contador_iguales(array: list, opcion: int) -> int:
    """Cuenta los positivos, los negativos o los ceros

    Args:
        array (list): array de enteros a buscar los valores positivos o negativos
        opcion (int): opcion para contar los tipos de valores de los numeros del array
                0: cuenta los ceros
                1: cuenta los positivos
                2: cuenta los negativo
    Returns:
        int: retorna la cantidad de elementos positivos, negativos o ceros
    """
    contador = 0
    if opcion == 0:
        # cuenta los 0 en el array
        for elemento in array:
            if elemento == 0:
                contador += 1
    elif opcion == 1:
        # cuenta los positivos en el array
        for elemento in array:
            if elemento > 0:
                contador += 1
    else:
        # cuenta los negativos en el array
        for elemento in array:
            if elemento < 0:
                contador += 1 
    return contador

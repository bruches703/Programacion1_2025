import ingresos
from validate import validate_length

def new_Array(cantidad_elementos: int = 0, elemento: any = 0) -> list:
    """Crea un arreglo inicializado con 0 con la cantidad
    de elementos indicada en parametro

    Args:
        cantidad_elementos (int, optional): cantidad de
        elementos del arreglo. Defaults to 0.
        elemento (any, optional): elemento para
        inicializar los elementos. Defaults to 0

    Returns:
        list: array de enteros con cantidad de
        elementos ingresados por parametro
    """
    nuevo_array = [elemento] * cantidad_elementos
    return nuevo_array

def crear_array(mensaje: str, mensaje_error: str,
                minimo: int, maximo: int, reintentos: int,
                cantidad_elementos: int) -> list | None:
    """Crea un arreglo y permite el ingreso por consola de los elementos

    Args:
        mensaje (str): Cadena de caracteres que se
        muestra para el ingreso de elementos

        mensaje_error (str): Cadena de caracteres que
        muestra error si no se puede validar

        minimo (int): valor minimo a ingresar (-1000)

        maximo (int): valor maximo a ingresar (1000)

        reintentos (int): cantidad

        cantidad_elementos (int): cantidad de elementos que tendra el array

    Returns:
        list | None: Retorna la lista de enteros, o None si hay algun fallo
    """
    array_de_numeros = new_Array(cantidad_elementos)
    for i in range(cantidad_elementos):
        elemento = ingresos(mensaje, mensaje_error, minimo, maximo, reintentos)
        if elemento == None:
            print("Error de ingreso, finaliza el programa")
            return None
        else:
            array_de_numeros[i] = elemento
    return array_de_numeros

def completar_caracteres_restantes(cadena: str, longitud: int,
                                   caracter: str = " ") -> str:
    """Completa la cadena de caracteres con caracteres
    definido por el usuario, o por default
    con espacios

    Args:
        cadena (str): Palabra o frase a completar
        longitud (int): Largo total de la cadena
        caracter (str, optional): Se completara con el caracter.
        Defaults to " ".

    Returns:
        str: retorna la cadena con el caracter dado como referencia hasta
        llegar a la longitud
    """
    caracter = validate_length(caracter,
                               "Caracter demasiado larg o corto. Solo ingrese un caracter: ",
                               10, 1)
    for i in range(len(cadena) < longitud):
        if len(cadena) < 20:
            cadena = cadena + caracter
        else:
            break
    return cadena

def obtener_indice(lista: list, elemento: any, indice_inicial: int=0) -> int | None:
    """Encuentra el elemento y devuelve el indice donde
    esta posicionado
    Args:
        lista (list): vector donde buscar el elemento
        elemento (any): elemento a buscar en el vector
        indice_inicial (int, optional): indice inicial donde buscar. Defaults to 0.

    Returns:
        int | None: devuelve un int que representa el indicie
        del elemento, o None si no lo encuentra
    """
    for i in range(indice_inicial, len(lista), 1):
        if elemento == lista[i]:
            return i
    return None

def obtener_minimo(lista: list) -> int:
    """Busca el valor minimo de la lista

    Args:
        lista (list): lista de enteros

    Returns:
        int: el valor minimo de o los elementos
    """
    flag = True
    minimo = 0
    for elemento in lista:
        if flag or elemento < minimo:
            minimo = elemento
            flag = False
    return minimo

def obtener_maximo(lista: list) -> int:
    """Busca el valor maximo de la lista

    Args:
        lista (list): lista de enteros

    Returns:
        int: el valor maximo de o los elementos
    """
    flag = True
    maximo = 0
    for elemento in lista:
        if flag or elemento > maximo:
            maximo = elemento
            flag = False
    return maximo

def sumar_elementos(lista: list) -> int:
    """Suma todos los elementos del vector

    Args:
        lista (list): matr

    Returns:
        int: _description_
    """
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

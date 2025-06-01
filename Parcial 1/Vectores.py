from Ingresos import get_int
from Validate import validate_length
from Funciones_Generales import calcular_porcentaje

def crear_array(cantidad_elementos: int = 0, elemento: any = 0) -> list:
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

def crear_cargar_array(mensaje: str, mensaje_error: str,
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
    # Crea un array de la cantidad de elementos pasados por parametro
    array_de_numeros = crear_cargar_array(cantidad_elementos)
    # Recorre el vector y pide el ingreso del entero
    for i in range(cantidad_elementos):
        elemento = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
        # Si el elemento es None, se termina el ingreso
        if elemento == None:
            print("Error de ingreso, finaliza el programa")
            return None
        else:
            array_de_numeros[i] = elemento
    return array_de_numeros

def obtener_indice(lista: list, elemento: any,
                   indice_inicial: int = 0) -> int | None:
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
    if len(lista) == 0:
        return -1
    else: 
        minimo = lista[0]
        for elemento in lista:
            if elemento < minimo:
                minimo = elemento
    return minimo

def obtener_maximo(lista: list | float) -> int | float:
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
        lista (list): vector de enteros a sumar

    Returns:
        int: suma de los elementos del vector
    """
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def porcentaje_vector(lista: list, valor_parcial: int | float) -> float:
    """Calcula el porcentaje de la lista

    Args:
        lista (list): lista a calcular el porcentaje
        valor_parcial(int | float): valor a calcualr el porcentaje

    Returns:
        float: porcentaje de la lista
    """
    suma = sumar_elementos(lista)
    porcentaje = calcular_porcentaje(suma, valor_parcial)
    return porcentaje

def mostrar_elementos(lista: list) -> bool:
    """Muestra los elementos de la lista

    Args:
        lista (list): lista a mostrar

    Returns:
        bool: devuelve True si se imprime correctamente,
        False si hubo algun error
    """
    if len(lista) == 0:
        return False
    else:
        for elemento in list:
            print(elemento)
        return True
    
def promedio_vector(lista: list) -> float:
    """Calcula el promedio de los elementos del vector

    Args:
        lista (list): vector de enteros a promediar

    Returns:
        float: promedio de los elementos del vector
    """
    if len(lista) == 0:
        return 0.0
    else:
        suma = sumar_elementos(lista)
        promedio = suma / len(lista)
        return promedio

def ordenamiento_burbujeo_ascendente(lista: list) -> list:
    """Ordena un vector de enteros usando el metodo burbuja
    en orden ascendente

    Args:
        lista (list): lista de enteros a ordenar

    Returns:
        list: lista ordenada
    """
    if len(lista) == 0:
        return []
    else:
        auxiliar = " "
        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if lista[j] > lista[j + 1]:
                    auxiliar = lista[i]
                    lista[j] = lista[i]
                    lista[i] = auxiliar       
    return lista

def ordenamiento_burbujeo_desendente(lista: list) -> list:
    """Ordena un vector de enteros usando el metodo burbuja
    en orden descendente

    Args:
        lista (list): lista de enteros a ordenar

    Returns:
        list: lista ordenada
    """
    if len(lista) == 0:
        return []
    else:
        auxiliar = " "
        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if lista[j] < lista[j + 1]:
                    auxiliar = lista[i]
                    lista[j] = lista[i]
                    lista[i] = auxiliar       
    return lista

def ordenar_vector_numerico(lista: list, opcion: int) -> list:
    """Ordena un vector de enteros, 1- Ascendente, 2- Descendente

    Args:
        lista (list): lista de enteros a ordenar
        opcion (int): 1- Ascendente, 2- Descendente

    Returns:
        list: lista ordenada
    """
    if len(lista) == 0:
        return []
    else:
        if opcion == 1:
            ordenamiento_burbujeo_ascendente(lista)
        elif opcion == 2:
            ordenamiento_burbujeo_desendente(lista)
        else:
            print("Opcion invalida, no se ordena el vector.")
        return lista

def buscar_elemento(lista: list, elemento: any, inicio: int=0) -> int :
    """Busca un elemento en la lista y devuelve los indices

    Args:
        lista (list): lista donde buscar el elemento
        elemento (any): elemento a buscar en la lista
        inicio (int, optional): punto de partida donde buscar. Defaults to 0.

    Returns:
        int: devuelve el indice del elemento si lo encuentra,
        -1 si no lo encuentra
    """
    for i in range(inicio, len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def ordenar_vector_alfabeticamente(lista: list, opcion: int) -> list:
    """Ordena un vector de cadenas alfabeticamente,
        1- Ascendente
        2- Descendente

    Args:
        lista (list): lista de cadenas a ordenar

    Returns:
        list: lista ordenada alfabeticamente
    """
    if len(lista) == 0:
        return []
    else:
        if opcion == 1:
           ordenamiento_burbujeo_ascendente(lista) 
        elif opcion == 2:
            lista.sort(reverse=True)
        else:
            print("Opcion invalida, no se ordena el vector.")
        return lista
     
def copiar_vector(lista: list) -> list:
    """Copia un vector y devuelve una copia

    Args:
        lista (list): lista a copiar

    Returns:
        list: copia del vector
    """
    if len(lista) == 0:
        return []
    else:
        copia = []
        for i in range(len(lista)):
            copia += [lista[i]]
    return copia
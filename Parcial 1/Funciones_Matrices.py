from Funciones_Inputs import *
from Funciones_Vectores import *

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """Inicializa la matriz

    Args:
        cantidad_filas (int): cantidad de filas
        cantidad_columnas (int): cantidad de columnas
        valor_inicial (any): lo que se le puede cargar

    Returns:
        list: devuelve la nueva matriz
    """
    matriz = []
    for i in range(cantidad_filas):
            fila = [valor_inicial] * cantidad_columnas
            matriz += [fila]
    return matriz

def carga_matriz_secuencial(matriz: list) -> bool:
    """Carga secuencial de una matriz

    Args:
        matriz (list): Matriz que se le cargara los datos
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            matriz[fila][columna] = get_int("Ingrese numero: ", "Error, reingrese: ", 1, 10, 10)
    return True 

def cargar_matriz_aleatoriamente(matriz: list) -> None:
    """Carga un dato en una posicion de la matriz

    Args:
        matriz (list): Matriz que se le cargara los datos
    """
    seguir = "s"
    while seguir == "s":
        fila = get_int("Ingrese indice de fila: ", "Error, indice no valido. Reingrese: ",
                                0, len(matriz)-1, 10)
        columna = get_int("Ingrese indice de columna: ", "Error, indice no valido. Reingrese: ",
                                0, len(matriz[0])-1, 10)
        dato = int(input("Ingrese el numero: "))
        matriz[fila][columna] = dato
        seguir = get_string("Desea seguir cargando? S/N: ", "Error, reingrese S/N: ", 1, 10).lower

def buscar_valor_entero(matriz: list, valor: int) -> None:
    """Busca un valor entero en la matriz

    Args:
        matriz (list): Matriz a buscar el elemento
        valor (int): Valor a buscar en la matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontro el numero en la fila {i} columna {j}!")

def contar_elementos_matriz(matriz:list) -> int:
    """Cuenta la cantidad de elementos de una matriz

    Args:
        matriz (list): matriz a contar los elementos

    Returns:
        int: la cantidad de elementos de la matriz en entero
    """
    if len(matriz) == 0:
        return 0
    else:
        cantidad_filas = len(matriz)
        cantidad_columnas = len(matriz[0])
        cantidad_elementos = cantidad_columnas * cantidad_filas
    return cantidad_elementos

def sumar_matriz(matriz: list) -> int:
    """Suma todos los elementos de la matriz

    Args:
        matriz (list): Matriz a sumar

    Returns:
        int: la suma de todos los elementos de la matriz
    """
    suma = 0
    for fila in matriz:
        suma = sumar_elementos(fila)
    return suma

def mostrar_matriz(matriz: list) -> None:
    """Muestra la matriz por pantalla

    Args:
        matriz (list): Matriz a mostrar
    """
    if len(matriz) == 0:
        print("La matriz esta vacia.")
    else:
        for fil in range(len(matriz)):
            for col in range(len(matriz[fil])):
                print(f"{matriz[fil][col]}",end=" ")
            print("")

def fila_valor_minimo(matriz: list) -> int:
    """Suma las filas de una matriz y devuelve el minimo

    Args:
        matriz (list): Matriz a buscar el valor minimo

    Returns:
        int: devuelve el valor minimo sumando los elementos de cada fila
    """
    if len(matriz) == 0:
        return -1
    else:
        minimo = obtener_minimo(matriz[0])
        for i in range(len(matriz)):
            if obtener_minimo(matriz[i]) < minimo:
                minimo = obtener_minimo(matriz[i])
    return minimo

def copiar_matriz(lista: list) -> list:
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
            copia += [copiar_vector(lista[i])]
    return copia
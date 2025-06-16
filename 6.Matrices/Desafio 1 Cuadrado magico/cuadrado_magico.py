import matrices
import random
import ingresos

def crear_matriz() -> list:
    """Crea una matriz de dimensiones que defina el usuario

    Returns:
        list: retorna la matriz inicializada en 0
    """
    filas = ingresos.get_int("Ingrese cantidad de filas: ", "Error, reingrese cantidad de filas",
                             1,10,10)
    columnas = ingresos.get_int("Ingrese cantidad de columnas: ", "Error, reingrese cantidad de columnas",
                             1,10,10)
    matriz = []
    for fila in range(filas):
        fila = [0] * columnas
        matriz += [fila]
    return matriz

def constante_magica(matriz: list) -> int:
    """Calcula la constante mágica

    Args:
        matriz (list): matriz que se necesita calcular la constante

    Returns:
        int : retorna el valor de la constante magica
    """
    n = len(matriz)
    return (n*( n**2 + 1 )) // 2

def validar_tamaño_matriz(matriz: list) -> bool:
    """Valida el tamaño de la matriz para que sea nxn
    Args:
        matriz (list): matriz a validar
    Return
        bool: Retorna True si tiene misma cantidad de filas que columnas
    """

    return len(matriz) == len(matriz)

def ingresar_valores(matriz: list) -> list:
    """Ingresa los valores de la matriz

    Args:
        matriz (list): matriz a ingresar los valores
    """
    if len(matriz) > 0:
        matriz = matrices.inicialziar_matriz(len(matriz), len(matriz), 0)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                elemento = int(input("Ingrese elemento: "))
                while validar_ingresados(matriz, elemento):
                    elemento = int(input("El elemento se repite, reingrese: "))
                matriz[i][j] = elemento
    return matriz

def ingresar_valores_aleatorios(matriz: list) -> bool:
    """Ingresa los valores de la matriz

    Args:
        matriz (list): matriz a ingresar los valores
    """
    if validar_tamaño_matriz(matriz):
        n = len(matriz)
        numeros = list(range(1, n**2 + 1))
        random.shuffle(numeros)
        index = 0
        for i in range(n):
            for j in range(n):
                matriz[i][j] = numeros[index]
                index += 1
        return True
    else:
        return False

def validar_ingresados(matriz: list, elemento: int) -> bool:
    """Valida el ingreso de los elementos, que no se repitan

    Args:
        matriz (list): matriz con elementos a validar
        elemento (int): elemento a buscar en la matriz
    Returns:
        bool: devuelve True si los elementos no se repiten
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == elemento:
                return True
    return False

def sumar_valores_matriz(matriz: list) -> bool:
    """Suma los valores de las filas, columnas y la diagonal principal

    Args:
        matriz (list): matriz a sumar los valores

    Returns:
        bool: Devuelve True si el valor de las tres sumas son iguales, dando la constante magica
    """
    if sumar_valores_matriz(matriz):
        suma_fila = 0
        suma_columna = 0
        suma_diagonal = 0
        
        for i in range(len(matriz)):
            #Suma los valores de la fila y columna, teniendo en cuenta que tienen el mismo largo
            suma_fila += matriz[i][0]
            suma_columna += matriz[0][i]
            for j in range(len(matriz[i])):
                #Si la fila y columna son las misma <Ejemplo: [0][0] [1][1] [2][2]> suma, sabiendo
                #que forman la diagonal
                if i == j:
                    suma_diagonal += matriz[i][j]
    # Si todas las sumas son iguales, la diagonal es magica
        return suma_fila == suma_columna and suma_fila == suma_diagonal
    else:
        return False
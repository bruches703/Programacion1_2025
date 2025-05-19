import ingresos
def crear_matriz(cantidad_filas: int, cantidad_columnas: int) -> list:
    """Inicializa la matriz

    Args:
        cantidad_filas (int): cantidad de filas
        cantidad_columnas (int): cantidad de columnas
        valor_inicial (any): lo que se le puede cargar

    Returns:
        list: devuelve la nueva matriz
    """
    matriz = []
    for fila in range(cantidad_filas):
        fila = [] * cantidad_columnas
        matriz += [fila]
    return matriz

def carga_matriz_secuencial(matriz: list) -> None:
    """Carga secuencial de una matriz

    Args:
        matriz (list): Matriz que se le cargara los datos
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            matriz[fila][columna] = ingresos.get_int(
                "Ingrese numero: ", "Error, reingrese: ", 0, 10, 10)
    return None

def cargar_matriz_aleatoriamente(matriz: list) -> None:
    """Carga un dato en una posicion de la matriz

    Args:
        matriz (list): Matriz que se le cargara los datos
    """
    seguir = "s"
    while seguir == "s":
        fila = ingresos.get_int("Ingrese indice de fila: ", "Error, indice no valido. Reingrese: ",
                                0, len(matriz)-1, 10)
        columna = ingresos.get_int("Ingrese indice de columna: ", "Error, indice no valido. Reingrese: ",
                                0, len(matriz[0])-1, 10)
        dato = int(input("Ingrese el numero: "))
        matriz[fila][columna] = dato
        seguir = ingresos.get_string("Desea seguir cargando? S/N: ", "Error, reingrese S/N: ", 1, 10).lower

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

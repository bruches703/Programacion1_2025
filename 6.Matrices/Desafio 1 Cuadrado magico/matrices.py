import ingresos

def inicialziar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
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
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def carga_matriz_secuencial(matriz: list) -> None:
    """Carga secuencial de una matriz

    Args:
        matriz (list): Matriz que se le cargara los datos
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            matriz[fila][columna] = ingresos.get_int("Ingrese numero: ", "Error, reingrese: ", 0, 10, 10)
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

def mostrar_matriz(matriz: list) -> bool:
    """Muestra los valores de la matriz

    Args:
        matriz (list): Matriz a mostrar
    """
    for i in range(len(matriz)):
        print(f"{matriz[i]} ")
    return True
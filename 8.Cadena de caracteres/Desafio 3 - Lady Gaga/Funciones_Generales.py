import os
def limpiar_pantalla():
    """Limpia la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def calcular_porcentaje(valor_total: int | float, valor_parcial: int | float) -> float:
    """calcula el porcentaje del valor total

    Args:
        valor_total (int | float): valor del 100%
        valor_parcial (int | float): valor a calcular el porcentaje

    Returns:
        float: porcentaje del valor parcial
    """
    porcentaje = valor_parcial * 100 / valor_total

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
        for elemento in lista:
            print(elemento)
        return True
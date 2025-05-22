from ingresos import get_int
import os
def menu(array: list) -> int:
    """Menu de opciones

    Args:
        array (list): array a trabajar

    Returns:
        int: devuelve 1 si todo el programa se ejecuta de manera correcta
    """

    os.system("cls")
    print("Menu de opciones: ")
    print("1. Cargar nombres.")
    print("2. Cargar votos.")
    print("3. Mostar votos.")
    print("0. Salir.")
    opcion = get_int("Ingrese opcion: ",
                     "Error de valor, reingrese opcion: ", 0, 3, 10)
    return opcion
from Ingresos import *
from Vectores import *
from Matrices import *
from Funciones_Generales import *
import random

#Funciones generales del programa
def inicializar_legajos() -> list:
    """Inicia la lista de legajos de manera aleatoria

    Returns:
        list: lista de legajos con valores aleatorios
    """
    legajos = [0] * 15
    for i in range(len(legajos)):
        legajos[i] = random.randint(1000, 2000)
    return legajos

def existe_legajo(legajos: list, legajo: int) -> bool:
    """Comprueba si un legajo existe en la lista

    Args:
        legajos (list): Lista de legajos
        legajo (int): Legajo a buscar

    Returns:
        bool: True si el legajo existe, False si no
    """
    for elemento in legajos:
        if legajo == elemento:
            return True
    return False
    
def menu() -> int:
    """Menu de opcion para el usuario

    Returns:
        int: Opcion escogida por el usuario
    """
    print("Menu de opciones")
    print("1- Cargar planilla de recaudación")
    print("2- Mostrar la recaudación de cada coche y línea")
    print("3- Calcular y mostrar la recaudación por línea")
    print("4- Calcular y mostrar la recaudación por coche")
    print("5- Calcular y mostrar la recaudación total")
    print("6- Salir")
    mensaje = "Ingrese opcion: "
    mensaje_error = "Error, reingrese opcion: "
    opcion = get_int(mensaje, mensaje_error, 1, 6, 10)
    return opcion

def cargar_planilla(legajos: list, planilla: list) -> bool:
    """Carga la planilla de recaudaciones

    Args:
        legajos (list): Lista de legajos
        planilla (list): Matriz de recaudaciones

    Returns:
        bool: True si se cargo la planilla, False si no
    """
    legajo = ingresar_legajo(legajos)
    if legajo is None:
        return False
    else:
        linea = get_int("Ingrese linea 1, 2 o 3: ", "Error, reingrese linea: ", 1, 3, 10)
        coche = get_int("Ingrese coche 1, 2, 3, 4, 5: ", "Error, reingrese coche: ", 1, 5, 10)
        if linea is None or coche is None:
            return False
        print(f"Legajo: {legajo}\n")
        recaudacion = ingresar_recaudacion(linea, coche)
        if recaudacion is None:
            return False
        planilla[linea-1][coche-1] += recaudacion

        return True

def ingresar_recaudacion(linea: int, coche: int) -> float | None:
    """Ingresar recaudacion

    Returns:
        float | None: Recaudacion ingresada, None si hubo un error
    """
    mensaje = f"Ingrese recaudacion para el coche {coche} de la linea {linea}: "
    mensaje_error = f"Error, reingrese recaudacion para el coche {coche} de la linea {linea}: "
    recaudacion = get_int(mensaje, mensaje_error, 0, 10000, 10)
    return recaudacion

def ingresar_legajo(legajos: list) -> int | None:
    """Ingresar legajo

    Returns:
        int | None: Legajo ingresado, None si hubo un error
    """
    while True:
        legajo = get_int("Ingrese legajo: ", "Error, reingrese legajo: ", 1000, 9999, 10)
        if legajo is None:
            return None
        if existe_legajo(legajos, legajo):
            break
        print("El legajo no existe. Intente nuevamente.")
    return legajo

def mostrar_recaudacion_detallado(planilla: list) -> None:
    """Muestra la recaudacion total

    Args:
        planilla (list): Matriz de recaudaciones
    """
    if len(planilla) == 0:
        print("La planilla esta vacia.")
        return None
    else:
        for i in range(len(planilla)):
            print(f"Total de la Linea {i+1}: {sumar_recaudacion_linea(planilla, i)}")
            mostrar_coches_de_linea(planilla, i)

def sumar_recaudacion_linea(planilla: list, linea: int) -> float:
    """Calcula la recaudacion de una linea

    Args:
        planilla (list): Matriz de recaudaciones
        linea (int): Linea a calcular

    Returns:
        float: Recaudacion de la linea
    """
    recaudacion_linea = 0
    for coche in planilla[linea]:
        recaudacion_linea += coche
    return recaudacion_linea

def mostrar_coches_de_linea(planilla: list, linea: int) -> None:
    """Muestra los coches de una linea

    Args:
        planilla (list): Matriz de recaudaciones
        linea (int): Linea a mostrar
    """
    for i in range(len(planilla[linea])):
        mostrar_un_coche(planilla, linea, i)
    print("----------------------------------------------")

def mostrar_un_coche(planilla: list, linea: int, coche: int) -> None:
    """Muestra un coche de una linea

    Args:
        planilla (list): Matriz de recaudaciones
        linea (int): Linea a mostrar
        coche (int): Coche a mostrar
    """
    print(f"Coche {coche+1} de la linea {linea+1}: ${planilla[linea][coche]}")

def mostrar_recaudacion_de_linea(planilla: list, linea: int) -> None:
    """Muestra la recaudacion por linea

    Args:
        planilla (list): Matriz de recaudaciones
        linea (int): Linea a mostrar
    """
    print(f"Total de la Linea {linea+1}: ${sumar_recaudacion_linea(planilla, linea-1)}")
    

def mostrar_recaudacion_por_linea(planilla: list) -> None:
    """Muestra la recaudacion de una linea

    Args:
        planilla (list): Matriz de recaudaciones
    """
    linea = get_int("Ingrese linea 1, 2 o 3: ", "Error, reingrese linea: ", 1, 3, 10)
    mostrar_recaudacion_de_linea(planilla, linea)
    if linea is None:
        return None
    mostrar_coches_de_linea(planilla, linea-1)
    print("----------------------------------------------")
    

def mostrar_recaudacion_un_coche(planilla: list) -> None:
    """Muestra la recaudacion de un coche

    Args:
        planilla (list): Matriz de recaudaciones
    """
    linea = get_int("Ingrese linea 1, 2 o 3: ", "Error, reingrese linea: ", 1, 3, 10)
    coche = get_int("Ingrese coche 1, 2, 3, 4 o 5: ", "Error, reingrese coche: ", 1, 5, 10)
    if linea is None or coche is None:
        return None
    limpiar_pantalla()
    mostrar_un_coche(planilla, linea-1, coche-1)
    print("----------------------------------------------")

def mostrar_recaudacion_total(planilla: list) -> None:
    """Muestra la recaudacion total

    Args:
        planilla (list): Matriz de recaudaciones
    """

    suma = 0
    for linea in range(len(planilla)):
        suma_linea = sumar_recaudacion_linea(planilla, linea)
        mostrar_recaudacion_de_linea(planilla, linea+1)
        suma += suma_linea
    print(f"La recaudacion total es: ${suma}")
    print("----------------------------------------------")
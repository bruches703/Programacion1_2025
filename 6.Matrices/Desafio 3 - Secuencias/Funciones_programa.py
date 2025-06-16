from Ingresos import *
from Vectores import *
from Matrices import *
from Funciones_Generales import *
import random

def menu() -> int:
    """Menu de opcion para el usuario

    Returns:
        int: Opcion escogida por el usuario
    """
    print("Menu de opciones")
    print("1- Cargar matriz")
    print("2- Verificar la existencia de secuencias de números consecutivos pares")
    print("3- Determinar la cantidad de ocurrencias")
    print("4- Identificar la secuencia más corta")
    print("5- Identificar la secuencia más larga")
    print("6- Salir")
    mensaje = "Ingrese opcion: "
    mensaje_error = "Error, reingrese opcion: "
    opcion = get_int(mensaje, mensaje_error, 1, 6, 10)
    return opcion
# Opcion 1
def menu_carga_matriz(matriz: list) -> bool:
    """Carga la matriz con numeros aleatorios

    Args:
        matriz (list): Matriz a cargar

    Returns:
        bool: True si la carga fue exitosa
    """
    print("Desea cargar la matriz de manera manual o aleatoria?")
    print("1- Manual")
    print("2- Aleatoria")
    mensaje = "Ingrese opcion: "
    mensaje_error = "Error, reingrese opcion: "
    opcion = get_int(mensaje, mensaje_error, 1, 2, 10)
    if opcion == 1:
        matriz = ingresar_matriz_manual(matriz)
    elif opcion == 2:
        matriz = ingresar_matriz_aleatoria(matriz)
    else:
        return False
    return True

def ingresar_matriz_manual(matriz: list) -> list:
    """Carga la matriz manualmente

    Args:
        matriz (list): Matriz a cargar

    Returns:
        list: Matriz cargada
    """
    matriz = carga_matriz_secuencial(matriz)
    return matriz

def ingresar_matriz_aleatoria(matriz: list) -> list:
    """Carga la matriz con numeros aleatorios

    Args:
        matriz (list): Matriz a cargar

    Returns:
        list: Matriz cargada
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            matriz[fila][columna] = random.randint(1, 10)
    return matriz

# Opcion 2
def verificar_secuencias_pares(matriz: list) -> bool:
    """Verifica si existen secuencias de numeros pares consecutivos

    Args:
        matriz (list): Matriz a verificar

    Returns:
        bool: True si existen secuencias de numeros pares consecutivos
    """
    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i]) - 1):
            if matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 0:
                return True
    return False

# Opcion 3
def contar_ocurrencias(matriz: list, dimension: int) -> int:
    """Cuenta la cantidad de ocurrencias de secuencias de numeros pares consecutivos

    Args:
        matriz (list): Matriz a verificar
        dimension (int): Dimension de la matriz

    Returns:
        int: Cantidad de ocurrencias
    """
    contador = 0
    secuencia_par = False
    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i]) - 1):
            # Si encuentra el inicio de una secuencia par y la vandera de inicio es False
            # levanta el flag en True para identificar la secuencia
            if matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 0 and not secuencia_par:
                secuencia_par = True
            # Si encuentra un numero impar y el flag de inicio es True, levanta el contador 
            # en uno y baja el flag
            elif secuencia_par and (matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 1) or (i+1 == dimension-1 and j+1 == dimension-1):
                secuencia_par = False
                contador += 1
    return contador

def es_par(numero: int) -> bool:
    """Verifica si el numero anterior es par

    Args:
        matriz (list): Matriz a verificar

    Returns:
        bool: True si el numero anterior es par
    """
    return numero % 2 == 0

# Opcion 4
def mostrar_secuencia_mas_corta(matriz: list, dimension: int) -> None:
    """Muestra la secuencia mas corta

    Args:
        matriz (list): Matriz a verificar
        dimension (int): Dimension de la matriz
    """
    secuencia_par = False

    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i]) - 1):
            if matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 0 and not secuencia_par:
                secuencia_par = True
            elif secuencia_par and (matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 1) or (i+1 == dimension-1 and j+1 == dimension-1):
                secuencia_par = False

def contar_secuencia_mas_corta(matriz: list) -> int:
    """Cuenta la cantidad de ocurrencias de secuencias de numeros pares consecutivos

    Args:
        matriz (list): Matriz a verificar

    Returns:
        int: Cantidad de ocurrencias
    """
    secuencia_mas_corta = crear_ma
    for i in range(len(matriz) - 1):
        for j in range(len(matriz[i]) - 1):
            if matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 0 and not secuencia_par:
                secuencia_par = True
                secuencia_mas_corta = 2
            if secuencia_mas_corta:
                secuencia_mas_corta += 1
            if secuencia_par and (matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 1) or (i+1 == dimension-1 and j+1 == dimension-1):
                secuencia_par = False
    return secuencia_mas_corta
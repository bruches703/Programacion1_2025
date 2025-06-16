# Ejercicio 1
# Crear una función que reciba como parámetro una cadena y 
# determine la cantidad de vocales que hay de cada una (individualmente). 
# La función retornará una matriz indicando en la columna 1 cada vocal,
# y en la columna 2 la cantidad.
# Por ejemplo, si la cadena ingresada es “murcielaguito”, 
# la salada por pantalla deberá ser: 
#                           (“a”: 1; “e”: 1; “i”: 2; “o”: 1; “u”:2)

def contar_vocales_de_matriz(cadena: str) -> list:
    """Cuenta la cantidad de vocales de una matriz y la
    guarda en otra matriz, guardando vocales en la primer columna
    y la cantidad en la segunda.

    Args:
        matriz (list): Matriz a contar vocales

    Returns:
        list: Matriz con vocales y cantidad
    """
    matriz = [
        ['a',0],
        ['e',0],
        ['i',0],
        ['o',0],
        ['u',0]    
    ]
    for letra in cadena:
        if letra == 'a':
            matriz[0][1] += 1
        elif letra == 'e':
            matriz[1][1] += 1
        elif letra == 'i':
            matriz[2][1] += 1
        elif letra == 'o':
            matriz[3][1] += 1
        elif letra == 'u':
            matriz[4][1] += 1
    
    return matriz

# Ejercicio 2 
# Crear una función que reciba una cadena y un caracter.
# La función deberá devolver el índice en el que se encuentre
# la primera ocurrencia de dicho caracter,
# o -1 en caso de que no esté.
def encontrar_indice_carcater(cadena: str, caracter: str) -> int:
    """Encuentra el indice de un caracter en una cadena

    Args:
        cadena (str): Cadena a buscar
        caracter (str): Caracter a buscar

    Returns:
        int: Indice del caracter en la cadena
    """
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            break
    return i

# Ejercicio 3 Crear una función que reciba como parámetro una cadena
# y determine si la misma es o no un palíndromo. Deberá retornar un
# valor booleano indicando lo sucedido.
def es_palindromo(cadena: str) -> bool:
    """Verifica si una cadena es palindromo

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es palindromo, False si no lo es
    """
    indice_decendiente = len(cadena) - 1
    for letra in cadena:
        if letra != cadena[indice_decendiente]:
            return False
        indice_decendiente -= 1
    return True

# Ejercicio 4 
# Crear una función que reciba como parámetro una cadena
# y suprima los caracteres repetidos consecutivos.
# 
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def quitar_caracteres_repetidos(cadena: str) -> str:
    """Quita los caracteres repetidos de manera consecutiva
    de una cadena

    Args:
        cadena (str): Cadena a quitar caracteres repetidos

    Returns:
        str: Cadena sin caracteres repetidos
    """
    nueva_cadena = cadena[0]
    for i in range(1,len(cadena)):
        if cadena[i] != nueva_cadena[len(nueva_cadena) - 1]:
            nueva_cadena += cadena[i]
    return nueva_cadena

# Ejercicio 5
# Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
# 
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
def quitar_vocales(cadena: str) -> str:
    """Quita las vocales de una cadena

    Args:
        cadena (str): Cadena a quitar vocales

    Returns:
        str: Cadena sin vocales
    """
    nueva_cadena = ''
    for letra in cadena:
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            nueva_cadena += letra
    return nueva_cadena

# Ejercicio 6
# Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
# 
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
def contar_subcadena(cadena: str, subcadena: str) -> int:
    """Cuenta la cantidad de veces que aparece una subcadena dentro de una cadena

    Args:
        cadena (str): Cadena a contar subcadena
        subcadena (str): Subcadena a contar

    Returns:
        int: Cantidad de veces que aparece la subcadena
    """
    contador = 0
    cantidad = 0
    for i in range(len(cadena)):
        if cadena[i] == subcadena[contador]:
            contador += 1
            if contador == len(subcadena):
                cantidad += 1
                contador = 0
    return cantidad
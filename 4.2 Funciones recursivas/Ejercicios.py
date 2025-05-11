# Ejercicios

# 1.Realizar una función recursiva que calcule la suma de los primeros números 
# naturales:
def sumar_naturales(numero: int) -> int:
    """suma los numeros naturales hasta el numero ingresado

    Args:
        numero (int): numero a sumar con los naturales

    Returns:
        int: devuelve la suma de los naturales
    """
    if numero <= 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)
    
# 2.Realizar una función recursiva que calcule la potencia de un número:
def calcular_potencia(base: int, exponente: int) -> int:
    """Calcula la potencia de un numero de manera recursiva

    Args:
        base (int): Define el numero a elevar
        exponente (int): es el exponente

    Returns:
        int: Devuelve el resultado de base^exponente o devuelve -1 si alguno de los valores es negativo
    """
    if base < 0 or exponente < 0:
        return -1
    else:
        if exponente == 0:
            return 1
        elif base == 0:
            return 0
        else:
            return base * calcular_potencia(base, exponente-1)

# 3.Realizar una función recursiva que permita realizar la suma de los dígitos 
# de un número:
def sumar_digitos(numero: int) -> int:
    """Suma los digitos de un numero

    Args:
        numero (int): representa el numero al que se le va a sumar los digitos

    Returns:
        int: retorna el resultado de dicha suma
    """
    suma = 0
    if numero < 10 :
        return numero
    else:
        return (numero % 10) + sumar_digitos (numero // 10)

# 4.Realizar una función para calcular el número de Fibonacci de un número 
# ingresado por consola. La función deberá seguir el siguiente prototipo:
def calcular_fibonacci(numero: int) -> int:
    """Calcula el fibonacci de un numero

    Args:
        numero (int): numero a calcular el fiboncci

    Returns:
        int: devuelve el valor del fibonacci del numero ingresado
    """
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero-1) + calcular_fibonacci(numero-2)


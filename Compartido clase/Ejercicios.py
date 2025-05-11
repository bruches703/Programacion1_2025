def sumar(numero_uno:int,numero_dos:int) -> int:
    """Se encarga de sumar dos numeros enteros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la suma
    """
    resultado = numero_uno + numero_dos
    return resultado

def restar(numero_uno:int,numero_dos:int) -> int:
    """Se encarga de restar dos numeros enteros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la resta
    """
    resultado = numero_uno - numero_dos
    return resultado

def dividir(numero_uno:int,numero_dos:int) -> float | str:
    """Se encarga de dividir dos numeros entero , si el divisor es cero da error

    Args:
        numero_uno (int): Primer numero
        numero_dos (int): Segundo numero

    Returns:
        float | str: Retorna la división o un mensaje de error en caso de dividir por cero
    """
    if numero_dos != 0:
        resultado = numero_uno / numero_dos
    else:
        resultado = "ERROR"
        
    return resultado

def multiplicar(numero_uno:int,numero_dos:int) -> int:
    """Se encarga de multiplicar dos numeros enteros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la multiplicacion
    """
    resultado = numero_uno * numero_dos
    return resultado

# PUNTO 1
def pedir_numero_entero(mensaje:str) -> int:
    numero = int(input(mensaje))
    #Valide (el rango que quieran)
    return numero

def mostrar_resultados(numero_uno:int,numero_dos:int,resultado_suma:int,resultado_resta:int,resultado_division:float | str, resultado_multiplicacion:int) -> None:
    print(f"La suma ente {numero_uno} y {numero_dos} es {resultado_suma}")
    print(f"La resta ente {numero_uno} y {numero_dos} es {resultado_resta}")
    if resultado_division == "ERROR":
        print("NO SE PUEDE DIVIDIR POR CERO")
    else:
        print(f"La division ente {numero_uno} y {numero_dos} es {resultado_division}")
    print(f"La multiplicacion ente {numero_uno} y {numero_dos} es {resultado_multiplicacion}")

numero_uno = pedir_numero_entero("Ingrese el numero 1: ")
numero_dos = pedir_numero_entero("Ingrese el numero 2: ")

resultado_suma = sumar(numero_uno,numero_dos)
resultado_resta = restar(numero_uno,numero_dos)
resultado_division = dividir(numero_uno,numero_dos)
resultado_multiplicacion = multiplicar(numero_uno,numero_dos)

mostrar_resultados(numero_uno,numero_dos,resultado_suma,resultado_resta,resultado_division,resultado_multiplicacion)
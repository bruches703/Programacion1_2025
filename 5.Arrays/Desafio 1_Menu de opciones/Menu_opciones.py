import funcion_input
import Especificas
import os
# Menu de opciones
def menu(array: list) -> int:
    """Menu de opciones

    Args:
        array (list): array a trabajar

    Returns:
        int: devuelve 1 si todo el programa se ejecuta de manera correcta
    """

    os.system("cls")
    print("Menu de opciones: ")
    print("1. Ingresar datos.")
    print("2. Cantidad de positivos y negativos. ")
    print("3. Suma de los números pares. ")
    print("4. Mayor número impar.")
    print("5. Listar los números ingresados.")
    print("6. Listar los números pares.")
    print("7. Listar los números en posiciones impares.")
    print("8. Salir.")
    opcion = funcion_input.get_int("Ingrese opcion: ", "Error de valor, reingrese opcion: ", 1, 8, 10)
    if len(array) == 0 and opcion == 8:
        return 8
    else:
        return Especificas.comprobar_opcion_menu(opcion, array)
    
def opcion_1() -> list | None:
    """Genera un nuevo array donde el usuario ingrese los valores del -1000 al 1000

    Returns:
        list: devuelve un array de 10 numeros enteros, o None si no se puede crear el array
    """
    os.system('cls')
    print("Ingrese 10 numeros enteros con el valor desde -1000 al 1000")
    nuevo_array = funcion_input.crear_array("Ingrese valor del elemento: ",
                                    "Error, Ingreso incorrecto. Reingrese con valores de -1000 al 1000: ",
                                    -1000, 1000, 10, 10)
    if nuevo_array == None:
        return None
    else:
        return nuevo_array
    
def opcion_2(array: list) -> int | None:
    """Mostrar cantidad de positivos y cantidad de negativos ingresados

    Args:
        array (list): vector de enteros a contar los positivos y negativos

    Returns:
        int | None: Retorna 1 si todo funciono bien, None si hubo algun
    """
    ceros = Especificas.contador_iguales(array,0)
    positivos = Especificas.contador_iguales(array,1)
    negativos = Especificas.contador_iguales(array,2)
    os.system("cls")
    if ceros == None or positivos == None or positivos == None:
        print("Ocurrio un error")
        return None
    else:
        print(f"Hay {ceros} ceros")
        print(f"Hay {positivos} positivos")
        print(f"Hay {negativos} negativos")
        return 1

def opcion_3(array: list) -> int | None:
    """Suma todos los elementos pares, devolviendo el resultado

    Args:
        arary (list): array de enteros a calcular

    Returns:
        int | None: retorna el resultado de los pares, o None si hubo error
    """
    
    if len(array) == 0:
        return None
    else:
        suma_pares = 0
        for elemento in array:
            if elemento % 2 == 0:
                suma_pares += elemento
    return suma_pares

def opcion_4(array: list) -> int | None:
    """Identificar y mostar el mayor numero impar

    Args:
        arary (list): array de enteros a identificar impares

    Returns:
        int | None: Retorna un entero para reconocer resultado o None si hubo error
                0: Si no hay impares
                1: Si salio todo bien
    """
    flag = 0 
    if len(array) == 0:
        return None
    else:
        for elemento in array: # Recorre los elementos del arreglo
            if elemento % 2 == 1: # Evalua que el elemento actual sea impar
                if flag == 0: # Si es el primer impar, lo asigna y cambia la bandera
                    mayor_impar = elemento
                    flag = 1
                elif mayor_impar < elemento: # Evalua si el elemento impar actual es mayor al anterior
                    mayor_impar = elemento
    if flag == 0:
        print("No se encontraron impares")
    else:
        print(f"El impar de mayor valor es: {mayor_impar}")

    return flag # Valor de flag 0 si no hay impares, 1 si hubo impares

def opcion_5(array: list) -> int | None:
    """Muestra todos los elementos en el orden ingresado

    Args:
        array (list): Lista de elementos de tipo entero a mostrar

    Returns:
        int | None: retorna 1 si salio todo bien, None si hubo algun error
    """
    if len(array) == 0:
        return None
    else:
        print("Numeros ingresados:")
        for elemento in array:
            print(elemento)
    return 1

def opcion_6(array: list) -> int | None:
    """Muestra unicamente los Números pares de la lista

    Args:
        array (list): Lista de elementos de tipo entero a mostrar

    Returns:
        int | None: retorna 1 si salio todo bien, None si hubo algun error
    """
    if len(array) == 0:
        return None
    else:
        flag = True
        print("Lista de Números pares ")
        for elemento in array:
            if elemento % 2 == 0:
                print(elemento)
                flag = False
    if flag:
        print("No se encontraron Números pares: ")
    return 1

def opcion_7(array: list) -> int | None:
    """Muestra los elementos en posiciones impares

    Args:
        array (list): Lista de elementos de tipo entero a mostrar

    Returns:
        int | None: retorna 1 si salio todo bien, None si hubo algun error
    """
    if len(array) == 0:
        return None
    else:
        print("Números en las posiciones impares")
        for i in range (1, len(array), 2):
            print(array[i])
    return 1
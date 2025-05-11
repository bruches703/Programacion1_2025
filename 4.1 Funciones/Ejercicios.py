# EJERCICIO FUNCIONES

# # 1-Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# def ingreso_de_entero() -> int:
#     """Pide el ingreso de un numero entero

#     Returns:
#         int: Devuelve un numero entero que es ingresado
#     """
#     return int(input("Ingrese un numero entero: "))

# # 2-Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
# def ingreso_de_flotane() -> float:
#     """Pide el ingreso de un numero flotante

#     Returns:
#         float: Devuelve un numero flotante
#     """
#     return float(input("Ingrese un numero flotante: "))

# # 3-Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
# def ingreso_de_string() -> str:
#     """Pide el ingreso de una cadena
#         Returns:
#             string: devuelve la cadena ingresada.
#     """
#     return input("Ingrese una palabra o frase: ")

# # 4-Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área
#  def calcular_area_del_rectangulo(base:int, altura:int) -> int:
#     """Calcula el area de un rectangulo con los valores que ingrese el usuario

#     Args:
#         base (int): recibe un entero con el valor de la base del rectangulo
#         altura (int): recibe un entero con el valor de la altura del rectangulo

#     Returns:
#         int: devuelve el area calculada (base * altura)
#     """
# base = int(input("Ingrese base del rectanguilo: "))
# altura = int(input("Ingrese altura: "))
# print(f"El area del rectangulo es: {calcular_area_del_rectangulo(base, altura)}")

# # 5-Escribe una función que calcule el área de un círculo. La función debe recibir el 
# # radio como parámetro y devolver el área.
# # import math
# def calcular_area_del_circulo(radio:int)->int:
#     """Calcula el area de un circulo

#     Args:
#         radio (int): recibe un entero, con el valor del radio del circulo

#     Returns:
#         int: devuelve el area calculada del circulo (Pi * radio **2)
#     """
# radio = int(input("Ingrese radio del circulo: "))
# print(f"El area del circulo es {calcular_area_del_circulo(radio)}")

# # 6-Crea una función que verifique si un número dado es par o impar. 
# # La función debe imprimir un mensaje indicando si el número es par o impar.
# def verificar_numero_par(numero_a:int):
#     """Valida si el numero recibido es par o impar, dando un mensaje indicando si es par o par

#     Args:
#         numero_a (int): Numero entero que sera validado como par o impar
#     """
#     if(numero_a%2==0):
#         print("El valor ingresado es par")
#     else:
#         print("El valor ingresado es impar")

# verificar_numero_par(int(input("Ingrese un numero: ")))

# # 7-Crea una función que verifique si un número dado es par o impar. 
# # La función retorna True si el número es par, False en caso contrario.
# def validar_Verdadero_numero_par(numero:int)->bool:
#     """Valida si el numero recibido es par o impar

#     Args:
#         numero (int): recibe numero entero a validar si es par o impar

#     Returns:
#         bool: retorna True si el numero es par, de lo contrario devuelve False
#     """
#     if(numero%2==0):
#         return True
#     else:
#         return False
# if (validar_Verdadero_numero_par(int(input("Ingrese numero: ")))):
#     print("Es par")
# else:
#     print("Es impar")

# # 8-Define una función que encuentre el máximo de tres números. 
# # La función debe aceptar tres argumentos y devolver el número más grande.
# def calcular_numero_maximo(numero_a:int , numero_b:int , numero_c:int) -> int:
#     """Calcula el valor maximo de una serie de numeros dados

#     Args:
#         numero_a (int): Primer numero
#         numero_b (int): Segundo numero
#         numero_c (int): tercer numero

#     Returns:
#         int: devuelve el numero de mayor valor
#     """
#     maximo = numero_a
#     if maximo < numero_b :
#         maximo = numero_b
#     if maximo < numero_c :
#         maximo = numero_c
#     return maximo

# numeroA = int(input("Ingrese primer numero: "))
# numeroB = int(input("Ingrese segundo numero: "))
# numeroC = int(input("Ingrese primer numero: "))
# print (f"El numero mayor es {calcular_numero_maximo(numero_a=numeroA , numero_b=numeroB , numero_c=numeroC)}")

# # 9-Diseña una función que calcule la potencia de un número. 
# # La función debe recibir la base y el exponente como argumentos y devolver el resultado.
# def calcular_potencia(base:int , exponente:int) -> int:
#     """Calcula la potencia de un numero

#     Args:
#         base (int): es el numero base a calcular su potencia
#         exponente (int): exponente del numero base

#     Returns:
#         int: devuelve la potencia de la base elevada al expoente
#     """
#     return base ** exponente

# base = int(input("Ingrese el numero base: "))
# exponente = int(input("Ingrese el exponente: "))
# print(calcular_potencia(base,exponente))

# # 10-Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
# def es_numero_primo(numero:int) -> bool :
#     """Define si el numero ingresado es primo

#     Args:
#         numero (int): numero a definir si es primo o no

#     Returns:
#         bool: es True si el numero ingresado es primo, de lo contrario sera false
#     """
#     if numero < 2:
#         return False
#     else:
#         for i in range (2 , int(numero**0.5 +1)):
#             if numero % i == 0:
#                 return False
#     return True

# if es_numero_primo(int(input("Ingrese el numero: "))) :
#     print("El numero es primo: ")
# else:
#     print("El numero no es primo")

# # 11-Crear una función que (utilizando el algoritmo del ejercicio de la guia de for),
# # muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
# # La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# # Del ejercicio 1
# def ingreso_de_entero() -> int:
#     """Pide el ingreso de un numero entero

#     Returns:
#         int: Devuelve un numero entero que es ingresado
#     """
#     return int(input("Ingrese un numero entero: "))
# # Del ejercicio 10
# def es_numero_primo(numero:int) -> bool :
#     """Define si el numero ingresado es primo

#     Args:
#         numero (int): numero a definir si es primo o no

#     Returns:
#         bool: es True si el numero ingresado es primo, de lo contrario sera false
#     """
#     if numero < 2:
#         return False
#     else:
#         for i in range (2 , int(numero**0.5 +1)):
#             if numero % i == 0:
#                 return False
#     return True

# def contador_de_numeros_primos() -> int:
#     """Cuenta la cantidad de numeros primos

#     Returns:
#         int: devuelve la cantidad de numeros primos
#     """
#     numero = ingreso_de_entero()
#     contador = 0
#     for i in range(1, numero+1):
#         esPrimo = True
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 esPrimo = es_numero_primo(i)
#                 break
#         if esPrimo:
#             print(i)
#             contador += 1
#     return contador

# print(f"Hubo: {contador_de_numeros_primos()} numeros primos")


# 12-Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
# Por defecto es del 1 al 10.

# def imprimir_tabla_de_multiplicar(numero: int, inicio:int = 1, fin:int = 10 ) :
#     """Imprimir la tabla de multiplicar de un numero dado, dado un inicio y un fin. Inicio sera 1 por defecto y fin sera 10 por defecto

#     Args:
#         numero (int): Valor a imprimir la tabla
#         inicio (int, optional): valor inicial de la tabla. Defaults to 1.
#         fin (int, optional): valor final de la tabla. Defaults to 10.
#     """
#     for i in range(inicio, fin+1, 1):
#         print(f"{numero}*{i}={numero*i}")

# inicio = int(input("Ingrese numero inicio: "))
# fin = int(input("Ingrese numero fin: "))
# numero = int(input("Ingrese numero: "))

# imprimir_tabla_de_multiplicar(numero, inicio, fin)

# # 13-Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
# def ingreso_de_entero(mensaje:str) -> int:
#     """Pide el ingreso de un numero entero

#     Args:
#         mensaje (str): mensaje que saldra por pantalla

#     Returns:
#         int: Devuelve un numero entero que es ingresado
#     """
#     return int(input(mensaje))

# def ingreso_de_flotane(mensaje:str) -> float:
#     """Pide el ingreso de un numero flotante

#     Args:
#         mensaje (str): mensaje que saldra por pantalla

#     Returns:
#         float: Devuelve un numero flotante
#     """
#     return float(input(mensaje))

# def ingreso_de_string(mensaje:str) -> str:
#     """Pide el ingreso de una cadena

#         Args:
#         mensaje (str): mensaje que saldra por pantalla

#         Returns:
#             string: devuelve la cadena ingresada.
#     """
#     return input(mensaje)

# numeroEntero = ingreso_de_entero("Ingrese un numero entero: ")
# numeroFlotante = ingreso_de_flotane("Ingrese un numero flotante: ")
# cadena = ingreso_de_string("Ingrese una palabra o frase: ")

# print(f"Entero: {numeroEntero}")
# print(f"Flotante: {numeroFlotante}")
# print(f"Cadena {cadena}")
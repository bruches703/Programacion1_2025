#1.Funciones ord() y chr()

#ord(caracter) --> Devuelve el valor ASCII del caracter

# print(ord("A"))#65
# print(ord("z"))#122
# print(ord(" "))#32
# print(ord("\n"))#10
# #print(ord(""))#ERROR
# #print(ord("aa"))#ERROR

#chr(numero_ascii) --> Devuelve el caracter correspondiente a ese código ascii

# print(chr(80))#TAB
# print(chr(9))#TAB
# print(chr(32))#ESPACIO
# print(chr(64))#@
# print(chr(109))#m

import random
import time

#1.Crear una función que llene una cadena de letras mayusculas aleatorias

def crear_cadena_aleatoria(cantidad_letras:int) -> str:
    cadena_aux = ""
    
    for i in range(cantidad_letras):
        valor_ascii = random.randint(65,90)
        caracter = chr(valor_ascii)
        cadena_aux += caracter
    
    return cadena_aux

#2.Crear una funcion que convierta una cadena de minuscula a mayuscula

def convertir_mayuscula(cadena:str) -> str:
    cadena_aux = ""
    
    for i in range(len(cadena)):
        valor_ascii = ord(cadena[i])
        if valor_ascii >= 97 and valor_ascii <= 122:
            valor_ascii_mayuscula = valor_ascii - 32
            caracter = chr(valor_ascii_mayuscula)
            cadena_aux += caracter
        else:
            cadena_aux += cadena[i]
            
    return cadena_aux
            
# cadena = "hOLa"
# print(convertir_mayuscula(cadena))

#3.Crear una función que verifique si una cadena tiene solo numeros enteros positivos

def es_entero(cadena:str) -> bool:
    retorno = len(cadena) > 0
    
    for i in range(len(cadena)):
        valor_ascii = ord(cadena[i])
        if valor_ascii > 57 or valor_ascii < 48:
            #Significa que ese caracter no es numero entero
            retorno = False
            break
    
    return retorno


# print(es_entero("ABC"))
# print(es_entero("123"))
# print(es_entero("123A"))
# print(es_entero("123 "))

#cadena_aleatoria = crear_cadena_aleatoria(4)

# contador = 0
# inicio = time.time()

# while True:
#     contador+= 1
#     cadena_aleatoria = crear_cadena_aleatoria(7)
#     print(f"cadena: {cadena_aleatoria} - contador: {contador}")
    
#     if cadena_aleatoria == "HOLA":
#         fin = time.time()
#         break
    
# segundos = fin - inicio
# print(f"Tardo {contador} intentos en generar la palabra HOLA")
# print(f"Tardo {round(segundos,2)} segundos en generar la palabra HOLA")


nota = input("Ingrese una nota del 1 al 10: ")

while es_entero(nota) == False :
    print("Lo que ingreso no es un numero, intentelo de nuevo")
    nota = input("Ingrese una nota del 1 al 10: ")

nota = int(nota)

while nota > 10 or nota < 1:
    print("NOTA INVALIDA DEBE SER ENTRE 1 Y 10")
    nota = input("Reingrese una nota del 1 al 10: ")

    while es_entero(nota) == False :
        print("Lo que ingreso no es un numero, intentelo de nuevo")
        nota = input("Reingrese una nota del 1 al 10: ")
    
    nota = int(nota)
    
print(f"La nota es: {nota}/10")
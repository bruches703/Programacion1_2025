# # 1.Mostrar los números ascendentes desde el 1 al 10
# for i in range(10):
#     print(i+1)
# print("")

# # 2.Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
# for i in range(10, 0, -1):
#     print(i)
# print("")

# # 3.Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
# numero = int(input("Ingrese numero: "))
# for i in range(0, numero+1, 1):
#     print(i)
# print("")

# # 4.Ingresar un número y mostrar la tabla de multiplicar de ese número.
# # Da la tabla del 0 al 10
# numero = int(input("Ingrese numero: "))
# for i in range(0, 10, 1):
#     print(f"{numero}*{i}= {numero*i}")
# print(f"{numero}*10= {numero*10}")

# # 5.Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
# # Mostrar la suma y el promedio de todos los números.
# contador = 0
# suma = 0

# for i in range(10):
#     numero = int(input("Ingrese numero: "))
#     if(numero != 0):
#         suma = suma + numero
#         contador += 1
#     else:
#         break
# print(f"La suma es: {suma}")
# print(f"Se ingresaron {contador} numeros")
# print(f"El promedio es: {suma/contador}")

# # 6.Imprimir los números múltiplos de 3 entre el 1 y el 10.
# for i in range(1, 11, 1):
#     if (i)%3 == 0:
#         print(i)

# # 7.Mostrar los números pares que hay desde la unidad hasta el número 50.
# for i in range(1, 51, 1):
#     if i%2 == 0 :
#         print(i)

# # 8.Realizar un programa que permita mostrar una pirámide de números
# numero = int(input("Ingrese numero: "))
# cadena = ""
# for i in range(1, numero+1, 1):
#     cadena = cadena + str(i)
#     print(cadena)

# # 9.Ingresar un número. 
# # Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
# # Mostrar la cantidad de divisores encontrados.
# numero =  int(input("Ingrese numero: "))
# contador = 0
# print("\nLista de divisores: ")
# for i in range(1, numero+1, 1):
#     if numero % i == 0:
#         print(i)
#         contador += 1
# print(f"Se encontraron {contador} divisores")

# # 10.Ingresar un número. Determinar si el número es primo o no
# numero = int(input("Ingrese numero: "))
# esPrimo = True

# if numero < 2:
#     esPrimo = False
# else:
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             esPrimo = False
#             break

# if esPrimo:
#     print("El numero es primo.")
# else:
#     print("El numero no es primo.")

# 11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.

numero = int(input("Ingrese numero: "))

for i in range(1, numero+1):
    esPrimo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            esPrimo = False
            break
    if esPrimo:
        print(i)

# Esta lista de ejercicios es otra guia diferente a la que nos habian pasado el dia de la clase de FOR
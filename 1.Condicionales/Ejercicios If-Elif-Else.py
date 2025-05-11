# Ejercicio IF - ELSE -ELIF
#
# 1.A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
#   Menos de 160 cm: Base
#   Entre 160 cm y 179 cm: Escolta
#   Entre 180 cm y 199 cm: Alero
#   200 cm o más: Ala-Pívot o Pívot

altura = int(input ("Ingrese altura en cm: "))

if altura < 160 :
    posicion ="Base"
elif altura < 180 :
    posicion ="Escolta"
elif altura < 200 :
    posicion ="Alero"
else:
    posicion="Ala-Pívot o Pívot"

print(f"La posicion es {posicion}")


# -----------------------------------------------------------
# Ejercicio IF - ELSE -ELIF
#
# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5            ---> Aprobado, la nota es ...
# 1, 2 y 3         ---> Desaprobado, la nota es ...

import random
numero = random.randint(1 , 10)

if numero > 5 :
    print(f"Promoción directa, la nota es {numero}")
elif numero > 3 :
    print(f"Aprobado, la nota es {numero}")
else:
    print(f"Desaprobado, la nota es{numero}")

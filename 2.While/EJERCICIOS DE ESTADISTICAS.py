# EJERCICIOS DE ESTADISTICAS
# ACLARACION: en cada ejercicio hay inicializado varias veces la misma variable, fue pensado para poner en otro archivo o en otra funcion
# 1.Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
contador = 0
while contador < 10:
    contador += 1
    print(f"{contador}")
print("") #Un salto de linea

# 2.Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
contador = 10
while contador > 0:
    print(f"{contador}")
    contador -= 1
print("") #Un salto de linea

# 3.Mostrar la suma de los números desde el 1 hasta el 10.
contador = 0
suma = 0
while contador < 10:
    contador += 1
    suma = suma + contador
    print(f"{suma}")
    
print("") #Un salto de linea

# 4.Mostrar la suma de los números pares desde el 1 hasta el 10.
contador = 0
suma = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        suma = suma + contador
        print(f"{suma}")

print("") #Un salto de linea

# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.

contador = 0
suma = 0
promedio = 0

while contador < 5:
    suma = suma + int (input ("Ingrese un numero: "))
    contador += 1
promedio = suma / contador

print(f"La suma de los numeros es: {suma}")
print(f"El promedio es de: {promedio}")

print("") #Un salto de linea

# 6.Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.
continuar = 1
contador = 0
suma = 0
promedio = 0

while continuar == 1:
    suma = suma + int(input("Ingrese un numero: "))
    contador += 1

    # Menu de "continuar
    print("Ingresar otro numero?")
    print("1- continuar")
    print("0- Salir")
    continuar = int(input("Ingrese opcion: "))

promedio = suma / contador

print(f"La suma de los numeros es: {suma}")
print(f"El promedio es de: {promedio}")

print("") #Un salto de linea

# 7.Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

continuar = 1
contador = 0
suma = 0
producto = 0

while continuar == 1:
    numero = int(input("Ingrese un numero: "))
    if(numero > 0):
        suma += numero

    contador += 1

    # Menu de "continuar"
    print("Ingresar otro numero?")
    print("1- continuar")
    print("0- Salir")
    continuar = int(input("Ingrese opcion: "))

print(f"La suma de los numeros es: {suma}")
if contador >= 1 and suma >0:   
    producto = suma % contador
    print(f"El producto es de: {producto}")
else:
    print("No es posible calcular el producto")

# # 8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.
contador = 0
flag = True
minimo = 0
maximo = 0

while contador < 5:
    contador += 1
    numero = int(input("Ingrese numero: "))
    # Si es el primer numero que se ingresa, entra al bloque if y setea el minimo y el maximo con el primer valor ingresado
    # y flag pasa a falso

    if flag:
        minimo = numero
        maximo = numero
        flag = False
    else:
        # Reemplaza el valor maximo si el ultimo numero ingresado es mayor
        if numero > maximo:
            maximo = numero

        # Reemplaza el valor minimo si el ultimo numero es mas chico
        if numero < minimo:
            minimo = numero

print(f"El valor maximo es: {maximo}")
print(f"El valor minimo es: {minimo}")

print("") #Un salto de linea

# # 9.Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma = 0
opcion = 1

# Mientras opcion sea valor 1 seguira pidiendo ingreso de numeros
while opcion == 1:
    # Cuando el contador llegue al 5° loop consulta si continua pidiendo ingresos
    suma += int(input("Ingrese numero: "))
    contador += 1
    if contador > 4: 
        print("Desea seguir ingresando numeros? ")
        opcion = int(input("1-continuar 2-finalizar: "))
print(f"La suma es de: {suma}")
if suma > 0:
    print(f"El promedio es de: {suma/contador}")
else:
    print("No se puede calcular el promedio si la suma es 0")
print("") #Un salto de linea

# 10.Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos

contador = 0
suma = 0
opcion = 1

while opcion == 1 and contador < 10:
    # Cuando el contador llegue al 5° loop consulta si continua pidiendo ingresos
    print(f"Numeros restantes maximos a ingresar: {10-contador}")
    suma += int(input("Ingrese numero: "))
    contador += 1

    if contador > 4 and contador < 10: 
        print("Desea seguir ingresando numeros? ")
        opcion = int(input("1-continuar 2-finalizar: "))

print(f"La suma es de: {suma}")
if suma > 0:
    print(f"El promedio es de: {suma/contador}")
else:
    print("No se puede calcular el promedio si la suma es 0")
print("") #Un salto de linea

# INTEGRADOR WHILE
# 1.Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
#   a. La suma acumulada de los números negativos.
#   b. La suma acumulada de los números positivos.
#   c. La cantidad de números negativos ingresados.
#   d. El promedio de los números positivos.
#   e. El número positivo más grande.
#   f. El porcentaje de números negativos ingresados, respecto del total de ingresos.

contador = 0

sumaNegativos = 0
contadorDeNegativos = 0
porcentajeNegativos = 0

contadorPositivos = 0
sumaPositivos = 0
promedioDePositivos = 0
maximoPositivo = 0
flagPositivo = True

numerosAIngresar = int(input("Ingrese la cantidad de numeros que desa ingresar: "))

while contador<numerosAIngresar:
    numero = int(input("Ingrese numero: "))
    # Doy por hecho que el cero se lo trabaja como numero positivo, ya que no especifica que el nunmero cero tenga valor nulo o similar
    if numero >= 0:
        sumaPositivos += numero
        if flagPositivo:
            maximoPositivo = numero
            flagPositivo = False
        elif numero > maximoPositivo:
            maximoPositivo = numero
        contadorPositivos += 1

    else:
        sumaNegativos += numero
        contadorDeNegativos += 1
    contador += 1

print("") #Un salto de linea
# Si no se inreso ningun valor positivo se dejara el mensaje, sino se mostrara lo pedido en pantalla
if contadorPositivos > 0:
    print(f"La suma de los positivos es de: {sumaPositivos}")
    print(f"El numero positivo mas grande es: {maximoPositivo}")
    print(f"El promedio de los positivos es de: {sumaPositivos/contadorPositivos}")
else:
    print("No se ingreso ningun numero positivo")

print("") #Un salto de linea
# Si no se inreso ningun valor negativo se dejara el mensaje, sino se mostrara lo pedido en pantalla
if contadorDeNegativos > 0:
    print(f"La suma de los negativos es de : {sumaNegativos}")
    print(f"Se ingresaron {contadorDeNegativos} numeros negativos")
    print(f"El porcentaje de numeros negativos ingresados es de: {(contadorDeNegativos*100)/contador}")
else:
    print("No se ingreso ningun numero negativo")
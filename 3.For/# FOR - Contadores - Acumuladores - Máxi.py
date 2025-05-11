# FOR - Contadores - Acumuladores - Máximos y mínimo
# 
# 1.Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
for i in range(10):
    print(i+1)
print("")

# 2.Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
for i in range(10, 0, -1):
    print(i)
print("")

# 3.Mostrar la suma de los números desde el 1 hasta el 10.
suma = 0
for i in range(10):
    suma += i
print(suma)
print("")

# 4.Mostrar la suma de los números pares desde el 1 hasta el 10.
suma = 0
for i in range(10):
    if i % 2 == 0:
        suma += i
print(suma)
print("")

# 5.Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.
suma = 0
contador = 0
for contador in range(5):
    suma += int(input("Ingrese un numero: "))
print(suma/(contador+1))
print("")

# 6.Ingresar 10 números enteros. Determinar el máximo y el mínimo.
flagMinimo = True
flagMaximo = True
minimo = 0
maximo = 0
for i in range(10):
    numero = int(input("Ingrese numero: "))
    if flagMinimo or numero < minimo:
        minimo = numero
        flagMinimo = False

    if flagMaximo or numero > maximo:
        maximo = numero
        flagMaximo = False
print(f"El numero minimo es: {minimo}")
print(f"El numero maximo es: {maximo}")


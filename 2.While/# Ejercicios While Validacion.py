# Ejercicios While Validacion
# 1.Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

contraseñaAsignada = "123ABC"
continuar = True
while continuar:
    contraseñaIngresada = input("Ingrese contraseña: ")
    if contraseñaIngresada != contraseñaAsignada:
        print("La contraseña ingresada es incorrecta, reingrese\n")
    else:
        continuar = False
        print("Contraseña correcta, finalizando programa")

# 2.Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

contador = 3
contraseñaAsignada = "123ABC"

while contador > 0:
    print(f"Intentos restantes: {contador}")
    contador -= 1
    contruaseñaIngresada = input("Ingrese contraseña: ")
    if contruaseñaIngresada != contraseñaAsignada and contador > 0:
        print("La contraseña ingresada es incorrecta, reingrese\n")
    elif contruaseñaIngresada == contraseñaAsignada:
        contador = -1
        print("Contraseña correcta")    
    elif contador == 0:
        print("Se quedo sin intentos")

# 3. Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota = int(input("Ingrese una nota, los valores son entre 1 y 10: "))
if nota < 1 or nota > 10:
    print("Valor incorrecto, ingreso un numero fuera del rango aceptable")
else:
    print(f"Nota ingresada es: {nota}")

# 4. Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul

color = input("Ingrese color rojo, verde, azul: ")
if color in ["rojo", "verde", "azul"]:
    print(f"El color ingresado es: {color}")
else:
    print("Ingreso incorrecto")



# INTEGRACION VALIDACION
# 1.Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
#   a.Apellido
#   b.Edad, entre 18 y 90 años inclusive.
#   c.Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
#   d.Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

print("Ingrese los siguientes datos: ")
apellido = input("Ingrese apellido: ")
# Ingreso y validacion de la edad
edad = int(input("Ingrese edad, entre 18 y 90 años: "))
while 18 > edad or edad > 90:
    edad = int(input("Edad ingresada incorrecta, reingrese: "))

# Ingreso y validacion del estado civil
estadoCivil = input("Ingrese estado civil (Soltero/a, Casado/a, Divorciado/a o Viudo/a): ")
while not estadoCivil in ["Soltero", "Soltera", "Casado", "Casada", "Divorciado", "divorciada", "Viudo", "Viuda"]:
    estadoCivil = input("Ingreso invalido, rengrese: ")

# Ingreso y validacion del legajo
legajo = int(input("Ingrese numero de legajo, sin ceros a la izquierda y de 4 cifras: "))
while legajo < 1000 or legajo > 9999:
    legajo= int(input("Ingrese numero de legajo habilitado, sin ceros a la izquierda y de 4 cifras: "))

# Salida de informacion
print(f"\n\nApellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estadoCivil}")
print(f"Legajo: {legajo}")
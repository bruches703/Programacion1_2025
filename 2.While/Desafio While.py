# 📌 Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo 
# desarrollo en Python, con el objetivo de revolucionar el mercado.

# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)

# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos

# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)

# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.

# 🔹 Análisis de Datos

# A partir de las respuestas, se deben calcular las siguientes métricas:

# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


# 🔹 Requisitos del Programa
#  ✔️ Los datos deben solicitarse y validarse correctamente.
#  ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
#  ✔️ Presentar los resultados de manera clara y organizada.

contadorGeneral = 0
contadorMasculinosVotantes = 0
contadorDeNoVotantesAIA = 0
# Puedo inicializar la variable de "edadDeMasculinoMayor" en cero ya que no pueden tener menos de 18
edadDeMasculinoMayor = 0
flagMasculinos = True #Un flag para mostrar si hubo o no ingreso de personas de genero masculino

while contadorGeneral < 10:

    nombre = input("\nIngrese nombre: ")

    # Ingreso y validacion de la edad
    edad = int(input("Ingrese edad, entre 18 y 90 años: "))
    while 18 > edad:
        edad = int(input("Edad ingresada incorrecta, reingrese: "))

    # Ingreso y validacion de genero
    genero = input("Ingrese genero (Masculino, Femenino, Otro): ")
    while not genero in ["Masculino", "Femenino", "Otro"]:
        genero = input("Ingreso incorrecto. Ingrese genero (Masculino, Femenino, Otro): ")
    
    # Ingreso y validacion de tecnologia escogida
    tecnologiaElegida = input("Ingrese tecnologia elegida  (IA, RV/RA, IOT): ")
    while not tecnologiaElegida in ["IA", "RV/RA", "IOT"]:
        tecnologiaElegida = input("Ingreso incorrecto.  tecnologia elegida  (IA, RV/RA, IOT): ")

# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años
    if genero == "Masculino":
        #Defino al masculino de mayor edad y guarda sus datos
        if  edad > edadDeMasculinoMayor:
            nombreDelMasculinoMayor = nombre
            edadDeMasculinoMayor = edad
            tecnologiaElegidaPorElMayor = tecnologiaElegida
            flagMasculinos = False
        #Aumenta el contador si el masculino tiene entre 25 y 50 años y voto IOT o IA
        if 25 > edad < 51 and tecnologiaElegida in ["IOT", "IA"]:
            contadorMasculinosVotantes += 1

    #Si voto IA, y no es de genero femeniono y tiene entre 33 y 40 años aumenta el contador
    if tecnologiaElegida != "IA":
        if genero != "Femenino" and (edad > 33 or edad < 40):
            contadorDeNoVotantesAIA += 1
    contadorGeneral += 1

#Si hubo ingreso de masculinos, mostrara lo pedido en pantalla, de lo contrario mostrara un mensaje que no hubo ingresados
if flagMasculinos:
    print("No hubo ingreso de masculinos")
else:
    print(f"Cantidad de masculinos que votaron IA o IOT con la edad entre 25 y 50 años inclusive: {contadorMasculinosVotantes}\n")
    print("Datos del hombre de mayor edad")
    print(f"Nombre: {nombreDelMasculinoMayor}")
    print(f"Edad: {edadDeMasculinoMayor}")
    print(f"Tecnologia escogida: {tecnologiaElegidaPorElMayor}")

print(f"\nPorcentaje de empleados que no son femeninos entre 33 y 40 años que no votaron ia son: {(contadorDeNoVotantesAIA*100)/contadorGeneral}")
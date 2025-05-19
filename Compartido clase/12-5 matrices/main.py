from Funciones import *

#Menú

#Necesitamos crear un sistema que me permita guardar las notas de 5 alumnos, cada nota se va a guardar por trimestre

#Matrices de datos con apoyo de vectores paralelos 

# 1. Cargar nombres alumnos
# 2. Cargar notas de cada trimestre
# 3. Mostrar alumnos
# 4. Mostrar promedio de notas
# 5. Mostrar nombre de los alumnos que se llevan la materias
# 6. Mostrar nombre de los alumnos que como nota final les quedo un aplazo
# 7. Salir

import os
from funciones import *

array_nombres = crear_array(2,0)
matriz_notas = crear_matriz(2,3,0)

# print(array_nombres)
# mostrar_matriz(matriz_notas)

while True:
    print("1. Cargar nombres alumnos\n2. Cargar notas de cada trimestre\n3. Mostrar alumnos\n4. Mostrar promedio de notas\n5. Mostrar nombre de los alumnos que se llevan la materias\n6. Mostrar nombre de los alumnos que como nota final les quedo un aplazo\n7. Salir")

    opcion = int(input("Su opcion: "))
    while opcion > 7 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-7): "))
    if opcion == 1:
        print("CARGANDO NOMBRES")
        cargar_nombres_alumnos(array_nombres)
        # cargar_array_string(array_nombres,"Ingrese apellido alumno")
        print("NOMBRES CARGADOS CORRECTAMENTE")
    elif opcion == 2:
        print("CARGANDO NOTAS")
        cargar_notas_trimestre(matriz_notas)
        print("NOTAS CARGADAS CORRECTAMENTE")
        mostrar_matriz(matriz_notas)
    elif opcion == 3:
        mostrar_alumnos(array_nombres,matriz_notas)
    elif opcion == 4:
        mostrar_promedio_alumnos(matriz_notas)
    elif opcion == 5:
        mostrar_alumnos_no_superan_nota_promedio(array_nombres,matriz_notas,7)
    elif opcion == 6:
        mostrar_alumnos_no_superan_nota_promedio(array_nombres,matriz_notas,4)
    elif opcion == 7:
        print("Saliendo...")
        break
    input("Toque cualquier boton para continuar...")
    os.system("clear")
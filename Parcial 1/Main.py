from Funciones import *
from Vectores import *
from Matrices import *

def main():
    """Funcion principal del programa que ejecuta el menu y las opciones"
    """
    flag_carga_participantes = False
    flag_carga_puntuaciones = False
    participantes = crear_array(5, "")
    puntuaciones = crear_matriz(5, 3, 0)

    while True:
        opcion = menu()
        if opcion == 0:
            print("\nSaliendo del programa...")
            break
        elif opcion == 1:
            limpiar_pantalla()
            if cargar_participantes(participantes):
                input("\nParticipantes cargados. Presione Enter para continuar...")
                flag_carga_participantes = True
            else: 
                print("\nError al cargar los participantes.")
                input("Presione Enter para continuar...")   
        elif opcion == 2:
            limpiar_pantalla()
            if not flag_carga_participantes:
                print("Debe cargar los participantes primero.")
            else:
                if not cargar_puntuaciones(participantes, puntuaciones):
                    print("\nError al cargar las puntuaciones.")
                else:
                    flag_carga_puntuaciones = True
            input("Presione Enter para continuar...")
        elif opcion == 3:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("\n\n\n\n")
                mostrar_puntuaciones(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 4:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Participantes con promedio mayor a 4:\n")
                participantes_con_promedio_mayor_a(participantes, puntuaciones, 4)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 5:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Participantes con promedio mayor a 7:\n")
                participantes_con_promedio_mayor_a(participantes, puntuaciones, 7)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 6:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Promedio de cada jurado:\n")
                mostrar_promedio_jurado(puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 7:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Promedios del jurado:\n")
                if mostrar_jurados_mas_estrictos(puntuaciones):
                    print("ok")
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 8:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                mostrar_participante_por_nombre(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 9:  
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                top_tres_participantes(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        elif opcion == 10:
            if flag_carga_participantes and flag_carga_puntuaciones:
                limpiar_pantalla()
                mostrar_participantes_ordenados_alfabetico(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        else:
            print("Opcion no valida, reingrese.")

main()
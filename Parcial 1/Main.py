from Funciones import *
from Funciones_Vectores import *
from Funciones_Matrices import *

def main():
    """Funcion principal del programa que ejecuta el menu y las opciones"
    """
    # Variables de control
    # 
    # Declaramos dos flags para corraborar que se cargaron los participantes y las puntuaciones
    flag_carga_participantes = False
    flag_carga_puntuaciones = False
    # Creamos un vector de participantes y una matriz de puntuaciones
    participantes = crear_array(5, "")
    puntuaciones = crear_matriz(5, 3, 0)

    while True:
        opcion = menu()
        # Opcion de salida
        if opcion == 0:
            print("\nSaliendo del programa...")
            break
        # Opcion de carga de participantes
        elif opcion == 1:
            limpiar_pantalla()
            # Verifica si ya se cargaron los participantes y cambia la variable de control
            if cargar_participantes(participantes):
                input("\nParticipantes cargados. Presione Enter para continuar...")
                flag_carga_participantes = True
            # Si no se cargaron, dara un error
            else: 
                print("\nError al cargar los participantes.")
                input("Presione Enter para continuar...")   
        # Opcion de carga de puntuaciones
        elif opcion == 2:
            limpiar_pantalla()
            # Si los participantes no se cargaron, no se podran cargar las puntuaciones
            if not flag_carga_participantes:
                print("Debe cargar los participantes primero.")
            else:
                # Comprueba si se cargaron las puntuaciones y cambia la variable de control
                if cargar_puntuaciones(participantes, puntuaciones):
                    flag_carga_puntuaciones = True
                else:
                    print("\nError al cargar las puntuaciones.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar puntuaciones
        elif opcion == 3:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("\n\n\n\n")
                mostrar_puntuaciones(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar participantes con promedio mayor a 4
        elif opcion == 4:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Participantes con promedio mayor a 4:\n")
                participantes_con_promedio_mayor_a(participantes, puntuaciones, 4)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar participantes con promedio mayor a 7
        elif opcion == 5:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Participantes con promedio mayor a 7:\n")
                participantes_con_promedio_mayor_a(participantes, puntuaciones, 7)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar promedio de cada jurado
        elif opcion == 6:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Promedio de cada jurado:\n")
                mostrar_promedio_jurado(puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar jurados mas estrictos
        elif opcion == 7:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                print("Promedios del jurado:\n")
                if mostrar_jurados_mas_estrictos(puntuaciones):
                    print("ok")
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar participante por nombre
        elif opcion == 8:
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                mostrar_participante_por_nombre(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar top 3 participantes
        elif opcion == 9:  
            limpiar_pantalla()
            if flag_carga_participantes and flag_carga_puntuaciones:
                top_tres_participantes(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        # Opcion de mostrar participantes ordenados alfabeticamente
        elif opcion == 10:
            if flag_carga_participantes and flag_carga_puntuaciones:
                limpiar_pantalla()
                mostrar_participantes_ordenados_alfabetico(participantes, puntuaciones)
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")
            input("Presione Enter para continuar...")
        else:
            print("Opcion no valida, reingrese.")

# Llamada a la funcion principal
main()
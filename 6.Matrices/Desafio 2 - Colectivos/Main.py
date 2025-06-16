from Funciones_Colectivos import *

lista_legajos = inicializar_legajos()
lista_coches = crear_matriz(3,5,0)
def main():
    """_summary_
    """
    while True:
        limpiar_pantalla()
        mostrar_elementos(lista_legajos)
        if len(lista_legajos) == 0:
            print("No se cargaron choferes, se redirige al ingreso\n")
            input("Presione tecla enter para continuar...")
        else:
            opcion = menu()
            if opcion == 1:
                while True:
                    limpiar_pantalla()                
                    if cargar_planilla(lista_legajos, lista_coches):
                        print("Planilla cargada con exito\n")
                        print("Desea cargar mas planillas?\n")
                        print("1- Si\n2- No\n")
                        opcion = get_int("Ingrese opcion: ", "Error, reingrese opcion: ", 1, 2, 10)
                        if opcion == 2:
                            break
                    else:
                        print("Error al cargar la planilla\n")
            elif opcion == 2:
                limpiar_pantalla()
                mostrar_recaudacion_detallado(lista_coches)
            elif opcion == 3:
                limpiar_pantalla()
                mostrar_recaudacion_por_linea(lista_coches)
            elif opcion == 4:
                limpiar_pantalla()
                mostrar_recaudacion_un_coche(lista_coches)
            elif opcion == 5:
                limpiar_pantalla()
                mostrar_recaudacion_total(lista_coches)
            elif opcion == 6:
                input("\nFinalizando programa... precione enter para terminar...")
                break
            else:
                print("Opcion incorrecta\n")
                input("Presione tecla enter para continuar...")
            input("Presione tecla enter para continuar...")
main()
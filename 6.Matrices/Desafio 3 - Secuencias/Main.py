from Funciones_programa import *

def main() -> None:
    """Controlador de menu principal

    Returns:
        None: No devuelve nada
    """
    dimension = 5
    matriz_numerica = crear_matriz(dimension,dimension,0)

    while True:
        if len(matriz_numerica) == 0:
            print("No se pudo crear la matriz\n")
            break
        else:
            limpiar_pantalla()
            mostrar_matriz(matriz_numerica)
            opcion = menu()
            if opcion == 1:
                limpiar_pantalla()
                if menu_carga_matriz(matriz_numerica):
                    print("Matriz cargada con exito\n")
                else:
                    print("Error al cargar la matriz\n")
            elif opcion == 2:
                limpiar_pantalla()
                if verificar_secuencias_pares(matriz_numerica):
                    print("Existen secuencias de numeros consecutivos pares\n")
                else:
                    print("No existen secuencias de numeros consecutivos pares\n")
            elif opcion == 3:
                limpiar_pantalla()
                cantidad_ocurrencias = contar_ocurrencias(matriz_numerica, dimension)
                print(f"La cantidad de ocurrencias es: {cantidad_ocurrencias}\n")
            elif opcion == 6:
                print("Gracias por utilizar el programa\n")
                break
            else:
                print("Opcion no valida\n")
        input("Presione enter para continuar...")

main()
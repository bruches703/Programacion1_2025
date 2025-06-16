from Funciones_especificas import *
from LadyGaga_playlist import *

def main():
    """Controlador de menu principal
    """
    while True:
        limpiar_pantalla()
        opcion = menu()
        limpiar_pantalla()
        if opcion == 1:
            mostrar_elementos(obtener_todos_los_colaboradores(playlist_lady_gaga))
        elif opcion == 2:
            mostrar_elementos(obtener_todos_los_nombre_tema(playlist_lady_gaga))
        elif opcion == 3:
            mostrar_elementos(convertir_todas_las_vistas_numericas(playlist_lady_gaga))
        elif opcion == 4:
            mostrar_elementos(convertir_todas_las_duracion_numericas(playlist_lady_gaga))
        elif opcion == 5:
            mostrar_elementos(obtener_todas_las_urls(playlist_lady_gaga))
        elif opcion == 6:
            mostrar_elementos(formatear_todas_las_fechas(playlist_lady_gaga))
        elif opcion == 0:
            print("Programa finalizado")
        else:
            print("Opcion no valida")
        input("Presione tecla enter para continuar...")
main()
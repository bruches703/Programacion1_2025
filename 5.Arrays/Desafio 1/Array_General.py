import Menu_opciones

def controlar_menu() -> int:
    """Funcion main que llama a todas las funciones

    Returns:
        int: retorna 0 si todo finalizo correctamente o 1 si hubo algun error
    """
    array = []
    while True:
        match(Menu_opciones.menu(array)):
            case 1:
                # Genera un nuevo array donde el usuario ingrese los valores del -1000 al 1000
                array = Menu_opciones.opcion_1()
                print("El arreglo se creo correctamente\n")
                input("Presione tecla enter para continuar...")

            case 2:
                # Mostrar cantidad de positivos y cantidad de negativos ingresados
                respuestas_funciones = Menu_opciones.opcion_2(array)
                input("\n\nPresione cualquier tecla para continuar...")
                if respuestas_funciones == None:
                    print("Ocurrio un error!\n")
                    input("Presione tecla enter para continuar...")
                    break

            case 3:
                # Suma todos los elementos pares, devolviendo el resultado
                respuestas_funciones = Menu_opciones.opcion_3(array)
                if respuestas_funciones == None:
                    print("Ocurrio un error!\n")
                    input("Presione tecla enter para continuar...")
                    break
                else:
                    print(f"La suma de los pres es: {respuestas_funciones}")
                    input("Presione tecla enter para continuar...")

            case 4:
                # Identificar y mostar el mayor numero impar
                respuestas_funciones = Menu_opciones.opcion_4(array)
                input("Presione tecla enter para continuar...")
                if respuestas_funciones == None:
                    print("Ocurrio un error!")
                    input("Presione tecla enter para continuar...")
                    break
                
            case 5:
                # Muestra todos los elementos en el orden ingresado
                respuestas_funciones = Menu_opciones.opcion_5(array)
                input("Presione tecla enter para continuar...")
                if respuestas_funciones == None:
                    print("Ocurrio un error!")
                    input("Presione tecla enter para continuar...")
                    break

            case 6:
                # Muestra unicamente los Números pares de la lista
                respuestas_funciones = Menu_opciones.opcion_6(array)
                input("Presione tecla enter para continuar...")
                if respuestas_funciones == None:
                    print("Ocurrio un error!")
                    input("Presione tecla enter para continuar...")
                    break

            case 7:
                # Muestra los elementos en posiciones impares
                respuestas_funciones = Menu_opciones.opcion_7(array)
                input("Presione tecla enter para continuar...")
                if respuestas_funciones == None:
                    print("Ocurrio un error!")
                    input("Presione tecla enter para continuar...")
                    break
            case 8:
                print("Finalizando el programa")
                break

resultado = controlar_menu()
if resultado == 0:
    print("Ocurrio algun error")
else:
    print("Todo finaliza de manera correcta")
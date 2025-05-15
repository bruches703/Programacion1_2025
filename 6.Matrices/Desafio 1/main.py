import ingresos
import cuadrado_magico
import matrices
def menu() -> int:
    """Menu de opciones

    Returns:
        int: Devuelve la opcion
    """

    print("Menu")
    print("1- Crear matriz")
    print("2- Cargar matriz de manera aleatoria")
    print("3- Cargar matriz manualmente")
    print("4- Calcular la constante mágica")
    print("5- Mostrar matriz")
    print("0- Salir")

    return ingresos.get_int("Ingrese opcion: ",
                              "Error, reingrese opcion: ", 0, 5, 10)

def main(matriz: list) -> bool:
    """Controlador de menu

    Args:
        matriz (list): matriz a trabajar

    Returns:
        bool: Devuelve True si finalizo de manera correcta,
        False si hubo algun error
    """
    while True:
        match menu():
            case 1:
                matriz = cuadrado_magico.crear_matriz()
                print("Se creo correctamente...\n")
            case 2:
                if cuadrado_magico.ingresar_valores_aleatorios(matriz):
                    print("Se ingreso de manera correcta...\n")
                else:
                    print("No se pudo ingresar valores\n")
            case 3:
                matriz = cuadrado_magico.ingresar_valores(matriz)
                print("Se ingreso de manera correcta...\n")
            case 4:
                if cuadrado_magico.validar_tamaño_matriz(matriz):
                    constante = cuadrado_magico.constante_magica(matriz)
                    print(f"La constante magica es: {constante}")
                else:
                    print("La matriz no es cuadrada\n")
            case 5:
                if matrices.mostrar_matriz(matriz):
                    print("Presione para continuar\n")
            case 0:
                return True

matriz = matrices.inicialziar_matriz(3, 3, 0)
resultado = main(matriz)
if resultado:
    input("Finalizo correctamente...")
else:
    input("Ocurrio algun error...")
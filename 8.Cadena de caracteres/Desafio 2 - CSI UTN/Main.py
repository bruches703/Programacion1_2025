from Funciones_CSIUTN import *
from Sospechosos import *
def main() -> None:
    """Controlador de menu principal

    Returns:
        None: No devuelve nada
    """
    muestra = "CGTTTAATG"
    while True:
        opcion = menu_csiutn()
        if opcion == 1:
            pass
        elif opcion == 2:
            print("Opcion 2")
        elif opcion == 3:
            print("Opcion 3")
        elif opcion == 4:
            print("Opcion 4")
        elif opcion == 5:
            print("Opcion 5")
            break
        else:        
            print("Opcion no valida")
            
        input("Presione tecla enter para continuar...")

print(len(sospechosos))
print(len(muestras))
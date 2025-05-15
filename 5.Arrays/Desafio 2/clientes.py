import ingresos

def nuevo_cliente(lista_clientes : list) -> list | None:
    """crea una nueva lista de tipo "cliente"

    Returns:
        list | None: Retorna la lista de cliente, o None si no se logro
        crear la lista
    """
    lista_productos = []
    # Si no hay clientes ingresados, se crea la primera id con el formatao 1001
    if len(lista_clientes) == 0:
        nuevo_id = 1001
    else:
    # Se toma el ultimo id y se agrega el continuo
        nuevo_id = len(lista_clientes)

    if not menu_ingreso_productos(lista_productos):
        return None
    nuevo_nombre_cliente = ingresos.get_string("Ingrese nombre del nuevo cliente\nHasta 20 caracteres: ", 
                                               "Error, nombre extenso, reingrese: ", 20, 10)
    return [nuevo_id, lista_productos, nuevo_nombre_cliente]
     
def menu_ingreso_productos(lista: list) -> bool:
    """Permite ingresar elementos a la lista

    Args:
        lista (list): Lista a concatenar elementos

    Returns:
        bool: devuelve True si se ingreso de manera correcta, False si no
        finalizao correctamente
    """
    opcion = 1
    while opcion == 1 :
        nuevo_producto = ingresos.get_string("Ingrese nuevo producto: ",
                                             "Error, nombre de producto muy largo. Reingrese: ",
                                             15, 10)
        if nuevo_producto != None:
            lista.append()
        else:
            print("Error al ingresar el producto, se corta la carga")
            input("Presione Enter para continuar... ")
            return False

        opcion = ingresos.get_int("Desea ingresar mas productos?\n1- Si\n2- No\nIngrese opcion: ",
                                  "Error, reingrese opcion 1 o 2: ", 1, 2, 10)
        if nuevo_producto == None:
            print("Error, se ingreso la opcion mal en varias ocaciones, se corta la carga")
            input("Presione Enter para continuar... ")
            return False
    return True

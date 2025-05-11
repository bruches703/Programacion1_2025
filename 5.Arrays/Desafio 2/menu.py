import ingresos
import vectores

def main_menu() -> int | None:
    """Muestra el menu y toma la opcion ingresada por el usuario

    Returns:
        int | None: Retorna un entero, representa la opcion
        escogida por el usuario, o None si hay algun error
    """
    print("MENÚ\n")
    print("1- Productos en común")
    print("2- Productos exclusivos")
    print("3- Catalogo total")
    print("4- Recomendaciones")
    print("5- Ingresar listas")
    print("0- Salir")
    return ingresos.get_int("\nIngrese opcion: ",
                            "Error, reingrese opcion valida: ", 0, 5, 10)

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

def productos_mas_comun(lista_A: list, lista_B: list) -> list | None:
    """Busca los elementos mas comunes en las listas y las devuelve en una sola

    Args:
        lista_A (list): lista de productos del primer cliente
        lista_B (list): lista de productos del segundo cliente

    Returns:
        list | None: retorna la lista de los elementos en comun,
        o None si hubo algun error
    """
    #Si una o ambas listas estan vacias, se finaliza el bloque
    if len(lista_A) == 0 or len(lista_B) == 0 :
        print("Una o ambas listas estan vacia/as, No se pueden encontar productos en comun")
        input("Presione Enter para continuar... ")
        return None
    else:
        nueva_lista = vectores.new_Array(1)
        for elemento_de_B in lista_B:
            if elemento_de_B in lista_A:
                nueva_lista.append(elemento_de_B)
    return nueva_lista

def productos_exclusivos(lista_A: list, lista_B: list) -> list | None:
    """Crea una lista con los productos que no tienen iguales

    Args:
        lista_A (list): lista de productos del primer cliente
        lista_B (list): lista de productos del segundo cliente

    Returns:
        list | None: retorna la lista de los elementos que no tienen
        en comun, o None si hubo algun error
    """
    #Si una o ambas listas estan vacias, se finaliza el bloque
    if len(lista_A) == 0 or len(lista_B) == 0 :
        print("Una o ambas listas estan vacia/as, No se pueden encontar productos en comun")
        input("Presione Enter para continuar... ")
        return None
    else:
        nueva_lista = vectores.new_Array(1)
        # Se agregan los elementos de la lista B
        nueva_lista = productos_exclusivos_de_una_lista(lista_A, lista_B)
        # Se agregan los elementos de la lista A
        nueva_lista = productos_exclusivos_de_una_lista(lista_B, lista_A)
    return nueva_lista

def catalogo_total(lista_A: list, lista_B: list) -> list | None:
    """Muestra un catálogo completo de todos los productos

    Args:
        lista_A (list): lista de productos del primer cliente
        lista_B (list): lista de productos del segundo cliente

    Returns:
        list | None: Retorna una lista de todos los productos,
        o None si hubo un error
    """
    #Si una o ambas listas estan vacias, se finaliza el bloque
    if len(lista_A) == 0 or len(lista_B) == 0 :
        print("Una o ambas listas estan vacia/as, No se pueden encontar productos en comun")
        input("Presione Enter para continuar... ")
        return None
    else:
        nueva_lista = lista_A
        for elemento_de_B in lista_B:
            if elemento_de_B not in lista_A:
                nueva_lista.append(elemento_de_B)
    return nueva_lista

def recomendaciones(lista_A: list, listas: list) -> list | None:
    """Busca similitudes y recomienda productos al primer comprador

    Args:
        lista_A (list): Lista de productos del primer comprador
        lista_B (list): Lista de otro comprador a buscar cosas en común

    Returns:
        list | None: Retorna una lista con 
    """
        #Si una o ambas listas estan vacias, se finaliza el bloque
    if len(lista_A) == 0:
        print("Una o ambas listas estan vacia/as, No se pueden encontar productos en comun")
        input("Presione Enter para continuar... ")
        return None
    else:
        nueva_lista = []
        lista_recomendaciones = []
        for sublista in listas:
            nueva_lista = productos_mas_comun(lista_A, sublista)
            # Si tiene mas de tres productos en comun, se le recomendara elementos de la lista
            if len(nueva_lista) >= 3:
                lista_recomendaciones.append()
    return nueva_lista

def productos_exclusivos_de_una_lista(lista_A: list, lista_B: list) -> list | None:
    """Crea una lista con los productos que solo tiene la lista_B

    Args:
        lista_A (list): lista de productos del primer cliente
        lista_B (list): lista de productos del segundo cliente

    Returns:
        list | None: retorna la lista de los elementos que solo tiene
        la lista_B, o None si hubo algun error
    """        
    #Si una o ambas listas estan vacias, se finaliza el bloque
    if len(lista_A) == 0 or len(lista_B) == 0 :
        print("Una o ambas listas estan vacia/as, No se pueden encontar productos en comun")
        input("Presione Enter para continuar... ")
        return None
    else:
        nueva_lista = vectores.new_Array(0)
        for elemento_de_B in lista_B:
            if elemento_de_B not in lista_A:
                nueva_lista.append(elemento_de_B)
    return nueva_lista
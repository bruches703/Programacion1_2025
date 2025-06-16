def ordenar_array(array: list, ordenamiento: bool=False) -> list:
    """Ordena un array de enteros de manera ascendente

    Args:
        array (list): array a ordenar
        ordenamiento (bool): True: ascendente, False: descendente

    Returns:
        list: array ordenado
    """
    if len(array) == 0:
        return []
    else:
        if ordenamiento:
            for i in range(len(array)-1):
                for j in range(i+1, len(array)):
                    if array[j] > array[i]:
                        auxiliar = array[i]
                        array[i] = array[j]
                        array[j] = auxiliar
        else:
            for i in range(len(array)-1):
                for j in range(i+1, len(array)):
                    if array[j] < array[i]:
                        auxiliar = array[i]
                        array[i] = array[j]
                        array[j] = auxiliar            
    return array

def intercalar_vectores(array_uno: list, array_dos: list, ordenamiento: bool=False) -> list:
    """Intercala dos vectores y los ordena

    Args:
        array_uno (list): vector 1
        array_dos (list): vector 2
        ordenamiento (bool): True: ascendente, False: descendente

    Returns:
        list: vector intercalado
    """
    array_intercalado = []
    for i in range(len(array_uno)):
        array_intercalado += [array_uno[i]]
        array_intercalado += [array_dos[i]]
    return ordenar_array(array_intercalado, ordenamiento)

def mostrar_array(array: list) -> None:
    """Muestra un array de enteros, si es positivo lo ordena de manera
    creciente, de ser negativo de forma descendente

    Args:
        array (list): array a mostrar
    """
    nuevo_array = ordenar_array(array)
    for elemento in nuevo_array:
        if elemento > 0:
            print(f"{elemento}", end=" ")
    print("")
    for elemento in nuevo_array:
        if elemento < 0:
            print(f"{elemento}", end=" ")


# array1 = [1,-2,5]
# array2 = [1,8,-3,2]
# new_array = intercalar_vectores(array1, array2)
# print(new_array)
# print("")
# mostrar_array(new_array)
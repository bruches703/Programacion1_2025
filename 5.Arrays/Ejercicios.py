# Ejercicios
# 1.Desarrollar una función que permita crear un array
# de números con la cantidad de elementos que establezca el parámetro recibido.
def new_Array(cantidad_elementos: int) -> list:
    """

    Args:
        cantidad_elementos (int): _description_

    Returns:
        _type_: _description_
    """
    nuevo_array = [0] * cantidad_elementos
    return nuevo_array 

# 2.Escribir una función que permita ingresar la cantidad de números que reciba 
# como parámetro.  Crear el array con la función del punto 1.
def crear_array() -> list:
    """Crea un arreglo del tamaño que ingrese y permine llenar con los valores
    
    Returns:
        int: promedio de los numeros del arreglo
    """
    parametro = int(input("Ingrese cantidad de numeros del array: "))
    array_de_numeros = new_Array(parametro)

    for i in range(len(array_de_numeros)):
        array_de_numeros[i] = int(input("Ingrese nuevo valor: "))
    return array_de_numeros

# 3.Escribir una función que reciba una lista de enteros, 
# la misma calculará y devolverá el promedio de todos los números. 
def calcular_promedio_lista(array: list) -> int:
    """
        Calcula y devolverá el promedio de todos los números
    Args:
        array (list): lista de numeros

    Returns:
        int: promedio de los numeros del arreglo
    """
    suma=0
    for i in range (len(array)):
        suma += array[i]
    return suma//len(array)

# 4.Escribir una función parecida a la anterior, pero la misma 
# deberá calcular y devolver el promedio de los números positivos.
def calcular_promedio_positivos_lista(array: list) -> int:
    """Calcula el promedio de los numeros positivos del arreglo

    Args:
        array (list): arreglo de numeros

    Returns:
        int: promedio de los positivos
    """
    suma=0
    contador_positivos = 0
    for i in range (len(array)):
        if array[i] % 2 == 0:
            suma += array[i]
            contador_positivos += 1
    return suma // contador_positivos

# 5.Escribir una función que calcule y retorne el producto de 
# todos los elementos de la lista que recibe como parámetro.
def calcular_producto_lista(array: list) -> int:
    """Calcula el producto del todos los elementos del arreglo

    Args:
        array (list): arreglo de enteros que se calculara el producto

    Returns:
        int: resultado del producto de todos los elementos del arreglo
    """
    producto = 1
    for i in range(len(array)):
        producto = producto * array[i]
    return producto

# 6.Escribir una función que reciba como parámetros una lista de
# enteros y retorne la posición del valor máximo encontrado
def indice_del_valor_mas_alto(array: list) -> int | list :
    """Busca y devuelve el o los indices del valor mas alto de la lista

    Args:
        array (list): lista de numeros enteros que se debe encontar el valor mas alto

    Returns:
        int | list: devuelve un entero con el indice del valor mas alto, de repetirse devuelve un array con los indices
    """
    flag = True
    indice = 0
    maximo = 0
    # Busca el valor mas alto
    if len(array)==0:
        return None
    else:
        for i in range(len(array)):
            if flag or maximo <= array[i]:
                maximo = array[i]
                flag = False
                indice = i
        return indice

# 7.Escribir una función que reciba como parámetros una
# lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
def indices_del_valor_mas_alto(array: list) -> list | None:
    """Busca el o los indices del elemento de mayor valor

    Args:
        array (list): vector de enteros

    Returns:
        list | None: 
            list: devuelve una lista con los indices de haber repetido el valor maximo
            None: si la lista esta vacia
    """
    # Si el array esta vacio, retorna None
    if(len(array) == 0):
        return None
    else:
    # Busca el valor maximo del array
        maximo = 0
        flag = True
        for i in range(len(array)):
            if flag or maximo < array[i]:
                maximo = array[i]
                flag = False
    # Teniendo el maximo, buscamos los indices que tengan ese mismo valor y lo retornamos
        indices = []
        for i in range(len(array)):
            if array[i] == maximo:
                indices.append(i)

    return indices

# 8.Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# 
# Una lista de nombres (lista_nombres).
# Un nombre a buscar en la lista (nombre_antiguo).
# Un nombre de reemplazo (nombre_nuevo).
# 
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados
def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int | None:
    """Reemplaza el string 'nombre_nuevo' por todas las apariciones del string 'nombre_antiguo'
        en el array.

    Args:
        lista_nombres (e): array de strings a modificar
        nombre_antiguo (str): cadena de caracteres a buscar para ser reemplazado.
        nombre_nuevo (str): nuevo string que reemplazara a los elementos indicados.

    Returns:
        int | None: retornara un int con la cantidad de sustituciones o None si el array esta vacio.
    """
    # Verificar si la cadena esta vacia
    if len(lista_nombres) == 0:
        return None
    else:
        sustituciones = 0
        for i in range(len(lista_nombres)):
            if lista_nombres[i] == nombre_antiguo:
                lista_nombres[i] = nombre_nuevo
                sustituciones += 1
        return sustituciones

# 9.Crear una función que reciba como parámetros dos arrays. 
# La función deberá retornar un array con la intersección de los dos arrays.
def interseccion_de_arrays(arreglo_uno: list, arreglo_dos: list) -> list | None:
    """Retornar un array con la intersección de los dos arrays.

    Args:
        arreglo_uno (list): Primer arreglo a analizar los elementos
        arreglo_dos (list): Segundo arreglo a analizar los elementos

    Returns:
        list | None: Retorna una lista con los elementos en comun, 
        o None si algun array esta vacio
    """
    # Verificar si la cadena esta vacia
    if len(arreglo_uno) == 0 or len(arreglo_dos) == 0:
        return None
    else:
        arreglo_intersecciones = []
        for i in range(len(arreglo_uno)):
            for j in range(len(arreglo_dos)):
                if arreglo_uno[i] == arreglo_dos[j]:
                    arreglo_intersecciones.append(arreglo_uno[i])
    return arreglo_intersecciones

# 10. Crear una función que reciba como parámetros dos arrays.
# La función deberá retornar un array con la unión de los dos arrays
def union_de_arrays(array_uno: list, array_dos: list) -> list:
    """Concatena dos arreglos

    Args:
        array_uno (list): Primer array a concatenar
        array_dos (list): Segundo array a concatenar

    Returns:
        list: Retorna un arreglo resultado de concatenar los dos arrays del parametro
    """
    array_concatenado = []
    # Si los dos arreglos estan vacios, evita todo lo demas y retorna uno vacio
    if len(array_uno) == 0 or len(array_dos) == 0:
        return array_concatenado
    else:
    # Se le asigna el valor del primer arreglo a la variable
    # y se recorre el segundo arreglo y lo concatena
        array_concatenado = array_uno
        for elemento in array_dos:
            if elemento not in array_concatenado:
                array_concatenado.append(elemento)

    return array_concatenado

# 11. Crear una función que reciba como parámetros dos arrays. 
# La función deberá retornar un array con la diferencia de los dos arrays.
def diferencia_entre_arreglos(array_uno: list, array_dos: list) -> list :
    """_summary_

    Args:
        array_uno (list): _description_
        array_2 (list): _description_

    Returns:
        list: _description_
    """
    array_resultado = []
    if len(array_uno) == 0 or len(array_dos) == 0: 
        # Devuelve arreglo vacio si no hay elementos en ningun parametro
        return array_resultado
    elif len(array_uno) == 0 and len(array_dos) > 0:
        # Devuelve el segundo arreglo si el primer no parametro no tiene elementos.
        return array_dos
    elif len(array_uno) > 0 and len(array_dos) == 0:
        # Devuelve el primer arreglo si el segundo no parametro no tiene elementos.
        return array_uno
    else:
        # Agrega los elementos del primer arreglo si es que no estan en el segundo.
        for elemento in array_uno:
            if elemento not in array_dos:
                array_resultado.append(elemento)
        # Agrega los elementos del segundo arreglo si es que no estan en el primero.
        for elemento in array_dos:
            if elemento not in array_uno:
                array_resultado.append(elemento)
    return array_resultado

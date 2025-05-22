#GENERAL
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
        
    return matriz

#GENERAL
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array

#ESPECIFICA
def cargar_nombre_partidos(array_nombres:list) -> bool:
    if type(array_nombres) == list and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            #Pedimos el dato
            #Ustedes deberian llamar a su propia función get_string()
            nombre = input(f"Ingrese el nombre partido {i + 1}: ")
            #Lo agregamos al array
            array_nombres[i] = nombre
    else:
        retorno = False
        
    return retorno

#GENERAL
def mostrar_array(array:list):
    for i in range(len(array)):
        print(f"{array[i]}")

#GENERAL
def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}",end=" ")
        print("")

#ESPECIFICA
def cargar_votos(matriz_votos:list) -> bool:
    if type(matriz_votos) == list and len(matriz_votos) > 0:
        retorno = True
        for fil in range(len(matriz_votos)):
            for col in range(len(matriz_votos[fil])):
                #Pedir el dato
                #Ustedes deberian llamar a su propia función get_int()
                voto = int(input(f"Ingrese la cantidad de votos del turno {col + 1} para el partido {fil + 1}: "))
                #Agregarlo en la matriz
                matriz_votos[fil][col] = voto
    else:
        retorno = False
        
    return retorno

#ESPECIFICA
def mostrar_partido(array_nombres:list,matriz_votos:list,indice:int) -> bool:
    if len(array_nombres) > indice and indice >= 0:
        votos_total = sumar_matriz(matriz_votos)
        votos_partido = sumar_fila(matriz_votos,indice)
        porcentaje = calcular_porcentaje(votos_total,votos_partido)
        
        print(f"PARTIDO: {array_nombres[indice]}")
        print(f"CANTIDAD VOTOS TURNO 1: {matriz_votos[indice][0]}")
        print(f"CANTIDAD VOTOS TURNO 2: {matriz_votos[indice][1]}")
        print(f"CANTIDAD VOTOS TURNO 3: {matriz_votos[indice][2]}")
        print(f"PORCENTAJE DE LOS VOTOS : {round(porcentaje,2)} %")
        retorno = True
    else:
        retorno = False
        
    return retorno

#ESPECIFICA
def mostrar_partidos(array_nombres:list,matriz_votos:list) -> bool:
    if type(array_nombres) == list and type(matriz_votos) == list and len(array_nombres) > 0 and len(matriz_votos) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            mostrar_partido(array_nombres,matriz_votos,i)
            print("")
    else:
        retorno = False
        
    return retorno 
    

#GENERAL
def calcular_porcentaje(cantidad_total:int | float,cantidad_parcial: int | float) -> float:
    porcentaje = cantidad_parcial * 100 / cantidad_total
    return porcentaje

#GENERAL
def sumar_matriz(matriz_numerica:list) -> int | float:
    suma = 0
    
    for fil in range(len(matriz_numerica)):
        for col in range(len(matriz_numerica[fil])):
            if type(matriz_numerica[fil][col]) == int or type(matriz_numerica[fil][col]) == float:
                suma += matriz_numerica[fil][col]
                
    return suma

#GENERAL
def sumar_fila(matriz_numerica:list,indice_fila:int) -> int | float:
    suma_fila = 0
    
    for col in range(len(matriz_numerica[0])):
        if type(matriz_numerica[indice_fila][col]) == int or type(matriz_numerica[indice_fila][col]) == float :
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila
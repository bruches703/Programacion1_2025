from Funciones_Inputs import *
from Funciones_Matrices import *
from Funciones_Vectores import *
import os

# Funcion de limpiar pantalla
def limpiar_pantalla():
    """Limpia la pantalla
    """
    os.system('cls')
#----------------------------------------------------------------------------------------
# Funcion con el menu de opciones
def menu() -> int:
    """Muestra un menu por pantalla para que el usuario elija una opcion

    Returns:
        int: opcion escogida por el usuario
    """
    limpiar_pantalla()
    # Muestra el menu de opciones
    print("Menu de opciones:")
    print("--------------------------------------------")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. particiapantes con promedio mayor a 4")
    print("5. Participantes con puntuacion mayor a 7")
    print("6. Promedio de cada jurado")
    print("7. Jurado mas estricto")
    print("8. Buscar participante por nombre")
    print("9. Top 3 participantes")
    print("10. Participantes ordenados alfabeticamente")
    print("0. Salir")
    # Levanta la opcion del usuario, lo valida y lo devuelve
    opcion = get_int("Seleccione una opcion: ", "Error, reingrese: ", 0, 10, 10)
    return opcion
#----------------------------------------------------------------------------------------
# Funcion de opcion 1
def cargar_participantes(participantes: list) -> bool:
    """Carga los participantes en el array

    Args:
        participantes (list): Array donde se cargaran los participantes

    Returns:
        bool: True si se cargaron los participantes, False si hubo un error
    """
    mensaje_error = "Error, reingrese el nombre: "
    # Carga los participantes en el vector
    for i in range(len(participantes)):
        # Guardamos "mensaje" y "nombre" para quue al llamar la funcion get_string
        # sea mas legible
        mensaje = f"Ingrese el nombre del participante {i+1}: "
        nombre = get_string( mensaje, mensaje_error, 3, 30, 10)
        participantes[i] = nombre
    return True
#----------------------------------------------------------------------------------------
# Funcion de opcion 2
def cargar_puntuaciones(participantes: list, puntuaciones: list) -> bool:
    """Carga las puntuaciones de los participantes

    Args:
        puntuaciones (list): Matriz donde se cargaran las puntuaciones
        de cada participante

    Returns:
        bool: True si se cargaron las puntuaciones, False si hubo un error
    """
    mensaje_error = "Error, reingrese valor aceptable: "
    # Carga las puntuaciones de los participantes
    for i in range(len(participantes)):
        # Puntuacion del participante actual
        print(f"Ingrese las puntuaciones para el participante {participantes[i]}:")
        for j in range(len(puntuaciones[i])):
            mensaje =(f"Ingrese la {j+1}° puntuacion: ")
            elemento = get_int(mensaje , mensaje_error, 1, 10, 10)
            # Verifica si el elemento guardado es None
            if elemento is None:
                print("Error de ingreso, finaliza la carga")
                return False
            else:
                # Asigna el elemento a la matriz de puntuaciones
                puntuaciones[i][j] = elemento
        print("\n")
    return True
#----------------------------------------------------------------------------------------
# Funcion de opcion 3
def mostrar_puntuaciones(participantes: list, puntuaciones: list):
    """Muestra las puntuaciones de los participantes

    Args:
    participantes (list): Array de participantes
        puntuaciones (list): Matriz de puntuaciones
        
    """
    # verifica si hay participantes y puntuaciones cargadas
    if len(puntuaciones) == 0 or len(participantes) == 0:
        print("No hay puntuaciones o participantes cargados.")
        return False
    else:
        for i in range(len(participantes)):
            mostrar_puntuacion_un_participante(participantes[i], puntuaciones[i])
            print("--------------------------------------------")

def mostrar_puntuacion_un_participante(participant: str, puntuaciones: list):
    """Muestra las puntuaciones de un participante

    Args:
        participantes (list): Array de participantes
        puntuaciones (list): Matriz de puntuaciones
        indice (int): Indice del participante a mostrar

    """
    # Mostramos el participante
    print(f"Participante: {participant}")
    # Recorremos la lista de puntuaciones e imprimimos las puntuaciones
    for i in range(len(puntuaciones)):
        print(f"Puntuacion jurado {i+1}: {puntuaciones[i]}")
    print(f"Promedio: {promedio_vector(puntuaciones):.2f}")
#----------------------------------------------------------------------------------------
# Funciones de opcion 4 y 5
def participantes_con_promedio_mayor_a(participantes: list,
                                       puntuaciones: list, promedio_esperado: int):
    """Muestra los participantes con promedio mayor a 4

    Args:
        participantes (list): Array de participantes
        puntuaciones (list): Matriz de puntuaciones
    """
    # Inicializamios una variable de control en TRUE que validara que no hay participantes
    # con promedio mayor a 4
    flag = True
    # Recorremos la listas de puntuacions, utilizamos la lsita PARTICIPANTES para el bucle
    # porque tiene la misma cantidad de elementos
    for i in range(len(participantes)):
        # Sumamos los elementos en la funcion que recibe una lista y suma cada uno. El resultado
        # lo dividimos por la cantidad de elementos de la lista y obtenemos el promedio
        promedio = sumar_elementos(puntuaciones[i]) / len(puntuaciones[i])
        if promedio > promedio_esperado:
            flag = False
            print(f"Participante: {participantes[i]} - Promedio: {promedio:.2f}")
    if flag:
        print(f"No hay participantes con promedio mayor a {promedio_esperado}.")

# Funciones de opcion 6
def promedio_jurado(puntuaciones: list) -> list:
    """Calcula el promedio de cada jurado

    Args:
        puntuaciones (list): Matriz de puntuaciones

    Returns:
        list: Lista con los promedios de cada jurado
    """
    # Evaluamos que la lista no este vacia, sino devuelve una lista vacia
    if len(puntuaciones) == 0:
        return []
    # Creamos la lista de PROMEDIOS
    promedios = []
    # Recorremos la lista
    for i in range(len(puntuaciones[0])):
        suma = 0
        for j in range(len(puntuaciones)):
            # Usamos las variables de control invertidas, porque necesitamos
            # los elementos de cada columna y los sumamos y calculamos el promedio
            suma += puntuaciones[j][i]
        promedios += [suma / len(puntuaciones)]
    return promedios

def mostrar_promedio_jurado(puntuaciones: list) -> bool:
    """Muestra el promedio de cada jurado

    Args:
        puntuaciones (list): Matriz de puntuaciones

    Returns:
        bool: True si se muestra correctamente, False si hubo un error
    """
    if len(puntuaciones) == 0:
        print("No hay puntuaciones cargadas.")
        return False
    else:
        promedios = promedio_jurado(puntuaciones)
        if promedios is None:
            print("No hay jurados cargados.")
            return False
        else:
            for i in range(len(promedios)):
                print(f"Promedio del jurado N°{i+1}: {promedios[i]:.2f}")
    return True

# Funciones de opcion 7
def mostrar_jurados_mas_estrictos(puntuaciones: list) -> bool:
    """Muestra el jurado mas estricto

    Args:
        puntuaciones (list): Matriz de puntuaciones

    Returns:
        bool: True si se muestra correctamente, false si hubo un error
    """
    # calcula el promedio mas bajo de los jurados
    promedio_mas_bajo = calcular_promedio_mas_bajo(puntuaciones)
    # verifica si el promedio mas bajo es None
    if promedio_mas_bajo == None:
        print("No hay puntuaciones cargadas.")
        return False
    else:
        # calcula el promedio de cada jurado
        promedios = promedio_jurado(puntuaciones)
        # verifica si la lista de promedios esta vacia
        if len(promedios) == 0:
            print("No hay jurados cargados.")
            return False
        else:
            # Recorremos la lista de promedios para mostrar
            # los jurados con el promedio mas bajo
            for i in range(len(promedios)):
                if promedios[i] == promedio_mas_bajo:
                    print(f"El jurado N°{i+1} es el mas estricto con un promedio de {promedios[i]:.2f}")

def calcular_promedio_mas_bajo(puntuaciones: list) -> float:
    """Calcula el promedio mas bajo de los jurados

    Args:
        puntuaciones (list): Matriz de puntuaciones

    Returns:
        float: Promedio mas bajo
    """
    # Verifica si la matriz de puntuaciones esta vacia
    if len(puntuaciones) == 0:
        return None
    else:
        # Calcula el promedio de cada uno jurado
        promedios = promedio_jurado(puntuaciones)
        # Verifica si la lista de promedios esta vacia
        if len(promedios) == 0:
            return None
        else:
            # El promedio mas bajo es el primer elemento de la lista
            promedio_mas_bajo = promedios[0]
            # Recorre la lista de promedios para encontrar el promedio mas bajo
            for i in range(len(promedios)):
                if promedios[i] < promedio_mas_bajo:
                    promedio_mas_bajo = promedios[i]
    return promedio_mas_bajo

# Funcion de opcion 8
def mostrar_participante_por_nombre(participantes: list, puntuaciones: list) -> bool:
    """Busca un participante por su nombre y muestra sus datos

    Args:
        participantes (list): Array de participantes
        puntuaciones (list): Matriz de puntuaciones

    Returns:
        bool: Devuelve True si se encuentra el participante,
        False si no se encuentra o si hubo un error
    """

    if len(participantes) == 0:
        print("No hay participantes cargados.")
        return False
    else: 
        mensaje = "Ingrese el nombre del participante a buscar (solo letras y espacios): "
        mensae_error = "Error, reingrese el nombre: "
        nombre = get_string(mensaje,mensae_error, 3, 30, 10)
    if nombre is None:
        print("Error de ingreso, finaliza la busqueda")
        return False
    
    for i in range(len(participantes)):
        if comparar_cadenas_ignorando_case(participantes[i], nombre):
            mostrar_puntuacion_un_participante(participantes[i], puntuaciones[i])
            return True
    print("Participante no encontrado.")
    return False

# Funcion de opcion 9
def top_tres_participantes(participantes: list, puntuaciones: list):
    """Muestra el top 3 de participantes con mejor promedio

    Args:
        participantes (list): Array de participantes
        puntuaciones (list): Matriz de puntuaciones
    """
    # Evaluamos que las listas no esten vacias
    if len(participantes) == 0 or len(puntuaciones) == 0:
        print("No hay participantes o puntuaciones cargadas.")
    else:
        # Creamos dos listas, una tendra los promedios de cada participante
        # la otra es un auxiliar para guardar los participantes y
        # no modificar la lista original
        promedios = []
        participantes_auxiliar = []
        # Copiamos la lista de participantes a la auxiliar
        participantes_auxiliar = copiar_vector(participantes)
        for i in range(len(participantes_auxiliar)):
            promedios += [promedio_vector(puntuaciones[i])]
        # inicializamos las variables auxiliares para el swapeo
        auxiliar_float = 0
        auxiliar_string = ""
        # Recorremos la lista de PROMEDIOS y calculamos
        # cual tuvo el promedio de mayor valor
        for i in range(len(promedios)-1):
            for j in range(i+1, len(promedios)):
                if promedios[i] < promedios[j]:
                    # Intercambia los promedios
                    auxiliar_float = promedios[i]
                    promedios[i] = promedios[j]
                    promedios[j] = auxiliar_float
                    # Intercambia los participantes
                    auxiliar_string = participantes_auxiliar[i]
                    participantes_auxiliar[i] = participantes_auxiliar[j]
                    participantes_auxiliar[j] = auxiliar_string
        # Mostramos todo por pantalla
        print("Top 3 participantes con mejor promedio:\n")
        for i in range(3):
            print(f"Top {i+1}.Participante {participantes_auxiliar[i]} con promedio: {promedios[i]:.2f}")

# Funcion de opcion 10
def mostrar_participantes_ordenados_alfabetico(participantes: list, puntuaciones: list):
    """Muestra los participantes ordenados alfabeticamente

    Args:
        participantes (list): Array de participantes
    """
    
    if len(participantes) == 0:
        print("No hay participantes cargados.")
        return
    else:
        # Copia los participantes y las puntuaciones para no modificar los originales
        auxiliar_participantes = copiar_vector(participantes)
        puntuaciones_auxiliar = copiar_matriz(puntuaciones)
        # Ordena los participantes alfabeticamente usando el metodo burbuja
        for i in range(len(auxiliar_participantes)-1):
            for j in range(i+1, len(auxiliar_participantes)):
                if auxiliar_participantes[i] > auxiliar_participantes[j]:
                    # Intercambia los participantes
                    aux = auxiliar_participantes[i]
                    auxiliar_participantes[i] = auxiliar_participantes[j]
                    auxiliar_participantes[j] = aux
                    # Intercambia las puntuaciones correspondientes
                    aux = puntuaciones_auxiliar[i] 
                    puntuaciones_auxiliar[i] = puntuaciones_auxiliar[j]
                    puntuaciones_auxiliar[j] = aux
        # Muestra los participantes ordenados alfabeticamente
        print("\n\n\nParticipantes ordenados alfabeticamente:")
        mostrar_puntuaciones(auxiliar_participantes, puntuaciones_auxiliar)
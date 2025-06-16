from Ingresos import *
from Vectores import *
from Matrices import *
from Sospechosos import *
from Funciones_Generales import *
 
def menu_csiutn() -> int:
    """
    Muestra el menu principal del programa

    Returns:
        int: Opcion escogida
    """
    print("Menu principal")
    print("1. Analizar cada secuencia de ADN de los sospechosos.")
    print("2. Compararla con la secuencia hallada en la escena del crimen.")
    print("3. Determinar si hay coincidencia exacta.")
    print("4. Mostrar el nombre del sospechoso culpable")
    print("5. Salir")
    opcion = get_int("Seleccione una opcion: ", "Error, reingrese: ", 1, 5, 10)
    return opcion

def analisis_secuencia(muestra: str, sospechosos: list) -> list:
    """Analiza la secuencia de ADN de cada sospechoso
    
    Args:
        muestra (str): Secuencia de ADN hallada en la escena del crimen
        sospechosos (list): Lista de sospechosos
    
    """
    lista_coincidencias = []
    for sospechoso in sospechosos:
        contador = 0
        if len(muestra) != len(sospechoso):
            for i in range(len(muestra)):
                if muestra[i] == sospechoso[i]:
                    contador +=1
        if contador == len(muestra):
            lista_coincidencias += [sospechoso]
    return lista_coincidencias

def analisis_secuencia(muestras: list, sospechosos: list) -> list:
    """Analiza la secuencia de ADN de cada sospechoso
    
    Args:
        muestras (list): Lista de secuencias de ADN halladas en la escena del crimen
        sospechosos (list): Lista de sospechosos
    
    Returns:
        list: Lista de sospechosos con coincidencias
    
    """
    lista_coincidencias = []
    for muestra in muestras:
        lista_coincidencias += [analisis_secuencia(muestra, sospechosos)]
    return lista_coincidencias
from LadyGaga_playlist import *
from Ingresos import *
from Funciones_Generales import *
from datetime import datetime, date

def menu() -> int:
    """Muestra un menu por pantalla para que el usuario elija una opcion

    Returns:
        int: opcion escogida por el usuario
    """
    print("Menu de opciones")
    print("1- Obtener colaboradores")
    print("2- Obtener nombre de tema")
    print("3- Convertir visitas numericas de forma extensa")
    print("4- Convertir duracion a formato sengudos")
    print("5- Obtener url de la cancion")
    print("6- Formatear fecha")
    print("0 -Salir")
    
    return get_int("Ingrese opcion: ", "Opcion incorrecta, reingrese: ", 0, 6, 10)

# opcion 1
def obtener_todos_los_colaboradores(playlist: list) -> list:
    """Obtener todos los colaboradores de la playlist

    Args:
        playlist (list): Playlist de canciones
        
    Returns:
        list: Lista de colaboradores
    """
    colaboradores = []
    for cancion in playlist:
        colaboradores.extend(obtener_colaboradores(cancion["Tema"]))
    return colaboradores

def obtener_colaboradores(titulo: str) -> list:
    """Obtener colaboradores de un tema

    Args:
        titulo (str): Titulo de la cancion

    Returns:
        list: Lista de colaboradores
    """
    indice_guion = titulo.find("-")
    if indice_guion == -1:
        return []
    subcadena = titulo[:indice_guion]
    colaboradores = subcadena.split(" | ")
    return colaboradores

# opcion 2
def obtener_nombre_tema(titulo: str) -> str:
    """Obtener el nombre de un tema

    Args:
        título (str): Titulo de la cancion

    Returns:
        str: Nombre del tema
    """
    indice_guion = titulo.find("-")
    if indice_guion == -1:
        return titulo
    else:
        subcadena = titulo[indice_guion + 2:]
    return subcadena

def obtener_todos_los_nombre_tema(lista: list) -> list:
    """Obtener todos los nombres de los temas de la playlist

    Args:
        lista (list): Playlist de canciones

    Returns:
        list: Lista de temas
    """
    nueva_lista = []
    for cancion in lista:
        nueva_lista.append(obtener_nombre_tema(cancion["Tema"]))
    return nueva_lista

# opcion 3
def convertir_vistas_numerico(vistas: str) -> int:
    """Convertir visitas numericas de forma extensa a numericas

    Args:
        vistas (str): Visitas en formato extenso

    Returns:
        int: Visitas en formato numerico
    """
    indice_espacio = vistas.find(" ")
    numero = int(vistas[:indice_espacio])
    numero = numero * 1000000
    return numero

def convertir_todas_las_vistas_numericas(playlist: list) -> list:
    """Convertir todas las visitas numericas de la playlist

    Args:
        playlist (list): Playlist de canciones

    Returns:
        list: Lista de visitas numericas
    """
    vistas_numericas = []
    for cancion in playlist:
        vistas_numericas.append(convertir_vistas_numerico(cancion["Vistas"]))
    return vistas_numericas

# opcion 4
def convertir_duracion_numerico(duracion: str) -> int:
    """Convertir duracion a formato numerico

    Args:
        duracion (str): Duracion en formato sengudos

    Returns:
        int: Duracion en formato numerico
    """
    indice_dos_puntos = duracion.find(":")
    minutos = int(duracion[:indice_dos_puntos])
    segundos = int(duracion[indice_dos_puntos + 1:])
    return (minutos * 60) + segundos

def convertir_todas_las_duracion_numericas(playlist: list) -> list:
    """Convertir todas las duraciones numericas de la playlist

    Args:
        playlist (list): Playlist de canciones

    Returns:
        list: Lista de duraciones numericas
    """
    duraciones_numericas = []
    for cancion in playlist:
        duraciones_numericas.append(convertir_duracion_numerico(cancion["Duracion"]))
    return duraciones_numericas

# opcion 5
def obtener_codigo(url: str) -> str:
    """Obtener el codigo de la url

    Args:
        url (str): Url de la cancion

    Returns:
        str: Codigo de la url
    """
    indice_interrogacion = url.find("=")
    if indice_interrogacion == -1:
        return url
    else:
        subcadena = url[indice_interrogacion + 1:]
    return subcadena

def obtener_todas_las_urls(playlist: list) -> list:
    """Obtener todas las urls de la playlist

    Args:
        playlist (list): Playlist de canciones

    Returns:
        list: Lista de urls
    """
    urls = []
    for cancion in playlist:
        urls.append(obtener_codigo(cancion["Link Youtube"]))
    return urls

def formatear_fecha(fecha: str) -> date:
    """Formatear fecha

    Args:
        fecha (str): Fecha en formato string

    Returns:
        date: Fecha en formato date
    """
    return datetime.strptime(fecha, "%Y-%m-%d").date()

def formatear_todas_las_fechas(playlist: list) -> list:
    """Formatear todas las fechas de la playlist

    Args:
        playlist (list): Playlist de canciones

    Returns:
        list: Lista de fechas
    """
    fechas = []
    for cancion in playlist:
        fechas.append(formatear_fecha(cancion["Fecha lanzamiento"]))
    return fechas
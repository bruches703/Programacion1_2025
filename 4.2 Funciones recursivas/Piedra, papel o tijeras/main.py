# El clásico juego de la infancia, donde dos jugadores eligen entre tres elementos y 
# la victoria se determina según las siguientes reglas:
# 
# Piedra aplasta Tijera → 🏆 Gana la Piedra
# Tijera corta Papel → 🏆 Gana la Tijera
# Papel envuelve Piedra → 🏆 Gana el Papel
# Si ambos jugadores eligen el mismo elemento, la ronda termina en empate.

# 📌 Reglas del Juego
# La partida se juega al mejor de 3 rondas.
# Si un jugador (humano o máquina) logra dos aciertos seguidos, la partida finaliza automáticamente.
# En caso de empate en las 3 rondas, el juego continuará hasta que haya un ganador.

import ingresos
import random

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """Verifica el ganador de la partida, 1-Piedra, 2-Papel, 3-Tijeras

    Args:
        jugador (int): indica la eleccion del jugador
        maquina (int): indica la eleccion de la maquina

    Returns:
        str: devuelve quien gano. devuelve "Jugador", "Maquina" si hay un ganador, o en caso de empate devuelve "Empate"
    """
    if jugador == maquina:
        return "Empate"
    if (jugador, maquina) in [(1, 2), (2, 3), (3, 1)]:
        return "Maquina"
    else:
        return "Jugador" 

def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """Determina si la partida sigue en curso o ya ha finalizado.

    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
        aciertos_maquina (int): Cantidad de rondas ganadas por la maquina
        ronda_actual (int): Número de la ronda actual.

    Returns:
        bool: 
            True → Si la partida sigue en curso.
            False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).
    """

    if ronda_actual < 2: #Si hubo menos de 3 rondas va a seguir la partida
        return True
    else: #Si hubo mas de 3 rondas, se verifican las puntuaciones
        if aciertos_jugador == 2 or aciertos_maquina == 2:
            return False
        
    return True
def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """Determina quién ganó la partida comparando los aciertos finales.

    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
        aciertos_maquina (int): Cantidad de rondas ganadas por la maquina.

    Returns:
        str: 
            "Jugador" → Si el jugador tiene más aciertos.
            "Máquina" → Si la máquina tiene más acierto
    """
    if aciertos_jugador == 2:
        return "Jugador"
    else:
        return "Maquina"

def mostrar_elemento(eleccion: int) -> str:
    """Convierte la elección numérica en un texto legible.

    Args:
        eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).

    Returns:
        str: 
            "Piedra" cuando su elección == 1.
            "Papel" cuando su elección == 2.
            "Tijera" cuando su  elección == 3.
    """
    match eleccion:
        case 1:
            return("Escogio Piedra")
        case 2:
            return("Escogio Papel")
        case 3:
            return("Escogio Tijera")
        

def jugar_piedra_papel_tijera() -> str:
    """Gestiona toda la lógica del juego, usando las funciones anteriores.

        Inicia una partida donde el jugador compite contra la máquina.
        En cada ronda, el jugador elige una opción y la máquina genera una 
        elección aleatoria.
        Se determina el ganador de la ronda.
        Se verifica si la partida continúa o si alguien ha ganado.
        Al finalizar, la función devuelve quién ganó la partida 
        ("Jugador" o "Máquina").

    Returns:
        str: devuelve quién ganó la partida ("Jugador" o "Máquina").
    """
    # Inicializacion de variables necesarias para mostrar el resultado al final del juego
    aciertos_jugador = 0
    aciertos_maquina = 0
    contador_empates = 0
    ronda_actual = 0

    # si aun no hay ningun jugador con 2 aciertos, el juego continuara
    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual): 
        # mostrar por pantalla las opciones a escoger y mostrar la eleccion de cada jugador
        ronda_actual += 1
        opcion_jugador = seleccionar_opcion()
        opcion_maquina = random.randint(1,3)
        print(f"El jugador: {opcion_jugador}")
        print(f"La maquina: {opcion_maquina}\n")

        ganador_de_ronda = verificar_ganador_ronda(opcion_jugador, opcion_maquina)
        mostrar_resultado_ronda(ganador_de_ronda)
        if ganador_de_ronda == "Jugador":
            aciertos_jugador += 1
        elif ganador_de_ronda == "Maquina":
            aciertos_maquina += 1
        else:
            contador_empates += 1
    #Se muestra la puntuacion y se devuelve el ganador del juego
    mostrar_puntuacion(aciertos_jugador, aciertos_maquina, contador_empates, ronda_actual)
    return verificar_ganador_partida(aciertos_jugador, aciertos_maquina)

def seleccionar_opcion() -> int:
    """Menu de opciones para seleccionar piedra, papel o tijeras

    Returns:
        int: devuelve la ipcion seleccionada
    """
    print("1- piedra")
    print("2- papel")
    print("3- tijera")
    opcion = ingresos.get_int("Intrese opcion: ", "Error, reingrese 1, 2 o 3: ", 1, 3)
    return opcion

def mostrar_puntuacion(aciertos_jugador: int, aciertos_maquina: int, empates: int, rondas: int) :
    """ Muestra en patalla un mesaje mostrando los puntajes

    Args:
        aciertos_jugador (int): puntos que tuvo el jugador
        aciertos_maquina (int): puntos que tuvo la maquina
        empates (int): empates de la partida
    """
    print("\n\n\n\n---------PUNTAJE--------")
    print(f"\nSe jugaron {rondas} rondas")
    print(f"El jugador tuvo {aciertos_jugador} aciertos")
    print(f"La maquina tuvo {aciertos_maquina} aciertos")
    print(f"Hubo {empates} empates")

def mostrar_resultado_ronda(resultado: str):
    """Muestra el resultado de la ronda

    Args:
        resultado (str): Resultado de la ronda: Jugador, Maquina o Empate
    """
    if resultado == "Jugador" or resultado == "Maquina":
        print(f"El ganador de la ronda es: {resultado}")
    else:
        print("La ronda termino en empate")

print(f"El ganador es: {jugar_piedra_papel_tijera()}")


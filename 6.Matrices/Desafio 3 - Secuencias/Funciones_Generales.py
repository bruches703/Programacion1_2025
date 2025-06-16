import os
def limpiar_pantalla():
    """Limpia la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')

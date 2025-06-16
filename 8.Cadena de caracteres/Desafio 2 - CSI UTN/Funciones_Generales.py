import os
def limpiar_pantalla():
    """Limpia la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def calcular_porcentaje(valor_total: int | float, valor_parcial: int | float) -> float:
    """calcula el porcentaje del valor total

    Args:
        valor_total (int | float): valor del 100%
        valor_parcial (int | float): valor a calcular el porcentaje

    Returns:
        float: porcentaje del valor parcial
    """
    porcentaje = valor_parcial * 100 / valor_total

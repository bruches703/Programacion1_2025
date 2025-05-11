#1.Definicion y desarrollo
#Definicion
def sumar(numero_uno:int,numero_dos:int) -> int:
    """Se encarga de sumar dos numeros enteros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la suma
    """
    #Desarrollo (Proceso)
    resultado = numero_uno + numero_dos
    #Retorno (Salida)
    return resultado

def calcular_precio_con_iva(precio_sin_iva:float, porcentaje_iva:float = 21) -> float:
    """Se encarga de calcular el precio con iva

    Args:
        precio_sin_iva (float): El precio sin iva
        porcentaje_iva (float): El porcentaje con iva

    Returns:
        float: El precio con iva incluido
    """
    monto_con_iva = precio_sin_iva * porcentaje_iva / 100
    precio_final_con_iva = precio_sin_iva + monto_con_iva
    
    return precio_final_con_iva

#2.Invocación o llamada
numero_a = int(input("Ingrese el numero uno: "))
numero_b = int(input("Ingrese el numero dos: "))
#Parametros por posición
resultado_suma = sumar(numero_a,numero_b)
#Parametros por nombre
#resultado_suma = sumar(numero_dos=numero_b,numero_uno=numero_a)
print(resultado_suma)

# precio = float(input("Ingrese precio: ($)"))
# #precio_con_iva = calcular_precio_con_iva(precio,21)
# #precio_con_iva = calcular_precio_con_iva(precio)
# precio_con_iva = calcular_precio_con_iva(precio,10.5)

# print(f"El precio con iva es $ {precio_con_iva}")
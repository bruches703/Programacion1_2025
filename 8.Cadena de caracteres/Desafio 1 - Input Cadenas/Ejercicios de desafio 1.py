def es_caracter_de_tipo(caracter: str, ascii_inicio: int, ascii_final: int) -> bool:
    """Verifica si un caracter pertenece a un rango de ascii

    Args:
        caracter (str): Caracter a verificar
        ascii_inicio (int): Ascii inicial del rango
        ascii_final (int): Ascii final del rango

    Returns:
        bool: True si pertenece al rango, False si no lo pertenece
    """
    return ord(caracter) >= ascii_inicio and ord(caracter) <= ascii_final

# Ejercicio 1
# Verificacion de Cadena Alfabetica
def es_alfabetica(cadena: str) -> bool:
    """Verifica si una cadena es alfabetica

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es alfabetica, False si no lo es
    """
    for caracter in cadena:
        codigo = ord(caracter)
        if not es_caracter_de_tipo(caracter, 65, 90) and not es_caracter_de_tipo(caracter, 97, 122):
            return False
    return True

# Ejercicio 2
# Validacion de numero entero
def es_numero_entero(cadena: str) -> bool:
    """Verifica si una cadena es un numero entero
    positivo o negativo

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es un numero entero, False si no lo es
    """
    es_negativo = False
    if len(cadena) == 0:
        return False
    
    if cadena[0] == '-':
        if len(cadena) == 1:
            return False
        inicio = 1
    else:
        inicio = 0 
    for i in range(inicio, len(cadena)):
        codigo = ord(cadena[i])
        if not es_caracter_de_tipo(cadena[i], 48, 57):  # Solo dígitos '0' a '9'
            return False
    return True

# Ejercicio 3
# Validacion numero decimal
def es_numero_decimal(cadena: str) -> bool:
    """Verifica si una cadena es un numero decimal

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es un numero decimal, False si no lo es
    """
    if len(cadena) == 0:
        return False

    i = 0
    punto_encontrado = False


    if cadena[0] == '-':
        if len(cadena) == 1:
            return False
    i = 1

    for j in range(i, len(cadena)):
        caracter = cadena[j]
        if caracter == '.':
            if punto_encontrado:
                return False 
            punto_encontrado = True
            if j == i or j == len(cadena) - 1:
                return False
        elif not es_caracter_de_tipo(caracter, 48, 57):
            return False

    if len(cadena) == i or (punto_encontrado and len(cadena) == i + 1):
        return False

    return True

# Ejercicio 4
# Validación de Clave Segura
def encontrar_mayuscula(cadena: str) -> bool:
    """Verifica si una cadena contiene al menos una mayuscula

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si contiene al menos una mayuscula, False si no lo es
    """
    for caracter in cadena:
        if es_caracter_de_tipo(caracter, 65, 90):
            return True
    return False

def encontrar_minuscula(cadena: str) -> bool:
    """Verifica si una cadena contiene al menos una minuscula

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si contiene al menos una minuscula, False si no lo es
    """
    for caracter in cadena:
        if es_caracter_de_tipo(caracter, 97, 122):
            return True
    return False

def encontrar_numero(cadena: str) -> bool:
    """Verifica si una cadena contiene al menos un numero

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si contiene al menos un numero, False si no lo es
    """
    for caracter in cadena:
        if es_caracter_de_tipo(caracter, 48, 57):
            return True
    return False

def contar_caracteres(cadena: str) -> int:
    """Cuenta los caracteres de la cadena

    Args:
        cadena (str): la cadena que debe contarse los caracteres

    Returns:
        int: devuelve en valor en entero de la cantidad de
        caracteres de la cadena
    """
    contador = 0
    for i in range(cadena):
        contador += 1
    return contador

def validar_clave_segura(cadena: str) -> bool:
    """Verifica si una cadena es una clave segura

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es una clave segura, False si no lo es
    """
    
    return contar_caracteres(cadena) >= 8 and encontrar_mayuscula(cadena) and encontrar_minuscula(cadena) and encontrar_numero(cadena)

# Ejercicio 5
# Verificación de Palíndromo

def es_palindromo(cadena: str) -> bool:
    """Verifica si una cadena es palindromo

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es palindromo, False si no lo es
    """
    cadena_minuscula = convertir_en_minuscula(cadena)
    indice_decendiente = len(cadena_minuscula) - 1
    for letra in cadena_minuscula:
        if letra != cadena_minuscula[indice_decendiente]:
            return False
        indice_decendiente -= 1
    return True

def convertir_en_minuscula(cadena: str) -> str:
    """Convierte una cadena a minuscula

    Args:
        cadena (str): Cadena a convertir

    Returns:
        str: Cadena en minuscula
    """
    auxiliar = ''
    for caracter in cadena:
        if es_caracter_de_tipo(caracter, 65, 90):
            codigo_ascii = ord(caracter) + 32
            auxiliar += chr(codigo_ascii)
        else:
            auxiliar += caracter
    return auxiliar

# Ejercicio 6
# Verificación de correo electronico

def hay_caracter(cadena: str, caracter: int) -> bool:
    """Verifica si una cadena contiene al menos un arroba

    Args:
        cadena (str): Cadena a verificar
        caracter (int): codigo ascii del caracter a buscar

    Returns:
        bool: True si contiene al menos un arroba, False si no lo es
    """
    
    for i in cadena:
        if i == caracter:
            return True
    return False
def buscar_indice_caracter(cadena: str, caracter: int) -> int:
    """Busca el indice del caracter

    Args:
        cadena (str): Cadena a verificar
        caracter (int): codigo ascii del caracter a buscar

    Returns:
        int: devuelve el indice del caracter
    """
    for i in range(len(cadena)):
        if ord(cadena[i]) == caracter:
            return i
    return -1
def validar_punto_de_correo(cadena: str, indice_arroba: int, valor_ascii: int) -> bool:
    """Verifica si una cadena es un correo electronico

    Args:
        cadena (str): Cadena a verificar
        indice_arroba (int): Indice del arroba
        valor_ascii (int): Valor ascii del caracter

    Returns:
        bool: True si es un correo electronico, False si no lo es
    """
    for i in range(indice_arroba + 1, indice_arroba + 2):
        if ord(cadena[i]) == valor_ascii:
            return False
    return True
def validar_correo_electronico(cadena: str) -> bool:
    """Verifica si una cadena es un correo electronico

    Args:
        cadena (str): Cadena a verificar

    Returns:
        bool: True si es un correo electronico, False si no lo es
    """
    indice_arroba = buscar_indice_caracter(cadena, '@')

    if contar_caracter_en_cadena(cadena, '@') != 1 or (indice_arroba < 1 or indice_arroba == len(cadena) - 1):
        return False
    else:
        if not validar_punto_de_correo(cadena, indice_arroba, 64):
            return False
    return True

# Ejercicio 7
# Contador de Vocales y Consonantes

def contar_vocales_y_consonantes(cadena: str) -> None:
    """Cuenta la cantidad de vocales y consonantes de una cadena
    y lo muestra por pantalla

    Args:
        cadena (str): Cadena a contar vocales y consonantes

    Returns:
        tuple: Tupla con la cantidad de vocales y consonantes
    """
    vocales = 0
    consonantes = 0
    for caracter in cadena:
        if es_caracter_de_tipo(caracter, 65, 90) or es_caracter_de_tipo(caracter, 97, 122):
            if es_vocal(caracter):
                vocales += 1
            else:
                consonantes += 1
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")
    
def es_vocal(caracter: str) -> bool:
    """Verifica si un caracter es una vocal

    Args:
        caracter (str): Caracter a verificar

    Returns:
        bool: True si es una vocal, False si no lo es
    """
    es_minuscula = ord(caracter) == 97 or ord(caracter) == 101 or ord(caracter) == 105 or ord(caracter) == 111 or ord(caracter) == 117
    es_mayuscula = ord(caracter) == 65 or ord(caracter) == 69 or ord(caracter) == 73 or ord(caracter) == 79 or ord(caracter) == 85
    return es_minuscula or es_mayuscula

# Ejercicio 8
# Validación de Número de Teléfono
def validar_numero_de_telefono(cadena: str, codigo_pais: str) -> bool:
    """Verifica si una cadena es un numero de telefono

    Args:
        cadena (str): Cadena a verificar
        codigo_pais (str): Codigo del pais

    Returns:
        bool: True si es un numero de telefono, False si no lo es
    """
    # Comienza con 0 si esta en el codigo del pais
    cadena_completa = codigo_pais + cadena
    if len(cadena) + len(codigo_pais) != 10:
        return False
    for cadena in cadena_completa:
        if not es_caracter_de_tipo(cadena, 48, 57):
            return False        
    return True
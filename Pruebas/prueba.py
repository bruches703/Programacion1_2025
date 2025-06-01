# array = [ [1001, ["choclo", "mail", "pororo"], "Nombre"] , [1002, ["nada"], "Apellido"]]

# # print(array)
# # print(array[0][0])
# # print(array[0][1])
# # print(array[0][2])
# # print(array[len(array) -1 ][0])

# if len(array[1][2]) < 20:
#     for i in range(len(array[1][2]), 20, 1):
#         array[1][2] = array[1][2] + "-"

# print(array[1][2])

# cuadrado = [
#     [8, 1, 6],
#     [3, 5, 7],
#     [4, 9, 2]
# ]
# suma1 = 0
# suma2 = 0
# for i in range(len(cuadrado)):
#     suma1 += cuadrado[0][i]
#     suma2 += cuadrado[i][0]
# print (suma1)
# print (suma2)

# n = len(cuadrado)
# array = [1, 2, 3, 4]
# print(array)
# elemento = "Hola"
# array = []
# array += [elemento]
# print(array[0])

# cadenaA = 'hola mundo'
# cadenaB = 'HOLA MUNDO'
# print(f"ID: {cadenaA[0:6]}")
# print(f"ID: {id(cadenaB)}")

# caracter = 'A'
# codigo_ascii = ord(caracter)
# print(codigo_ascii)  # Imprime 65



def copiar_vector(lista: list) -> list:
    """Copia un vector y devuelve una copia

    Args:
        lista (list): lista a copiar

    Returns:
        list: copia del vector
    """
    if len(lista) == 0:
        return []
    else:
        copia = []
        for i in range(len(lista)):
            copia += [lista[i]]
        return copia
    
a = [[1,2,3,],[4,5,6],[7,8,9]]
b = []
b = copiar_vector(a)
print(b)
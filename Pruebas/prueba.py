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
diccionario = [
    {
        "Tema": "Ariana Grande | The Weeknd - Starlight",
        "Vistas": "15 millones",
        "Duracion": "3:50",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2024c",
        "Fecha lanzamiento": "2024-11-01"
    },
    {
        "Tema": "Dua Lipa | Sia - Electric Love",
        "Vistas": "20 millones",
        "Duracion": "3:30",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2025a",
        "Fecha lanzamiento": "2025-02-14"
    },
    {
        "Tema": "The Weeknd | Ariana Grande - Midnight Sky",
        "Vistas": "30 millones",
        "Duracion": "4:00",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2025b",
        "Fecha lanzamiento": "2025-06-10"
    }
]

primer_elemento = diccionario[0]

print(primer_elemento["Vistas"])
# indice_guion = primer_elemento["Tema"].find("-")
# subcadena = primer_elemento["Tema"][:indice_guion]

# flag = True
# colaboradores = ""
# for i in range(len(primer_elemento["Tema"])):
#     if primer_elemento["Tema"][i] == "-":
#         break
#     else:
#         colaboradores += primer_elemento["Tema"][i]
    
# colaborador = ""
# lista_colaboradores = []
# i = 0
# while i < len(colaboradores):
#     if colaboradores[i] == "|" or i == len(colaboradores)-1:
#         lista_colaboradores += [colaborador]    
#         colaborador = ""
#         i += 2
#     else:
#         colaborador += colaboradores[i]
#         i += 1
# indice_pippe = subcadena.find('|')
# if indice_pippe > 0:
#     print(subcadena[:indice_pippe])  # Imprime desde el inicio hasta antes de '|'
# elif indice_pippe == 0:
#     print("El carácter '|' está al principio, no hay nada antes.")
# else:
#     print("No se encontró '|'")

if primer_elemento["Vistas"].isnumeric():
    print("Es un numero")
else:
    print("No es un numero")
    
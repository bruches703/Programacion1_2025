# cadena = "'Hola Mundo'"
# print(cadena)

# cadena = '"Hola Mundo"'
# print(cadena)

#1.Secuencias de escape

# cadena = "'Hola' "Mundo""#ERROR
# cadena = "'Hola' \"Mundo\""
# print(cadena)

#cadena = "Hola\nMundo"
#cadena = "Hola\tMundo"
# cadena = "Hola Mundo\a"
# print(cadena)

#2.Operaciones básicas

#a.Indexación --> La forma en la que yo puedo acceder a cada uno de los caracteres de mi cadena

# cadena = "Mariano"
# cantidad_caracteres = len(cadena)
# print(f"La cantidad de caracteres es: {cantidad_caracteres}")
# print(cadena[0])#M
# print(cadena[1])#a
# # print(cadena[-1])#o --> Solo en python
# print(cadena[cantidad_caracteres - 1])

#b.Slicing (dividir la cadena en partes más pequeñas)

# cadena = "Mariano"

# print(cadena[inicio,fin])
#incio --> Incluyente
#fin --> Excluyente
# print(cadena[0:3]) #Muestra los caracteres del indice 0|1|2
# print(cadena[2:8]) #Muestra los caracteres del indice 2|3|4|5|6
# print(cadena[2:]) #Muestra los caracteres del indice 2|3|4|5|6

# cadena_dos = cadena[0:3]
# print(cadena_dos)

#c.Longitud 

cadena = "Mariano"
cantidad_caracteres = len(cadena)
print(f"La cantidad de caracteres es: {cantidad_caracteres}")

#d.Concatenación --> Unir una cadena con otra

#Una vez definida una cadena no se puede modificar, pero si sustituir entonces la concatenación me va a servir mucho a la hora de hacer cambios en cadenas de caracteres.

#Una cadena no puede ser modificada una vez creada, lo que ocurre es que se asigna una cadena nueva con la información de la anterior y agregandola la nueva información

# +
# cadena = "Hola"
# print("ANTES")
# print(f"id cadena: {id(cadena)}")
# print(cadena)
# cadena += "Mundo"
# print("DESPUES")
# print(f"id cadena: {id(cadena)}")
# print(cadena)

#f-string
# cadena = "Hola"
# #cadena = f"{cadena}Mundo"
# cadena = f"Mundo{cadena}"
# print(cadena)

#format()
# cadena = "Hola"
# cadena = "{0}Mundo".format(cadena)
# print(cadena)

# % mascara

# numero = 58
# PI = 3.14

# cadena = "El numero es: %x" %numero
# cadena = "El numero es: %d" %PI
# print(cadena)

#e. Repetición --> SOLO PYTHON

# cadena = "Hola"
# #print(cadena * 10)
# cadena_dos = cadena * 10
# print(cadena_dos)

#f.Operadores Relacionales 

#==
# print("Mariano" == "Mariano")#True
# print("Mariano" == "Mariana")#False
# print("Mariano" == "mariano")#False

#!=
# print("Mariano" != "Mariano")#False
# print("Mariano" != "Mariana")#True
# print("Mariano" != "mariano")#True

# >
# print("Mariano" > "JoseJoseJose") #True
# print("Mariano" > "Mariana") #True
# print("Mariano" > "mariano") #False
# print("a" > "Z") #True

# <
# print("Mariano" < "JoseJoseJose") #False
# print("Mariano" < "Mariana") #False
# print("Mariano" < "mariano") #True
# print("a" < "Z") #False

# print("~" > "z")

#3. Recorrer cadena --> Una cadena al ser un tipo de objeto iterable como una lista se puede recorrer con un for

# cadena = "Mariano"

# for i in range(len(cadena)):
#     print(cadena[i])

#a) Mostrar la cadena sin la letra 'a"
# for i in range(len(cadena)):
#     if cadena[i] != 'a':
#         print(cadena[i],end="")

# print("")
# cadena = "Mariano"

#b) Contar la cantidad de "a" que hay

# contador = 0

# for i in range(len(cadena)):
#     if cadena[i] == 'a':
#         contador += 1
    
# print(f"En la cadena hay {contador} de letras 'a'")

#4. Modificar cadenas
#Las cadenas no se pueden modificar una vez creadas
#Pero si puedo reasignar en otra cadena la modificación que me piden (concatenando)

cadena = "Mariano"
# cadena[0] = "A" #ERROR

# #a) Reemplazar todas letra "a" por una "z"

# def reemplazar_cadena(cadena_original:str,caracter_a_reemplazar:str,reemplazo:str) -> str:
#     cadena_aux = ""
#     for i in range(len(cadena_original)):
#         if cadena_original[i] == caracter_a_reemplazar:
#             # cadena[i] = "z" #NO FUNCIONA
#             cadena_aux += reemplazo
#         else:
#             cadena_aux += cadena_original[i]
#     return cadena_aux

# print(f"cadena:{cadena} - id:{id(cadena)}")
# cadena = reemplazar_cadena(cadena,"a","z")
# print(f"cadena:{cadena} - id:{id(cadena)}")

#b) Reemplazar caracter

cadena = "Hola"
#Aola
#cadena[0] = "A"#ERROR

def reemplazar_caracter(cadena_original:str,indice:int,reemplazo:str) -> str:
    cadena_aux = ""
    
    for i in range(len(cadena_original)):
        if indice == i:
            cadena_aux += reemplazo
        else:
            cadena_aux += cadena_original[i]
            
    return cadena_aux

print(cadena)
cadena = reemplazar_caracter(cadena,0,"A")
print(cadena)
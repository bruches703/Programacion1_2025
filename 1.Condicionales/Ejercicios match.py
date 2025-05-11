# Ejercicios match
# 
# 
# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche

estacion = input("Ingrese la estacion del año: ")
destino = input("Ingrese el destino del viaje: ")

match estacion:
    case "invierno":
        if destino == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")

    case "verano":
        if destino == "mar del plata" or destino == "Cataratas":
            print("Se viaja")
        else:
            print("No se viaja")

    case "otoño":
        print ("Se viaja")

    case "primavera":
        if destino!="bariloche":
            print("Se viaja")
        else:
            print("No se viaja")

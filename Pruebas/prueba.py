#  Biblioteca de funciones y validaciones

def validar_rango_numerico(numeroAValidar, valorA, valorB, mensajeReingreso):
    # Valida numeroAValidar en un rango de valorA a valorB
    # valorA: define la base minima del numero
    # valorB: define la base maxima del numero
    # mensajeReingreso: define el mensaje que se mostrara en pantalla
    # retorna el valor entero validado

    while numeroAValidar < valorA and numeroAValidar > valorB:
        print(f"Error, {numeroAValidar} esta fuera de rango")
        numeroAValidar = int(input(mensajeReingreso))
    return numeroAValidar

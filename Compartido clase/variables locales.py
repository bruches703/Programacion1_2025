def saludar():
    global nombre
    nombre = "Juan"
    print(f"Dentro de la funcion: {nombre}")
    #nombre = "Juan"
    
nombre = input("Ingrese su nombre: ")
saludar()
print(f"Fuera de la funcion: {nombre}")

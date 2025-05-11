def prueba(numero:int,lista:list):
    numero = 30
    lista.clear()
    print("DENTRO DE LA FUNCION")
    print(f"variable numero {numero}")
    print(f"variable lista {lista}")
    
#Cuandot tengan una variable Sea lista-diccionario-set

lista = [1,3,5] #MUTABLE
numero = 20 #INMUTABLE
prueba(numero,lista)
print("DENTRO DEL MAIN")
print(f"variable numero {numero}")
print(f"variable lista {lista}")

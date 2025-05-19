import vectores
import matrices 
import Manejo_listas_desafio

lista_choferes = vectores.new_Array(15)
matriz_coches = matrices.crear_matriz(3, 6)
matriz_recaudacion = matrices.crear_matriz(3, 6)

for i in range(len(matriz_recaudacion)):
   matriz_recaudacion[i] = vectores.new_Array(4)

aux = Manejo_listas_desafio.generar_id_coches(matriz_coches)
# aux = Manejo_listas_desafio.generar_id_coches(matriz_recaudacion)
# print(lista_choferes)
print(matriz_coches)
print(" ")
print(matriz_coches[0])
print(matriz_coches[1])
print(matriz_coches[2])
print(" ")
print(matriz_recaudacion)

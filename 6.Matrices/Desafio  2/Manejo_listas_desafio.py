def generar_id_coches(matriz: list) -> None:
    """Genera id a cada linea de colectivo
            codigos id: 
                1000 -> representa a la primera linea de colectivo
                2000 -> representa a la segunda linea de colectivo
                3000 -> representa a la ultima linea de colectivo
        
        matriz (list): Matriz con carga 0 a modificar
    """
    matriz[0] = 1001
    matriz[1]= 2001
    matriz[2] = 3001

    return None
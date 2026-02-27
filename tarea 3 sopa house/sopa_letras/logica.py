import random
import string

def crear_matriz(dimension=20):
    return [[" " for _ in range(dimension)] for _ in range(dimension)]

def insertar_palabra(matriz, palabra):
    """
    Intenta colocar una palabra y devuelve la lista de coordenadas (fila, col) ocupadas.
    """
    dimension = len(matriz)
    palabra = palabra.upper()
    intentos = 0
    
    while intentos < 100:
        orientacion = random.choice(['H', 'V'])
        f = random.randint(0, dimension - 1)
        c = random.randint(0, dimension - 1)
        
        # Coordenadas que ocuparía la palabra
        coords = []
        if orientacion == 'H' and c + len(palabra) <= dimension:
            coords = [(f, c + i) for i in range(len(palabra))]
        elif orientacion == 'V' and f + len(palabra) <= dimension:
            coords = [(f + i, c) for i in range(len(palabra))]
        
        if coords and all(matriz[r][col] == " " for r, col in coords):
            for i, (r, col) in enumerate(coords):
                matriz[r][col] = palabra[i]
            return coords # Retornamos las posiciones exactas
        intentos += 1
    return None

def rellenar_aleatorio(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] == " ":
                matriz[f][c] = random.choice(string.ascii_uppercase)
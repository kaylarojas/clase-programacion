from sopa_letras.logica import crear_matriz, insertar_palabra, rellenar_aleatorio
from sopa_letras.visualizador import mostrar_matriz

def menu():
    palabras_ingresadas = []
    print("--- Generador Pro de Sopas de Letras ---")
    
    while len(palabras_ingresadas) < 15:
        p = input(f"Palabra {len(palabras_ingresadas)+1} (o 'FIN'): ").strip().upper()
        if p == 'FIN': break
        if p: palabras_ingresadas.append(p)
    
    matriz = crear_matriz(20)
    palabras_ubicadas = {} # Guardará { 'LUPUS': [(0,0), (0,1)...] }

    for p in palabras_ingresadas:
        coords = insertar_palabra(matriz, p)
        if coords:
            palabras_ubicadas[p] = coords

    # Mostrar sopa con relleno
    import copy
    sopa_final = copy.deepcopy(matriz)
    rellenar_aleatorio(sopa_final)
    
    mostrar_matriz(sopa_final)
    
    input("\nPresiona ENTER para ver la solución...")
    mostrar_matriz(sopa_final, mapa_palabras=palabras_ubicadas, resolver=True)

if __name__ == "__main__":
    menu()
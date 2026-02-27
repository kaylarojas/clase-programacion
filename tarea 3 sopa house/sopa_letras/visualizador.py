def mostrar_matriz(matriz, mapa_palabras=None, resolver=False):
    """
    mapa_palabras: Diccionario donde la clave es la palabra y el valor son sus coordenadas.
    """
    # Lista de colores ANSI (Verde, Azul, Amarillo, Magenta, Cian, Rojo)
    COLORES = ["\033[32m", "\033[34m", "\033[33m", "\033[35m", "\033[36m", "\033[31m"]
    RESET = "\033[0m"

    print("\n" + "="*45)
    print("      SOPA DE LETRAS - DR. HOUSE")
    print("="*45 + "\n")

    # Crear un mapa inverso: (fila, col) -> Color
    colores_coords = {}
    if resolver and mapa_palabras:
        for i, (palabra, coords) in enumerate(mapa_palabras.items()):
            color_elegido = COLORES[i % len(COLORES)]
            for pos in coords:
                colores_coords[pos] = color_elegido

    for f in range(len(matriz)):
        linea = ""
        for c in range(len(matriz[f])):
            letra = matriz[f][c]
            if (f, c) in colores_coords:
                linea += f"{colores_coords[(f,c)]}{letra}{RESET} "
            else:
                linea += f"{letra} "
        print(linea)
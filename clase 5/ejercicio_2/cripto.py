# cripto.py

def procesar_cesar(texto, desplazamiento, modo):
   
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    
    if modo == "desencriptar":
        desplazamiento = -desplazamiento
        
    for letra in texto.lower():
        if letra in alfabeto:
            posicion_actual = alfabeto.find(letra)
            
            nueva_posicion = (posicion_actual + desplazamiento) % 26
            resultado += alfabeto[nueva_posicion]
        else:
            resultado += letra
            
    return resultado
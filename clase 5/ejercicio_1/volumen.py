# volumen.py
import math

def volumen_cubo(lado):
    return lado ** 3

def volumen_paralelepipedo(largo, ancho, alto):
    return largo * ancho * alto

def volumen_cilindro(radio, altura):
    return math.pi * (radio ** 2) * altura

def volumen_esfera(radio):
    return (4/3) * math.pi * (radio ** 3)

def volumen_cono(radio, altura):
    return (1/3) * math.pi * (radio ** 2) * altura
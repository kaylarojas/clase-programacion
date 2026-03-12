import math
from abc import ABC, abstractmethod

# REQUISITO 1: Clase abstracta Figura
class Figura(ABC):
    @abstractmethod
    def volumen(self):
        """Método abstracto que deben implementar las hijas"""
        pass

# REQUISITO 2: Clases que heredan de Figura
class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado
    def volumen(self):
        return self.lado ** 3

class Paralelepipedo(Figura):
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    def volumen(self):
        return self.largo * self.ancho * self.alto

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura

class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio
    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

class Cono(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def volumen(self):
        return (1/3) * math.pi * (self.radio ** 2) * self.altura
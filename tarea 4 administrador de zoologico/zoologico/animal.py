class Animal:
    """
    Clase base para todos los animales del zoológico.
    
    Atributos:
        especie (str): La especie biológica.
        edad (int): Edad en años.
    """
    def __init__(self, especie, edad):
        self._especie = especie
        self._edad = edad

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, valor):
        self._especie = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

    def __str__(self):
        return f"Especie: {self._especie} | Edad: {self._edad} años"
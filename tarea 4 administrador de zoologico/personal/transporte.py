class Transporte:
    """
    Clase base para los medios de transporte utilizados en el zoológico.
    """
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    def __str__(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"

# Clases hijas (Requerimiento 4.a)
class Bicicleta(Transporte):
    def __str__(self):
        return f"Bicicleta - {super().__str__()}"

class Cuadraciclo(Transporte):
    def __str__(self):
        return f"Cuadraciclo - {super().__str__()}"

class Patineta(Transporte):
    def __str__(self):
        return f"Patineta - {super().__str__()}"
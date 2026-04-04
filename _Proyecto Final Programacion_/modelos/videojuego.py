class VideoJuego:
    """Clase base con encapsulamiento y validación de datos."""
    def __init__(self, identificador, nombre, categoria, precio, esrb, stock, consola):
        self._identificador = identificador
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._esrb = esrb
        self._stock = stock
        self._consola = consola

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._stock = nueva_cantidad

    @property
    def consola(self):
        return self._consola

    def obtener_detalles(self):
        # Uso de concatenación para evitar f-strings (regla de aprendizaje)
        return "ID: " + str(self._identificador) + " | " + self._nombre + " (" + self._consola + ") - $" + str(self._precio)

class JuegoPS5(VideoJuego):
    def __init__(self, id, nom, cat, pre, esrb, st):
        super().__init__(id, nom, cat, pre, esrb, st, "PS5")

class JuegoXbox(VideoJuego):
    def __init__(self, id, nom, cat, pre, esrb, st):
        super().__init__(id, nom, cat, pre, esrb, st, "Xbox")

class JuegoNintendo(VideoJuego):
    def __init__(self, id, nom, cat, pre, esrb, st):
        super().__init__(id, nom, cat, pre, esrb, st, "Nintendo Switch")
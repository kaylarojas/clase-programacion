# modelos/videojuego.py

class VideoJuego:
    """Clase padre con toda la lógica compartida."""
    
    def __init__(self, identificador, nombre, categoria, precio, esrb, stock, consola):
        self._identificador = identificador
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._esrb = esrb
        self._stock = stock
        self._consola = consola

    # --- Propiedades (Getters y Setters) ---
    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def esrb(self):
        return self._esrb

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
        """Devuelve la información completa del juego para el catálogo."""
        detalles = "ID: " + str(self._identificador)
        detalles = detalles + " | " + self._nombre
        detalles = detalles + " [" + self._consola + "]"
        detalles = detalles + " | Cat: " + self._categoria
        detalles = detalles + " | Clasif: " + self._esrb
        detalles = detalles + " | Precio: $" + str(self._precio)
        return detalles


# --- Clases Hijas (Herencia) ---

class JuegoPS5(VideoJuego):
    def __init__(self, id, nom, cat, pre, esrb, st):
        # Llama al constructor del padre y pasa "PS5" como consola fija
        super().__init__(id, nom, cat, pre, esrb, st, "PS5")

class JuegoXbox(VideoJuego):
    def __init__(self, id, nom, cat, pre, esrb, st):
        super().__init__(id, nom, cat, pre, esrb, st, "Xbox")

class JuegoNintendo(VideoJuego):
    def __init__(self, id, nom, cat, pre, esrb, st):
        super().__init__(id, nom, cat, pre, esrb, st, "Nintendo Switch")
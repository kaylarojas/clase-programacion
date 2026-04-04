import datetime

class Carrito:
    def __init__(self):
        self._items = []
        self._total = 0.0

    def agregar(self, videojuego):
        if videojuego.stock > 0:
            self._items.append(videojuego)
            videojuego.stock = videojuego.stock - 1
            self._total = self._total + videojuego.precio
            print("Agregado: " + videojuego.nombre)
        else:
            print("Sin stock disponible.")

    def mostrar(self):
        if not self._items:
            print("Carrito vacío.")
        else:
            for i in range(len(self._items)):
                print(str(i) + ". " + self._items[i].obtener_detalles())
            print("Total: $" + str(self._total))

    def exportar_datos(self, cliente):
        lista_juegos = []
        for j in self._items:
            lista_juegos.append({"nombre": j.nombre, "precio": j.precio})
        
        return {
            "cliente": cliente,
            "fecha": str(datetime.date.today()),
            "videojuegos": lista_juegos,
            "total": self._total
        }

    @property
    def total(self):
        return self._total
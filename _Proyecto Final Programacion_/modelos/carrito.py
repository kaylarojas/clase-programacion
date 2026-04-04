
import datetime

class Carrito:
    def __init__(self):
        self._items = []
        self._total = 0.0

    def agregar(self, videojuego):
        """Agrega un videojuego al carrito y descuenta el stock."""
        if videojuego.stock > 0:
            self._items.append(videojuego)
            videojuego.stock = videojuego.stock - 1
            self._total = self._total + videojuego.precio
            print("Agregado: " + videojuego.nombre)
        else:
            print("Sin stock disponible.")

    def eliminar_videojuego(self, indice):
        """
        Elimina un juego del carrito según su índice.
        Este es el método que causaba el error.
        """
        try:
            # Quitamos el objeto de la lista
            juego_removido = self._items.pop(indice)
            # Devolvemos el stock al catálogo
            juego_removido.stock = juego_removido.stock + 1
            # Restamos del total
            self._total = self._total - juego_removido.precio
            print("Se eliminó '" + juego_removido.nombre + "' del carrito.")
        except IndexError:
            print("Error: El número de índice no existe en el carrito.")

    def mostrar(self):
        """Muestra los productos actuales."""
        if not self._items:
            print("El carrito está vacío.")
        else:
            for i in range(len(self._items)):
                # Usamos el índice 'i' para que el usuario sepa qué número marcar para eliminar
                print(str(i) + ". " + self._items[i].obtener_detalles())
            print("Total actual: $" + str(round(self._total, 2)))

    def exportar_datos(self, cliente):
        """Prepara los datos para la factura final."""
        lista_juegos = []
        for j in self._items:
            lista_juegos.append({"nombre": j.nombre, "precio": j.precio})
        
        return {
            "cliente": cliente,
            "fecha": str(datetime.date.today()),
            "videojuegos": lista_juegos,
            "total": round(self._total, 2)
        }

    @property
    def total(self):
        return self._total
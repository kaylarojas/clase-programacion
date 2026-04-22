
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
       
        try:
            # Quita el objeto de la lista
            juego_removido = self._items.pop(indice)
            # Devolve el stock al catálogo
            juego_removido.stock = juego_removido.stock + 1
            # Resta del total
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
        # Agrupamos por nombre para calcular cantidad
        agrupado = {}
        for j in self._items:
            if j.nombre in agrupado:
                agrupado[j.nombre]["cantidad"] += 1
            else:
                agrupado[j.nombre] = {
                    "nombre": j.nombre,
                    "precio_unitario": j.precio,
                    "cantidad": 1
                }
        
        lista_juegos = list(agrupado.values())
        
        return {
            "cliente": cliente,
            "fecha": str(datetime.date.today()),
            "videojuegos": lista_juegos,
            "total": round(self._total, 2)
        }

    @property # Permite leer el total acumulado del carrito desde afuera como si fuera un atributo normal (carrito.total), pero sin permitir modificarlo directamente.
    def total(self):
        return self._total
from modelos.videojuego import JuegoPS5, JuegoXbox, JuegoNintendo
from modelos.carrito import Carrito
import servicios.archivos as repo

def crear_objeto_juego(d):
    """Crea el objeto correcto según la consola (Polimorfismo)."""
    if d["consola"] == "PS5":
        return JuegoPS5(d["id"], d["nombre"], d["categoria"], d["precio"], d["esrb"], d["stock"])
    elif d["consola"] == "Xbox":
        return JuegoXbox(d["id"], d["nombre"], d["categoria"], d["precio"], d["esrb"], d["stock"])
    else:
        return JuegoNintendo(d["id"], d["nombre"], d["categoria"], d["precio"], d["esrb"], d["stock"])

def main():
    catalogo = []
    carrito = Carrito()
    
    # --- SELECCIÓN DE ARCHIVO INICIAL ---
    print("--- INICIO DE SISTEMA ---")
    print("1. Cargar catalogo.json")
    print("2. Cargar catalogo.csv")
    op = input("Seleccione fuente de datos: ")
    
    datos_crudos = []
    if op == "1":
        datos_crudos = repo.cargar_desde_json("catalogo.json")
    elif op == "2":
        datos_crudos = repo.cargar_desde_csv("catalogo.csv")
    
    for d in datos_crudos:
        catalogo.append(crear_objeto_juego(d))

    while True:
        print("\n1. Ver Catálogo | 2. Agregar Juego | 3. Comprar | 4. Carrito | 5. Facturar | 6. Salir")
        accion = input("Opción: ")

        if accion == "1":
            for j in catalogo:
                print(j.obtener_detalles() + " [Stock: " + str(j.stock) + "]")

        elif accion == "2":
            try:
                id_n = int(input("ID: "))
                # Validación ID repetido
                repetido = False
                for j in catalogo:
                    if j.identificador == id_n: repetido = True
                
                if repetido:
                    print("Error: ID ya existe."); continue

                nom = input("Nombre: ")
                pre = float(input("Precio: "))
                st = int(input("Stock: "))
                
                if pre < 0 or st < 0 or nom == "":
                    print("Error: Datos inválidos."); continue

                print("1. PS5 | 2. Xbox | 3. Nintendo")
                c = input("Consola: ")
                cons = "PS5" if c=="1" else "Xbox" if c=="2" else "Nintendo"
                
                nuevo = crear_objeto_juego({"id":id_n, "nombre":nom, "categoria":"General", "precio":pre, "esrb":"E", "stock":st, "consola":cons})
                catalogo.append(nuevo)
            except ValueError:
                print("Error: Use números para ID, precio y stock.")

        elif accion == "3":
            try:
                id_buscado = int(input("ID del juego: "))
                encontrado = None
                for j in catalogo:
                    if j.identificador == id_buscado: encontrado = j
                if encontrado:
                    carrito.agregar(encontrado)
                else:
                    print("No encontrado.")
            except ValueError:
                print("ID no válido.")

        elif accion == "4":
            carrito.mostrar()

        elif accion == "5":
            if carrito.total > 0:
                cli = input("Cliente: ")
                nom_a = input("Nombre del archivo: ")
                form = "json" if input("Formato (1.JSON / 2.CSV): ") == "1" else "csv"
                repo.guardar_factura_generica(nom_a, carrito.exportar_datos(cli), form)
                break
            else:
                print("Carrito vacío.")

        elif accion == "6":
            break

if __name__ == "__main__":
    main()
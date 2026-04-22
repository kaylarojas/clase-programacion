import os
from modelos.videojuego import JuegoPS5, JuegoXbox, JuegoNintendo
from modelos.carrito import Carrito
import servicios.archivos as repo

def crear_objeto_juego(datos):
    """
    Transforma un diccionario de datos en un objeto de clase específico.
    Esto permite usar Polimorfismo más adelante.
    """
    # Extraemos los datos del diccionario
    consola = datos.get("consola")
    id_j = datos.get("id")
    nom = datos.get("nombre")
    cat = datos.get("categoria", "General")
    pre = datos.get("precio")
    esrb = datos.get("esrb", "E")
    stk = datos.get("stock")

    # Creamos el objeto según la consola correspondiente
    if consola == "PS5":
        return JuegoPS5(id_j, nom, cat, pre, esrb, stk)
    elif consola == "Xbox":
        return JuegoXbox(id_j, nom, cat, pre, esrb, stk)
    else:
        # Por defecto, si no es PS5 o Xbox, es para Nintendo
        return JuegoNintendo(id_j, nom, cat, pre, esrb, stk)

def main():
    # --- CONFIGURACIÓN DE RUTAS ---
    # Buscamos la carpeta donde está este archivo para no tener problemas de rutas
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    archivo_json = os.path.join(ruta_base, "catalogo.json")
    archivo_csv = os.path.join(ruta_base, "catalogo.csv")

    # Listas donde guardaremos la información mientras el programa corre
    catalogo_objetos = []
    carrito_compras = Carrito()
    
    # Variables para recordar qué archivo estamos usando
    ruta_activa = ""
    formato_elegido = ""

    print("--- BIENVENIDO A LA GESTIÓN DE LA TIENDA ---")
    print("¿Desde dónde desea cargar los datos hoy?")
    print("1. Archivo JSON")
    print("2. Archivo CSV")
    print("3. Catálogo nuevo (vacío)")
    
    seleccion = input("Seleccione una opción: ")
    formato_elegido = seleccion
    
    # --- CARGA DE DATOS INICIAL ---
    datos_crudos = []
    if seleccion == "1":
        ruta_activa = archivo_json
        datos_crudos = repo.cargar_desde_json(ruta_activa)
    elif seleccion == "2":
        ruta_activa = archivo_csv
        datos_crudos = repo.cargar_desde_csv(ruta_activa)
    
    # Convertir los diccionarios leídos en objetos reales
    for item in datos_crudos:
        nuevo_juego = crear_objeto_juego(item)
        catalogo_objetos.append(nuevo_juego)

    sistema_encendido = True
    while sistema_encendido:
        print("\n" + "="*30)
        print("       MENÚ DE TIENDA")
        print("="*30)
        print("1. Ver Inventario")
        print("2. Registrar Juego Nuevo")
        print("3. Agregar al Carrito")
        print("4. Ver Carrito Actual")
        print("5. Quitar del Carrito")
        print("6. Pagar y Salir")
        print("7. Solo Salir")
        
        opcion = input("¿Qué desea hacer?: ")

        # 1. MOSTRAR CATÁLOGO
        if opcion == "1":
            print("\n--- LISTA DE PRODUCTOS DISPONIBLES ---")
            for juego in catalogo_objetos:
                # El método obtener_detalles() viene de la clase VideoJuego
                info = juego.obtener_detalles()
                print(f"{info} | En Stock: {juego.stock}")

        # 2. REGISTRAR JUEGO NUEVO
        elif opcion == "2":
            try:
                print("\n--- INGRESO DE NUEVO PRODUCTO ---")
                id_nuevo = int(input("ID único: "))
                
                existe = False
                for j in catalogo_objetos:
                    if j.identificador == id_nuevo:
                        existe = True
                
                if existe:
                    print("Error: Ese ID ya pertenece a otro juego.")
                    continue

                nombre = input("Nombre del juego: ")
                categoria = input("Género/Categoría: ")
                esrb = input("Clasificación (E, T, M): ")
                precio = float(input("Precio: "))
                stock = int(input("Cantidad inicial: "))

                if nombre.strip() == "":
                    print("Error: El nombre no puede estar vacío.")
                    continue
                if categoria.strip() == "":
                    print("Error: La categoría no puede estar vacía.")
                    continue
                if esrb.strip() == "":
                    print("Error: La clasificación no puede estar vacía.")
                    continue
                if precio <= 0:
                    print("Error: El precio no puede ser negativo.")
                    continue
                if stock <= 0:
                    print("Error: El stock no puede ser negativo.")
                    continue
                # --- FIN VALIDACIONES ---

                print("Consola: 1. PS5 | 2. Xbox | 3. Nintendo")
                cons_op = input("Opción: ")
                consola_nom = "PS5" if cons_op == "1" else "Xbox" if cons_op == "2" else "Nintendo Switch"
                
                # Creamos el diccionario y luego el objeto
                dicc_datos = {
                    "id": id_nuevo, "nombre": nombre, "categoria": categoria,
                    "precio": precio, "esrb": esrb, "stock": stock, "consola": consola_nom
                }
                
                objeto_nuevo = crear_objeto_juego(dicc_datos)
                catalogo_objetos.append(objeto_nuevo)
                
                # Guarda en el archivo automáticamente
                if ruta_activa != "":
                    repo.guardar_catalogo_completo(ruta_activa, catalogo_objetos, formato_elegido)
                
                print("¡Juego guardado exitosamente!")

            except ValueError:
                print("Error: Asegúrese de poner números en ID, Precio y Stock.")

        # 3. AGREGAR AL CARRITO
        elif opcion == "3":
            try:
                id_buscado = int(input("ID del juego que desea comprar: "))
                
                # Busca el objeto en lista
                juego_encontrado = None
                for j in catalogo_objetos:
                    if j.identificador == id_buscado:
                        juego_encontrado = j
                
                if juego_encontrado:
                    # El carrito se encarga de bajar el stock
                    carrito_compras.agregar(juego_encontrado)
                    
                    # Guarda el cambio de stock en el archivo
                    if ruta_activa != "":
                        repo.guardar_catalogo_completo(ruta_activa, catalogo_objetos, formato_elegido)
                else:
                    print("No se encontró ningún juego con ese ID.")
            except ValueError:
                print("Error: ID no válido.")

        # 4. VER CARRITO
        elif opcion == "4":
            print("\n--- TU CARRITO ACTUAL ---")
            carrito_compras.mostrar()

        # 5. QUITAR DEL CARRITO
        elif opcion == "5":
            carrito_compras.mostrar()
            if carrito_compras.total > 0:
                try:
                    indice = int(input("Número de línea que desea quitar: "))
                    carrito_compras.eliminar_videojuego(indice)
                    
                    # Al devolver, el stock sube, guardamos ese cambio
                    if ruta_activa != "":
                        repo.guardar_catalogo_completo(ruta_activa, catalogo_objetos, formato_elegido)
                except ValueError:
                    print("Error: Entrada incorrecta.")

        # 6. FINALIZAR VENTA (FACTURA)
        elif opcion == "6":
            if carrito_compras.total == 0:
                print("No puedes pagar un carrito vacío.")
                continue
            
            cliente = input("Nombre del cliente: ")
            nombre_archivo = input("¿Cómo quiere llamar al archivo de factura?: ")
            
            print("Formato de factura: 1. JSON | 2. CSV")
            f_op = input("Opción: ")
            formato_factura = "json" if f_op == "1" else "csv"
            
            # Saca los datos del carrito para el reporte
            datos_factura = carrito_compras.exportar_datos(cliente)
            repo.guardar_factura_generica(nombre_archivo, datos_factura, formato_factura)
            
            print("¡Gracias por su compra!")
            sistema_encendido = False 

        # 7. SALIR
        elif opcion == "7":
            print("Cerrando el sistema... ¡Hasta luego!")
            sistema_encendido = False

if __name__ == "__main__":
    main()
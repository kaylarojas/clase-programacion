
import os
from modelos.videojuego import JuegoPS5, JuegoXbox, JuegoNintendo
from modelos.carrito import Carrito
import servicios.archivos as repo

def crear_objeto_juego(datos_diccionario):
    """
    Función auxiliar para transformar diccionarios en objetos de clase.
    Cumple con: Polimorfismo y Herencia.
    """
    consola = datos_diccionario["consola"]
    identificador = datos_diccionario["id"]
    nombre = datos_diccionario["nombre"]
    categoria = datos_diccionario.get("categoria", "General")
    precio = datos_diccionario["precio"]
    esrb = datos_diccionario.get("esrb", "E")
    stock = datos_diccionario["stock"]

    if consola == "PS5":
        return JuegoPS5(identificador, nombre, categoria, precio, esrb, stock)
    elif consola == "Xbox":
        return JuegoXbox(identificador, nombre, categoria, precio, esrb, stock)
    else:
        # Por defecto tratamos como Nintendo Switch si no es las anteriores
        return JuegoNintendo(identificador, nombre, categoria, precio, esrb, stock)

def main():
    # --- CONFIGURACIÓN DE RUTAS DINÁMICAS ---
    # Obtenemos la ruta absoluta de la carpeta donde reside este main.py
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    
    # Construimos las rutas hacia los archivos que te dio el profesor
    ruta_archivo_json = os.path.join(ruta_base, "catalogo.json")
    ruta_archivo_csv = os.path.join(ruta_base, "catalogo.csv")

    catalogo_objetos = []
    carrito_compras = Carrito()
    
    print("--- SISTEMA DE GESTIÓN: TIENDA DE VIDEOJUEGOS ---")
    print("Seleccione el archivo de origen para cargar el catálogo:")
    print("1. Cargar desde 'catalogo.json'")
    print("2. Cargar desde 'catalogo.csv'")
    print("3. Iniciar catálogo vacío")
    
    seleccion_inicial = input("Opción: ")
    
    datos_leidos = []
    if seleccion_inicial == "1":
        datos_leidos = repo.cargar_desde_json(ruta_archivo_json)
    elif seleccion_inicial == "2":
        datos_leidos = repo.cargar_desde_csv(ruta_archivo_csv)
    
    # Convertimos los datos planos a objetos de nuestras clases
    for item in datos_leidos:
        nuevo_juego = crear_objeto_juego(item)
        catalogo_objetos.append(nuevo_juego)

    # --- MENÚ PRINCIPAL DEL SISTEMA ---
    sistema_activo = True
    while sistema_activo:
        print("\n================ MENU PRINCIPAL ================")
        print("1. Ver Catálogo Completo")
        print("2. Registrar Nuevo Videojuego")
        print("3. Añadir Producto al Carrito")
        print("4. Revisar Carrito de Compras")
        print("5. Eliminar Producto del Carrito")
        print("6. Finalizar Venta y Generar Factura")
        print("7. Salir")
        print("================================================")
        
        opcion = input("Seleccione una acción (1-7): ")

        if opcion == "1":
            print("\n--- LISTADO DE PRODUCTOS EN STOCK ---")
            for juego in catalogo_objetos:
                print(juego.obtener_detalles() + " | Stock: " + str(juego.stock))

        elif opcion == "2":
            try:
                print("\n--- FORMULARIO DE NUEVO INGRESO ---")
                id_nuevo = int(input("Ingrese ID (número único): "))
                
                # Validación de Identificador repetido
                id_existe = False
                for j in catalogo_objetos:
                    if j.identificador == id_nuevo:
                        id_existe = True
                
                if id_existe:
                    print("Error: El ID " + str(id_nuevo) + " ya está registrado.")
                    continue

                nombre_j = input("Nombre del Videojuego: ")
                if nombre_j == "":
                    print("Error: El nombre no puede estar vacío.")
                    continue

                cat_j = input("Categoría (Aventura, Acción, etc.): ")
                esrb_j = input("Clasificación ESRB (E, T, M): ")
                
                # 2. Validación de Precio (Inmediata)
                precio_j = float(input("Precio de venta: "))
                if precio_j < 0:
                    print("Error: No se permiten precios negativos.")
                    continue # Regresa al menú sin pedir el stock

                # 3. Validación de Stock (Inmediata)
                stock_j = int(input("Cantidad en stock: "))
                if stock_j < 0:
                    print("Error: El stock no puede ser negativo.")
                    continue

                print("Seleccione la Consola:")
                print("1. PlayStation 5 | 2. Xbox Series | 3. Nintendo Switch")
                op_c = input("Opción: ")
                
                nom_consola = "PS5" if op_c == "1" else "Xbox" if op_c == "2" else "Nintendo Switch"
                
                diccionario_nuevo = {
                    "id": id_nuevo, "nombre": nombre_j, "categoria": cat_j,
                    "precio": precio_j, "esrb": esrb_j, "stock": stock_j, "consola": nom_consola
                }
                
                objeto_nuevo = crear_objeto_juego(diccionario_nuevo)
                catalogo_objetos.append(objeto_nuevo)
                print("¡Producto guardado exitosamente en el catálogo!")
            except ValueError:
                print("Error: Por favor ingrese datos numéricos donde se solicita.")

        elif opcion == "3":
            try:
                id_a_comprar = int(input("Ingrese el ID del juego para el carrito: "))
                encontrado = None
                for j in catalogo_objetos:
                    if j.identificador == id_a_comprar:
                        encontrado = j
                
                if encontrado:
                    carrito_compras.agregar(encontrado)
                else:
                    print("Error: El ID ingresado no existe en el catálogo.")
            except ValueError:
                print("Error: ID inválido.")

        elif opcion == "4":
            print("\n--- ESTADO DEL CARRITO ---")
            carrito_compras.mostrar()

        elif opcion == "5":
            carrito_compras.mostrar()
            if carrito_compras.total > 0:
                try:
                    indice_eliminar = int(input("Número de índice para eliminar: "))
                    carrito_compras.eliminar_videojuego(indice_eliminar)
                except ValueError:
                    print("Error: Entrada no válida.")

        elif opcion == "6":
            if carrito_compras.total == 0:
                print("Acción cancelada: El carrito no tiene productos.")
                continue
            
            print("\n--- PROCESO DE FACTURACIÓN ---")
            nombre_cliente = input("Nombre del Cliente: ")
            nombre_factura = input("Nombre deseado para el archivo: ")
            print("Formato de salida: 1. JSON | 2. CSV")
            formato_op = input("Seleccione: ")
            
            tipo_archivo = "json" if formato_op == "1" else "csv"
            datos_finales = carrito_compras.exportar_datos(nombre_cliente)
            
            repo.guardar_factura_generica(nombre_factura, datos_finales, tipo_archivo)
            print("Venta finalizada. Saliendo del sistema...")
            sistema_activo = False 

        elif opcion == "7":
            print("Cerrando sistema. ¡Tenga un excelente día!")
            sistema_activo = False

if __name__ == "__main__":
    main()
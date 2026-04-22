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
        return JuegoNintendo(identificador, nombre, categoria, precio, esrb, stock)

def main():
    # --- CONFIGURACIÓN DE RUTAS DINÁMICAS ---
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo_json = os.path.join(ruta_base, "catalogo.json")
    ruta_archivo_csv = os.path.join(ruta_base, "catalogo.csv")

    catalogo_objetos = []
    carrito_compras = Carrito()
    
    # --- VARIABLES DE PERSISTENCIA ---
    ruta_activa = ""
    formato_activo = ""

    print("--- SISTEMA DE GESTIÓN: TIENDA DE VIDEOJUEGOS ---")
    print("Seleccione el archivo de origen para cargar el catálogo:")
    print("1. Cargar desde 'catalogo.json'")
    print("2. Cargar desde 'catalogo.csv'")
    print("3. Iniciar catálogo vacío")
    
    seleccion_inicial = input("Opción: ")
    formato_activo = seleccion_inicial
    
    datos_leidos = []
    if seleccion_inicial == "1":
        ruta_activa = ruta_archivo_json
        datos_leidos = repo.cargar_desde_json(ruta_activa)
    elif seleccion_inicial == "2":
        ruta_activa = ruta_archivo_csv
        datos_leidos = repo.cargar_desde_csv(ruta_activa)
    
    for item in datos_leidos:
        nuevo_juego = crear_objeto_juego(item)
        catalogo_objetos.append(nuevo_juego)

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
                id_nuevo = int(input("Ingrese ID: "))
                
                id_existe = any(j.identificador == id_nuevo for j in catalogo_objetos)
                if id_existe:
                    print(f"Error: El ID {id_nuevo} ya existe.")
                    continue

                nombre_j = input("Nombre: ")
                cat_j = input("Categoría: ")
                esrb_j = input("Clasificación: ")
                precio_j = float(input("Precio: "))
                stock_j = int(input("Stock: "))

                print("Consola: 1. PS5 | 2. Xbox | 3. Nintendo")
                op_c = input("Opción: ")
                nom_consola = "PS5" if op_c == "1" else "Xbox" if op_c == "2" else "Nintendo Switch"
                
                diccionario_nuevo = {
                    "id": id_nuevo, "nombre": nombre_j, "categoria": cat_j,
                    "precio": precio_j, "esrb": esrb_j, "stock": stock_j, "consola": nom_consola
                }
                
                objeto_nuevo = crear_objeto_juego(diccionario_nuevo)
                catalogo_objetos.append(objeto_nuevo)
                
                # PERSISTENCIA AUTOMÁTICA
                if ruta_activa:
                    repo.guardar_catalogo_completo(ruta_activa, catalogo_objetos, formato_activo)
                
                print("¡Producto registrado y guardado permanentemente!")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "3":
            try:
                id_a_comprar = int(input("Ingrese ID para el carrito: "))
                encontrado = next((j for j in catalogo_objetos if j.identificador == id_a_comprar), None)
                
                if encontrado:
                    carrito_compras.agregar(encontrado)
                    # PERSISTENCIA AUTOMÁTICA (Actualiza el stock en el archivo)
                    if ruta_activa:
                        repo.guardar_catalogo_completo(ruta_activa, catalogo_objetos, formato_activo)
                else:
                    print("Error: ID no encontrado.")
            except ValueError:
                print("Error: ID inválido.")

        elif opcion == "4":
            print("\n--- ESTADO DEL CARRITO ---")
            carrito_compras.mostrar()

        elif opcion == "5":
            carrito_compras.mostrar()
            if carrito_compras.total > 0:
                try:
                    indice_eliminar = int(input("Índice para eliminar: "))
                    carrito_compras.eliminar_videojuego(indice_eliminar)
                    # PERSISTENCIA AUTOMÁTICA (Devuelve stock al archivo)
                    if ruta_activa:
                        repo.guardar_catalogo_completo(ruta_activa, catalogo_objetos, formato_activo)
                except ValueError:
                    print("Error: Entrada no válida.")

        elif opcion == "6":
            if carrito_compras.total == 0:
                print("El carrito está vacío.")
                continue
            
            nombre_cliente = input("Nombre del Cliente: ")
            nombre_factura = input("Nombre del archivo de factura: ")
            print("Formato: 1. JSON | 2. CSV")
            f_op = input("Opción: ")
            
            tipo = "json" if f_op == "1" else "csv"
            datos_f = carrito_compras.exportar_datos(nombre_cliente)
            repo.guardar_factura_generica(nombre_factura, datos_f, tipo)
            
            print("Venta finalizada con éxito.")
            sistema_activo = False 

        elif opcion == "7":
            print("Saliendo del sistema...")
            sistema_activo = False

if __name__ == "__main__":
    main()
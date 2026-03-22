import os
import procesador_datos

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def menu():
    print("\n================================")
    print("   SISTEMA DE ANÁLISIS (DATA)   ")
    print("================================")
    print("1. Procesar archivo CSV")
    print("2. Procesar archivo JSON")
    print("3. Salir")
    
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == "1":
        ruta = os.path.join(BASE_DIR, "data", "datos.csv") 
        datos = procesador_datos.leer_csv(ruta)
    elif opcion == "2":
        ruta = os.path.join(BASE_DIR, "data", "datos.json")
        datos = procesador_datos.leer_json(ruta)
    elif opcion == "3":
        print("Cerrando programa...")
        return
    else:
        print("Opción inválida.")
        return

    if datos is None:
        print(f"\ ERROR: No se encontró el archivo en: {ruta}")
        print("Asegúrate de que el archivo esté dentro de la carpeta 'data'.")
    elif len(datos) == 0:
        print("\n El archivo está vacío.")
    else:
        resultados = procesador_datos.calcular_estadisticas(datos)
        
        if resultados:
            print("\n" + "="*30)
            print("       RESULTADOS FINALES")
            print("="*30)
            print(f"Promedio de Edad:    {resultados['edad']:.2f} años")
            print(f"Promedio de Salario: ${resultados['salario']:.2f}")
            print(f"Promedio de Peso:    {resultados['peso']:.2f} kg")
            print("="*30)

if __name__ == "__main__":
    menu()
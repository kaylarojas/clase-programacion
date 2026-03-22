from agenda.gestor import GestorAgenda
from agenda.contacto import Contacto

def mostrar_menu():
    print("\n" + "-"*40)
    print("    AGENDA DE SHERLOCK HOLMES ")
    print("-"*40)
    print("1. Cargar agenda desde archivo")
    print("2. Agregar contacto")
    print("3. Buscar contacto por nombre")
    print("4. Buscar contacto por teléfono")
    print("5. Ver promedio de edad")
    print("6. Mostrar todos los contactos")
    print("7. Salir")
    return input("\nSeleccione una opción: ")

def ejecutar():
    gestor = GestorAgenda()
    
    while True:
        opc = mostrar_menu()
        
        if opc == "1":
            print("\na. Cargar JSON\nb. Cargar CSV")
            sub_opc = input("Elija formato (a/b): ").lower()
            ruta = input("Nombre del archivo (ej: datos.json o datos.csv): ")
            tipo = 'json' if sub_opc == 'a' else 'csv'
            cant = gestor.cargar_datos(ruta, tipo)
            print(f"\n✅ Éxito: {cant} contactos cargados.")

        elif opc == "2":
            if not gestor.archivo_actual:
                print("\n❌ Error: Primero cargue un archivo.")
                continue
            c = Contacto(
                input("Nombre: "),
                input("Teléfono: "),
                input("Email: "),
                input("Edad: "),
                input("Residencia: ")
            )
            gestor.agregar_contacto(c)
            print("\n✅ Contacto guardado y archivo actualizado.")

        elif opc == "3":
            nombre = input("Ingrese nombre (parcial): ")
            resultados = gestor.buscar_por_nombre(nombre)
            for r in resultados: print(r)

        elif opc == "4":
            tel = input("Ingrese teléfono (parcial): ")
            resultados = gestor.buscar_por_telefono(tel)
            for r in resultados: print(r)

        elif opc == "5":
            promedio = gestor.calcular_promedio_edad()
            print(f"\n📊 El promedio de edad es: {promedio:.2f} años.")

        elif opc == "6":
            print("\n--- LISTA TOTAL DE CONTACTOS ---")
            for c in gestor.contactos: print(c)

        elif opc == "7":
            print("Cerrando sistema seguro... ¡Adiós Sherlock!")
            break

if __name__ == "__main__":
    ejecutar()
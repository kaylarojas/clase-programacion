from figuras import Figura, Cubo, Paralelepipedo, Cilindro, Esfera, Cono

# REQUISITO 3: Función que aplica el Principio de Sustitución de Liskov
# Recibe una Figura (la madre) y funciona con cualquier hija
def imprimir_volumen(figura: Figura):
    resultado = figura.volumen()
    print(f"\nEl volumen de la figura seleccionada es: {resultado:.2f}")

# REQUISITO 4: Clase o archivo Main
def mostrar_menu():
    print("\n--- Menú de Volúmenes ---")
    print("1. Volumen del cubo")
    print("2. Volumen del paralelepípedo")
    print("3. Volumen del cilindro")
    print("4. Volumen de la esfera")
    print("5. Volumen del cono")
    print("6. Salir")

def ejecutar():
    # Creamos un objeto predefinido de cada figura (como pide el requisito 4)
    mi_cubo = Cubo(10)
    mi_paralelepipedo = Paralelepipedo(5, 4, 3)
    mi_cilindro = Cilindro(2, 10)
    mi_esfera = Esfera(5)
    mi_cono = Cono(3, 12)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo del programa...")
            break

        # Según la opción, pasamos el objeto predefinido a la función de Liskov
        if opcion == "1":
            imprimir_volumen(mi_cubo)
        elif opcion == "2":
            imprimir_volumen(mi_paralelepipedo)
        elif opcion == "3":
            imprimir_volumen(mi_cilindro)
        elif opcion == "4":
            imprimir_volumen(mi_esfera)
        elif opcion == "5":
            imprimir_volumen(mi_cono)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()
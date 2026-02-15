# main.py
import volumen

def mostrar_menu():
    print("\n--- Calculadora de Volúmenes ---")
    print("1. Cubo")
    print("2. Paralelepípedo")
    print("3. Cilindro")
    print("4. Esfera")
    print("5. Cono")
    print("6. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "6":
            print("¡Gracias por usar la calculadora!")
            break

        try:
            if opcion == "1":
                lado = float(input("Indique el lado del cubo: "))
                res = volumen.volumen_cubo(lado)
                print(f" El volumen del cubo es: {res:.2f}")

            elif opcion == "2":
                l = float(input("Indique el largo: "))
                an = float(input("Indique el ancho: "))
                al = float(input("Indique el alto: "))
                res = volumen.volumen_paralelepipedo(l, an, al)
                print(f" El volumen del paralelepípedo es: {res:.2f}")

            elif opcion == "3":
                r = float(input("Indique el radio: "))
                h = float(input("Indique la altura: "))
                res = volumen.volumen_cilindro(r, h)
                print(f" El volumen del cilindro es: {res:.2f}")

            elif opcion == "4":
                r = float(input("Indique el radio de la esfera: "))
                res = volumen.volumen_esfera(r)
                print(f" El volumen de la esfera es: {res:.2f}")

            elif opcion == "5":
                r = float(input("Indique el radio de la base: "))
                h = float(input("Indique la altura: "))
                res = volumen.volumen_cono(r, h)
                print(f" El volumen del cono es: {res:.2f}")

            else:
                print("Opción no válida, intenta de nuevo.")

        except ValueError:
            print("Error: Por favor ingresa solo números.")
        
        print("-" * 30)

if __name__ == "__main__":
    ejecutar_calculadora()
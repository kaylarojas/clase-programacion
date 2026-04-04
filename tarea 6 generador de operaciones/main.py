from logic.generador import crear_ejercicios

def menu():
    print("--- Generador de Prácticas: Prof. Jirafales ---")
    try:
        s = int(input("Cantidad de sumas: "))
        r = int(input("Cantidad de restas: "))
        m = int(input("Cantidad de multiplicaciones: "))
        d = int(input("Cantidad de divisiones: "))

        crear_ejercicios(s, r, m, d)
        
        print("\n[OK] Archivos 'practica.txt' y 'respuestas.txt' creados.")
    except ValueError:
        print("\n[Error] Use solo números enteros.")

if __name__ == "__main__":
    menu()
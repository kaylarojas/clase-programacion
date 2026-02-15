# main.py
import cripto

def ejecutar_programa():
    print(" Sistema de Cifrado César ")
    
    while True:
        print("\nOpciones:")
        print("1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "3":
            print("Programa finalizado.")
            break
            
        if opcion in ["1", "2"]:
            mensaje = input("Ingrese el mensaje: ")
            try:
                n = int(input("Ingrese el factor de desplazamiento (N): "))
                
                modo = "encriptar" if opcion == "1" else "desencriptar"
                resultado = cripto.procesar_cesar(mensaje, n, modo)
                
                print(f"\n Resultado ({modo}do): {resultado}")
            except ValueError:
                print(" Error: El desplazamiento debe ser un número entero.")
        else:
            print(" Opción no válida.")
            
        print("-" * 30)

if __name__ == "__main__":
    ejecutar_programa()
from mundo.administrador import MundoVirtual

def mostrar_menu():
    simulador = MundoVirtual()
    
    while True:
        print("\n********** SIMULADOR DE VIDA **********")
        print("1. Crear persona")
        print("2. Crear mascota")
        print("3. Crear vehículo")
        print("4. Imprimir personas")
        print("5. Imprimir mascotas")
        print("6. Imprimir vehículos")
        print("7. Imprimir todas las entidades")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            simulador.agregar_persona()
        elif opcion == "2":
            simulador.agregar_mascota()
        elif opcion == "3":
            simulador.agregar_vehiculo()
        elif opcion == "4":
            simulador.imprimir_lista(simulador.personas, "LISTA DE PERSONAS")
        elif opcion == "5":
            simulador.imprimir_lista(simulador.mascotas, "LISTA DE MASCOTAS")
        elif opcion == "6":
            simulador.imprimir_lista(simulador.vehiculos, "LISTA DE VEHÍCULOS")
        elif opcion == "7":
            simulador.imprimir_todo()
        elif opcion == "8":
            print("¡Gracias por jugar! Cerrando mundo virtual...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
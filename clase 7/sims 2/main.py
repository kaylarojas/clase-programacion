from mundo.administrador import MundoVirtual

def menu_principal():
    sim = MundoVirtual()
    
    opciones = {
        "1": sim.registrar_persona,
        "2": sim.registrar_mascota,
        "3": sim.registrar_vehiculo,
        "4": lambda: sim.imprimir_entidades("1"),
        "5": lambda: sim.imprimir_entidades("2"),
        "6": lambda: sim.imprimir_entidades("3"),
        "7": sim.imprimir_todo
    }

    while True:
        print("\n********** SIMULADOR DE VIDA **********")
        print("1. Crear persona\n2. Crear mascota\n3. Crear vehículo")
        print("4. Imprimir personas\n5. Imprimir mascotas\n6. Imprimir vehículos")
        print("7. Imprimir todas las entidades\n8. Salir")
        
        eleccion = input("\nSeleccione una opción: ")
        
        if eleccion == "8":
            break
        elif eleccion in opciones:
            opciones[eleccion]()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
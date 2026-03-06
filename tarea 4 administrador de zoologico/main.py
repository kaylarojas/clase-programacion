from personal.roles import Administrador, Guardian, Conserje, Veterinario
from personal.transporte import Bicicleta, Cuadraciclo, Patineta
from zoologico.especies import Leon, Cocodrilo, Aguila, Tiburon, Rana

# Listas globales para almacenar los objetos (Requerimiento 9)
empleados = []
transportes = []
animales = []

def menu_empleados():
    print("\n--- AGREGAR EMPLEADO ---")
    print("1.1 Agregar Administrador")
    print("1.2 Agregar Guardián")
    print("1.3 Agregar Conserje")
    print("1.4 Agregar Veterinario")
    opcion = input("Seleccione tipo: ")
    
    nombre = input("Nombre del empleado: ")
    id_emp = input("ID del empleado: ")
    
    if opcion == "1": empleados.append(Administrador(nombre, id_emp))
    elif opcion == "2": empleados.append(Guardian(nombre, id_emp))
    elif opcion == "3": empleados.append(Conserje(nombre, id_emp))
    elif opcion == "4": empleados.append(Veterinario(nombre, id_emp))
    else: print("Opción no válida.")

def menu_transporte():
    print("\n--- AGREGAR TRANSPORTE ---")
    print("3.1 Agregar Bicicleta")
    print("3.2 Agregar Cuadraciclo")
    print("3.3 Agregar Patineta")
    opcion = input("Seleccione tipo: ")
    
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    
    if opcion == "1": transportes.append(Bicicleta(marca, modelo))
    elif opcion == "2": transportes.append(Cuadraciclo(marca, modelo))
    elif opcion == "3": transportes.append(Patineta(marca, modelo))
    else: print("Opción no válida.")

def menu_animales():
    print("\n--- AGREGAR ANIMAL ---")
    print("5.1 Agregar Reptil (Cocodrilo)")
    print("5.2 Agregar Mamífero (León)")
    print("5.3 Agregar Ave (Águila)")
    print("5.4 Agregar Pez (Tiburón)")
    print("5.5 Agregar Anfibio (Rana)")
    opcion = input("Seleccione categoría: ")
    
    especie = input("Nombre/Especie: ")
    try:
        edad = int(input("Edad: "))
        if opcion == "1": animales.append(Cocodrilo(especie, edad))
        elif opcion == "2": animales.append(Leon(especie, edad))
        elif opcion == "3": animales.append(Aguila(especie, edad))
        elif opcion == "4": animales.append(Tiburon(especie, edad))
        elif opcion == "5": animales.append(Rana(especie, edad))
        else: print("Opción no válida.")
    except ValueError:
        print("Error: La edad debe ser un número.")

def listar_todo(lista, titulo):
    print(f"\n--- {titulo} ---")
    if not lista:
        print("No hay registros todavía.")
    for item in lista:
        print(item) # Aquí se ejecuta el método __str__ (Req. 2)

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ZOOLÓGICO ==========")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Agregar medio de transporte")
        print("4. Listar medios de transporte")
        print("5. Agregar animal")
        print("6. Listar animales")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1": menu_empleados()
        elif opcion == "2": listar_todo(empleados, "LISTA DE EMPLEADOS")
        elif opcion == "3": menu_transporte()
        elif opcion == "4": listar_todo(transportes, "LISTA DE TRANSPORTES")
        elif opcion == "5": menu_animales()
        elif opcion == "6": listar_todo(animales, "LISTA DE ANIMALES")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
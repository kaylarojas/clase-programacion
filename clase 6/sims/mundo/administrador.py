from .entidades import Persona, Mascota, Vehiculo

class MundoVirtual:
    def __init__(self):
        # Almacenamiento de datos solicitado
        self.personas = []
        self.mascotas = []
        self.vehiculos = []

    def agregar_persona(self):
        print("\n--- Nueva Persona ---")
        n = input("Nombre: ")
        e = input("Edad: ")
        p = input("Profesión: ")
        nueva = Persona(n, e, p)
        self.personas.append(nueva)
        print("¡Persona creada con éxito!")

    def agregar_mascota(self):
        print("\n--- Nueva Mascota ---")
        n = input("Nombre: ")
        es = input("Especie (Perro, Gato, etc): ")
        en = input("Nivel de energía: ")
        nueva = Mascota(n, es, en)
        self.mascotas.append(nueva)

    def agregar_vehiculo(self):
        print("\n--- Nuevo Vehículo ---")
        m = input("Marca: ")
        mo = input("Modelo: ")
        c = input("Color: ")
        nuevo = Vehiculo(m, mo, c)
        self.vehiculos.append(nuevo)

    def imprimir_lista(self, lista, titulo):
        print(f"\n=== {titulo} ===")
        if not lista:
            print("No hay registros todavía.")
        for item in lista:
            print(item)

    def imprimir_todo(self):
        self.imprimir_lista(self.personas, "PERSONAS")
        self.imprimir_lista(self.mascotas, "MASCOTAS")
        self.imprimir_lista(self.vehiculos, "VEHÍCULOS")
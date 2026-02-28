from .entidades import Persona, Mascota, Vehiculo

class MundoVirtual:
    def __init__(self):
        self.__personas = []
        self.__mascotas = []
        self.__vehiculos = []

    # Se llama registrar_persona para que coincida con tu main.py
    def registrar_persona(self):
        print("\n--- Nueva Persona ---")
        n = input("Nombre: ")
        e = input("Edad: ")
        p = input("Profesión: ")
        nueva_p = Persona(n, e, p)
        
        # Lógica de Asociación: permite elegir una mascota existente
        if self.__mascotas:
            print("\nMascotas disponibles para asociar:")
            for i, m in enumerate(self.__mascotas):
                print(f"{i}. {m.nombre}")
            sel = input("Seleccione el número de la mascota (o Enter para ninguna): ")
            if sel.isdigit() and int(sel) < len(self.__mascotas):
                nueva_p.mascota = self.__mascotas[int(sel)]
        
        self.__personas.append(nueva_p)
        print("¡Persona registrada!")

    def registrar_mascota(self):
        print("\n--- Nueva Mascota ---")
        n = input("Nombre: ")
        es = input("Especie: ")
        en = input("Energía (0-100): ")
        self.__mascotas.append(Mascota(n, es, en))

    def registrar_vehiculo(self):
        print("\n--- Nuevo Vehículo ---")
        ma = input("Marca: ")
        mo = input("Modelo: ")
        co = input("Color: ")
        self.__vehiculos.append(Vehiculo(ma, mo, co))

    def imprimir_entidades(self, tipo):
        # Mapeo de listas según la opción elegida
        mapa = {"1": (self.__personas, "PERSONAS"), 
                "2": (self.__mascotas, "MASCOTAS"), 
                "3": (self.__vehiculos, "VEHÍCULOS")}
        
        lista, titulo = mapa[tipo]
        print(f"\n=== {titulo} ===")
        if not lista:
            print("No hay datos.")
        for item in lista:
            print(f"{item} (Dato len: {len(item)})")

    def imprimir_todo(self):
        for op in ["1", "2", "3"]:
            self.imprimir_entidades(op)
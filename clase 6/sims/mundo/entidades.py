class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def __str__(self):
        return f"[Persona] Nombre: {self.nombre}, Edad: {self.edad}, Profesión: {self.profesion}"

class Mascota:
    def __init__(self, nombre, especie, energia):
        self.nombre = nombre
        self.especie = especie
        self.energia = energia

    def __str__(self):
        return f"[Mascota] Nombre: {self.nombre}, Especie: {self.especie}, Energía: {self.energia}%"

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"[Vehículo] Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"
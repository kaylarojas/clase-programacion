class Corazon:
    def __init__(self, ritmo="70 BPM"):
        self.__ritmo = ritmo
    def __str__(self):
        return f"Latido: {self.__ritmo}"

class Mascota:
    def __init__(self, nombre, especie, energia):
        self.__nombre = nombre
        self.__especie = especie
        self.__energia = energia # Atributo recuperado

    @property
    def nombre(self): return self.__nombre

    def __str__(self):
        return f"Mascota: {self.__nombre} (Especie: {self.__especie}, Energía: {self.__energia}%)"

    def __len__(self):
        return int(self.__energia)

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.__nombre = nombre
        self.__edad = edad
        self.__profesion = profesion # Atributo recuperado
        self.__corazon = Corazon()   # Composición
        self.__mascota = None        # Asociación

    @property
    def nombre(self): return self.__nombre

    @property
    def mascota(self): return self.__mascota

    @mascota.setter
    def mascota(self, objeto_mascota):
        self.__mascota = objeto_mascota

    def __str__(self):
        asoc = f"Dueño de {self.__mascota.nombre}" if self.__mascota else "Sin mascota"
        return f"Persona: {self.__nombre} ({self.__profesion}) | Edad: {self.__edad} | {asoc} | [{self.__corazon}]"

    def __len__(self):
        return int(self.__edad)

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color # Atributo recuperado

    def __str__(self):
        return f"Vehículo: {self.__marca} {self.__modelo} | Color: {self.__color}"

    def __len__(self):
        return len(self.__marca)
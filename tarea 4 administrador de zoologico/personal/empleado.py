class Empleado:
    """
    Clase base para representar a un empleado del zoológico.
    
    Atributos:
        nombre (str): Nombre del empleado.
        id_empleado (int): Identificador único.
    """
    def __init__(self, nombre, id_empleado):
        self._nombre = nombre
        self._id_empleado = id_empleado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, valor):
        self._id_empleado = valor

    def __str__(self):
        return f"ID: {self._id_empleado} | Nombre: {self._nombre}"
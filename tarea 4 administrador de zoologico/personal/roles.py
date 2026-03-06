from .empleado import Empleado

class Administrador(Empleado):
    def __str__(self):
        return f"[Administrador] {super().__str__()}"

class Guardian(Empleado):
    def __str__(self):
        return f"[Guardián] {super().__str__()}"

class Conserje(Empleado):
    def __str__(self):
        return f"[Conserje] {super().__str__()}"

class Veterinario(Empleado):
    def __str__(self):
        return f"[Veterinario] {super().__str__()}"
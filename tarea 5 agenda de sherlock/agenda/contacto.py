class Contacto:
    def __init__(self, nombre, telefono, email, edad, residencia):
        self.nombre = nombre
        self.telefono = str(telefono)
        self.email = email
        self.edad = int(edad)
        self.residencia = residencia

    def to_dict(self):
        """Convierte el objeto a diccionario para guardarlo en JSON/CSV."""
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "edad": self.edad,
            "residencia": self.residencia
        }

    def __str__(self):
        """Formato visual para mostrar en la lista."""
        return f"👤 {self.nombre.ljust(15)} | 📞 {self.telefono.ljust(10)} | 📧 {self.email.ljust(20)} | 🎂 {str(self.edad).center(4)} | 🏠 {self.residencia}"
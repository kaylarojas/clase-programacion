from .animal import Animal

# --- 1. REPTILES ---
class Reptil(Animal):
    def __str__(self):
        return f"[Reptil] {super().__str__()}"

class Cocodrilo(Reptil): # Especie específica (Req 6.a)
    def __str__(self):
        return f"{super().__str__()} - Tipo: Cocodrilo del Nilo"

# --- 2. MAMÍFEROS ---
class Mamifero(Animal):
    def __str__(self):
        return f"[Mamífero] {super().__str__()}"

class Leon(Mamifero): # Especie específica (Req 6.b)
    def __str__(self):
        return f"{super().__str__()} - Tipo: León Africano"

# --- 3. AVES ---
class Ave(Animal):
    def __str__(self):
        return f"[Ave] {super().__str__()}"

class Aguila(Ave): # Especie específica (Req 6.c)
    def __str__(self):
        return f"{super().__str__()} - Tipo: Águila Real"

# --- 4. PECES ---
class Pez(Animal):
    def __str__(self):
        return f"[Pez] {super().__str__()}"

class Tiburon(Pez): # Especie específica (Req 6.d)
    def __str__(self):
        return f"{super().__str__()} - Tipo: Tiburón Blanco"

# --- 5. ANFIBIOS ---
class Anfibio(Animal):
    def __str__(self):
        return f"[Anfibio] {super().__str__()}"

class Rana(Anfibio): # Especie específica (Req 6.e)
    def __str__(self):
        return f"{super().__str__()} - Tipo: Rana Toro"

import math
from abc import ABC, abstractmethod

# Abstracción común para todas las figuras
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Cada clase tiene una responsabilidad
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Nueva figura: no modifica las clases anteriores
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

def mostrar_area(figura):
    print(f"Área: {figura.calcular_area():.2f}")

figuras = [
    Rectangulo(5, 3),
    Circulo(2),
    Triangulo(4, 6)
]

for figura in figuras:
    mostrar_area(figura)

import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

print("Rectángulo:", calcular_area_rectangulo(5, 3))
print("Cuadrado:", calcular_area_cuadrado(4))
print("Círculo:", round(calcular_area_circulo(2), 2))
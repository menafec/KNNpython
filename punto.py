import math

class Punto:
    def __init__(self, x, y, etiqueta):
        self.x = x
        self.y = y
        self.etiqueta = etiqueta

    # Método para calcular la distancia entre dos puntos
    def calcular_distancia(self, otro):
        return math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)
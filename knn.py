from punto_distancia import PuntoDistancia

class KNN:
    def __init__(self, puntos_de_entrenamiento, k):
        self.puntos_de_entrenamiento = puntos_de_entrenamiento
        self.k = k

    # Método para clasificar un nuevo punto
    def clasificar(self, nuevo_punto):
        distancias = []

        # Calcular la distancia desde el nuevo punto a cada punto de entrenamiento
        for punto in self.puntos_de_entrenamiento:
            distancia = nuevo_punto.calcular_distancia(punto)
            distancias.append(PuntoDistancia(punto, distancia))

        # Ordenar por distancia
        distancias.sort(key=lambda pd: pd.distancia)

        # Tomar los k vecinos más cercanos
        k_vecinos = [distancias[i].punto for i in range(self.k)]

        # Contar la frecuencia de cada etiqueta
        frecuencias = {}
        for vecino in k_vecinos:
            if vecino.etiqueta in frecuencias:
                frecuencias[vecino.etiqueta] += 1
            else:
                frecuencias[vecino.etiqueta] = 1

        # Retornar la etiqueta con mayor frecuencia
        return max(frecuencias, key=frecuencias.get)
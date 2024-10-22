from knn import KNN
from punto import Punto
import matplotlib.pyplot as plt

def main():
    # Crear puntos de entrenamiento basados en el dataset
    puntos_de_entrenamiento = [
        Punto(108, 95, "Alta"),
        Punto(115, 96, "Alta"),
        Punto(106, 95, "Alta"),
        Punto(97, 97, "Alta"),
        Punto(95, 93, "Media"),
        Punto(91, 94, "Media"),
        Punto(97, 93, "Media"),
        Punto(83, 92, "Media"),
        Punto(83, 86, "Media"),
        Punto(78, 80, "Baja"),
        Punto(54, 73, "Baja"),
        Punto(67, 80, "Baja"),
        Punto(56, 65, "Baja"),
        Punto(53, 69, "Baja"),
        Punto(61, 77, "Baja"),
        Punto(115, 96, "Alta"),
        Punto(81, 87, "Media"),
        Punto(78, 89, "Media"),
        Punto(80, 90, "Media"),
        Punto(45, 63, "Baja"),
        Punto(99, 95, "Alta"),
        Punto(32, 61, "Baja"),
        Punto(25, 55, "Baja"),
        Punto(28, 56, "Baja"),
        Punto(90, 94, "Media"),
        Punto(89, 93, "Media")
    ]

    # Crear el clasificador KNN con k = 5
    knn = KNN(puntos_de_entrenamiento, 5)

    # Clasificar un nuevo punto
    nuevo_punto = Punto(85, 91, None)
    clase_predicha = knn.clasificar(nuevo_punto)

    print(f"El nuevo punto pertenece a la clase: {clase_predicha}")

    # Mostrar gráfico
    mostrar_grafico(puntos_de_entrenamiento, nuevo_punto, clase_predicha)

def mostrar_grafico(puntos, nuevo_punto, clase_predicha):
    colores = {"Alta": "red", "Media": "blue", "Baja": "green"}

    # Graficar puntos de entrenamiento
    for punto in puntos:
        plt.scatter(punto.x, punto.y, color=colores[punto.etiqueta], label=punto.etiqueta)

    # Graficar el nuevo punto
    plt.scatter(nuevo_punto.x, nuevo_punto.y, color="yellow", edgecolors="black", s=100, label="Nuevo Punto")

    # Etiquetas y leyenda
    plt.title(f"Clasificación KNN - Clase predicha: {clase_predicha}")
    plt.xlabel("X")
    plt.ylabel("Y")
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
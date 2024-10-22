# K-Nearest Neighbors (KNN) Classifier in Python

## Descripción

Este proyecto implementa un clasificador K-Nearest Neighbors (KNN) en Python. El algoritmo se utiliza para predecir la clase de un nuevo punto basado en los puntos de entrenamiento existentes. Además, se incluye una representación gráfica que muestra cómo se distribuyen los puntos y la clasificación del nuevo punto utilizando la biblioteca `matplotlib`.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- **main.py**: Contiene la función principal para ejecutar el clasificador KNN, clasificar un nuevo punto y mostrar el resultado en un gráfico.
- **punto.py**: Define la clase `Punto`, que representa un punto en el espacio con coordenadas `(x, y)` y una etiqueta.
- **knn.py**: Define la clase `KNN`, que implementa el algoritmo de clasificación K-Nearest Neighbors.
- **punto_distancia.py**: Define la clase `PuntoDistancia`, que se utiliza para calcular y almacenar la distancia entre el nuevo punto y los puntos de entrenamiento.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3 y las siguientes bibliotecas:

- `matplotlib` (para la visualización de gráficos)

Puedes instalar las bibliotecas requeridas usando:

pip install matplotlib


El programa clasificará un nuevo punto con coordenadas (85, 91) y mostrará la clase a la que pertenece, además de generar un gráfico visualizando los puntos de entrenamiento y el nuevo punto clasificado.

Ejemplo de Salida

Al ejecutar el programa, deberías ver una salida similar a:

El nuevo punto pertenece a la clase: Media

Explicación del Código

	1.	main.py: Configura el conjunto de datos de puntos de entrenamiento, crea un objeto de la clase KNN, clasifica un nuevo punto y luego muestra un gráfico que visualiza el resultado.
	2.	punto.py: Contiene la clase Punto, que almacena las coordenadas (x, y) y la etiqueta de un punto, y también calcula la distancia euclidiana entre dos puntos.
	3.	knn.py: Define la lógica del algoritmo KNN. Calcula las distancias entre el nuevo punto y todos los puntos de entrenamiento, selecciona los k vecinos más cercanos y determina la clase basada en la mayoría de votos.
	4.	punto_distancia.py: Define la clase PuntoDistancia que facilita el almacenamiento y ordenamiento de puntos por distancia.

Visualización del Gráfico

El gráfico generado muestra los puntos de entrenamiento de cada clase en diferentes colores:

	•	Rojo: Clase “Alta”
	•	Azul: Clase “Media”
	•	Verde: Clase “Baja”
	•	Amarillo: Nuevo punto clasificado

El título del gráfico mostrará la clase predicha para el nuevo punto.

Personalización

Puedes modificar el valor de k o añadir/quitar puntos de entrenamiento en main.py para observar cómo afecta la clasificación del nuevo punto.


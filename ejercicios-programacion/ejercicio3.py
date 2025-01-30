"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
 la que el siguiente siempre es la suma de los dos anteriores.
 0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    anterior, actual = 0, 1  # Inicializa los dos primeros números de la secuencia
    print(anterior)  # Imprime el primer número (0)

    for _ in range(1, 51):  # Itera 50 veces para generar los siguientes 50 números
        anterior, actual = actual, anterior + actual  # Actualiza los valores de anterior y actual simultáneamente
        print(anterior)  # Imprime el siguiente número de la secuencia

fibonacci()

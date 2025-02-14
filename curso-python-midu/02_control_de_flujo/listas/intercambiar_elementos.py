"""
Ejercicio 2: Intercambio de posiciones
Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
Intercambia la primera y la última posición utilizando solo asignación por índice.
"""

numeros = [10, 20, 30, 40, 50]

# El intercambio se realiza utilizando asignación por índice.
# "numeros[0]" se refiere al primer elemento (10) y "numeros[-1]" al último elemento (50).
# En este caso, estamos usando una asignación múltiple, que permite intercambiar los valores de las dos posiciones de forma directa.
# 1. "numeros[0], numeros[-1]" toma el valor de "numeros[0]" (que es 10) y lo asigna temporalmente a la posición de "numeros[-1]" (la última posición).
# 2. "numeros[-1], numeros[0]" toma el valor de "numeros[-1]" (que es 50) y lo asigna a "numeros[0]" (la primera posición).
# Así, los valores de la primera y última posición se intercambian directamente.
numeros[0], numeros[-1] = numeros[-1], numeros[0]

print(numeros)  # La salida será: [50, 20, 30, 40, 10]

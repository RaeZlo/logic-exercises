"""
Ejercicio 2: Calcular la media de una lista
Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
Calcula la media de los números usando un bucle for.
"""

numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num

promedio = suma / len(numeros)
print(f"La promedio es: {promedio}")

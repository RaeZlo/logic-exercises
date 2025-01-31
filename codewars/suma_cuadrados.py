"""
Calcula la suma de los cuadrados de todos los números en una lista.
"""

def suma_cuadrados(numbers:list) -> int:
    # Esta línea utiliza una expresión generadora y la función sum() para calcular la suma de los cuadrados.
    # 1. "num**2 for num in numbers": Esta parte eleva al cuadrado cada número en la lista y crea un nuevo iterable.
    # 2. `sum()` suma todos los elementos de ese iterable.
    return sum(num**2 for num in numbers)

respuesta = suma_cuadrados([1, 2, 4])
print(respuesta)

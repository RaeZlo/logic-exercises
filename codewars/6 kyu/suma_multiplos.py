"""
Escribe una función que reciba un número entero positivo n y calcule la suma de todos 
los múltiplos de 3 o 5 que sean menores que n.
"""

def suma_multiplos(n: int) -> int:
    # Usamos una comprensión de listas para generar los números menores a 'n'
    # y filtramos los que son múltiplos de 3 o 5.
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

respuesta = suma_multiplos(10)
print(respuesta)  # Salida esperada: 23

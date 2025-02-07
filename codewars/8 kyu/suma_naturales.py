"""
Crea una función que calcule la suma de los primeros 'n' números naturales.
Por ejemplo, si n es 5, la función debe calcular 1 + 2 + 3 + 4 + 5.
"""

def suma_naturales(n: int) -> int:
    suma = 0
    for i in range(1, n + 1):  # Itera desde 1 hasta n (inclusive)
        suma += i  # Suma el número actual a la suma acumulada
    return suma

def suma_naturales_formula(n: int) -> int:
    return n * (n + 1) // 2  # Fórmula de Gauss para la suma de los primeros n números naturales

def suma_naturales_recursividad(n:int) -> int:
    # Caso base: si n es 1, la suma es 1
    if n == 1:
        return 1
    return n + suma_naturales_recursividad(n - 1)
    

# Ejemplo de uso:
resultado1 = suma_naturales(3)  # 1 + 2 + 3 = 6
print(f"Suma de naturales (iterativa): {resultado1}")

resultado2 = suma_naturales_formula(8)  # 8 * (8 + 1) // 2 = 36
print(f"Suma de naturales (fórmula): {resultado2}")

resultado3 = suma_naturales_recursividad(2)
print(f"Suma de naturales (recursividad): {resultado3}")

"""
Crea una función que reciba una lista de números enteros, donde debera encontrar 
el que aparece un número impar de veces.
Siempre habrá un solo número entero que aparecerá un número impar de veces.
"""

def encontrar_impar(lista_numeros: list) -> int:
    for num in lista_numeros:
        # Cuenta cuántas veces aparece el número en la lista
        if lista_numeros.count(num) % 2 != 0:
            return num  # Devuelve el número si aparece un número impar de veces

def alternativa(lista_numeros: list) -> int:
    resultado = 0  # Inicializamos la variable en 0
    for num in lista_numeros:
        resultado ^= num  # Aplicamos XOR con cada número
    return resultado  # El resultado final será el número impar


print(encontrar_impar([7]))  # 7
print(encontrar_impar([0]))  # 0
print(encontrar_impar([1, 1, 2]))  # 2
print(encontrar_impar([0, 1, 0, 1, 0]))  # 0
print(encontrar_impar([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  # 4
print(alternativa([0, 1, 1, 3, 0]))  # 

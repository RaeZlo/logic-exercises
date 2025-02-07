"""
Obtienes una lista de números y devuelves la suma de todos los positivos.
"""

def suma_positivos(lista: list) -> int:
    suma = 0  # Inicializa la variable suma a 0
    for num in lista:  # Itera sobre cada número en la lista
        if num > 0:  # Verifica si el número es positivo
            suma = num + suma  # Suma el número positivo a la variable suma
    return suma  # Retorna la suma total de los números positivos


def alternativa(lista: list) -> int:
    # Explicación detallada de la expresión generadora:
    # 1. "numero for numero in lista": Itera sobre cada elemento de la lista y lo asigna a la variable "numero".
    # 2. "if numero > 0": Filtra los números los números que no sean mayores a 0.
    # 3. La combinación de los puntos 1 y 2 crea una secuencia de números positivos.
    # La función sum() toma esta secuencia y calcula la suma de todos sus elementos.
    return sum(numero for numero in lista if numero > 0)

lista_numeros = [1, -2, 3, 2]

# Usando la función suma_positivos
suma1 = suma_positivos(lista_numeros)
print(f"Suma de positivos (versión 1): {suma1}")  # Imprime 6

# Usando la función alternativa
suma2 = alternativa(lista_numeros)
print(f"Suma de positivos (versión 2): {suma2}")  # Imprime 6

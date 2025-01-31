"""
Crea una función qeu convierta un número (int) a una cadena de texto.
"""

def numero_a_cadena(numero: int) -> str:
    # La función str() en Python convierte cualquier objeto a una cadena.
    # En este caso, convertimos el número entero a una cadena de texto.
    return str(numero)

# Ejemplo de uso:
respuesta = numero_a_cadena(333)
print(f"El número {respuesta} es de tipo {type(respuesta)}")  # Imprime "333"

"""
Crea una foncón que repita una cadena un número determinado de veces.
"""
def repetir_cadena(repetidor: int, cadena: str) -> str:
    # La multiplicación de una cadena por un número en Python tiene un comportamiento especial:
    # Repite la cadena el número de veces indicado.
    # Por ejemplo, "hola" * 3 resulta en "holaholahola".
    return cadena * repetidor

# Ejemplo de uso:
respuesta = repetir_cadena(3, "pepe")
print(respuesta)  # Imprime "pepepepepepe"

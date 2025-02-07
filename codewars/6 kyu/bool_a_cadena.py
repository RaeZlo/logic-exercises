"""
Convierte un valor booleano (True o False) a una cadena de texto.
Si el valor es True retorna la cadena "Yes", y "No" si es False.
"""

def bool_a_cadena(booleano: bool) -> str:
    # Utilizamos una expresión condicional (if-else) para convertir el valor booleano en una cadena.
    # Si el valor booleano es True, se retorna "Yes".
    # De lo contrario, se retorna "No".
    return "Yes" if booleano else "No"

# Ejemplo de uso:
resultado = bool_a_cadena(True)
print(resultado)  # Imprime "Yes"

resultado = bool_a_cadena(False)
print(resultado)  # Imprime "No"

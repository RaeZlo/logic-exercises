"""
Ejercicio:
Encuentra las palabras de 4 a 6 letras en el siguiente texto
"""

import re

words = "ala casa árbol león cinco murcielago"

# Expresión regular para encontrar palabras de 4 a 6 letras
# \b: Indica el límite de una palabra.
# \w{4,6}: Coincide con palabras que tienen entre 4 y 6 caracteres (alfanuméricos o guión bajo).
# \b: Otro límite de palabra para asegurarse de que se capture una palabra completa.
pattern = r"\b\w{4,6}\b"

result = re.findall(pattern, words)

print(result)

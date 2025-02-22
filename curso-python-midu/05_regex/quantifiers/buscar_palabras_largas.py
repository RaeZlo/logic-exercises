"""
Ejercicio
Encuentra las palabras de más de 6 letras
"""

import re

words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"

result = re.findall(pattern, words)
print(result)

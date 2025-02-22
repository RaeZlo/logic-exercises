"""
Ejercicio:
Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
Solo queremos las palabras man, fan y ban
"""

import re

text = "omniman fanatico man bandana"
pattern = r"[mfb]an"

result = re.findall(pattern, text)
print(result)

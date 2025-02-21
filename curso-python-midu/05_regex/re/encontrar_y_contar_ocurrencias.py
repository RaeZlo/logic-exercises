"""
EJERCICIO 02
Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que 
posición empieza y termina cada coincidencia y cuantas veces se encontró.
"""

import re

pattern = "midu"
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

results = list(re.finditer(pattern, text))

for result in results:
    print(f"Encontrado '{result.group()}' desde la posición {result.start()} hasta la posición {result.end()}")

print(f"Total de las ocurrencias: {len(results)}")

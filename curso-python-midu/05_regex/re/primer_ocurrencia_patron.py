"""
EJERCICIO 01
Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
e indica en que posición empieza y termina la coincidencia.
"""

import re

pattern = "IA"
text = """Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta 
            ver cómo la puede cagar con las Regex para ir con cuidado"""
result = re.search(pattern, text)

if result:
  print(f"He encontrado el patrón en el texto en la posición {result.start()} y termina en la posición {result.end()}")
else:
  print("No he encontrado el patrón en el texto")


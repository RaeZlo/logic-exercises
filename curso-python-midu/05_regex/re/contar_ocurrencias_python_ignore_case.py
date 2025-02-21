"""
EJERCICIO 03
Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre 
mayúsculas y minúsculas.
"""

import re

pattern = "python"
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

# Se usa re.IGNORECASE para hacer la búsqueda insensible a mayúsculas y minúsculas
result = re.findall(pattern, text, re.IGNORECASE)
print(f"Se encontraron {len(result)} ocurrencias.")

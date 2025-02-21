"""
Ejercicio: 
Detectar si hay un número de España en el texto gracias al prefijo +34
"""

import re

# Patrón para detectar números de teléfono de España con el prefijo +34
pattern = r"\+34 \d{9}"
text = "El número de teléfono de mi primo es +34 123456789"

# Búsqueda del número con el patrón
result = re.search(pattern, text)

if result:
    print(f"Número de teléfono encontrado: {result.group()}")
else:
    print("No se encontró ningún número de teléfono válido de España.")

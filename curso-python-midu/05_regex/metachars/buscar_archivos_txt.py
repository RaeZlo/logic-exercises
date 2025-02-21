"""
EJERCICIO:
Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
"""

import re

text = "pepe.pdf oratoria.txt cv.pdf horarios.txt"

# Patrón para encontrar los archivos con extensión .txt
pattern = r"\b\w+\.txt\b"  
# \b es un límite de palabra, asegura que coincida solo con archivos completos
# \w+: Coincide con uno o más caracteres alfanuméricos

# Buscar todas las coincidencias
results = re.findall(pattern, text)

if results:
    print(f"Se encontraron los siguientes archivos .txt: {', '.join(results)}")
else:
    print("No se encontraron archivos con extensión .txt.")


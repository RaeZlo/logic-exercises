"""
EJERCICIO
Valida que un correo sea de gmail
"""

import re

pattern = r"@gmail\.com$"
text = "pepe_vengas@hotmail.com"
result = re.search(pattern, text)

if result:
    print("El correo es válido.")
else:
    print("El correo no es válido. Debe ser de Gmail.")
  

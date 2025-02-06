"""
Crea una función que reciba una cadena de caracteres y genere una nueva cadena siguiendo este patrón:
- Cada letra de la cadena original se repite tantas veces como su posición en la cadena (comenzando desde 0).
- La primera aparición de cada letra es en mayúscula, mientras que las siguientes en minúscula.
- Los grupos de letras resultantes se unen con un guion (-).
"""

def acumulador(palabra:str) -> str:
    # Usamos comprensión de listas con `join()` para construir la nueva cadena.
    # Para cada carácter en la palabra, aplicamos:
    # 1. `char.upper()`: Convertimos la primera letra a mayúscula.
    # 2. `char.lower() * indice`: Repetimos el carácter en minúscula según su posición en la cadena.
    # 3. `enumerate(palabra)`: Obtiene el índice y el carácter de la palabra original.
    # 4. `'-'.join(...)`: Une todos los segmentos generados con guiones ("-").
    return '-'.join(char.upper() + char.lower() * indice for indice, char in enumerate(palabra))

respuesta = acumulador("abcd")
print(respuesta)  # Salida esperada: "A-Bb-Ccc-Dddd"

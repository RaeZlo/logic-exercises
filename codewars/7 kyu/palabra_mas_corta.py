"""
Crea una función que reciba una cadena de texto con varias palabras 
y devuelva la longitud de la palabra más corta.
"""

def palabra_mas_corta(cadena: str) -> int:
    # Dividimos la cadena en una lista de palabras con `.split()`.
    # Aplicamos `len(palabra)` a cada palabra para obtener su longitud.
    # Usamos `min()` para encontrar la menor longitud en la lista de longitudes.
    return min(len(palabra) for palabra in cadena.split())

respuesta = palabra_mas_corta("Pepe es medio raro")
print(respuesta)  # Salida esperada: 2

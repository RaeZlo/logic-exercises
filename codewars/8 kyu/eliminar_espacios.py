"""
Escribe una función que elimine los espacios de la cadena y luego devuelva la cadena resultante.
"""

def eliminar_espacios(cadena:str) -> str:
    # El método replace() de las cadenas en Python es muy útil para reemplazar caracteres.
    # En este caso, reemplazamos todos los espacios (" ") por cadenas vacías (""),
    # lo que tiene el efecto de eliminarlos.
    return cadena.replace(" ", "")

respuesta = eliminar_espacios("p p e p re pe j j pk")
print(respuesta)

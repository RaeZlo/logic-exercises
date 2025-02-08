"""
En una imprenta, los códigos de impresión solo pueden contener letras minúsculas en el rango de 'a' a 'm'.
Crea una función que reciba una cadena de caracteres y devuelva la cantidad de errores de 
impresión en formato de fracción (errores/total).
Un error ocurre cuando un carácter en codigo no pertenece al rango 'a' - 'm'.
"""

def printer_error(codigo: str) -> str:
    # Longitud total de la cadena (número total de caracteres)
    largo = len(codigo)

    # Contamos los caracteres que NO están en el rango permitido ('a' a 'm')
    errores = sum(1 for char in codigo if char not in "abcdefghijklm")

    # Retornamos la fracción errores/total en formato de cadena
    return f"{errores}/{largo}"


# Ejemplo de uso
print(printer_error("aaabbbbhaijjjm"))  # Salida esperada: "0/14"
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))  # Salida esperada: "8/22"

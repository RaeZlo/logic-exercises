"""
Crea una función que reciba una cadena no vacía y devuelva el o los caracteres centrales.
Si la longitud de la cadena es impar, retorna el carácter central.
Si la longitud de la cadena es par, retorna los dos caracteres centrales.
"""

def obtener_centro(palabra: str) -> str:
    # Calculamos la mitad de la longitud de la palabra
    mitad = len(palabra) // 2
    # Retornamos el carácter central si la longitud es impar, o dos caracteres si es par
    return palabra[mitad  - 1:mitad  + 1] if len(palabra) % 2 == 0 else palabra[mitad ]

respuesta = obtener_centro("elopir")
print(respuesta)  # Salida esperada: "op"

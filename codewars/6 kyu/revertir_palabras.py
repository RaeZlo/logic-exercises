"""
Crea una función que reciba una cadena de texto y revierte todas las palabras que tengan cinco o más letras, 
manteniendo el orden de las palabras y los espacios.

✅ Reglas:
La entrada solo contendrá letras y espacios.
Si la palabra tiene menos de 5 letras, se mantiene igual.
Si la palabra tiene 5 o más letras, se invierte.
"""

def revertir_palabras(texto: str) -> str:
    # Separa la cadena en palabras y aplica la transformación:
    return " ".join(
        palabra[::-1] if len(palabra) >= 5 else palabra  # Si la palabra tiene 5+ letras, se invierte
        for palabra in texto.split()  # Separa la cadena en palabras
    )

respuesta = revertir_palabras("Hey wollef sroirraw")
print(respuesta)  # Salida esperada: "Hey fellow warriors"

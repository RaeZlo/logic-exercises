"""
Crea una función que tome una cadena como parámetro y retorne la cadena invertida.
"""

def cadenas_invertidas(palabra: str) -> str:
    # Se utiliza el slicing con un paso de -1 para invertir la cadena de forma eficiente.
    # palabra[::-1] crea una nueva cadena que es la inversa de la original.
    return palabra[::-1]

respuesta = cadenas_invertidas("hora")
print(respuesta)  # Imprime "aroh"

respuesta = cadenas_invertidas("reconocer")
print(respuesta)  # Imprime "reconocer" (es un palíndromo)

respuesta = cadenas_invertidas("")
print(respuesta)  # Imprime "" (la cadena vacía invertida es vacía)

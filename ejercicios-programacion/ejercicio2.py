"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word1:str, word2:str) -> bool:
    # Convertimos ambas palabras a minúsculas y verificamos si son iguales.
    # Si son idénticas, no se consideran anagramas.
    if word1.lower() == word2.lower():
        return False

    # Eliminamos espacios, convertimos a minúsculas y ordenamos los caracteres.
    # Si las listas resultantes son iguales, las palabras son anagramas.
    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))

# Prueba de la función con un ejemplo.
respuesta = is_anagram("Quieren", "Enrique")
print(respuesta) # Imprime True

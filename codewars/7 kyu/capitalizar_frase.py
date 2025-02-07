"""
Crea una función que convierta la primera letra de cada palabra en mayúscula y deje el resto en minúsculas.
"""

def capitalizar_frase(frase: str) -> str:
    # Usamos `.split()` para dividir la frase en palabras.
    # Luego aplicamos `.capitalize()` a cada palabra para asegurarnos de que la primera letra sea mayúscula.
    # Finalmente, unimos las palabras con un espacio utilizando `" ".join()`.
    
    return " ".join(palabra.capitalize() for palabra in frase.split())

respuesta = capitalizar_frase("pepe es un programador talentoso")
print(respuesta)  # Salida esperada: "Pepe Es Un Programador Talentoso"

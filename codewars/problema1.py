"""
Crea una función que tome un número entero como argumento. 
y devuelve "Par" para números pares o "Impar" para números impares.
"""

def par_o_impar(numero: int) -> str:
    return "par" if numero % 2 == 0 else "impar"

respuesta = par_o_impar(5)
print(respuesta)

respuesta = par_o_impar(4)
print(respuesta)

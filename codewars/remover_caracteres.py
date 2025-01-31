"""
Crea una función que elimina el primer y último carácter de una cadena.
"""

def remover_caracteres(palabra:str) -> str:
    # La sintaxis s[1:-1] realiza un "slice" o rebanada de la cadena.
    # 1: Indica el inicio del corte (el segundo carácter, ya que los índices empiezan en 0).
    # -1: Indica el fin del corte (el penúltimo carácter, ya que los índices negativos cuentan desde el final).
    # Al omitir el primer y último índice, se eliminan el primer y último carácter de la cadena.
    return palabra[1:-1]

resultado = remover_caracteres("Hola mundo")
print(resultado)  # Imprime "ola mund"

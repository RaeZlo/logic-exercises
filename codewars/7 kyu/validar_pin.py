"""
Un cajero automático (ATM) solo acepta códigos PIN que cumplan las siguientes condiciones:
✅ Deben contener exactamente 4 o 6 dígitos numéricos.
❌ No pueden contener letras, caracteres especiales ni más o menos dígitos.

Crea una función que reciba una cadena de texto y devuelva True si el PIN es válido o False en caso contrario.
"""

import re

def validar_pin(pin: str) -> bool:
    # Verifica si la longitud del PIN es exactamente 4 o 6 caracteres
    # y si está compuesto solo por dígitos
    return len(pin) in (4, 6) and pin.isdigit()


def validar_pin_regex(pin: str) -> bool:
    # La expresión regular `^\d{4}$|^\d{6}$` valida:
    # - `^\d{4}$`  → Exactamente 4 dígitos numéricos
    # - `^\d{6}$`  → Exactamente 6 dígitos numéricos
    return bool(re.fullmatch(r"^\d{4}$|^\d{6}$", pin))

print(validar_pin_regex("1234"))   # True
print(validar_pin("12341"))        # False
print(validar_pin("abcd"))         # False
print(validar_pin("123456"))       # True
print(validar_pin("123 6"))        # False

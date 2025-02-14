"""
Ejercicio 4: Categorizar edades
Pide al usuario que introduzca una edad y la clasifique en:
 - Bebé (0-2 años)
 - Niño (3-12 años)
 - Adolescente (13-17 años)
 - Adulto (18-64 años)
 - Adulto mayor (65 años o más)
"""

edad = int(input("Ingresa una edad: "))

if 0 <= edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto Mayor")
else:
    print("Edad no válida.")

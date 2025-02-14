"""
Ejercicio 3: Año bisiesto
Pide al usuario que introduzca un año y determina si es bisiesto.
Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
"""

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")

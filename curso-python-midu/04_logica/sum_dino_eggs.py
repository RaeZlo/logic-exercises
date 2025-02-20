"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan 
un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa 
la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos 
pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def sum_dino_eggs(egg_list:list) -> int:
    count_eggs = 0
    for num in egg_list:
        if num % 2 == 0:
            count_eggs += num
    return count_eggs

def alt_sum_dino_eggs(egg_list:list) -> int:
    return sum(num for num in egg_list if num % 2 == 0)

print(sum_dino_eggs([3, 4, 7, 5, 8])) # 12
print(alt_sum_dino_eggs([1, 2, 3, 4])) # 6

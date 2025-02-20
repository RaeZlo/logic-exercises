"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal 
y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""


def find_first_sum(num_list:list, goal:int) -> list:
    for actual_index in range(len(num_list)):
        for befor_index in range(actual_index + 1, len(num_list)):
            if num_list[actual_index] + num_list[befor_index] == goal:
                return [actual_index, befor_index]
    return None

nums = [4, 5, 6, 2]
goal = 8

print(find_first_sum(nums, goal)) # [2, 3]

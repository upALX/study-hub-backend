algorith_list = [7, 2, 1, 6, 8, 5, 3, 4]

# STEPS TO QUICKSORT 
# CHOICE AN PIVOT
# SEPARAR OS MENORES QUE O PIVO A ESQUERDA 
# SEPARAR OS MAIORES QUE O PIVO A DIREITA
# TER O PIVO NO MEIO

from time import time

def quicksort_algo(items): 

    if len(items) <= 1:
        return items

    #pivot = items[len(items) // 2]
    median = sorted(arr)[len(arr) // 2]
    pivot = min(arr, key=lambda x: abs(x - median))

    minor_values = [item for item in items if item < pivot]
    middle_value = [item for item in items if item == pivot]
    biggest_values = [item for item in items if item > pivot]

    print(pivot)
    print(minor_values)
    print(middle_value)
    print(biggest_values)

    return quicksort_algo(minor_values) + middle_value + quicksort_algo(biggest_values)

array_desordenado = [7, 2, 1, 6, 8, 5, 3, 4]

start = time()

result_sorted = quicksort_algo(items=array_desordenado)

end = time()

print(start - end)

print(result_sorted)

import random 


def my_func(list_items: list) -> list:
    return lambda list_items: quicksort(list_items)


def quicksort(list_items: list) -> list:

    if len(list_items) < 1:
        return list_items

    pivo = list_items[len(list_items) // 2]

    left = [item for item in list_items if item < pivo]
    middle = [item for item in list_items if item == pivo]
    right = [item for item in list_items if item > pivo]


    return quicksort(left) + middle + quicksort(right)


list_of_items = [random.randint(1, 1000) for _ in range(100)]

ordened_list = lambda x: quicksort(x)

print(ordened_list(list_of_items))

list_items = [item for item in range(10)]

print(list_items)


item_change = [item * 3 for item in list_items if item < 4]

print(item_change)

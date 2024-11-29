# list_counter = [2,2,3,4,4,4,5,6,6]

# def count_values(list_items) -> dict:
#     counter_dict = {}
#     for item in list_items:
#         if item not in counter_dict:
#             counter_dict[item] = 0
#         counter_dict[item] += 1
    
#     return counter_dict

# result = count_values(list_items=list_counter)

# print(result)

from collections import Counter

# names = 'alice duda beat duda duda half laren half'

# counter_names = Counter(list(names.split()))

# print(counter_names)

salads = {'tomate': 3, 'batata': 5, 'couve': 10}

salads_counter = Counter(salads)
to_update_counter = Counter(tomate=10, couve=5, batata=3)

salads_counter.update(to_update_counter)

print(salads_counter)
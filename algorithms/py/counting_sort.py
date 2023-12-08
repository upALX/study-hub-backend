def counting_sort(list_values):
    # Find the maximum value in the array
    max_value = max(list_values)

    print(max_value)

    #Create a counting array to store the count of each element
    if max_value + 1 != len(list_values):
        for position in range(len(list_values)):
            max_value += 1
            if max_value + 1 == len(list_values):
                list_counters = [0] * (max_value+1)
    else:
        list_counters = [0] * (max_value+1)

    # Count the occurrences of each element in the array
    for value in list_values:
        list_counters[value] += 1

    print('count array', list_counters)

    # Reconstruct the sorted array using the counting array
    sorted_list = []
    for i in range(len(list_counters)):
        sorted_list.extend([i] * list_counters[i])

    return sorted_list

# Example usage:
my_str = '1 1 1 1 1 1'

str_to_list = list(map(int, my_str.split(' ')))
print(str_to_list)
sorted_list = counting_sort(str_to_list)
print(sorted_list)
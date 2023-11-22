# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    list_of_sums = []
    biggest_sum = 0
    lowest_sum = 0

    for value in arr:
        
        new_arr_without_one_value = [item for item in arr if item != value] 

        sum_of_values = int(sum(new_arr_without_one_value))

        is_equals_than_all = all(item == value for item in arr)

        is_biggest_than_all = all(sum_of_values > x for x in list_of_sums)

        is_lowest_than_all = all(sum_of_values < x for x in list_of_sums)

        print(is_equals_than_all)

        list_of_sums.append(sum_of_values)

        if is_biggest_than_all:
            biggest_sum = sum_of_values
        if is_lowest_than_all:
            lowest_sum = sum_of_values
        if is_equals_than_all:
            sum_of_values = sum(arr)
            biggest_sum = sum_of_values - arr[0]
            lowest_sum = sum_of_values - arr[0]

    print(f'{lowest_sum} {biggest_sum}')

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
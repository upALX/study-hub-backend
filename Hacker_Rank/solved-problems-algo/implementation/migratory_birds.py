#!/bin/python3
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter

def migratoryBirds(arr):
    # Write your code here
    
    # determine the id of the most frequently sighted
    # counter_dict = {}
    
    # for value in arr:
    #     if value not in counter_dict:
    #         counter_dict[value] = 0
    #     counter_dict[value] += 1

    counter_dict = Counter(arr)

    max_value_of_dict = max(counter_dict, key=counter_dict.get) 

    # matching_keys = [key for key, value in counter_dict.items() if value == max_value_of_dict]
    
    print(counter_dict)
    print(max_value_of_dict)
    # If more than 1 type has been spotted that maximum amount, return the smallest of their ids
    # if max_value_of_dict
    # print(arr[counter_dict[max_value_of_dict]])

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(len(arr))

    migratoryBirds(arr)

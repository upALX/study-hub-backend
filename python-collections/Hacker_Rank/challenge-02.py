# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    if len(arr) > 5:
        raise Exception()

    max_value = max(arr, key=int)

    print(max_value)

    min_value = min(arr, key=int)

    print(min_value)

    max_list = [item for item in arr if item != min_value]
    min_list = [item for item in arr if item != max_value]

    if len(max_list) == 0 and len(min_list) == 0:
        any_value_identical_list = arr[0]
        sum_of_list = sum(arr) 
        print(f'{sum_of_list - any_value_identical_list} {sum_of_list - any_value_identical_list}')
    else:
        print(f'{sum(min_list)} {sum(max_list)}')

if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))

    arr = list()
    for i in range(5):
        value_input = int(input())
        
        if value_input > 0:
            print('IS true')

            arr.append(value_input)
        else:
            print('IS FALSE')
            raise Exception

    miniMaxSum(arr)

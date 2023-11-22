# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.


import math
import os
import random
import re
from fractions import Fraction
from decimal import Decimal

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr: list):
    counter = 0 
    total_lenght_array = len(arr)
    total_rate_values_dict = {'positives': 0, 'negatives': 0, 'zero': 0}
    # Write your code here
    for position in range(total_lenght_array):
        if arr[position] > 0:
            total_rate_values_dict["positives"] += 1
        elif arr[position] < 0:
            total_rate_values_dict["negatives"] += 1
        else:
            total_rate_values_dict["zero"] += 1

        counter += 1

        if counter == total_lenght_array:

            decimal_positive_rate = total_rate_values_dict["positives"] / total_lenght_array
            decimal_negative_rate = total_rate_values_dict["negatives"] / total_lenght_array
            decimal_zero_rate = total_rate_values_dict["zero"] / total_lenght_array

            print(f'{decimal_positive_rate:.6f}')
            print(f'{decimal_negative_rate:.6f}')
            print(f'{decimal_zero_rate:.6f}')

            break


        # f_value = Fraction(value_of_arr)
        # print(type(f_value))
        # decimal_value = Decimal(f_value)
        # print(Decimal(f'{decimal_value:.06f}'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

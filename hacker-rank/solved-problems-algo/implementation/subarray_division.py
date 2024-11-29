

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.

# print sum of two values that is equals to 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(chocolate, value_bit, bits_intervalo):
    # Write your code here
    counter_bit = 0

    sub_arrays_by_lenght = [chocolate[i:i + bits_intervalo]for i in range(len(chocolate))]

    for array in sub_arrays_by_lenght:
        if sum(array) == value_bit:
            counter_bit +=1

    return counter_bit

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])

result = birthday(s, d, m)

print(result)
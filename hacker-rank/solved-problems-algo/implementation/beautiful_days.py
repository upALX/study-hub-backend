#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    counter = 0
    
    for value in range(i, j+1):
        print(value)
        print('REVERSE: ', str(value)[::-1])
        print('I', value, 'COUNT: ', value-int(str(value)[::-1]))
        calculate_beautiful_day = (value-int(str(value)[::-1])) / k
        
        print(calculate_beautiful_day)
        
        print(type(calculate_beautiful_day))
        
        if isinstance(calculate_beautiful_day, int) or (isinstance(calculate_beautiful_day, float) and calculate_beautiful_day.is_integer()):
            counter += 1 
    
    # beautiful day == reverse i - j and % k == 0
    
    return counter


first_multiple_input = input().rstrip().split()

i = int(first_multiple_input[0])

j = int(first_multiple_input[1])

k = int(first_multiple_input[2])

result = beautifulDays(i, j, k)

print(result)
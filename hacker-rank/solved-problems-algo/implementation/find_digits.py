#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # broke the n into list
    list_of_numbers = list(str(n))
    # print('list of numbers: ', list_of_numbers)
    
    counter_value = 0 
    for number in list_of_numbers:
        if int(number) == 0:
            pass
        else:
            if n % int(number) == 0:
                counter_value += 1
    
    # print(f'The counter value is {counter_value}')
    return counter_value


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    result = findDigits(n)

print(result)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

# road is indice

def serviceLane(widths, cases):
    # Write your code here
    min_values = []
    print(widths)
    print(cases)
    
    for case in cases:
        print(type(widths))
        values_of_list = widths[case[0]:case[1] + 1]
        
        print(values_of_list)
        
        min_values.append(min(values_of_list))
        
    # return the max width value to pass in all statements of lane
    return min_values
    # Based on cases with init index and final [1,2] index of statement, get the values into this interval (not include the last index value) 
    
    # for each value in interval, get the min of them and return
    
    # verify if the values colect is > 1, if is only 1, return it

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

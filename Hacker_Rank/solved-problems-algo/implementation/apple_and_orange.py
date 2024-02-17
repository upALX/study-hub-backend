#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # discover how many fruits fall on the house
    # S and T are the house
    # APPLES = positions of apples fall
    # ORANGES = positions of oranges fall
    # A = apple tree
    # B = orange tree
    # D = units of distance

    condition = lambda x, y: x <=  y <= x
    
    #calculate the values
    counter_apples = 0
    counter_oranges = 0
    
    apples_values = [counter_apples+1 for value_distance in apples if s <= (a)+value_distance <= t] 
    orange_values = [counter_oranges+1 for value_distance in oranges if s <= (b)+value_distance <= t] 
    
    if apples_values.__len__() == 0:
        apples_values = [0]
    if orange_values.__len__() == 0:
        orange_values = [0]

    print(apples_values)
    print(orange_values)

    # values_to_print = [apples_values, orange_values]

    # print('\n'.join(map(str, values_to_print)))

    print(apples_values[0])
    print(orange_values[0])

first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)

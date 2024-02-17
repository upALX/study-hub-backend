#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    
    #verify if the value k > max(heigth) 
    max_heigth_hurdle = max(height)
    # print('this is the max of hurdles: ', max_heigth_hurdle)
    if k >= max_heigth_hurdle:
        return 0
    else:
        number_of_potion_need = max_heigth_hurdle - k
        # print('number of potion needed is: ', number_of_potion_need)
        return number_of_potion_need
    
    # the value to jump all hurdles is the max of heigths - value of initial potion 


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(result)

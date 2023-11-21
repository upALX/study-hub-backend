# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

#!/bin/python3

from decimal import Decimal
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    counter_positive = 0 
    counter_negative = 0
    counter_zero = 0
    list_ratios = []
    for value in arr:
        if value > 0:
            counter_positive+=1
        elif value == 0:
            counter_zero+=1
        else:
            counter_negative+=1
    
    list_ratios.append(round(Decimal(counter_positive/arr.__len__()), 6)) 
    list_ratios.append(round(Decimal(counter_negative/arr.__len__()), 6)) 
    list_ratios.append(round(Decimal(counter_zero/arr.__len__()), 6)) 

    for value in list_ratios:
        print(value)    

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)

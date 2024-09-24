#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    contador = {}   
    
    for elemento in arr:
        if elemento in contador:
            contador[elemento] += 1  
        else:
            contador[elemento] = 1 
            
    valor_mais_comum = max(contador, key=contador.get)

    return len(arr) - arr.count(valor_mais_comum) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

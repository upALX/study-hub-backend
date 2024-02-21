#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(sequence):
    n = len(sequence)
    result = []
    
    # Iterate over each integer from 1 to n
    for x in range(1, n + 1):
        # Find y such that p(p(y)) == x
        y = sequence.index(sequence.index(x) + 1) + 1
        result.append(y)
    
    return result


n = int(input().strip())

p = list(map(int, input().rstrip().split()))

result = permutationEquation(p)

print(result)
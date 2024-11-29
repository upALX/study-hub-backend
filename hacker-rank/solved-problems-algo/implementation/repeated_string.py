#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

# Isso é O(n)

def repeatedString(s, n):
    count_in_s = s.count('a')
    
    full_repeats = n // len(s)
    
    rest = n % len(s)
    
    total_count = full_repeats * count_in_s
    if rest != 0:
        
        total_count += s[:rest].count('a')
    
    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

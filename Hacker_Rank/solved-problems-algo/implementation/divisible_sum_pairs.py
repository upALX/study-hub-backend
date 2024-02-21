#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(k, arr):
    remainder_freq = {}
    count = 0

    # Iterate through the array
    for num in arr:
        # Calculate the remainder when num is divided by k
        remainder = num % k
        # Calculate the complement required for the sum to be divisible by k
        complement = (k - remainder) % k
        # Increment count by the frequency of the complement
        count += remainder_freq.get(complement, 0)
        # Update the frequency of the current remainder
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

    return count

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs( k, ar)

print(result)

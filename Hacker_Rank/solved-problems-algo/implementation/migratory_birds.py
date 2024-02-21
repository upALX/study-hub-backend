#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
     # Create a dictionary to store the frequency of each bird type
    frequency = {}
    
    # Count the frequency of each bird type
    for bird_id in arr:
        frequency[bird_id] = frequency.get(bird_id, 0) + 1
    
    # Find the maximum frequency
    max_frequency = max(frequency.values())
    
    # Find the bird type(s) with the maximum frequency
    most_frequent_birds = [bird_id for bird_id, freq in frequency.items() if freq == max_frequency]
    
    # Return the smallest bird type ID among the most frequent ones
    return min(most_frequent_birds)

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)

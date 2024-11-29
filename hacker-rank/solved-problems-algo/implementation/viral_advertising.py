#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    counter = 0
    people_received_ad = 5
    value_of_middle_division = 2
    sum_likes = 0
    
    while counter != n:
    
        sum_likes += math.floor(people_received_ad/value_of_middle_division)
        
        print('RECEIVE', people_received_ad)
        
        people_received_ad = math.floor(people_received_ad/value_of_middle_division) * 3
        
        print('Counter', counter)
        print('LIKES', sum_likes)
        print('People', people_received_ad)
        
        counter += 1
        
    return sum_likes


n = int(input().strip())

result = viralAdvertising(n)

print(result)
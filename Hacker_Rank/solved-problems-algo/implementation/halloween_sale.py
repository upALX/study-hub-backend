#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def how_many_games(p: int, d:int, m: int, s: int) -> int:
    '''
        this function get calculate how many games you can buy by value  
    '''
    
    counter_games_bayed = 0
    
    sum_values = p
    
    while True:
        print(sum_values)
        if sum_values > s:
            return counter_games_bayed
        elif s < p:
            return 0
        else:
            if p - d <= m:
                sum_values += m
                counter_games_bayed += 1
            else:
                p = p - d
                sum_values += p
                counter_games_bayed += 1

first_multiple_input = input().rstrip().split()

p = int(first_multiple_input[0])

d = int(first_multiple_input[1])

m = int(first_multiple_input[2])

s = int(first_multiple_input[3])

answer = how_many_games(p, d, m, s)

print('COUNTER BUYED: ', answer)
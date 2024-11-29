#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(user_string: str):
    # Write your code here
    
    # cannot change c to d or d to b
    # can change d to c
    # We need reduce the value of letter by 1
    # cannot reduce the letter a
    # each reduction must be counted on a single operation
    
    # we need find the minimum operation numbers to do this, so turn a string to an palindrome
    
    # verify if is a palindrom
    reversed_str = user_string[::-1]
    
    start = 0
    end = len(user_string) - 1
    
    same_values_change_list = []
    
    if reversed_str == user_string:
        return 0
    else:
        operations_count = 0
        
        while start < end:
            if user_string[start] != user_string[end]:
                same_values_change_list.append((user_string[start], user_string[end]))
                operations_count += abs(ord(user_string[start]) - ord(user_string[end]))
                
            start+=1
            end-=1
        
        return operations_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()

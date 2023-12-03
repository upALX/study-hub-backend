#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for value in range(1,n+1):
        if value % 3 == 0 and value % 5 == 0:
            print('FizzBuzz')
        elif value % 3 == 0 and not value % 5 == 0:
            print('Fizz')
        elif value % 5 == 0 and not value % 3 == 0:
            print('Buzz')
        else:
            print(value) 

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

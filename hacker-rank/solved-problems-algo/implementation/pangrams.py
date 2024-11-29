#!/bin/python3

import math
import os
import random
import re
import sys
from re import sub

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    
    set_string = set(sub(r'[^a-zA-Z0-9]', '', s.lower()))
    
    if len(set_string) == 26:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

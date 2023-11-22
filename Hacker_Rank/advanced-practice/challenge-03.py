import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    
    if s[-2:] == 'AM' and s[0:2] == '12':
        return s[:-2].replace('12', '00')
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]
    else:
        print('is here')

        if s[:1] != '0' and int(s[:2]) == 11:
            return str(int(s[:2]) + 12) + (s[2:8])

        elif s[:1] != '0':
            print(f'{int(s[:2])}')
            hour_value = '0' + s[:1] 
            new_str = hour_value + s[1:7]
            return str(int(hour_value) + 12) + (new_str[2:8])
        else:
            print('ON ELSE ELSE')
            return str(int(s[:2]) + 12) + (s[2:8])

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
#!/bin/python3


#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    
	print(type(ar[0]))
    
    sum_values = 0
    
    for value in ar:
        sum_values += value
    
    return sum_values
    # return ''.join(sum(ar))


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)

print(result)

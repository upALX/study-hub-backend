# Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

# Function Description

# Complete the staircase function in the editor below.

# staircase has the following parameter(s):

# int n: an integer

#!/bin/python3


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    counter = 0
    character = '#'
    for _ in range(n):
        counter += 1
        print(f'{character * counter}'.rjust(n))


n = int(input().strip())

staircase(n)

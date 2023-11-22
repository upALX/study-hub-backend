# given a square matrix, calculate the absolute difference between the sums of its diagonals.abs

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(matrix_numbers):
    # Write your code here

    matrix_lenght = len(matrix_numbers)

    first_diagonal = 0
    second_diagonal = 0

    for first in range(matrix_lenght):
        for second in range(matrix_lenght):
            if first == second:
                first_diagonal += matrix_numbers[first][second]
            if first == matrix_lenght -1 - second:
                second_diagonal += matrix_numbers[first][second]

    return abs(first_diagonal - second_diagonal)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)


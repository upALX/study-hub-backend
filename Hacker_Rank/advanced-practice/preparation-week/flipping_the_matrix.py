#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    R = C = len(matrix)
    Sum = 0

    for i in range(0, R // 2):
        for j in range(0, C // 2):
            r1, r2 = i, R - i - 1
            c1, c2 = j, C - j - 1

            Sum += max(matrix[r1][c1], matrix[r1][c2],
                       matrix[r2][c1], matrix[r2][c2])

    return Sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    max_gap = 0
    for i in range(1, len(c)):
        max_gap = max(max_gap, (c[i] - c[i-1]) // 2)
    edge_left = c[0]
    edge_right = n - 1 - c[-1]
    return max(max_gap, edge_left, edge_right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

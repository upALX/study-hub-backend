#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(clouds, jump_size):
    energy = 100
    current_cloud = 0
    while True:
        next_cloud = (current_cloud + jump_size) % len(clouds)
        energy -= 1  # Consume 1 unit of energy for each jump
        if clouds[next_cloud] == 1:  # If next cloud is a thundercloud
            energy -= 2  # Decrease energy by 2
        if next_cloud == 0:  # If the character lands back on the starting cloud
            break
        current_cloud = next_cloud
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

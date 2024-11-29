#!/bin/python3

import os
import sys


#
# Complete the catAndMouse function below.
#
def closest_value(numbers, x):
    return min(numbers, key=lambda num: abs(num - x))

def catAndMouse(x, y, z):
    
    delta_A = z - x
    delta_B = z - y
    
    if abs(delta_A) == abs(delta_B):
        print('Mouse C')
    else:
        value_target = closest_value(numbers=[x,y], x=z)
        # print('VALUE TARGET', value_target)
        if value_target == x:
            print('Cat A')
        elif value_target == y:
            print('Cat B')
        else:
            print('NOT valid VALUE: ', value_target)
        

q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    catAndMouse(x, y, z)

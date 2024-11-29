#!/bin/python3

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

# x1 + v1 compair with x2 + v2 
# if in one of jumps both camgus are in the same position

def kangaroo(x1, v1, x2, v2):
    
    counter = 0
    camgu_position_1 = 0
    camgu_position_2 = 0
    
    while range(0, 10000):
        if counter == 0:
            if x1 == 0:
                camgu_position_1 += v1
            else:
                camgu_position_1 += x1 + v1
        else:
            camgu_position_1 += v1
        
        if counter == 0:  
            if x2 == 0:
                camgu_position_2 += v2
            else:
                camgu_position_2 += x2 + v2
        else:
            camgu_position_2 += v2
        
        # print('CAMGU POSITION A', camgu_position_1)
        # print('CAMGU POSITION B', camgu_position_2)
        
        if camgu_position_1 == camgu_position_2:
            print('YES')
            break
        
        counter += 1
        
        if counter == 10000:
            print('NO')
            break

first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

kangaroo(x1, v1, x2, v2)

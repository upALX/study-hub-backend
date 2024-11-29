#!/bin/python3

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
from collections import Counter

def countingValleys(steps, path):
    # Write your code here
    
    # Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude

    # mountain is a step up sea level
    # valley is a step down sea level

    # find and print the number of valleys walked through.
    
    sea_level = 0
    valley_counter = 0
    s_d = 0
    s_u = 0
    mountain = 'U'
    list_valley = [0]


    for position, step in enumerate(path):
        if step == 'D':
            s_d += -1
        else:
            s_u += 1

        if sum([s_d, s_u]) == sea_level:
            print('LIST VALLEY', list_valley)
             
            is_valley = path[list_valley[0]:position+1] 

            print('position: ', position)
            print('SUBSTRING: ', path[list_valley[0]:position+1])

            list_valley.pop()
            list_valley.append(position+1)
            
            if is_valley[0] != mountain:
                print('IS VALLEY: ', is_valley)
            # new_str = path[:position]
                print(s_d, s_u)
                valley_counter += 1

    return valley_counter

    # steps_down = Counter(path)['D']
    # steps_up = Counter(path)['U']

    # print(f'STEP DOWN: ', steps_down, 'STEPS UP: ', steps_up)

steps = int(input().strip())

path = input()

result = countingValleys(steps, path)

print(result)

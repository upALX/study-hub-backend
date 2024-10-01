# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'countApplesAndOranges' function below.
# #
# # The function accepts following parameters:
# #  1. INTEGER s
# #  2. INTEGER t
# #  3. INTEGER a
# #  4. INTEGER b
# #  5. INTEGER_ARRAY apples
# #  6. INTEGER_ARRAY oranges
# #

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     # Write your code here
#     # discover how many fruits fall on the house
#     # S and T are the house
#     # APPLES = positions of apples fall
#     # ORANGES = positions of oranges fall
#     # A = apple tree
#     # B = orange tree
#     # D = units of distance

#     condition = lambda x, y: x <=  y <= x
    
#     #calculate the values
#     counter_apples = 0
#     counter_oranges = 0
    
#     apples_values = [counter_apples+1 for value_distance in apples if s <= (a)+value_distance <= t] 
#     orange_values = [counter_oranges+1 for value_distance in oranges if s <= (b)+value_distance <= t] 
    
#     if apples_values.__len__() == 0:
#         apples_values = [0]
#     if orange_values.__len__() == 0:
#         orange_values = [0]

#     print(apples_values)
#     print(orange_values)

#     # values_to_print = [apples_values, orange_values]

#     # print('\n'.join(map(str, values_to_print)))

#     print(apples_values[0])
#     print(orange_values[0])

# first_multiple_input = input().rstrip().split()

# s = int(first_multiple_input[0])

# t = int(first_multiple_input[1])

# second_multiple_input = input().rstrip().split()

# a = int(second_multiple_input[0])

# b = int(second_multiple_input[1])

# third_multiple_input = input().rstrip().split()

# m = int(third_multiple_input[0])

# n = int(third_multiple_input[1])

# apples = list(map(int, input().rstrip().split()))

# oranges = list(map(int, input().rstrip().split()))

# countApplesAndOranges(s, t, a, b, apples, oranges)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    #s is house's lenght start
    #t is house's lenght end
    
    #a is apple
    # b orange
    # d is distance of fall fruit
    # negative d means that falls from left and positive falls from right
    
    counter = {}
    
    count_distances_apples = [a + apple_distance for apple_distance in apples]
    count_distances_oranges = [a + orange_distance for orange_distance in oranges]

    print(count_distances_apples)
    print(count_distances_oranges)
    
    for index, list_itt in enumerate([count_distances_apples, count_distances_oranges]):
        for value in list_itt:
            if index not in counter:
                    counter[index] = 0
            if value in range(s, t + 1):
                
                
                counter[index] += 1
    
    print(counter)
    
    for value in counter.values():
        print(value)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

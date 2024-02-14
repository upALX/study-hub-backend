#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angry_professor(number_of_min_students: int, students_hour_list: list) -> None:
    '''
    this function verify if has students to the class dont be cancelled
    '''
    # Write your code here
    
    #arrive <= 0 is ok
    
    #arrive >= 0 is bad
    
    # a is an list with the hours
    
    #k is a limit of students late
    
    counter_list = []
    
    for student_hour in students_hour_list:
        if student_hour <= 0:
             counter_list.append(student_hour)
            #  print(f'The counter list with student {student_hour} is {counter_list}')
    
    if len(counter_list) >= number_of_min_students:
        print('NO')
    else:
        print('YES')
    

t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    angry_professor(k, a)

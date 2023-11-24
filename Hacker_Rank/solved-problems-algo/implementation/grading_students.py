# Complete the function gradingStudents in the editor below.

# gradingStudents has the following parameter(s):

# int grades[n]: the grades before rounding







# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round g up to the next multiple of 5.
# If the value of g is less than 38, no rounding occurs as the result will still be a failing grade.

# rouding process

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def calculate_next_multiple_of_5(value):
    # Ensure the input value is a multiple of 5
    value = (value // 5) * 5 + 5
    return value

def gradingStudents(grades):
    list_rounded_grades = []
    for grade in grades:
        multiple_of_five = calculate_next_multiple_of_5(grade)
        # print('Grade: ', grade)
        # print('Multiple: ',multiple_of_five)
        # Any  less than 40 is a failing grade.
        if grade < 40 and multiple_of_five - grade <= 2: 
            if multiple_of_five > 39:
                list_rounded_grades.append(multiple_of_five)
            else:
                list_rounded_grades.append(grade)
        elif (multiple_of_five - grade) <= 2:
            list_rounded_grades.append(multiple_of_five)
        else:
            list_rounded_grades.append(grade)

    return list_rounded_grades


grades_count = int(input().strip())

if grades_count <= 60:

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        # Every student receives a  in the inclusive range from 0 to 100
        # if grades_item > 0 and grades_item < 101:
        grades.append(grades_item)

    results = gradingStudents(grades)

    for result in results:
        print(result)


# NOT SOLVED
from collections import namedtuple

number_students = int(input())

name_of_colums = input().split()

StudentsTuples = namedtuple('Students', name_of_colums)

for _ in range(number_students):



    table_information = StudentsTuples()
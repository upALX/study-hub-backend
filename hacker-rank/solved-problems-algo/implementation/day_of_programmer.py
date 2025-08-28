#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
from datetime import datetime

def verify_if_is_bissex(year: int, calendar_type: str) -> bool:
    is_bissex = (year % 4 == 0)

    if is_bissex 

def format_date_pattern(date: datetime):
    pass
def define_calendar_by_year(year):
    pass
    
def get_date_of_1918():
    quantity_day_of_year = 365 - 14
    
    return format_date_pattern()

def is_bissex(year: int, calendar: str):
    # RANGE 1700 A 2700
    #se < 1918 JULIANO
    # divisivel por 4  = 12 SENAO 11

    # se 18 a data é 25/09/18

    # GREGO
    # se % 4 = 0 e nao por 100 entao 12
    #  se é por 400 12
    # se nao por 4 é 11/09
    # se e por 4 e 100, mas não por 400 é 11 

def dayOfProgrammer(year):
    # Write your code here
    # Range 1700 - 2700 
    # Julian is < 1917 jan
    # Gregorian is >=1918 fev
    
    

    # Define the type of calendar by year 
    cal_bissexto_year_gregorian = (value // 4 == 0) and  
    
    # By the type of calendar, check the 256 day 
    
    # ano e bissexto 
    
    # Se o ano for maior que 1918, o dia é 12 de setembro, se for ano bissexto. se nao for -e 1 dia a menos.
    
    # convert to pattern dd.mm.yyyy
    
    # print on the screen
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

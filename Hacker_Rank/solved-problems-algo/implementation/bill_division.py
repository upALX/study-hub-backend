# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna.


# sum(bill) 
# s - bill[k] / 2 == b
# if b - 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

from decimal import Decimal 

def bonAppetit(bill, k, b):
    sum_bill = sum(bill)
    if (sum_bill - bill[k]) / 2 == b:
        print('Bon Appetit')
    else:
        print(Decimal(round(int(b - ((sum_bill - bill[k]) / 2)))))

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)

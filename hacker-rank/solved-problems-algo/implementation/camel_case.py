#!/bin/python3

import math
import os
import random
import re
import sys
import re

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(phrase):
    upper_list = re.findall('[A-Z][^A-Z]*', phrase)
    
    return len(upper_list) + 1


s = input()

result = camelcase(s)

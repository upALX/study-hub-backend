# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in  hour format

from datetime import datetime

def timeConversion(s):
    new_string_format = datetime.strptime(s, "%I:%M:%S%p")
    print(datetime.strftime(new_string_format, '%H:%M:%S')) 



s = input()

result = timeConversion(s)


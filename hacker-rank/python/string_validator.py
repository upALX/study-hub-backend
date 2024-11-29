# #You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

def check_string(string):
    

    #Because some functions returns True to values WHITESPACE
    new_string = string.replace(" ", "")

    isalnum = any(value.isalnum() for value in new_string)
    isalpha = any(value.isalpha() for value in new_string)
    isdigit = any(value.isdigit() for value in new_string)
    islower = any(value.islower() for value in new_string)
    isupper = any(value.isupper() for value in new_string)

    list_bol_verify = [isalnum, isalpha, isdigit, islower, isupper] 

    return  list_bol_verify

s = input()

list_bol_verified = check_string(string=s)

for value in list_bol_verified:
    print(value)
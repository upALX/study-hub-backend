# #You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

def check_string(string):
    list_bol_verify = []

    for value in string.split():

        list_bol_verify.append(value.isalnum())
        list_bol_verify.append(value.isalpha())
        list_bol_verify.append(value.isdigit())
        list_bol_verify.append(value.islower())
        list_bol_verify.append(value.isupper())

    return  list_bol_verify

s = input()

list_bol_verified = check_string(string=s)

for value in list_bol_verified:
    print(value)
# the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):

    lenght_substring = sub_string.__len__()
    indexes = [index for index, value in enumerate(string) if value == sub_string[0]]

    counter_substring = 0
    for item in indexes:
        if string[item:item+lenght_substring] == sub_string:

            counter_substring += 1

    return counter_substring

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)

    print(count)